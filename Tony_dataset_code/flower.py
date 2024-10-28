import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_material_texture_color_flower(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': texture_coordinate.outputs["Generated"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_xyz.outputs["Y"]})
    colorramp.color_ramp.elements[0].position = 0.3000
    colorramp.color_ramp.elements[0].color = [1.0000, 0.1442, 0.0021, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.9878, 1.0000, 0.0068, 1.0000]
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Color': colorramp.outputs["Color"]})
    
    diffuse_bsdf = nw.new_node(Nodes.DiffuseBSDF, input_kwargs={'Color': hue_saturation_value})
    
    translucent_bsdf = nw.new_node(Nodes.TranslucentBSDF, input_kwargs={'Color': hue_saturation_value})
    
    transparent_bsdf = nw.new_node(Nodes.TransparentBSDF, input_kwargs={'Color': hue_saturation_value})
    
    mix_shader_1 = nw.new_node(Nodes.MixShader, input_kwargs={1: translucent_bsdf, 2: transparent_bsdf})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={1: diffuse_bsdf, 2: mix_shader_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketInt', 'NumPetalos', 100)])
    
    mesh_line = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': group_input.outputs["NumPetalos"], 'Offset': (0.0000, 0.0000, 0.0000)})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['petalo']})
    
    index = nw.new_node(Nodes.Index)
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: group_input.outputs["NumPetalos"]}, attrs={'operation': 'DIVIDE'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Vector': divide, 11: (20.0000, 20.0000, 20.0000)},
        attrs={'data_type': 'FLOAT_VECTOR', 'interpolation_type': 'STEPPED'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': map_range.outputs["Vector"], 'Z': multiply})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Factor': divide, 'Value': 0.5000})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.8136, 0.3375), (1.0000, 1.0000)])
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve, 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': mesh_line, 'Instance': object_info.outputs["Geometry"], 'Rotation': combine_xyz, 'Scale': multiply_1})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': instance_on_points})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material_texture_color_flower, selection=selection)
apply(bpy.context.active_object)
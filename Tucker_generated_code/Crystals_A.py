import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_crystal_a(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Generated"]})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping},
        attrs={'projection': 'BOX', 'image': bpy.data.images['18.jpg']})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.5815, 0.5815, 0.5815, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5409
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.2545
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.2234, 0.2234, 0.2234, 1.0000]
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 10.0000, 'Detail': 15.0000, 'Distortion': 1.7000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.3091
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.4273
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.3750, 'Distance': 0.0100, 'Height': colorramp_1.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0191, 0.8000, 0.0210, 1.0000), 'Metallic': colorramp_2.outputs["Color"], 'Roughness': colorramp.outputs["Color"], 'Emission Strength': 0.0000, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_crystal_a(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Min', 0.0400),
            ('NodeSocketFloat', 'Max', 1.0100),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketFloat', 'Density', 37.6000)])
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': group_input.outputs["Geometry"], 'Density': group_input.outputs["Density"], 'Seed': 27},
        attrs={'use_legacy_normal': True})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['1'], 'Separate Children': True, 'Reset Children': True})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': collection_info})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 2.3000, 3: 0.8000})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': random_value_1.outputs[1], 'Y': distribute_points_on_faces.outputs["Rotation"], 'Z': distribute_points_on_faces.outputs["Rotation"]})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input.outputs["Min"], 3: group_input.outputs["Max"], 'Seed': group_input.outputs["Seed"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': transform, 'Rotation': combine_xyz, 'Scale': random_value.outputs[1]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points}, attrs={'legacy_behavior': True})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': realize_instances}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_crystal_a, selection=selection, attributes=[])
    surface.add_material(obj, shader_crystal_a, selection=selection)
apply(bpy.context.active_object)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_crystal_c(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    ambient_occlusion = nw.new_node(Nodes.AmbientOcclusion,
        input_kwargs={'Color': (0.0256, 0.0000, 1.0000, 1.0000), 'Distance': 0.1300},
        attrs={'samples': 128})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': ambient_occlusion.outputs["AO"]})
    colorramp_1.color_ramp.elements[0].position = 0.5000
    colorramp_1.color_ramp.elements[0].color = [0.5887, 0.5887, 0.5887, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    texture_coordinate_2 = nw.new_node(Nodes.TextureCoord)
    
    value_1 = nw.new_node(Nodes.Value)
    value_1.outputs[0].default_value = 0.7000
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_2.outputs["Generated"], 'Scale': value_1})
    
    image_texture_1 = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping_1},
        attrs={'projection': 'BOX', 'image': bpy.data.images['tex1.png']})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = -0.8600
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Location': (0.8600, 0.2200, -1.4000), 'Rotation': (0.0000, -3.6338, 0.0000), 'Scale': value})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping},
        attrs={'projection': 'BOX', 'image': bpy.data.images['tex3.png']})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0252, 0.5166, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 1.0000
    colorramp_2.color_ramp.elements[1].color = [0.0435, 1.0000, 0.0000, 1.0000]
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={6: image_texture_1.outputs["Color"], 7: colorramp_2.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_1.outputs["Color"], 7: mix_2.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    texture_coordinate_3 = nw.new_node(Nodes.TextureCoord)
    
    mapping_2 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_3.outputs["Generated"]})
    
    image_texture_3 = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping_2},
        attrs={'projection': 'BOX', 'image': bpy.data.images['50.jpg']})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture_3.outputs["Color"]})
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.5474, 0.5474, 0.5474, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 1.0000
    colorramp_3.color_ramp.elements[1].color = [0.0236, 0.0236, 0.0236, 1.0000]
    
    geometry = nw.new_node(Nodes.NewGeometry)
    
    separate_rgb = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': geometry.outputs["Normal"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_rgb.outputs["Blue"]})
    colorramp.color_ramp.elements[0].position = 0.9545
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Color': colorramp.outputs["Color"]})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: invert, 7: image_texture.outputs["Color"]},
        attrs={'clamp_result': True, 'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.7333, 'Distance': 0.0100, 'Height': mix.outputs[2]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_1.outputs[2], 'Metallic': 0.8545, 'Roughness': colorramp_3.outputs["Color"], 'Transmission': 0.5455, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_crystal_c(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Min', -0.9000),
            ('NodeSocketFloat', 'Max', 0.8200),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketFloat', 'Density', 10.0000),
            ('NodeSocketVectorXYZ', 'Scale', (1.0000, 1.0000, 1.0000))])
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Scale': group_input.outputs["Scale"]})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': transform_1, 'Density': group_input.outputs["Density"]},
        attrs={'use_legacy_normal': True})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['C']})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': object_info.outputs["Geometry"], 'Translation': (0.0000, 0.0000, 0.9000)})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input.outputs["Min"], 3: group_input.outputs["Max"], 'Seed': group_input.outputs["Seed"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': transform, 'Scale': random_value.outputs[1]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points}, attrs={'legacy_behavior': True})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': realize_instances}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_crystal_c, selection=selection, attributes=[])
    surface.add_material(obj, shader_crystal_c, selection=selection)
apply(bpy.context.active_object)
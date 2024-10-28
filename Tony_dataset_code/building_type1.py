import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_building_interior_lights(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry = nw.new_node(Nodes.NewGeometry)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': geometry.outputs["Random Per Island"]})
    colorramp.color_ramp.interpolation = "CONSTANT"
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5091
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"], 1: 50.0000}, attrs={'operation': 'MULTIPLY'})
    
    emission = nw.new_node(Nodes.Emission, input_kwargs={'Color': (1.0000, 0.6603, 0.2831, 1.0000), 'Strength': multiply})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': emission}, attrs={'is_active_output': True})

def shader_building_interior_floor(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.8000, 0.5829, 0.3524, 1.0000), 'Specular': 1.0000, 'Roughness': 0.6254})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_building_windows(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        attrs={'extension': 'CLIP', 'image': bpy.data.images['TexturesCom_Various_HighRise5_1K_albedo.tif']})
    
    image_texture_1 = nw.new_node(Nodes.ShaderImageTexture,
        attrs={'image': bpy.data.images['TexturesCom_Various_HighRise5_1K_metallic.tif']})
    
    image_texture_2 = nw.new_node(Nodes.ShaderImageTexture,
        attrs={'image': bpy.data.images['TexturesCom_Various_HighRise5_1K_roughness.tif']})
    
    image_texture_3 = nw.new_node(Nodes.ShaderImageTexture,
        attrs={'image': bpy.data.images['TexturesCom_Various_HighRise5_1K_normal.tif']})
    
    normal_map = nw.new_node(Nodes.ShaderNodeNormalMap, input_kwargs={'Color': image_texture_3.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': image_texture.outputs["Color"], 'Metallic': image_texture_1.outputs["Color"], 'Roughness': image_texture_2.outputs["Color"], 'Transmission': 1.0000, 'Transmission Roughness': 0.0045, 'Alpha': 0.8000, 'Normal': normal_map})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_building_base(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        attrs={'extension': 'CLIP', 'image': bpy.data.images['TexturesCom_Various_HighRise5_1K_albedo.tif']})
    
    image_texture_1 = nw.new_node(Nodes.ShaderImageTexture,
        attrs={'image': bpy.data.images['TexturesCom_Various_HighRise5_1K_metallic.tif']})
    
    image_texture_2 = nw.new_node(Nodes.ShaderImageTexture,
        attrs={'image': bpy.data.images['TexturesCom_Various_HighRise5_1K_roughness.tif']})
    
    image_texture_3 = nw.new_node(Nodes.ShaderImageTexture,
        attrs={'image': bpy.data.images['TexturesCom_Various_HighRise5_1K_normal.tif']})
    
    normal_map = nw.new_node(Nodes.ShaderNodeNormalMap, input_kwargs={'Color': image_texture_3.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': image_texture.outputs["Color"], 'Metallic': image_texture_1.outputs["Color"], 'Specular': 0.0010, 'Roughness': image_texture_2.outputs["Color"], 'Normal': normal_map})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Max Building Height', 10),
            ('NodeSocketInt', 'Building Height Multiplier', 1),
            ('NodeSocketInt', 'Max X Array Size', 2),
            ('NodeSocketFloat', 'Building Width Multiplier', 2.0000),
            ('NodeSocketVectorTranslation', 'Z Array Offset', (0.0000, 0.0000, 10.0000)),
            ('NodeSocketVectorTranslation', 'X Array Offset', (-10.0000, 0.0000, 0.0000)),
            ('NodeSocketBool', 'Should Randomize Lights (1=yes, 0=no)', True),
            ('NodeSocketFloat', 'Position Object Multiplier', 1.0000),
            ('NodeSocketFloat', 'Add to Seed', 0.0000),
            ('NodeSocketFloat', 'Noise Scale', 10.0000),
            ('NodeSocketFloat', 'Random Rotation Min', 0.0000),
            ('NodeSocketFloat', 'Random Rotation Max', 0.0000),
            ('NodeSocketInt', 'Random Rotation Seed', 0),
            ('NodeSocketInt', 'Distance Array X Size', 1),
            ('NodeSocketInt', 'Distance Array Y Size', 1),
            ('NodeSocketFloat', 'Distance Array X Distance', 0.0000),
            ('NodeSocketFloat', 'Distance Array Y Distance', 0.0000),
            ('NodeSocketObject', 'Location Object (set to self)', None),
            ('NodeSocketFloat', 'Z Position Randomness', 0.5000),
            ('NodeSocketFloat', 'Building Density', 0.8800),
            ('NodeSocketVectorTranslation', 'Building Origin Offset', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketObject', 'Emitter', None)])
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': group_input.outputs["Emitter"]})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': object_info_1.outputs["Geometry"]})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input.outputs["Distance Array X Distance"]})
    
    mesh_line_2 = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': group_input.outputs["Distance Array X Size"], 'Offset': combine_xyz_2})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': group_input.outputs["Distance Array Y Distance"]})
    
    mesh_line_3 = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': group_input.outputs["Distance Array Y Size"], 'Offset': combine_xyz_3})
    
    instance_on_points_3 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_line_2, 'Instance': mesh_line_3})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_3}, attrs={'legacy_behavior': True})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={'Seed': group_input.outputs["Add to Seed"]})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: random_value_1.outputs[1], 1: group_input.outputs["Building Density"]},
        attrs={'operation': 'GREATER_THAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': realize_instances, 'Selection': greater_than})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': group_input.outputs["Location Object (set to self)"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Position Object Multiplier"], 'Y': group_input.outputs["Position Object Multiplier"], 'Z': group_input.outputs["Position Object Multiplier"]})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: object_info.outputs["Location"], 1: combine_xyz},
        attrs={'operation': 'MULTIPLY'})
    
    white_noise_texture_2 = nw.new_node(Nodes.WhiteNoiseTexture, input_kwargs={'Vector': multiply.outputs["Vector"]})
    
    add = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Add to Seed"], 1: white_noise_texture_2.outputs["Color"]})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': object_info.outputs["Location"], 'W': add, 'Scale': group_input.outputs["Noise Scale"]},
        attrs={'noise_dimensions': '4D'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: noise_texture_2.outputs["Color"], 1: group_input.outputs["Building Width Multiplier"]},
        attrs={'operation': 'MULTIPLY'})
    
    mesh_line_1 = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': multiply_1, 'Start Location': group_input.outputs["Building Origin Offset"], 'Offset': group_input.outputs["X Array Offset"]})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={5: group_input.outputs["Max Building Height"], 'ID': noise_texture_2.outputs["Color"]},
        attrs={'data_type': 'INT'})
    
    mesh_line = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': random_value_2.outputs[2], 'Offset': group_input.outputs["Z Array Offset"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': mesh_line, 'Instance': group_input.outputs["Geometry"]})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_line_1, 'Instance': instance_on_points})
    
    split_edges = nw.new_node(Nodes.SplitEdges,
        input_kwargs={'Mesh': instance_on_points_1, 'Selection': group_input.outputs["Should Randomize Lights (1=yes, 0=no)"]})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input.outputs["Random Rotation Min"], 3: group_input.outputs["Random Rotation Max"], 'Seed': group_input.outputs["Random Rotation Seed"]})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': random_value.outputs[1]})
    
    instance_on_points_4 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': delete_geometry, 'Instance': split_edges, 'Rotation': combine_xyz_1})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 94.8000})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: noise_texture_1.outputs["Color"], 1: group_input.outputs["Z Position Randomness"]},
        attrs={'operation': 'MULTIPLY'})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Z Position Randomness"], 1: 2.0000},
        attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: divide}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': subtract})
    
    translate_instances = nw.new_node(Nodes.TranslateInstances,
        input_kwargs={'Instances': instance_on_points_4, 'Translation': combine_xyz_4})
    
    instance_on_points_5 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_to_points, 'Instance': translate_instances})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances, input_kwargs={'Instances': instance_on_points_5, 'Rotation': combine_xyz_1})
    
    translate_instances_1 = nw.new_node(Nodes.TranslateInstances, input_kwargs={'Instances': rotate_instances, 'Translation': combine_xyz_4})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': translate_instances_1}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_building_base, selection=selection)
    surface.add_material(obj, shader_building_windows, selection=selection)
    surface.add_material(obj, shader_building_interior_floor, selection=selection)
    surface.add_material(obj, shader_building_interior_lights, selection=selection)
apply(bpy.context.active_object)
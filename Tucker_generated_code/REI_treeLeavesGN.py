import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_leaves_small_wind_u_v', singleton=False, type='ShaderNodeTree')
def nodegroup_leaves_small_wind_u_v(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'UVMap'})
    
    separate_rgb_1 = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': attribute_1.outputs["Color"]})
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Scale Wind', 1.5000),
            ('NodeSocketFloat', 'Wind Strength', 2.0000),
            ('NodeSocketFloat', 'Wind Resist Base', 0.1000),
            ('NodeSocketFloat', 'W', 0.0000)])
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_rgb_1.outputs["Green"], 1: group_input.outputs["Wind Resist Base"], 4: group_input.outputs["Wind Strength"]},
        attrs={'clamp': False})
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord, attrs={'object': bpy.data.objects['TreeWind_empty']})
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_1, 'W': group_input.outputs["W"], 'Scale': group_input.outputs["Scale Wind"], 'Detail': 0.0000, 'Roughness': 0.0000},
        attrs={'noise_dimensions': '4D'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: map_range.outputs["Result"], 6: separate_rgb_1.outputs["Red"], 7: noise_texture.outputs["Fac"]},
        attrs={'data_type': 'RGBA'})
    
    combine_rgb_1 = nw.new_node(Nodes.CombineColor,
        input_kwargs={'Red': mix_1.outputs[2], 'Green': separate_rgb_1.outputs["Green"], 'Blue': separate_rgb_1.outputs["Blue"]})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_rgb_1, 1: (0.0100, 0.0100, 0.0100), 'Scale': -0.1000},
        attrs={'operation': 'SCALE'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': scale.outputs["Vector"]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_leaves_col', singleton=False, type='ShaderNodeTree')
def nodegroup_leaves_col(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketVector', 'Normal', (0.0000, 0.0000, 0.0000))])
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: group_input.outputs["Normal"], 1: (-0.1600, 0.0000, 0.0600)})
    
    diffuse_bsdf = nw.new_node(Nodes.DiffuseBSDF, input_kwargs={'Normal': add.outputs["Vector"]})
    
    shader_to_rgb = nw.new_node('ShaderNodeShaderToRGB', input_kwargs={'Shader': diffuse_bsdf})
    
    separate_color = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': shader_to_rgb.outputs["Color"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_color.outputs["Red"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.2773
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    invert = nw.new_node(Nodes.MapRange, input_kwargs={'Value': colorramp.outputs["Color"], 3: 1.0000, 4: 0.0000}, label='Invert')
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 0.5000, 'Detail': 1.0000})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': noise_texture.outputs["Fac"], 1: 0.4200, 2: 0.7100, 4: 0.3000})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: map_range.outputs["Result"], 6: (0.1655, 0.6223, 0.0696, 1.0000), 7: (0.7358, 0.4204, 0.0548, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp.outputs["Color"], 7: mix_1.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.2583, 6: mix_1.outputs[2], 7: (0.0000, 0.0161, 0.6077, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'LINEAR_LIGHT'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: invert.outputs["Result"], 6: mix.outputs[2], 7: mix_3.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'LIGHTEN'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: group_input.outputs["Normal"], 1: (0.0000, 0.0900, 0.0000)})
    
    diffuse_bsdf_1 = nw.new_node(Nodes.DiffuseBSDF, input_kwargs={'Normal': add_1.outputs["Vector"]})
    
    shader_to_rgb_1 = nw.new_node('ShaderNodeShaderToRGB', input_kwargs={'Shader': diffuse_bsdf_1})
    
    separate_color_1 = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': shader_to_rgb_1.outputs["Color"]})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_color_1.outputs["Red"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.2864
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_1.outputs["Color"], 7: mix_1.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Hue': 0.5300, 'Saturation': 2.0000, 'Value': 1.4700, 'Color': mix_5.outputs[2]})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_2.outputs[2], 7: hue_saturation_value},
        attrs={'data_type': 'RGBA', 'blend_type': 'LIGHTEN'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Color': mix_4.outputs[2]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_leaves_wind', singleton=False, type='GeometryNodeTree')
def nodegroup_leaves_wind(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Wind Speed', 1.0000),
            ('NodeSocketFloat', 'Wind Mvt Range', 1.0000),
            ('NodeSocketFloat', 'Wind Noise Scale', 0.7000),
            ('NodeSocketFloat', 'Wind Noise Detail', 1.5000)])
    
    position = nw.new_node(Nodes.InputPosition)
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['TreeWind_empty']})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: object_info.outputs["Location"], 1: group_input.outputs["Wind Speed"]},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 1: multiply.outputs["Vector"]})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add.outputs["Vector"], 1: (0.3000, 0.3000, 0.3000)},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': multiply_1.outputs["Vector"], 'Scale': group_input.outputs["Wind Noise Scale"], 'Detail': group_input.outputs["Wind Noise Detail"], 'Roughness': 0.5250})
    
    multiply_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Fac"], 1: group_input.outputs["Wind Mvt Range"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Offset': multiply_2.outputs["Vector"]})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Wind Mvt Range"], 1: -0.5000},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_2, 'Offset': multiply_3})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_position_3}, attrs={'is_active_output': True})

def shader_leaf(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'UVMap'})
    
    group = nw.new_node(nodegroup_leaves_small_wind_u_v().name,
        input_kwargs={'Wind Strength': 8.0000, 'Wind Resist Base': 0.3000})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: attribute_1.outputs["Vector"], 1: group})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': add.outputs["Vector"]},
        attrs={'image': bpy.data.images['TreeLeaves01.png.001']})
    
    transparent_bsdf = nw.new_node(Nodes.TransparentBSDF)
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'LeavesNormal_GN'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 2.3000, 'Distortion': 2.0000})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 5.9000, 'Distortion': 0.4000})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: noise_texture_1.outputs["Color"], 7: noise_texture_2.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: attribute.outputs["Vector"], 1: mix_2.outputs[2]},
        attrs={'operation': 'MULTIPLY'})
    
    group_2 = nw.new_node(nodegroup_leaves_col().name, input_kwargs={'Normal': multiply.outputs["Vector"]})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': image_texture.outputs["Color"], 1: transparent_bsdf, 2: group_2})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def shader_leaves_sphere(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry = nw.new_node(Nodes.NewGeometry)
    
    normal = nw.new_node('ShaderNodeNormal')
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1000, 6: geometry.outputs["Normal"], 7: normal.outputs["Normal"]},
        attrs={'data_type': 'RGBA'})
    
    group = nw.new_node(nodegroup_leaves_col().name, input_kwargs={'Normal': mix.outputs[2]})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': group}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_4 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketObject', 'Leaf Mesh Source', None), #bpy.data.objects['Leaf']
            ('NodeSocketMaterial', 'Sphere Material', None), #surface.shaderfunc_to_material(shader_leaves_sphere)
            ('NodeSocketMaterial', 'Leaf Material', None), #surface.shaderfunc_to_material(shader_leaf)
            ('NodeSocketFloat', 'Scale Sphere', 0.8000),
            ('NodeSocketInt', 'Sphere Subdiv', 0),
            ('NodeSocketFloat', 'Density', 10.0000),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketFloat', 'Scale', 4.0000),
            ('NodeSocketFloat', 'Leaves Offset', 0.0000),
            ('NodeSocketFloat', 'Offset Random', 0.5000),
            ('NodeSocketBool', 'Sphere Visibility', True),
            ('NodeSocketFloat', 'Wind Intensity', 4.0000),
            ('NodeSocketFloat', 'Wind Mvt Range', 0.2500),
            ('NodeSocketFloat', 'Wind Noise Scale', 0.7000),
            ('NodeSocketFloat', 'Wind Noise Detail', 1.5000),
            ('NodeSocketFloat', 'Wind Rotate Intensity', 0.5000)])
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': group_input_4.outputs["Geometry"], 'Scale': group_input_4.outputs["Scale Sphere"]})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': scale_elements, 'Density': group_input_4.outputs["Density"], 'Seed': group_input_4.outputs["Seed"]},
        attrs={'use_legacy_normal': True})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': group_input_4.outputs["Leaf Mesh Source"]})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': distribute_points_on_faces.outputs["Rotation"], 'Vector': distribute_points_on_faces.outputs["Normal"]})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={3: 360.0000})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: random_value_1.outputs[1], 1: (1.0000, 1.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: align_euler_to_vector, 1: multiply.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.3000, 3: 1.2000})
    
    multiply_add = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_4.outputs["Scale"], 1: 0.1000, 2: 0.0000},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: random_value.outputs[1], 1: multiply_add}, attrs={'operation': 'MULTIPLY'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': object_info.outputs["Geometry"], 'Rotation': multiply_1.outputs["Vector"], 'Scale': multiply_2})
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={3: group_input_4.outputs["Offset Random"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: random_value_2.outputs[1], 1: group_input_4.outputs["Leaves Offset"]})
    
    translate_instances = nw.new_node(Nodes.TranslateInstances, input_kwargs={'Instances': instance_on_points, 'Translation': add})
    
    position = nw.new_node(Nodes.InputPosition)
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['TreeWind_empty']})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 1: object_info_1.outputs["Location"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': add_1.outputs["Vector"], 'Scale': group_input_4.outputs["Wind Noise Scale"], 'Detail': group_input_4.outputs["Wind Noise Detail"], 'Roughness': 0.0000})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: noise_texture.outputs["Fac"], 1: group_input_4.outputs["Wind Rotate Intensity"]},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_3, 'Y': multiply_3})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances, input_kwargs={'Instances': translate_instances, 'Rotation': combine_xyz})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': rotate_instances})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': realize_instances_1, 'Material': group_input_4.outputs["Leaf Material"]})
    
    leaveswind = nw.new_node(nodegroup_leaves_wind().name,
        input_kwargs={'Geometry': set_material, 'Wind Speed': group_input_4.outputs["Wind Intensity"], 'Wind Mvt Range': group_input_4.outputs["Wind Mvt Range"], 'Wind Noise Scale': group_input_4.outputs["Wind Noise Scale"], 'Wind Noise Detail': group_input_4.outputs["Wind Noise Detail"]})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': scale_elements, 'Level': group_input_4.outputs["Sphere Subdiv"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subdivision_surface})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute, 'Material': group_input_4.outputs["Sphere Material"]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, set_material_1]})
    
    leaveswind_1 = nw.new_node(nodegroup_leaves_wind().name,
        input_kwargs={'Geometry': join_geometry, 'Wind Speed': group_input_4.outputs["Wind Intensity"], 'Wind Mvt Range': group_input_4.outputs["Wind Mvt Range"], 'Wind Noise Scale': group_input_4.outputs["Wind Noise Scale"], 'Wind Noise Detail': group_input_4.outputs["Wind Noise Detail"]})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_4.outputs["Sphere Visibility"], 14: leaveswind, 15: leaveswind_1})
    
    leaveswind_2 = nw.new_node(nodegroup_leaves_wind().name,
        input_kwargs={'Geometry': reroute, 'Wind Speed': group_input_4.outputs["Wind Intensity"], 'Wind Mvt Range': group_input_4.outputs["Wind Mvt Range"], 'Wind Noise Scale': group_input_4.outputs["Wind Noise Scale"], 'Wind Noise Detail': group_input_4.outputs["Wind Noise Detail"]})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements, input_kwargs={'Geometry': leaveswind_2})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': scale_elements_1, 1: normal},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    sample_nearest_surface = nw.new_node(Nodes.SampleNearestSurface,
        input_kwargs={'Mesh': capture_attribute.outputs["Geometry"], 3: capture_attribute.outputs["Attribute"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': switch.outputs[6], 'Sphere Normals': sample_nearest_surface.outputs[2]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_leaves_sphere, selection=selection)
apply(bpy.context.active_object)
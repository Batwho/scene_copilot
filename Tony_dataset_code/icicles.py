import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_asphalt_rough(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["UV"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mapping})
    
    base_color = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Base Color',
        attrs={'image': bpy.data.images['ulylecao_4K_Albedo.jpg']})
    
    roughness = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Roughness',
        attrs={'image': bpy.data.images['ulylecao_4K_Roughness.jpg']})
    
    normal = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Normal',
        attrs={'image': bpy.data.images['ulylecao_4K_Normal.jpg']})
    
    normal_map = nw.new_node(Nodes.ShaderNodeNormalMap, input_kwargs={'Color': normal.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': base_color.outputs["Color"], 'Roughness': roughness.outputs["Color"], 'Normal': normal_map})
    
    displacement = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Displacement',
        attrs={'image': bpy.data.images['ulylecao_4K_Displacement.exr']})
    
    displacement_1 = nw.new_node(Nodes.Displacement, input_kwargs={'Height': displacement.outputs["Color"]})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': principled_bsdf, 'Displacement': displacement_1},
        attrs={'is_active_output': True})

def shader_i_c_e(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: texture_coordinate.outputs["Object"], 1: (0.2100, 0.2100, 0.2100)})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': add.outputs["Vector"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["Z"], 1: 3.7500},
        attrs={'operation': 'MULTIPLY', 'use_clamp': True})
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Scale': (1.0000, 1.0000, 10.0600)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 6.0500})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.1250, 'Height': noise_texture.outputs["Fac"]})
    
    glass_bsdf = nw.new_node(Nodes.GlassBSDF, input_kwargs={'Roughness': multiply, 'IOR': 1.3050, 'Normal': bump})
    
    principled_volume = nw.new_node(Nodes.PrincipledVolume,
        input_kwargs={'Color': (1.0000, 1.0000, 1.0000, 1.0000), 'Density': 0.4000, 'Emission Strength': 1.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': glass_bsdf, 'Volume': principled_volume},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_3 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatFactor', 'Density', 1.0000),
            ('NodeSocketFloatFactor', 'Len', 0.4333),
            ('NodeSocketFloatFactor', 'min_radious', 0.4333),
            ('NodeSocketFloatFactor', 'max Radious', 0.4333),
            ('NodeSocketFloatDistance', 'Main radiousRadius', 0.0400),
            ('NodeSocketFloatFactor', 'Main len', 0.4333),
            ('NodeSocketFloatFactor', 'closter', 1.0000),
            ('NodeSocketFloatFactor', 'closter rait ', 0.0000),
            ('NodeSocketFloatFactor', 'noise', 0.0000),
            ('NodeSocketFloatFactor', 'Resolution ', 0.4333)])
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["Density"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    map_range_4 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': mix.outputs[2], 3: 1.0000, 4: 20.0000})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: map_range_4.outputs["Result"]}, attrs={'operation': 'DIVIDE'})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': 1.0000, 'Scale': 27.0000, 'Roughness': 0.0000},
        attrs={'noise_dimensions': '4D'})
    
    mix_6 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["closter"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    map_range_7 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': noise_texture_2.outputs["Fac"], 3: mix_6.outputs[2]},
        attrs={'clamp': False})
    
    mix_8 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["closter rait "], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    map_range_8 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': mix_8.outputs[2], 3: 0.4000, 4: 0.6000}, attrs={'clamp': False})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_7.outputs["Result"], 1: map_range_8.outputs["Result"]},
        attrs={'operation': 'GREATER_THAN'})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': group_input_3.outputs["Geometry"], 'Distance Min': divide, 'Density Max': 1436.0900, 'Density Factor': greater_than},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["Len"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    map_range_5 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': mix_3.outputs[2], 4: -3.0000})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': map_range_5.outputs["Result"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_1})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.3700, 3: 1.4000, 'Seed': 2})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 1.0000, 'Z': random_value.outputs[1]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': curve_line, 'Scale': combine_xyz})
    
    scale_instances = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': instance_on_points})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': scale_instances}, attrs={'legacy_behavior': True})
    
    mix_10 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["Resolution "], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    map_range_9 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': mix_10.outputs[2], 4: 40.0000})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': realize_instances, 'Count': map_range_9.outputs["Result"]})
    
    curve_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["Main len"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    greater_than_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: curve_parameter_1.outputs["Factor"], 1: mix_7.outputs[2]},
        attrs={'operation': 'GREATER_THAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': resample_curve_1, 'Selection': greater_than_1})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["max Radious"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["min_radious"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': curve_parameter.outputs["Factor"], 3: mix_5.outputs[2], 4: mix_4.outputs[2]})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range.outputs["Result"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.9227, 0.9000), (0.9500, 0.9875), (1.0000, 1.0000)])
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: float_curve, 1: 1.0100}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': delete_geometry, 'Radius': multiply})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': 24, 'Radius': group_input_3.outputs["Main radiousRadius"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': curve_to_mesh}, attrs={'legacy_behavior': True})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': realize_instances_1, 1: normal},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': capture_attribute_1.outputs["Geometry"], 1: position_1},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 17.7300})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': noise_texture.outputs["Fac"], 3: -0.5000, 4: 0.5000},
        attrs={'clamp': False})
    
    mix_9 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["noise"], 6: (1.0000, 1.0000, 1.0000, 1.0000), 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    map_range_6 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': mix_9.outputs[2], 3: 4.0000, 4: 100.0000}, attrs={'clamp': False})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: map_range_6.outputs["Result"]}, attrs={'operation': 'DIVIDE'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_2.outputs["Result"], 1: divide_1},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 0.2800})
    
    map_range_3 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': noise_texture_1.outputs["Fac"], 3: -0.5000, 4: 0.5000},
        attrs={'clamp': False})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: divide_1, 1: map_range_3.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    mix_2 = nw.new_node(Nodes.Mix, input_kwargs={0: 0.2417, 6: multiply_2, 7: multiply_4}, attrs={'data_type': 'RGBA'})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: mix_2.outputs[2], 1: -1.0000}, attrs={'operation': 'ABSOLUTE'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': absolute, 'Y': absolute})
    
    multiply_5 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: capture_attribute_1.outputs["Attribute"], 1: combine_xyz_2},
        attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Offset': multiply_5.outputs["Vector"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position, 'Material': surface.shaderfunc_to_material(shader_i_c_e)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': set_material})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_i_c_e, selection=selection)
    surface.add_material(obj, shader_asphalt_rough, selection=selection)
apply(bpy.context.active_object)
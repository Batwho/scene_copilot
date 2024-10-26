import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_f_l_o_w_e_r_s(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["UV"]})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping},
        attrs={'image': bpy.data.images['FINAL.png']})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Hue': 0.5000, 'Saturation': 1.1000, 'Color': image_texture.outputs["Color"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.4206, 'Height': colorramp.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': hue_saturation_value, 'Subsurface': 0.1500, 'Subsurface Color': hue_saturation_value, 'Specular': 0.0364, 'Roughness': 0.8818, 'Emission Strength': 1.6000, 'Alpha': image_texture.outputs["Alpha"], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_stem(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 57.2000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.interpolation = "B_SPLINE"
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5560
    colorramp.color_ramp.elements[1].color = [0.0113, 0.0343, 0.0000, 1.0000]
    colorramp.color_ramp.elements[2].position = 1.0000
    colorramp.color_ramp.elements[2].color = [0.1196, 0.2053, 0.0000, 1.0000]
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_2.color_ramp.elements[0].position = 0.4095
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5560
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.1190, 'Height': colorramp_2.outputs["Color"]},
        attrs={'invert': True})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Roughness': colorramp_1.outputs["Color"], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_vassel_01(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Rotation': (0.0000, 1.5708, 0.0000)})
    
    gradient_texture_1 = nw.new_node(Nodes.GradientTexture, input_kwargs={'Vector': mapping})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': gradient_texture_1.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.7112
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.7672
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    gradient_texture = nw.new_node(Nodes.GradientTexture, input_kwargs={'Vector': mapping})
    
    magic_texture = nw.new_node(Nodes.MagicTexture, input_kwargs={'Scale': 3.0000})
    
    mix_legacy = nw.new_node(Nodes.MixRGB,
        input_kwargs={'Fac': 0.2143, 'Color1': gradient_texture.outputs["Color"], 'Color2': magic_texture.outputs["Color"]})
    
    mix_legacy_2 = nw.new_node(Nodes.MixRGB,
        input_kwargs={'Fac': 1.0000, 'Color1': colorramp_1.outputs["Color"], 'Color2': mix_legacy},
        attrs={'blend_type': 'MULTIPLY'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_legacy_2})
    colorramp.color_ramp.elements[0].position = 0.3534
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.3578
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_legacy_1 = nw.new_node(Nodes.MixRGB,
        input_kwargs={'Fac': colorramp.outputs["Color"], 'Color1': (0.1052, 0.0087, 0.0009, 1.0000), 'Color2': (0.4924, 0.1662, 0.0632, 1.0000)})
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    mapping_1 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate_1.outputs["Generated"], 'Scale': (1.0000, 1.0000, 50.0000)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_1, 'Scale': 10.0000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 1.0000
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump_1 = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.1170, 'Height': noise_texture.outputs["Fac"]},
        attrs={'invert': True})
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.4830, 'Height': colorramp.outputs["Color"], 'Normal': bump_1},
        attrs={'invert': True})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_legacy_1, 'Roughness': colorramp_2.outputs["Color"], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_5 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Vassel_01', None),
            ('NodeSocketFloatDistance', 'Height', 0.4000),
            ('NodeSocketFloatFactor', 'Shape_Mod_01', 0.0714),
            ('NodeSocketFloat', 'Shape_Mod_02', 1.0000),
            ('NodeSocketInt', 'Vase_Resolution', 32),
            ('NodeSocketFloatDistance', 'Vassel_Radius', 0.1000),
            ('NodeSocketBool', 'Bevel_Corners', True),
            ('NodeSocketMaterial', 'Vassel_Material', None), #surface.shaderfunc_to_material(shader_vassel_01)
            ('NodeSocketFloat', 'Flower_Start_Beding', 0.0000),
            ('NodeSocketFloat', 'Flower_Bend', 16.0000),
            ('NodeSocketFloatDistance', 'Fower_Height', 0.7000),
            ('NodeSocketIntUnsigned', 'Number Of Flowers', 10),
            ('NodeSocketInt', 'Flower_Seed', 0),
            ('NodeSocketFloatDistance', 'End Radius', 0.0100),
            ('NodeSocketFloat', 'leafs Start point', 127.0300),
            ('NodeSocketFloat', 'leaf_scale', 0.0300)])
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': group_input_5.outputs["Number Of Flowers"], 'Start Radius': 0.0000, 'End Radius': group_input_5.outputs["End Radius"], 'Height': 0.0000})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_5.outputs["Fower_Height"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'Length': reroute_4}, attrs={'mode': 'DIRECTION'})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_1, 'Count': 30})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_5.outputs["Flower_Start_Beding"]})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: spline_parameter_1.outputs["Factor"], 1: reroute_2})
    
    position = nw.new_node(Nodes.InputPosition)
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_parameter_1.outputs["Factor"], 1: reroute_2},
        attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: subtract, 1: group_input_5.outputs["Flower_Bend"]},
        attrs={'operation': 'MULTIPLY'})
    
    radians = nw.new_node(Nodes.Math, input_kwargs={0: multiply}, attrs={'operation': 'RADIANS'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': position, 'Angle': radians},
        attrs={'rotation_type': 'Y_AXIS'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': resample_curve_1, 'Selection': greater_than, 'Position': vector_rotate})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={2: -5.0000, 3: 5.0000})
    
    radians_1 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_1.outputs[1]}, attrs={'operation': 'RADIANS'})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={3: 359.0000, 'Seed': group_input_5.outputs["Flower_Seed"]})
    
    radians_2 = nw.new_node(Nodes.Math, input_kwargs={0: random_value.outputs[1]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': radians_1, 'Z': radians_2})
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.9000, 3: 1.1000, 'Seed': 58})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 1.0000, 'Z': random_value_2.outputs[1]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': spiral, 'Instance': set_position, 'Rotation': combine_xyz, 'Scale': combine_xyz_1})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points})
    
    spline_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': spline_parameter_2.outputs["Factor"], 3: 1.0000, 4: 0.2000})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_5, 'Radius': map_range_1.outputs["Result"]})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 6, 'Radius': 0.0030})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh_1})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_6, 'Material': surface.shaderfunc_to_material(shader_stem)})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'Length': group_input_5.outputs["Height"]}, attrs={'mode': 'DIRECTION'})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': 30})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_5.outputs["Shape_Mod_01"]})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': spline_parameter.outputs["Factor"], 4: group_input_5.outputs["Shape_Mod_02"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.5000), (0.4310, 1.0000), (0.7974, 0.4286), (1.0000, 0.6607)])
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.6012), (0.2284, 0.9226), (0.6207, 0.6845), (1.0000, 0.4881)])
    
    mix = nw.new_node(Nodes.Mix, input_kwargs={0: reroute_1, 6: float_curve, 7: float_curve_1}, attrs={'data_type': 'RGBA'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve, 'Radius': mix.outputs[2]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_5.outputs["Vase_Resolution"], 'Radius': group_input_5.outputs["Vassel_Radius"]})
    
    fillet_curve = nw.new_node(Nodes.FilletCurve,
        input_kwargs={'Curve': curve_circle.outputs["Curve"], 'Count': 5, 'Radius': 0.0300},
        attrs={'mode': 'POLY'})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_5.outputs["Bevel_Corners"], 14: curve_circle.outputs["Curve"], 15: fillet_curve})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': switch.outputs[6], 'Fill Caps': True})
    
    index = nw.new_node(Nodes.Index)
    
    domain_size = nw.new_node(Nodes.DomainSize, input_kwargs={'Geometry': curve_to_mesh})
    
    subtract_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: domain_size.outputs["Face Count"], 1: 1.0000},
        attrs={'operation': 'SUBTRACT'})
    
    greater_equal = nw.new_node(Nodes.Compare,
        input_kwargs={2: index, 3: subtract_1},
        attrs={'data_type': 'INT', 'operation': 'GREATER_EQUAL'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': curve_to_mesh, 'Selection': greater_equal})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': delete_geometry, 'Offset Scale': -0.0100, 'Individual': False})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [extrude_mesh.outputs["Mesh"], delete_geometry]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': merge_by_distance, 'Material': group_input_5.outputs["Vassel_Material"]})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_2, set_material]})
    
    index_1 = nw.new_node(Nodes.Index)
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={0: index_1, 1: 28.9300})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['PFlower1']})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent}, attrs={'axis': 'Z'})
    
    random_value_3 = nw.new_node(Nodes.RandomValue, input_kwargs={3: 0.0800})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': random_value_3.outputs[1], 'Y': random_value_3.outputs[1], 'Z': random_value_3.outputs[1]})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': instance_on_points, 'Selection': greater_than_1, 'Instance': object_info.outputs["Geometry"], 'Rotation': align_euler_to_vector, 'Scale': combine_xyz_2})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points_1, 'Material': surface.shaderfunc_to_material(shader_f_l_o_w_e_r_s)})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry_1, set_material_1]})
    
    index_2 = nw.new_node(Nodes.Index)
    
    greater_than_2 = nw.new_node(Nodes.Compare, input_kwargs={0: index_2, 1: group_input_5.outputs["leafs Start point"]})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['PLeaf4']})
    
    random_value_6 = nw.new_node(Nodes.RandomValue, input_kwargs={2: -5.0000, 3: 5.0000})
    
    radians_3 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_6.outputs[1]}, attrs={'operation': 'RADIANS'})
    
    random_value_5 = nw.new_node(Nodes.RandomValue, input_kwargs={3: 359.0000, 'Seed': 30})
    
    radians_4 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_5.outputs[1]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': radians_3, 'Z': radians_4})
    
    random_value_4 = nw.new_node(Nodes.RandomValue, input_kwargs={2: group_input_5.outputs["leaf_scale"], 3: 0.0000})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': random_value_4.outputs[1], 'Y': random_value_4.outputs[1], 'Z': random_value_4.outputs[1]})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_6, 'Selection': greater_than_2, 'Instance': object_info_1.outputs["Geometry"], 'Rotation': combine_xyz_4, 'Scale': combine_xyz_3})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry_2, instance_on_points_2]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry_3})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_shade_smooth}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_vassel_01, selection=selection)
    surface.add_material(obj, shader_stem, selection=selection)


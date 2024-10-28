import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_bulb_pollen(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'TEST'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute.outputs["Color"]})
    colorramp.color_ramp.interpolation = "B_SPLINE"
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.1167, 0.1239, 0.5070, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.3091
    colorramp.color_ramp.elements[1].color = [0.0139, 0.0016, 0.0082, 1.0000]
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute.outputs["Color"]})
    colorramp_1.color_ramp.interpolation = "B_SPLINE"
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.7030, 1.0000, 0.2316, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.0227
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 0.1591
    colorramp_1.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Subsurface Color': colorramp.outputs["Color"], 'Metallic': 0.6364, 'Roughness': 0.1500, 'Emission': colorramp_1.outputs["Color"], 'Emission Strength': 4.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_fruit_3', singleton=False, type='GeometryNodeTree')
def nodegroup_fruit_3(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Amount of Leaves', 7),
            ('NodeSocketInt', 'Curve Resolution', 178),
            ('NodeSocketInt', 'Profile Resolution', 80),
            ('NodeSocketFloatDistance', 'Curve Radius', 0.0300),
            ('NodeSocketFloat', 'Leaf Shape Radius', 12.0000),
            ('NodeSocketFloatDistance', 'Instance Radius', 0.0150),
            ('NodeSocketFloat', 'X Rotation', 73.8000),
            ('NodeSocketFloat', 'Y Rotation', 5.0000),
            ('NodeSocketFloat', 'Z Rotation', 0.0000),
            ('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketVector', 'End Handle Position', (0.0000, -0.3590, 0.0650)),
            ('NodeSocketVector', 'Start Handle Position', (0.0000, -0.0500, 0.8280)),
            ('NodeSocketVectorTranslation', 'End Position', (0.0000, 0.8720, 0.0750)),
            ('NodeSocketVectorTranslation', 'Start Position', (0.0000, 0.0060, -0.0940)),
            ('NodeSocketColor', 'Color1', (0.5000, 0.5000, 0.5000, 1.0000)),
            ('NodeSocketColor', 'Color2', (0.5000, 0.5000, 0.5000, 1.0000))])
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Amount of Leaves"], 'Radius': group_input.outputs["Instance Radius"]})
    
    bezier_segment_1 = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Start': (0.0000, 0.0000, 0.5000), 'Start Handle': (0.0000, 0.0000, 0.0000), 'End': (0.0000, 0.0000, 0.0000)})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': bezier_segment_1, 'Selection': endpoint_selection, 'Offset': group_input.outputs["End Position"]})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': endpoint_selection_1, 'Offset': group_input.outputs["Start Position"]})
    
    set_handle_positions = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_position_1, 'Selection': endpoint_selection, 'Offset': group_input.outputs["End Handle Position"]},
        attrs={'mode': 'RIGHT'})
    
    set_handle_positions_1 = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_handle_positions, 'Selection': endpoint_selection_1, 'Offset': group_input.outputs["Start Handle Position"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_handle_positions_1, 'Count': group_input.outputs["Curve Resolution"]})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': resample_curve})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: spline_parameter.outputs["Factor"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': trim_curve, 'Name': 'TEST', 5: mix.outputs[2]},
        attrs={'data_type': 'FLOAT_COLOR'})
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': store_named_attribute, 3: mix.outputs[2]},
        attrs={'data_type': 'FLOAT_COLOR'})
    
    curve_tangent_1 = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent_1})
    
    radians = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["X Rotation"]}, attrs={'operation': 'RADIANS'})
    
    radians_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Y Rotation"]}, attrs={'operation': 'RADIANS'})
    
    radians_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Z Rotation"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians, 'Y': radians_1, 'Z': radians_2})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: align_euler_to_vector, 1: combine_xyz_1})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_circle_1.outputs["Curve"], 'Instance': capture_attribute.outputs["Geometry"], 'Rotation': add.outputs["Vector"], 'Scale': (0.1500, 0.1500, 0.1500)})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.1313), (0.0529, 0.3750), (0.1142, 0.1938), (0.6908, 0.0937), (0.9179, 0.1341), (0.9972, 0.0750)])
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': instance_on_points, 'Radius': multiply})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 16})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_bulb_pollen)})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': set_shade_smooth_1})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry, 'Rotation': (0.0000, 3.1416, 0.0000)})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': transform})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': set_shade_smooth, 'Attribute': capture_attribute.outputs[3]},
        attrs={'is_active_output': True})

def shader_bulb_fuit_2(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord, attrs={'object': bpy.data.objects['Fruit']})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': texture_coordinate.outputs["Normal"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz.outputs["Z"], 1: -1.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range.outputs["Result"]})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0364
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.0574
    colorramp.color_ramp.elements[1].color = [0.0912, 0.3381, 0.6173, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.1239
    colorramp.color_ramp.elements[2].color = [0.0912, 0.3381, 0.6173, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.2250
    colorramp.color_ramp.elements[3].color = [0.0212, 0.0437, 0.2346, 1.0000]
    colorramp.color_ramp.elements[4].position = 0.3045
    colorramp.color_ramp.elements[4].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Generated"]})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mapping, 'Scale': 8.6000},
        attrs={'feature': 'DISTANCE_TO_EDGE'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Distance"]})
    colorramp_1.color_ramp.interpolation = "EASE"
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.0045
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range.outputs["Result"]})
    colorramp_2.color_ramp.interpolation = "CONSTANT"
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.0636
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_1.outputs["Color"], 1: colorramp_2.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1250, 6: colorramp.outputs["Color"], 7: multiply},
        attrs={'blend_type': 'VALUE', 'data_type': 'RGBA'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.4000, 6: mix.outputs[2], 7: colorramp_1.outputs["Color"]},
        attrs={'blend_type': 'DODGE', 'data_type': 'RGBA'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Subsurface': 0.4045, 'Subsurface Radius': (0.2000, 0.2000, 0.4000), 'Subsurface Color': (0.0025, 0.0100, 0.0140, 1.0000), 'Metallic': 0.4227, 'Roughness': 0.0591, 'Clearcoat Roughness': 0.0000, 'Emission': mix_1.outputs[2]})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_bulb_2(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry = nw.new_node(Nodes.NewGeometry)
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': geometry.outputs["Pointiness"]})
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.1909
    colorramp_1.color_ramp.elements[0].color = [0.6145, 0.2344, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.3705
    colorramp_1.color_ramp.elements[1].color = [0.1139, 0.1003, 0.5000, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 0.5500
    colorramp_1.color_ramp.elements[2].color = [0.0011, 0.0013, 0.0033, 1.0000]
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Color': colorramp_1.outputs["Color"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': hue_saturation_value})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Generated"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Distortion': 9.7000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.3171, 0.3171, 0.3171, 1.0000]
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': colorramp.outputs["Color"]})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.2000, 'Distance': 0.2000, 'Height': reroute})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': reroute_1, 'Subsurface': 0.1091, 'Subsurface Radius': (0.3000, 0.7000, 1.0000), 'Subsurface Color': reroute_1, 'Specular': 0.1136, 'Roughness': 0.7318, 'Transmission': 0.4000, 'Emission Strength': 0.0000, 'Normal': bump})
    
    displacement = nw.new_node(Nodes.Displacement, input_kwargs={'Height': reroute, 'Scale': 0.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': principled_bsdf, 'Displacement': displacement},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Amount of Leaves', 12),
            ('NodeSocketInt', 'Curve Resolution', 10),
            ('NodeSocketInt', 'Profile Resolution', 16),
            ('NodeSocketFloatDistance', 'Curve Radius', 0.0300),
            ('NodeSocketFloat', 'Leaf Shape Radius', 12.0000),
            ('NodeSocketFloatDistance', 'Instance Radius', 0.0600),
            ('NodeSocketFloat', 'X Rotation', 45.0000),
            ('NodeSocketFloat', 'Y Rotation', 5.0000),
            ('NodeSocketFloat', 'Z Rotation', 0.0000),
            ('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketVector', 'End Handle Position', (0.0000, -0.1600, 0.9320)),
            ('NodeSocketVector', 'Start Handle Position', (0.0000, -0.0500, 0.5100)),
            ('NodeSocketVectorTranslation', 'End Position', (0.0000, 0.7800, -0.3760)),
            ('NodeSocketVectorTranslation', 'Start Position', (0.0000, 0.0000, -0.0940))])
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Amount of Leaves"], 'Radius': group_input.outputs["Instance Radius"]})
    
    bezier_segment_1 = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Start': (0.0000, 0.0000, 0.5000), 'Start Handle': (0.0000, 0.0000, 0.0000), 'End': (0.0000, 0.0000, 0.0000)})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': bezier_segment_1, 'Selection': endpoint_selection, 'Offset': group_input.outputs["End Position"]})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': endpoint_selection_1, 'Offset': group_input.outputs["Start Position"]})
    
    set_handle_positions = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_position_1, 'Selection': endpoint_selection, 'Offset': group_input.outputs["End Handle Position"]},
        attrs={'mode': 'RIGHT'})
    
    set_handle_positions_1 = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_handle_positions, 'Selection': endpoint_selection_1, 'Offset': group_input.outputs["Start Handle Position"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_handle_positions_1, 'Count': group_input.outputs["Curve Resolution"]})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': resample_curve})
    
    curve_tangent_1 = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent_1})
    
    radians = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["X Rotation"]}, attrs={'operation': 'RADIANS'})
    
    radians_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Y Rotation"]}, attrs={'operation': 'RADIANS'})
    
    radians_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Z Rotation"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians, 'Y': radians_1, 'Z': radians_2})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: align_euler_to_vector, 1: combine_xyz_1})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_circle_1.outputs["Curve"], 'Instance': trim_curve, 'Rotation': add.outputs["Vector"], 'Scale': (0.1500, 0.1500, 0.1500)})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0010), (0.1727, 0.3687), (0.4972, 0.6716), (0.8635, 0.3313), (0.9667, 0.1038), (1.0000, 0.0188)])
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: 0.2800}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': instance_on_points, 'Radius': multiply})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_curve_radius, 'Count': 24})
    
    quadrilateral = nw.new_node('GeometryNodeCurvePrimitiveQuadrilateral', input_kwargs={'Height': 0.2900})
    
    subdivide_curve = nw.new_node(Nodes.SubdivideCurve, input_kwargs={'Curve': quadrilateral, 'Cuts': 5})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': subdivide_curve})
    
    index = nw.new_node(Nodes.Index)
    
    pingpong = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: 1.0000}, attrs={'operation': 'PINGPONG'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"]}, attrs={'operation': 'ABSOLUTE'})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: absolute, 1: 0.9300}, attrs={'operation': 'LESS_THAN'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: pingpong, 1: less_than}, attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"], 1: 0.0100}, attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: 0.9400}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_2, 'Y': multiply_3})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Selection': multiply_1, 'Offset': combine_xyz})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': set_position_2})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': subdivision_surface})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': resample_curve_1, 'Profile Curve': mesh_to_curve, 'Fill Caps': True})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth_1, 'Material': surface.shaderfunc_to_material(shader_bulb_2)})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Radius': 0.0400})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute, 'Translation': (0.0000, 0.0000, 0.0400), 'Rotation': (0.0000, 3.1416, 0.0000)})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 0.0000
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements, input_kwargs={'Geometry': transform_1, 'Scale': 1.4500, 'Center': value})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': scale_elements_1, 'Material': surface.shaderfunc_to_material(shader_bulb_fuit_2)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_1, set_material]})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry, 'Rotation': (0.0000, 3.1416, 0.0000)})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': transform})
    
    fruit_3 = nw.new_node(nodegroup_fruit_3().name,
        input_kwargs={'Curve Resolution': 90, 'End Handle Position': (0.0691, -0.0612, 0.0940), 'Start Handle Position': (-0.0249, 0.3747, 0.7347), 'End Position': (-0.0009, 0.9040, 0.3047), 'Start Position': (-0.0249, -0.0249, -0.0249), 'Color1': (0.0000, 0.0000, 0.0000, 1.0000), 'Color2': (1.0000, 1.0000, 1.0000, 1.0000)})
    
    transform_2 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': fruit_3.outputs["Geometry"], 'Rotation': (-0.0249, -0.0249, -0.3411)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_shade_smooth, transform_2]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry_1, 'Attribute': fruit_3.outputs["Attribute"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_bulb_2, selection=selection)
apply(bpy.context.active_object)
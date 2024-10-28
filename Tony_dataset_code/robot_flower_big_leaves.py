import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_bulb_2_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry = nw.new_node(Nodes.NewGeometry)
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': geometry.outputs["Pointiness"]})
    colorramp_1.color_ramp.interpolation = "EASE"
    colorramp_1.color_ramp.elements[0].position = 0.1909
    colorramp_1.color_ramp.elements[0].color = [0.3761, 0.8164, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.5182
    colorramp_1.color_ramp.elements[1].color = [0.0398, 0.1084, 0.5000, 1.0000]
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': colorramp_1.outputs["Color"]})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Generated"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Distortion': 9.7000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.3171, 0.3171, 0.3171, 1.0000]
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': colorramp.outputs["Color"]})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.1808, 'Distance': 0.2000, 'Height': reroute})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': reroute_1, 'Subsurface': 0.1091, 'Subsurface Radius': (0.3000, 0.7000, 1.0000), 'Subsurface Color': reroute_1, 'Specular': 0.1136, 'Roughness': 0.1136, 'Transmission': 0.4000, 'Emission Strength': 0.0000, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Spiral Degrees (137.5 = Golden Ratio)', 137.5000),
            ('NodeSocketFloat', 'Spread', 1.0000),
            ('NodeSocketIntUnsigned', 'Resolution', 16),
            ('NodeSocketInt', 'Profile Resolution', 16),
            ('NodeSocketInt', 'Count', 137),
            ('NodeSocketFloat', 'Leaf Thickness', 12.0000),
            ('NodeSocketFloatDistance', 'Leaf Radius', 0.0300),
            ('NodeSocketFloat', 'Z', 0.0000),
            ('NodeSocketFloat', 'Twist', 0.0000),
            ('NodeSocketFloat', '[Open Flower] X Rotate', -64.2000),
            ('NodeSocketFloat', 'Y Rotate', 0.0000),
            ('NodeSocketFloat', 'Z Rotate', 0.0000),
            ('NodeSocketVectorTranslation', 'Start', (0.0000, 0.0000, 1.0000)),
            ('NodeSocketVectorTranslation', 'Start Handle', (0.0000, 1.0000, 0.0000)),
            ('NodeSocketVectorTranslation', 'End Handle', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVectorTranslation', 'End', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Inner spread', 1.0000),
            ('NodeSocketMaterial', 'Material', None)])
    
    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': group_input.outputs["Count"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Spread"], 1: 0.0010}, attrs={'operation': 'MULTIPLY'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: separate_xyz.outputs["Z"]}, attrs={'operation': 'MULTIPLY'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Inner spread"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: reroute_1})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add})
    
    radians = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Spiral Degrees (137.5 = Golden Ratio)"]},
        attrs={'operation': 'RADIANS'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: radians}, attrs={'operation': 'MULTIPLY'})
    
    cosine = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2}, attrs={'operation': 'COSINE'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: cosine}, attrs={'operation': 'MULTIPLY'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2}, attrs={'operation': 'SINE'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: sine}, attrs={'operation': 'MULTIPLY'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Z"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_3, 'Y': multiply_4, 'Z': reroute_4})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_line, 'Position': combine_xyz})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': set_position})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    length = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_1}, attrs={'operation': 'LENGTH'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': length.outputs["Value"]})
    
    attribute_statistic = nw.new_node(Nodes.AttributeStatistic, input_kwargs={'Geometry': mesh_to_points, 2: length.outputs["Value"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute, 2: attribute_statistic.outputs["Max"]})
    
    z_o_f_f_s_e_t_c_u_r_v_e = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range.outputs["Result"]}, label='Z OFFSET CURVE')
    z_o_f_f_s_e_t_c_u_r_v_e.color_ramp.interpolation = "EASE"
    z_o_f_f_s_e_t_c_u_r_v_e.color_ramp.elements.new(0)
    z_o_f_f_s_e_t_c_u_r_v_e.color_ramp.elements[0].position = 0.0000
    z_o_f_f_s_e_t_c_u_r_v_e.color_ramp.elements[0].color = [0.4833, 0.4833, 0.4833, 1.0000]
    z_o_f_f_s_e_t_c_u_r_v_e.color_ramp.elements[1].position = 0.3682
    z_o_f_f_s_e_t_c_u_r_v_e.color_ramp.elements[1].color = [0.3841, 0.3841, 0.3841, 1.0000]
    z_o_f_f_s_e_t_c_u_r_v_e.color_ramp.elements[2].position = 1.0000
    z_o_f_f_s_e_t_c_u_r_v_e.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': z_o_f_f_s_e_t_c_u_r_v_e.outputs["Color"]})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points, 'Offset': combine_xyz_1})
    
    bezier_segment_1 = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Start': group_input.outputs["Start"], 'Start Handle': group_input.outputs["Start Handle"], 'End Handle': group_input.outputs["End Handle"], 'End': group_input.outputs["End"]})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': bezier_segment_1, 'Selection': endpoint_selection})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_3, 'Selection': endpoint_selection_1})
    
    set_handle_positions = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_position_2, 'Selection': endpoint_selection},
        attrs={'mode': 'RIGHT'})
    
    set_handle_positions_1 = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_handle_positions, 'Selection': endpoint_selection_1})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_handle_positions_1, 'Count': group_input.outputs["Resolution"]})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': resample_curve})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter_1.outputs["Factor"]})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.0000, 0.0010), (0.1727, 0.3687), (0.4972, 0.6716), (0.8747, 0.8188), (0.9667, 0.1038), (1.0000, 0.0188)])
    
    multiply_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: float_curve_2, 1: group_input.outputs["Leaf Thickness"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': trim_curve, 'Radius': multiply_5})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_curve_radius_1, 'Count': 48})
    
    quadrilateral = nw.new_node('GeometryNodeCurvePrimitiveQuadrilateral', input_kwargs={'Height': 0.1700})
    
    subdivide_curve = nw.new_node(Nodes.SubdivideCurve, input_kwargs={'Curve': quadrilateral, 'Cuts': 6})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': subdivide_curve})
    
    index = nw.new_node(Nodes.Index)
    
    pingpong = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: 1.0000}, attrs={'operation': 'PINGPONG'})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_3})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["X"]}, attrs={'operation': 'ABSOLUTE'})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: absolute, 1: 0.9300}, attrs={'operation': 'LESS_THAN'})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: pingpong, 1: less_than}, attrs={'operation': 'MULTIPLY'})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["X"], 1: 0.0100}, attrs={'operation': 'MULTIPLY'})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Y"], 1: 0.9400}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_7, 'Y': multiply_8})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_to_mesh_2, 'Selection': multiply_6, 'Offset': combine_xyz_4})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': set_position_4})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': subdivision_surface})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': resample_curve_1, 'Profile Curve': mesh_to_curve, 'Fill Caps': True})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': group_input.outputs["Material"]})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': set_material})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': group_input.outputs["Twist"]})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    multiply_9 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_2, 1: (1.0000, 1.0000, 0.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': combine_xyz_3, 'Vector': multiply_9.outputs["Vector"]},
        attrs={'axis': 'Y'})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    o_p_e_n_c_u_r_v_e = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_xyz_1.outputs["Z"]}, label='OPEN CURVE')
    o_p_e_n_c_u_r_v_e.color_ramp.elements.new(0)
    o_p_e_n_c_u_r_v_e.color_ramp.elements[0].position = 0.0000
    o_p_e_n_c_u_r_v_e.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    o_p_e_n_c_u_r_v_e.color_ramp.elements[1].position = 0.4818
    o_p_e_n_c_u_r_v_e.color_ramp.elements[1].color = [0.5000, 0.5000, 0.5000, 1.0000]
    o_p_e_n_c_u_r_v_e.color_ramp.elements[2].position = 1.0000
    o_p_e_n_c_u_r_v_e.color_ramp.elements[2].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    align_euler_to_vector_1 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': align_euler_to_vector, 'Factor': o_p_e_n_c_u_r_v_e.outputs["Color"]},
        attrs={'axis': 'Y'})
    
    radians_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["[Open Flower] X Rotate"]},
        attrs={'operation': 'RADIANS'})
    
    radians_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Y Rotate"]}, attrs={'operation': 'RADIANS'})
    
    radians_3 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Z Rotate"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians_1, 'Y': radians_2, 'Z': radians_3})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: align_euler_to_vector_1, 1: combine_xyz_2})
    
    d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_xyz_1.outputs["Z"]}, label='DISPLACEMENT CURVE')
    d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e.color_ramp.interpolation = "B_SPLINE"
    d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e.color_ramp.elements.new(0)
    d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e.color_ramp.elements[0].position = 0.3000
    d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e.color_ramp.elements[1].position = 0.7045
    d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e.color_ramp.elements[1].color = [0.0084, 0.0084, 0.0084, 1.0000]
    d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e.color_ramp.elements[2].position = 1.0000
    d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    multiply_10 = nw.new_node(Nodes.Math,
        input_kwargs={0: d_i_s_p_l_a_c_e_m_e_n_t_c_u_r_v_e.outputs["Color"], 1: 1.6000},
        attrs={'operation': 'MULTIPLY'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_1, 'Instance': join_geometry_4, 'Rotation': add_1.outputs["Vector"], 'Scale': multiply_10})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': instance_on_points}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_bulb_2_001, selection=selection)
apply(bpy.context.active_object)
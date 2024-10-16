import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Scale': (3.4000, 24.8000, 1.0000)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': 13.9000, 'Detail': 15.0000, 'Roughness': 0.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.5273
    colorramp.color_ramp.elements[0].color = [0.0056, 0.0056, 0.0056, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5909
    colorramp.color_ramp.elements[1].color = [0.0563, 0.0181, 0.0054, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Subsurface IOR': 1.0100, 'Specular': 0.6864, 'Roughness': 0.6818})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_s_t_i_n_g_c_o_i_l_g_e_n_e_r_a_t_o_r(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketBool', 'sting type', False),
            ('NodeSocketBool', 'spiral or draw', False),
            ('NodeSocketInt', 'Count', 429),
            ('NodeSocketFloat', 'Max', 30.2000),
            ('NodeSocketString', 'spiral setting', ''),
            ('NodeSocketIntUnsigned', 'Resolution', 19),
            ('NodeSocketFloat', 'Rotations', 23.7000),
            ('NodeSocketFloatDistance', 'Height', 22.3000),
            ('NodeSocketFloatDistance', 'Radius', 1.0000)])
    
    spiral_1 = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': group_input.outputs["Resolution"], 'Rotations': group_input.outputs["Rotations"], 'Start Radius': group_input.outputs["Radius"], 'End Radius': group_input.outputs["Radius"], 'Height': group_input.outputs["Height"]})
    
    transform_5 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': spiral_1, 'Translation': (-1.2000, 8.8000, 0.1000), 'Rotation': (1.5708, 1.5708, 0.0000)})
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["spiral or draw"], 14: group_input.outputs["Geometry"], 15: transform_5})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': switch_1.outputs[6]}, attrs={'spline_type': 'BEZIER'})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_spline_type, 'Count': 140, 'Length': 0.8010},
        attrs={'mode': 'LENGTH'})
    
    resample_curve_5 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_spline_type, 'Count': group_input.outputs["Count"], 'Length': 0.8010})
    
    switch_3 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["spiral or draw"], 14: resample_curve_1, 15: resample_curve_5})
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': 7, 'Rotations': 3.0000, 'Start Radius': 0.0300, 'End Radius': 0.0300, 'Height': 0.0600})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': spiral, 'Selection': endpoint_selection, 'Offset': (0.0000, 0.1000, -0.0500)})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': endpoint_selection_1, 'Position': curve_tangent, 'Offset': (-0.4000, 0.8000, -0.0000)})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position_1, 'Count': 45})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.0135, 0.2313), (0.0337, 0.8250), (0.0449, 0.9875), (0.2172, 0.9625), (0.5099, 0.9562), (0.8855, 0.9562), (0.9377, 0.9250), (0.9596, 0.7437), (0.9815, 0.3937), (1.0000, 0.0000)])
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve, 'Radius': float_curve})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': 0.0080})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_to_mesh, 'Rotation': (1.5708, 0.0000, 0.0000), 'Scale': (0.9000, 0.9000, 0.9000)})
    
    curve_line = nw.new_node(Nodes.CurveLine)
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_line})
    
    resample_curve_3 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': transform_2, 'Count': 4})
    
    curve_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter_1.outputs["Factor"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 1.0000), (0.2545, 0.5813), (0.4818, 0.2000), (0.7182, 0.5687), (1.0000, 1.0000)], handles=['AUTO', 'AUTO', 'VECTOR', 'AUTO', 'AUTO'])
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve_3, 'Radius': float_curve_1})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_line, 'Translation': (-0.5000, 0.0000, 0.0000), 'Rotation': (0.0000, 1.5708, 0.0000)})
    
    resample_curve_4 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': transform_1, 'Count': 284})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': resample_curve_4})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: 0.0100, 1: 26.8000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0100, 1: 17.1000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 0.4000, 'Z': multiply_1})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_to_mesh_2, 'Translation': combine_xyz, 'Rotation': (0.0000, 0.0000, 1.5708), 'Scale': combine_xyz_1})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_3, 'Scale': (0.0000, 0.3000, 0.3000)})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["sting type"], 14: transform, 15: transform_4})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={3: group_input.outputs["Max"]})
    
    curve_tangent_1 = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': random_value.outputs[1], 'Vector': curve_tangent_1},
        attrs={'axis': 'Y'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': switch_3.outputs[6], 'Instance': switch.outputs[6], 'Rotation': align_euler_to_vector})
    
    curve_line_3 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 21.2000)})
    
    transform_11 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_line_3, 'Translation': (0.0000, 8.0000, 0.0000), 'Rotation': (1.5708, 0.0000, 0.0000)})
    
    resample_curve_6 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': transform_11, 'Count': 5})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': (0.0000, 0.0000, -5.1000), 'End': (0.0000, 0.0000, 0.0000)})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': 0.0800})
    
    curve_to_mesh_3 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line_1, 'Profile Curve': curve_circle_2.outputs["Curve"]})
    
    endpoint_selection_2 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': (0.0000, 0.0000, -1.9000), 'End': (0.0000, 0.0000, 0.0000)})
    
    curve_to_mesh_4 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line_2, 'Profile Curve': curve_circle_2.outputs["Curve"]})
    
    transform_8 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_to_mesh_4, 'Rotation': (0.0000, 2.4784, 0.0000)})
    
    transform_9 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_to_mesh_4, 'Rotation': (0.0000, 3.8537, 0.0000)})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_8, transform_9]})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_line_1, 'Selection': endpoint_selection_2, 'Instance': join_geometry_2})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_to_mesh_3, instance_on_points_1]})
    
    transform_10 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': join_geometry_3, 'Translation': (-1.3000, 0.1000, -1.2000), 'Rotation': (0.0000, 0.0000, 0.1309)})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': resample_curve_6, 'Instance': transform_10})
    
    switch_4 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["spiral or draw"], 15: instance_on_points_2})
    
    switch_2 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["spiral or draw"], 14: group_input.outputs["Geometry"], 15: transform_5})
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': switch_2.outputs[6], 'Count': 5816, 'Length': 0.0200},
        attrs={'mode': 'LENGTH'})
    
    index = nw.new_node(Nodes.Index)
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': resample_curve_2, 'Tilt': multiply_2})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 5, 'Radius': 0.0100})
    
    transform_6 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle_1.outputs["Curve"], 'Translation': (0.0000, 0.0000, 0.0000)})
    
    transform_7 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle_1.outputs["Curve"], 'Translation': (0.0100, 0.0000, 0.0000)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_6, transform_7]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_curve_tilt, 'Profile Curve': join_geometry_1})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [instance_on_points, switch_4.outputs[6], curve_to_mesh_1]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': surface.shaderfunc_to_material(shader_material)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_s_t_i_n_g_c_o_i_l_g_e_n_e_r_a_t_o_r, selection=selection, attributes=[])
    surface.add_material(obj, shader_material, selection=selection)
apply(bpy.context.active_object)
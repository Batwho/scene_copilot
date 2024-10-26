import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_count_faces', singleton=False, type='GeometryNodeTree')
def nodegroup_count_faces(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Value', 0)])
    
    index_1 = nw.new_node(Nodes.Index)
    
    corners_of_face = nw.new_node('GeometryNodeCornersOfFace', input_kwargs={'Face Index': index_1})
    
    vertex_of_corner = nw.new_node('GeometryNodeVertexOfCorner', input_kwargs={'Corner Index': corners_of_face.outputs["Corner Index"]})
    
    sample_index = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 2: group_input.outputs["Value"], 'Index': vertex_of_corner},
        attrs={'data_type': 'INT'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': sample_index.outputs[1]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_perturb', singleton=False, type='GeometryNodeTree')
def nodegroup_perturb(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketBool', 'Evaluate Curve', False),
            ('NodeSocketFloat', 'Factor', 1.0000),
            ('NodeSocketVector', 'Scale', (1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloat', 'Noise Size', 0.5000),
            ('NodeSocketInt', 'ID', 0)])
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': group_input.outputs["Geometry"]},
        attrs={'mode': 'EVALUATED'})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["Evaluate Curve"], 14: group_input.outputs["Geometry"], 15: resample_curve})
    
    position = nw.new_node(Nodes.InputPosition)
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: (111.0000, 0.0000, 0.0000), 'Scale': group_input.outputs["ID"]},
        attrs={'operation': 'SCALE'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 1: scale.outputs["Vector"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': add.outputs["Vector"], 'Scale': group_input.outputs["Noise Size"]})
    
    multiply_add = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (2.0000, 2.0000, 2.0000), 2: (-1.0000, -1.0000, -1.0000)},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_add.outputs["Vector"], 'Scale': group_input.outputs["Factor"]},
        attrs={'operation': 'SCALE'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale_1.outputs["Vector"], 1: group_input.outputs["Scale"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': switch.outputs[6], 'Offset': multiply.outputs["Vector"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_position_3}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_quadratic_interpolation', singleton=False, type='GeometryNodeTree')
def nodegroup_quadratic_interpolation(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'a', 0.5000),
            ('NodeSocketFloat', 'b', 0.5000),
            ('NodeSocketFloat', 'c', 0.5000),
            ('NodeSocketFloat', 'd', 0.5000),
            ('NodeSocketFloat', 't', 0.5000)])
    
    inv = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: group_input.outputs["t"]},
        label='inv',
        attrs={'operation': 'SUBTRACT'})
    
    inv_inv = nw.new_node(Nodes.Math, input_kwargs={0: inv, 1: inv}, label='inv * inv', attrs={'operation': 'MULTIPLY'})
    
    inv_inv_inv = nw.new_node(Nodes.Math, input_kwargs={0: inv_inv, 1: inv}, label='inv * inv * inv', attrs={'operation': 'MULTIPLY'})
    
    inv_inv_inv_a = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["a"], 1: inv_inv_inv},
        label='inv * inv * inv * a',
        attrs={'operation': 'MULTIPLY'})
    
    inv_inv_t = nw.new_node(Nodes.Math,
        input_kwargs={0: inv_inv, 1: group_input.outputs["t"]},
        label='inv * inv * t',
        attrs={'operation': 'MULTIPLY'})
    
    inv_inv_t_b = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["b"], 1: inv_inv_t},
        label='inv * inv * t * b',
        attrs={'operation': 'MULTIPLY'})
    
    times3 = nw.new_node(Nodes.Math, input_kwargs={0: inv_inv_t_b, 1: 3.0000}, label='times3', attrs={'operation': 'MULTIPLY'})
    
    sum = nw.new_node(Nodes.Math, input_kwargs={0: inv_inv_inv_a, 1: times3}, label='sum')
    
    t_t = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["t"], 1: group_input.outputs["t"]},
        label='t * t',
        attrs={'operation': 'MULTIPLY'})
    
    inv_t_t = nw.new_node(Nodes.Math, input_kwargs={0: inv, 1: t_t}, label='inv * t * t', attrs={'operation': 'MULTIPLY'})
    
    inv_t_t_c = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["c"], 1: inv_t_t},
        label='inv * t * t * c',
        attrs={'operation': 'MULTIPLY'})
    
    times3_1 = nw.new_node(Nodes.Math, input_kwargs={0: inv_t_t_c, 1: 3.0000}, label='times3', attrs={'operation': 'MULTIPLY'})
    
    t_t_t = nw.new_node(Nodes.Math,
        input_kwargs={0: t_t, 1: group_input.outputs["t"]},
        label='t * t * t',
        attrs={'operation': 'MULTIPLY'})
    
    t_t_t_d = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["d"], 1: t_t_t},
        label='t * t * t * d',
        attrs={'operation': 'MULTIPLY'})
    
    sum_1 = nw.new_node(Nodes.Math, input_kwargs={0: times3_1, 1: t_t_t_d}, label='sum')
    
    sum_2 = nw.new_node(Nodes.Math, input_kwargs={0: sum, 1: sum_1}, label='sum')
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'value': sum_2}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_curve_quadratic_radius', singleton=False, type='GeometryNodeTree')
def nodegroup_curve_quadratic_radius(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketBool', 'Evaluate Curve', False),
            ('NodeSocketFloat', 'Radius 1', 0.0000),
            ('NodeSocketFloat', 'Radius 2', 0.8000),
            ('NodeSocketFloat', 'Radius 3', 0.9000),
            ('NodeSocketFloat', 'Radius 4', 1.0000),
            ('NodeSocketFloat', 'Exponent', 1.0000)])
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': group_input.outputs["Curve"]}, attrs={'mode': 'EVALUATED'})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["Evaluate Curve"], 14: group_input.outputs["Curve"], 15: resample_curve})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: spline_parameter.outputs["Factor"]},
        attrs={'operation': 'SUBTRACT'})
    
    power = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_parameter.outputs["Factor"], 1: group_input.outputs["Exponent"]},
        attrs={'operation': 'POWER'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: power}, attrs={'operation': 'SUBTRACT'})
    
    power_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: group_input.outputs["Exponent"]}, attrs={'operation': 'POWER'})
    
    mix = nw.new_node(Nodes.Mix, input_kwargs={0: subtract, 2: subtract_1, 3: power_1})
    
    quadratic_interpolation = nw.new_node(nodegroup_quadratic_interpolation().name,
        input_kwargs={'a': group_input.outputs["Radius 1"], 'b': group_input.outputs["Radius 2"], 'c': group_input.outputs["Radius 3"], 'd': group_input.outputs["Radius 4"], 't': mix.outputs["Result"]})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': switch.outputs[6], 'Radius': quadratic_interpolation})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Curve': set_curve_radius}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_curve_solidify_u_v', singleton=False, type='GeometryNodeTree')
def nodegroup_curve_solidify_u_v(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Resolution', 16),
            ('NodeSocketFloatDistance', 'Radius', 0.1000),
            ('NodeSocketString', 'UV', 'uv')])
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 2: spline_parameter.outputs["Length"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Resolution"], 'Radius': group_input.outputs["Radius"]})
    
    index = nw.new_node(Nodes.Index)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 5: index},
        attrs={'data_type': 'INT'})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': capture_attribute.outputs["Geometry"], 'Profile Curve': capture_attribute_1.outputs["Geometry"], 'Fill Caps': True})
    
    countfaces = nw.new_node(nodegroup_count_faces().name,
        input_kwargs={'Geometry': curve_to_mesh, 'Value': capture_attribute_1.outputs[5]})
    
    capture_attribute_2 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_to_mesh, 5: countfaces},
        attrs={'domain': 'FACE', 'data_type': 'INT'})
    
    face_of_corner = nw.new_node('GeometryNodeFaceOfCorner')
    
    equal = nw.new_node(Nodes.Compare,
        input_kwargs={2: face_of_corner.outputs["Index in Face"], 3: 2},
        attrs={'data_type': 'INT', 'operation': 'EQUAL'})
    
    equal_1 = nw.new_node(Nodes.Compare,
        input_kwargs={2: face_of_corner.outputs["Index in Face"], 3: 1},
        attrs={'data_type': 'INT', 'operation': 'EQUAL'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: equal, 1: equal_1}, attrs={'use_clamp': True})
    
    capture_attribute_3 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': capture_attribute_2.outputs["Geometry"], 2: add},
        attrs={'domain': 'CORNER'})
    
    capture_attribute_4 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': capture_attribute_3.outputs["Geometry"], 2: capture_attribute_2.outputs[5]},
        attrs={'domain': 'CORNER'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: capture_attribute_3.outputs[2], 1: capture_attribute_4.outputs[2]})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: group_input.outputs["Resolution"]}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': capture_attribute.outputs[2], 'Y': divide})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': capture_attribute_4.outputs["Geometry"], 'Name': group_input.outputs["UV"], 3: combine_xyz},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT2'})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': store_named_attribute})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_shade_smooth}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_u_v_transform', singleton=False, type='GeometryNodeTree')
def nodegroup_u_v_transform(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketString', 'UV Name', ''),
            ('NodeSocketFloatAngle', 'Rotate', 0.0000),
            ('NodeSocketVector', 'Scale', (1.0000, 1.0000, 1.0000)),
            ('NodeSocketVector', 'Offset', (0.0000, 0.0000, 0.0000))])
    
    named_attribute = nw.new_node(Nodes.NamedAttribute,
        input_kwargs={'Name': group_input.outputs["UV Name"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: named_attribute.outputs["Attribute"], 1: group_input.outputs["Scale"]},
        attrs={'operation': 'MULTIPLY'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': multiply.outputs["Vector"], 'Angle': group_input.outputs["Rotate"]})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: vector_rotate, 1: group_input.outputs["Offset"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Name': group_input.outputs["UV Name"], 3: add.outputs["Vector"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT2'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': store_named_attribute}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_smooth_avg', singleton=False, type='GeometryNodeTree')
def nodegroup_smooth_avg(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketBool', 'Selection', True),
            ('NodeSocketFloatFactor', 'Amount', 1.0000)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    position = nw.new_node(Nodes.InputPosition)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': reroute, 1: position},
        attrs={'domain': 'FACE', 'data_type': 'FLOAT_VECTOR'})
    
    corners_of_vertex = nw.new_node('GeometryNodeCornersOfVertex')
    
    face_of_corner = nw.new_node('GeometryNodeFaceOfCorner', input_kwargs={'Corner Index': corners_of_vertex.outputs["Corner Index"]})
    
    sample_index = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 3: capture_attribute.outputs["Attribute"], 'Index': face_of_corner.outputs["Face Index"]},
        attrs={'domain': 'FACE', 'data_type': 'FLOAT_VECTOR'})
    
    corners_of_vertex_1 = nw.new_node('GeometryNodeCornersOfVertex', input_kwargs={'Sort Index': 1})
    
    face_of_corner_1 = nw.new_node('GeometryNodeFaceOfCorner', input_kwargs={'Corner Index': corners_of_vertex_1.outputs["Corner Index"]})
    
    sample_index_1 = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 3: capture_attribute.outputs["Attribute"], 'Index': face_of_corner_1.outputs["Face Index"]},
        attrs={'domain': 'FACE', 'data_type': 'FLOAT_VECTOR'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: sample_index.outputs[2], 1: sample_index_1.outputs[2]})
    
    corners_of_vertex_2 = nw.new_node('GeometryNodeCornersOfVertex', input_kwargs={'Sort Index': 2})
    
    face_of_corner_2 = nw.new_node('GeometryNodeFaceOfCorner', input_kwargs={'Corner Index': corners_of_vertex_2.outputs["Corner Index"]})
    
    sample_index_2 = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 3: capture_attribute.outputs["Attribute"], 'Index': face_of_corner_2.outputs["Face Index"]},
        attrs={'domain': 'FACE', 'data_type': 'FLOAT_VECTOR'})
    
    corners_of_vertex_3 = nw.new_node('GeometryNodeCornersOfVertex', input_kwargs={'Sort Index': 3})
    
    face_of_corner_3 = nw.new_node('GeometryNodeFaceOfCorner', input_kwargs={'Corner Index': corners_of_vertex_3.outputs["Corner Index"]})
    
    sample_index_3 = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 3: capture_attribute.outputs["Attribute"], 'Index': face_of_corner_3.outputs["Face Index"]},
        attrs={'domain': 'FACE', 'data_type': 'FLOAT_VECTOR'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: sample_index_2.outputs[2], 1: sample_index_3.outputs[2]})
    
    add_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: add.outputs["Vector"], 1: add_1.outputs["Vector"]})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add_2.outputs["Vector"], 'Scale': 0.2500},
        attrs={'operation': 'SCALE'})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input.outputs["Selection"], 8: position, 9: scale.outputs["Vector"]},
        attrs={'input_type': 'VECTOR'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["Amount"], 4: position_1, 5: switch.outputs[3]},
        attrs={'data_type': 'VECTOR'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute, 'Position': mix.outputs[1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_position_1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_tree_trunk_gen', singleton=False, type='GeometryNodeTree')
def nodegroup_tree_trunk_gen(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    curve_line = nw.new_node(Nodes.CurveLine)
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'not used', None),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketFloatDistance', 'Resolution', 0.2500),
            ('NodeSocketFloat', 'Noise Freq', 1.0000),
            ('NodeSocketFloat', 'Noise Amp', 0.5000),
            ('NodeSocketFloat', 'Z Min', 4.0000),
            ('NodeSocketFloat', 'Z Max', 8.0000)])
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': -2.0000, 'Y': -2.0000, 'Z': group_input.outputs["Z Min"]})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 2.0000, 'Y': 2.0000, 'Z': group_input.outputs["Z Max"]})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: combine_xyz, 1: combine_xyz_1, 'Seed': group_input.outputs["Seed"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_line, 'Selection': endpoint_selection, 'Offset': random_value.outputs["Value"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_position, 'Length': group_input.outputs["Resolution"]},
        attrs={'mode': 'LENGTH'})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.5091, 0.9875), (1.0000, 0.7563)])
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: float_curve, 1: group_input.outputs["Noise Amp"]},
        attrs={'operation': 'MULTIPLY'})
    
    index = nw.new_node(Nodes.Index)
    
    evaluate_on_domain = nw.new_node(Nodes.EvaluateonDomain, input_kwargs={1: index}, attrs={'domain': 'CURVE', 'data_type': 'INT'})
    
    perturb = nw.new_node(nodegroup_perturb().name,
        input_kwargs={'Geometry': resample_curve, 'Factor': multiply, 'Noise Size': group_input.outputs["Noise Freq"], 'ID': evaluate_on_domain.outputs[1]})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 2, 'End Size': 0})
    
    vector = nw.new_node(Nodes.Vector)
    vector.vector = (0.0000, 0.0000, 0.0000)
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': perturb, 'Selection': endpoint_selection_1, 'Position': vector})
    
    endpoint_selection_2 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_2, 'Selection': endpoint_selection_2, 'Offset': (0.0000, 0.0000, -0.5000)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Trunk Curve': set_position_3}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_curve_select_random', singleton=False, type='GeometryNodeTree')
def nodegroup_curve_select_random(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketBool', 'Delete Interior', False),
            ('NodeSocketFloatFactor', 'Probability', 0.5000),
            ('NodeSocketInt', 'Seed', 0)])
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': group_input_1.outputs["Curve"]})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={'Probability': group_input_1.outputs["Probability"], 'Seed': group_input_1.outputs["Seed"]},
        attrs={'data_type': 'BOOLEAN'})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': curve_to_mesh, 'Selection': random_value.outputs[3]},
        attrs={'domain': 'EDGE'})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': separate_geometry.outputs["Selection"]})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection)
    
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: endpoint_selection}, attrs={'operation': 'NOT'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': mesh_to_curve, 'Selection': op_not})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_1.outputs["Delete Interior"], 14: mesh_to_curve, 15: delete_geometry})
    
    curve_tilt = nw.new_node('GeometryNodeInputCurveTilt')
    
    radius = nw.new_node(Nodes.Radius)
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': curve_tilt, 'Y': radius, 'Z': spline_parameter.outputs["Factor"]})
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': group_input_1.outputs["Curve"], 1: combine_xyz},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': capture_attribute.outputs["Geometry"]})
    
    sample_nearest = nw.new_node(Nodes.SampleNearest, input_kwargs={'Geometry': curve_to_mesh_1})
    
    sample_index = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': curve_to_mesh_1, 3: capture_attribute.outputs["Attribute"], 'Index': sample_nearest},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': sample_index.outputs[2]})
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': switch.outputs[6], 2: separate_xyz.outputs["Z"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["Y"]})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius,
        input_kwargs={'Curve': capture_attribute_1.outputs["Geometry"], 'Radius': reroute_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["X"]})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': set_curve_radius, 'Tilt': reroute})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Segments': set_curve_tilt, 'Spline Factor': capture_attribute_1.outputs[2]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_tree\u2002_branch_gen', singleton=False, type='GeometryNodeTree')
def nodegroup_tree_branch_gen(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatDistance', 'Resolution', 0.2500),
            ('NodeSocketFloat', 'Length Basis', 0.5000),
            ('NodeSocketFloat', 'Length Scale', 4.0000),
            ('NodeSocketFloat', 'Bendiness', 0.2500),
            ('NodeSocketFloat', 'Noise Freq', 1.0000),
            ('NodeSocketFloat', 'Noise Amp', 0.5000),
            ('NodeSocketInt', 'Seed', 0)])
    
    curve_tangent_1 = nw.new_node(Nodes.CurveTangent)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 1: curve_tangent_1},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': capture_attribute.outputs["Geometry"], 'Count': 3})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0, 'End Size': 2})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: group_input.outputs["Length Basis"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: subtract, 1: group_input.outputs["Length Scale"]},
        attrs={'operation': 'MULTIPLY'})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: capture_attribute.outputs["Attribute"], 'Scale': multiply},
        attrs={'operation': 'SCALE'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': resample_curve, 'Selection': endpoint_selection_1, 'Offset': scale.outputs["Vector"]})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Seed"], 1: 22.0000})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-1.0000, -1.0000, 0.0000), 1: (1.0000, 1.0000, 0.0000), 'Seed': add},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Seed"], 1: 11.0000})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={2: -3.1416, 3: 3.1416, 'Seed': add_1})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: random_value_1.outputs[1], 1: group_input.outputs["Bendiness"]},
        attrs={'operation': 'MULTIPLY'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': scale.outputs["Vector"], 'Axis': random_value.outputs["Value"], 'Angle': multiply_1})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_1, 'Selection': endpoint_selection, 'Offset': vector_rotate})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position, 'Count': 4})
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': resample_curve_1, 'Count': 6})
    
    resample_curve_3 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': resample_curve_2})
    
    resample_curve_4 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': resample_curve_3, 'Length': group_input.outputs["Resolution"]},
        attrs={'mode': 'LENGTH'})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.5091, 0.9875), (1.0000, 0.7563)])
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: float_curve, 1: group_input.outputs["Noise Amp"]},
        attrs={'operation': 'MULTIPLY'})
    
    index = nw.new_node(Nodes.Index)
    
    evaluate_on_domain = nw.new_node(Nodes.EvaluateonDomain, input_kwargs={1: index}, attrs={'domain': 'CURVE', 'data_type': 'INT'})
    
    perturb = nw.new_node(nodegroup_perturb().name,
        input_kwargs={'Geometry': resample_curve_4, 'Factor': multiply_2, 'Noise Size': group_input.outputs["Noise Freq"], 'ID': evaluate_on_domain.outputs[1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Curve': perturb}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_curve_select_range', singleton=False, type='GeometryNodeTree')
def nodegroup_curve_select_range(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketBool', 'Evaluate', True),
            ('NodeSocketFloat', 'Min', 0.2500),
            ('NodeSocketFloat', 'Max', 0.7500)])
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': group_input.outputs["Curve"]}, attrs={'mode': 'EVALUATED'})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["Evaluate"], 14: group_input.outputs["Curve"], 15: resample_curve})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: spline_parameter.outputs["Factor"], 1: group_input.outputs["Min"]})
    
    less_than = nw.new_node(Nodes.Compare,
        input_kwargs={0: spline_parameter.outputs["Factor"], 1: group_input.outputs["Max"]},
        attrs={'operation': 'LESS_THAN'})
    
    op_and = nw.new_node(Nodes.BooleanMath, input_kwargs={0: greater_than, 1: less_than})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry, input_kwargs={'Geometry': switch.outputs[6], 'Selection': op_and})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Selection': separate_geometry.outputs["Selection"], 'Inverted': separate_geometry.outputs["Inverted"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_tree\u2002_leaf_instancer', singleton=False, type='GeometryNodeTree')
def nodegroup_tree_leaf_instancer(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketCollection', 'Instances', None),
            ('NodeSocketFloatDistance', 'Density', 0.7500),
            ('NodeSocketVector', 'Rotation Randomness', (0.2000, 0.2000, 0.7000)),
            ('NodeSocketFloat', 'Scale Randomness', 0.5000),
            ('NodeSocketFloat', 'Scale Min', 1.0000),
            ('NodeSocketFloat', 'Scale Curve A', 0.0000),
            ('NodeSocketFloat', 'Scale Curve B', 3.6000),
            ('NodeSocketFloat', 'Scale Curve C', 5.0000),
            ('NodeSocketFloat', 'Scale Curve D', 3.0000)])
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 1: curve_tangent},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 2: spline_parameter.outputs["Factor"]})
    
    curve_to_points = nw.new_node(Nodes.CurveToPoints,
        input_kwargs={'Curve': capture_attribute_1.outputs["Geometry"], 'Length': group_input.outputs["Density"]},
        attrs={'mode': 'LENGTH'})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, attrs={'data_type': 'BOOLEAN'})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': curve_to_points.outputs["Points"], 'Selection': random_value_1.outputs[3]})
    
    random_value_3 = nw.new_node(Nodes.RandomValue, input_kwargs={3: group_input.outputs["Scale Randomness"]})
    
    quadratic_interpolation = nw.new_node(nodegroup_quadratic_interpolation().name,
        input_kwargs={'a': group_input.outputs["Scale Curve A"], 'b': group_input.outputs["Scale Curve B"], 'c': group_input.outputs["Scale Curve C"], 'd': group_input.outputs["Scale Curve D"], 't': capture_attribute_1.outputs[2]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: random_value_3.outputs[1], 1: quadratic_interpolation})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: add, 1: group_input.outputs["Scale Min"]})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': group_input.outputs["Instances"], 'Separate Children': True, 'Reset Children': True})
    
    domain_size = nw.new_node(Nodes.DomainSize, input_kwargs={'Geometry': collection_info}, attrs={'component': 'INSTANCES'})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={5: domain_size.outputs["Instance Count"]}, attrs={'data_type': 'INT'})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Vector': capture_attribute.outputs["Attribute"]},
        attrs={'axis': 'Z'})
    
    align_euler_to_vector_1 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': align_euler_to_vector, 'Factor': 0.0000},
        attrs={'axis': 'Y', 'pivot_axis': 'Z'})
    
    cross_product = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: capture_attribute.outputs["Attribute"], 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'CROSS_PRODUCT'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': group_input.outputs["Rotation Randomness"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"], 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={2: multiply, 3: separate_xyz.outputs["X"]})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_2.outputs[1], 1: 3.1416}, attrs={'operation': 'MULTIPLY'})
    
    rotate_euler = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': align_euler_to_vector_1, 'Axis': cross_product.outputs["Vector"], 'Angle': multiply_1})
    
    cross_product_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: capture_attribute.outputs["Attribute"], 1: cross_product.outputs["Vector"]},
        attrs={'operation': 'CROSS_PRODUCT'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    random_value_4 = nw.new_node(Nodes.RandomValue, input_kwargs={2: multiply_2, 3: separate_xyz.outputs["Y"]})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_4.outputs[1], 1: 3.1416}, attrs={'operation': 'MULTIPLY'})
    
    rotate_euler_1 = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': rotate_euler, 'Axis': cross_product_1.outputs["Vector"], 'Angle': multiply_3})
    
    vector = nw.new_node(Nodes.Vector)
    vector.vector = (0.0000, 0.0000, 1.0000)
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': vector, 'Rotation': rotate_euler_1},
        attrs={'rotation_type': 'EULER_XYZ'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    random_value_5 = nw.new_node(Nodes.RandomValue, input_kwargs={2: multiply_4, 3: separate_xyz.outputs["Z"]})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_5.outputs[1], 1: 3.1416}, attrs={'operation': 'MULTIPLY'})
    
    rotate_euler_2 = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': rotate_euler_1, 'Axis': vector_rotate, 'Angle': multiply_5})
    
    align_euler_to_vector_2 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': rotate_euler_2, 'Factor': 0.5000},
        attrs={'axis': 'Z'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': separate_geometry.outputs["Selection"], 'Selection': greater_than, 'Instance': collection_info, 'Pick Instance': True, 'Instance Index': random_value.outputs[2], 'Rotation': align_euler_to_vector_2, 'Scale': add})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Instances': instance_on_points}, attrs={'is_active_output': True})

def shader_trunk(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.1282, 0.0644, 0.0295, 1.0000), 'Roughness': 0.8000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Seed', 0),
            ('NodeSocketInt', 'Resolution', 4),
            ('NodeSocketMaterial', 'Material', None), #surface.shaderfunc_to_material(shader_trunk)
            ('NodeSocketFloat', 'Height Control', 4.0000),
            ('NodeSocketFloat', 'Twistiness', 1.0000),
            ('NodeSocketFloat', 'Split Min', 0.1500),
            ('NodeSocketFloat', 'Split Max', 0.5000),
            ('NodeSocketFloatFactor', 'Split Probability', 0.3000),
            ('NodeSocketFloat', 'Split Length', 4.4000),
            ('NodeSocketFloat', 'Split Bend', 0.2500),
            ('NodeSocketFloatFactor', 'Branch Probability', 0.3000),
            ('NodeSocketFloat', 'Branch Length', 4.4000),
            ('NodeSocketFloat', 'Branch Bend', 0.2500),
            ('NodeSocketCollection', 'Leaf Instances', None),
            ('NodeSocketFloatDistance', 'Leaf Density', 1.0000),
            ('NodeSocketFloat', 'Leaf Scale', 1.0000)])
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: group_input_1.outputs["Resolution"]},
        attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input_1.outputs["Twistiness"]}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Twistiness"], 1: 1.5000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Height Control"], 1: 2.0000},
        attrs={'operation': 'MULTIPLY'})
    
    tree_trunk_gen = nw.new_node(nodegroup_tree_trunk_gen().name,
        input_kwargs={'Seed': group_input_1.outputs["Seed"], 'Resolution': divide, 'Noise Freq': multiply, 'Noise Amp': multiply_1, 'Z Min': group_input_1.outputs["Height Control"], 'Z Max': multiply_2})
    
    curve_select_range = nw.new_node(nodegroup_curve_select_range().name,
        input_kwargs={'Curve': tree_trunk_gen, 'Min': group_input_1.outputs["Split Min"], 'Max': group_input_1.outputs["Split Max"]})
    
    curve_select_random = nw.new_node(nodegroup_curve_select_random().name,
        input_kwargs={'Curve': curve_select_range.outputs["Selection"], 'Delete Interior': True, 'Probability': group_input_1.outputs["Split Probability"], 'Seed': group_input_1.outputs["Seed"]})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_1.outputs["Twistiness"]}, attrs={'operation': 'MULTIPLY'})
    
    tree_branch_gen = nw.new_node(nodegroup_tree_branch_gen().name,
        input_kwargs={'Geometry': curve_select_random.outputs["Segments"], 'Resolution': divide, 'Length Basis': curve_select_random.outputs["Spline Factor"], 'Length Scale': group_input_1.outputs["Split Length"], 'Bendiness': group_input_1.outputs["Split Bend"], 'Noise Freq': multiply_3, 'Noise Amp': group_input_1.outputs["Twistiness"], 'Seed': group_input_1.outputs["Seed"]})
    
    curve_select_random_1 = nw.new_node(nodegroup_curve_select_random().name,
        input_kwargs={'Curve': tree_branch_gen, 'Delete Interior': True, 'Probability': group_input_1.outputs["Branch Probability"], 'Seed': group_input_1.outputs["Seed"]})
    
    tree_branch_gen_1 = nw.new_node(nodegroup_tree_branch_gen().name,
        input_kwargs={'Geometry': curve_select_random_1.outputs["Segments"], 'Resolution': divide, 'Length Basis': curve_select_random_1.outputs["Spline Factor"], 'Length Scale': group_input_1.outputs["Branch Length"], 'Bendiness': group_input_1.outputs["Branch Bend"], 'Noise Freq': multiply_3, 'Noise Amp': group_input_1.outputs["Twistiness"], 'Seed': group_input_1.outputs["Seed"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': tree_branch_gen_1})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    curve_select_range_1 = nw.new_node(nodegroup_curve_select_range().name, input_kwargs={'Curve': reroute_7, 'Min': 0.3000, 'Max': 1.0000})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': tree_trunk_gen})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    curve_select_range_2 = nw.new_node(nodegroup_curve_select_range().name, input_kwargs={'Curve': reroute_10, 'Min': 0.6000, 'Max': 1.0000})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': tree_branch_gen})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    curve_select_range_3 = nw.new_node(nodegroup_curve_select_range().name, input_kwargs={'Curve': reroute_9, 'Min': 0.5000, 'Max': 1.0000})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [curve_select_range_1.outputs["Selection"], curve_select_range_2.outputs["Selection"], curve_select_range_3.outputs["Selection"]]})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Leaf Scale"], 1: 3.6000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Leaf Scale"], 1: 5.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Leaf Scale"], 1: 3.0000},
        attrs={'operation': 'MULTIPLY'})
    
    tree_leaf_instancer = nw.new_node(nodegroup_tree_leaf_instancer().name,
        input_kwargs={'Geometry': join_geometry_2, 'Instances': group_input_1.outputs["Leaf Instances"], 'Density': group_input_1.outputs["Leaf Density"], 'Scale Randomness': 1.0000, 'Scale Curve B': multiply_4, 'Scale Curve C': multiply_5, 'Scale Curve D': multiply_6})
    
    curve_quadratic_radius = nw.new_node(nodegroup_curve_quadratic_radius().name,
        input_kwargs={'Curve': reroute_3, 'Radius 1': 0.0100, 'Radius 2': 0.3000, 'Radius 3': 0.8000, 'Exponent': 2.0000})
    
    curve_solidify_uv = nw.new_node(nodegroup_curve_solidify_u_v().name,
        input_kwargs={'Geometry': curve_quadratic_radius, 'Resolution': 8, 'Radius': 0.3500})
    
    curve_quadratic_radius_1 = nw.new_node(nodegroup_curve_quadratic_radius().name,
        input_kwargs={'Curve': reroute_4, 'Radius 1': 0.0100, 'Radius 2': 0.3000, 'Radius 3': 0.8000, 'Radius 4': 0.5000, 'Exponent': 3.0000})
    
    curve_solidify_uv_1 = nw.new_node(nodegroup_curve_solidify_u_v().name,
        input_kwargs={'Geometry': curve_quadratic_radius_1, 'Resolution': 6, 'Radius': 0.2500})
    
    curve_quadratic_radius_2 = nw.new_node(nodegroup_curve_quadratic_radius().name,
        input_kwargs={'Curve': reroute_5, 'Radius 1': 0.0100, 'Radius 2': 0.3000, 'Radius 3': 0.8000, 'Radius 4': 0.5000, 'Exponent': 3.0000})
    
    curve_solidify_uv_2 = nw.new_node(nodegroup_curve_solidify_u_v().name,
        input_kwargs={'Geometry': curve_quadratic_radius_2, 'Resolution': 5, 'Radius': 0.1500})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [curve_solidify_uv, curve_solidify_uv_1, curve_solidify_uv_2]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': group_input_1.outputs["Material"]})
    
    uv_transform = nw.new_node(nodegroup_u_v_transform().name,
        input_kwargs={'Geometry': set_material, 'UV Name': 'uv', 'Rotate': 1.5708, 'Scale': (1.2000, 0.6000, 0.6000)})
    
    smooth_avg = nw.new_node(nodegroup_smooth_avg().name, input_kwargs={'Geometry': uv_transform, 'Amount': 0.5000})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [tree_leaf_instancer, smooth_avg]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_1}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_trunk, selection=selection)
apply(bpy.context.active_object)
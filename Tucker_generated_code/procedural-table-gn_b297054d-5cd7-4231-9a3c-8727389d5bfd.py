import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_multiswitch__v', singleton=False, type='GeometryNodeTree')
def nodegroup_multiswitch__v(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Switch', 0),
            ('NodeSocketVector', '0', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', '1', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', '2', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', '3', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', '4', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', '5', (0.0000, 0.0000, 0.0000))])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Switch"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_6, 3: 5}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_5, 3: 4}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_2 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_4, 3: 3}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_3 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_3, 3: 2}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_4 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_2, 3: 1}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_5 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    switch_3 = nw.new_node(Nodes.Switch, input_kwargs={0: equal_5, 9: group_input.outputs["0"]}, attrs={'input_type': 'VECTOR'})
    
    switch_4 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal_4, 8: switch_3.outputs[3], 9: group_input.outputs["1"]},
        attrs={'input_type': 'VECTOR'})
    
    switch_5 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal_3, 8: switch_4.outputs[3], 9: group_input.outputs["2"]},
        attrs={'input_type': 'VECTOR'})
    
    switch_6 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal_2, 8: switch_5.outputs[3], 9: group_input.outputs["3"]},
        attrs={'input_type': 'VECTOR'})
    
    switch_7 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal_1, 8: switch_6.outputs[3], 9: group_input.outputs["4"]},
        attrs={'input_type': 'VECTOR'})
    
    switch_8 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal, 8: switch_7.outputs[3], 9: group_input.outputs["5"]},
        attrs={'input_type': 'VECTOR'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': switch_8.outputs[3]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_transform_selection', singleton=False, type='GeometryNodeTree')
def nodegroup_transform_selection(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketBool', 'Selection', True),
            ('NodeSocketVector', 'Location', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVectorEuler', 'Rotation', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Rotation Center', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Scale', (1.0000, 1.0000, 1.0000))])
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    position = nw.new_node(Nodes.InputPosition)
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': position, 'Center': group_input.outputs["Rotation Center"], 'Rotation': group_input.outputs["Rotation"]},
        attrs={'rotation_type': 'EULER_XYZ'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: vector_rotate, 1: group_input.outputs["Scale"]},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: multiply.outputs["Vector"], 1: group_input.outputs["Location"]})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': reroute_5, 'Selection': group_input.outputs["Selection"], 'Position': add.outputs["Vector"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': set_position_1, 'Selection': group_input.outputs["Selection"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_multiswitch__f', singleton=False, type='GeometryNodeTree')
def nodegroup_multiswitch__f(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Switch', 0),
            ('NodeSocketFloat', '0', 0.0000),
            ('NodeSocketFloat', '1', 0.0000),
            ('NodeSocketFloat', '2', 0.0000),
            ('NodeSocketFloat', '3', 0.0000),
            ('NodeSocketFloat', '4', 0.0000),
            ('NodeSocketFloat', '5', 0.0000)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Switch"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_6, 3: 5}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_5, 3: 4}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_2 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_4, 3: 3}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_3 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_3, 3: 2}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_4 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_2, 3: 1}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_5 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    switch_3 = nw.new_node(Nodes.Switch, input_kwargs={0: equal_5, 3: group_input.outputs["0"]}, attrs={'input_type': 'FLOAT'})
    
    switch_4 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal_4, 2: switch_3.outputs["Output"], 3: group_input.outputs["1"]},
        attrs={'input_type': 'FLOAT'})
    
    switch_5 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal_3, 2: switch_4.outputs["Output"], 3: group_input.outputs["2"]},
        attrs={'input_type': 'FLOAT'})
    
    switch_6 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal_2, 2: switch_5.outputs["Output"], 3: group_input.outputs["3"]},
        attrs={'input_type': 'FLOAT'})
    
    switch_7 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal_1, 2: switch_6.outputs["Output"], 3: group_input.outputs["4"]},
        attrs={'input_type': 'FLOAT'})
    
    switch_8 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal, 2: switch_7.outputs["Output"], 3: group_input.outputs["5"]},
        attrs={'input_type': 'FLOAT'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Output': switch_8.outputs["Output"]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_curve_line_length', singleton=False, type='GeometryNodeTree')
def nodegroup_curve_line_length(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Length', 0.5000),
            ('NodeSocketInt', 'Orientation X / Y / Z', 0)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Orientation X / Y / Z"]})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Length"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply})
    
    multiswitch_v = nw.new_node(nodegroup_multiswitch__v().name,
        input_kwargs={'Switch': reroute, '0': combine_xyz_4, '1': combine_xyz_3, '2': combine_xyz_2})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': divide})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide})
    
    multiswitch_v_1 = nw.new_node(nodegroup_multiswitch__v().name,
        input_kwargs={'Switch': reroute, '0': combine_xyz_6, '1': combine_xyz_5, '2': combine_xyz_1})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': multiswitch_v, 'End': multiswitch_v_1, 'Length': 0.7000})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Curve': curve_line}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_to_pipe', singleton=False, type='GeometryNodeTree')
def nodegroup_to_pipe(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketFloatDistance', 'Profile Radius', 0.5000),
            ('NodeSocketInt', 'Profile Resolution', 20),
            ('NodeSocketFloatDistance', 'Curve Radius', 1.0000),
            ('NodeSocketBool', 'Fill Caps', False),
            ('NodeSocketBool', 'NURBS', False),
            ('NodeSocketBool', 'Selection', True),
            ('NodeSocketBool', 'Arc', False),
            ('NodeSocketFloatAngle', 'Arc Angle', 6.2832)])
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["NURBS"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Curve"]})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_36})
    
    separate_components = nw.new_node(Nodes.SeparateComponents, input_kwargs={'Geometry': reroute_37})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_components.outputs["Curve"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Selection"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Curve Radius"]})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_1, 'Selection': reroute_6, 'Radius': reroute_33})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_curve_radius})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': set_curve_radius}, attrs={'spline_type': 'NURBS'})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_spline_type})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_41})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_15, 14: reroute_38, 15: reroute_40})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch.outputs[6]})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_43})
    
    spline_parameter_3 = nw.new_node(Nodes.SplineParameter)
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': spline_parameter_3.outputs["Factor"]})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_47})
    
    capture_attribute_3 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': reroute_42, 2: reroute_48})
    
    reroute_60 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_3.outputs["Geometry"]})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_60})
    
    reroute_118 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Arc"]})
    
    reroute_116 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_118})
    
    reroute_122 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_116})
    
    reroute_123 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_122})
    
    reroute_124 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_123})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Profile Resolution"]})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Profile Radius"]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_22, 'Radius': reroute_26})
    
    reroute_102 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute_103 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    reroute_126 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Arc Angle"]})
    
    reroute_117 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_126})
    
    reroute_125 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_117})
    
    arc = nw.new_node('GeometryNodeCurveArc',
        input_kwargs={'Resolution': reroute_102, 'Radius': reroute_103, 'Sweep Angle': reroute_125})
    
    switch_2 = nw.new_node(Nodes.Switch,
        input_kwargs={1: reroute_124, 14: curve_circle.outputs["Curve"], 15: arc.outputs["Curve"]})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': switch_2.outputs[6], 2: spline_parameter.outputs["Factor"]})
    
    reroute_72 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs["Geometry"]})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_72})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Fill Caps"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': reroute_50, 'Profile Curve': reroute_49, 'Fill Caps': reroute_17})
    
    reroute_55 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs[2]})
    
    reroute_86 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_55})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_3.outputs[2]})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_54})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_86, 'Y': reroute_53})
    
    capture_attribute_5 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_to_mesh, 1: combine_xyz_1},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_63 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_5.outputs["Geometry"]})
    
    reroute_64 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_63})
    
    reroute_62 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_53})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_62}, attrs={'operation': 'EQUAL'})
    
    reroute_61 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_62})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_61, 1: 0.9990}, attrs={'operation': 'SUBTRACT'})
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={0: subtract}, attrs={'operation': 'EQUAL'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: equal, 1: equal_1})
    
    separate_geometry_1 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_64, 'Selection': add},
        attrs={'domain': 'FACE'})
    
    reroute_70 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_5.outputs["Attribute"]})
    
    reroute_69 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_70})
    
    reroute_68 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_69})
    
    capture_attribute_8 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': separate_geometry_1.outputs["Inverted"], 1: reroute_68},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_65 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_64})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_65, 'Selection': add},
        attrs={'domain': 'EDGE'})
    
    uv_unwrap = nw.new_node('GeometryNodeUVUnwrap', input_kwargs={'Seam': add})
    
    capture_attribute_6 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': separate_geometry.outputs["Selection"], 1: uv_unwrap},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [capture_attribute_8.outputs["Geometry"], capture_attribute_6.outputs["Geometry"]]})
    
    reroute_71 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_1})
    
    reroute_67 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_6.outputs["Attribute"]})
    
    reroute_66 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_67})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: capture_attribute_8.outputs["Attribute"], 1: reroute_66})
    
    reroute_74 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_1.outputs["Vector"]})
    
    reroute_73 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_74})
    
    capture_attribute_7 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': reroute_71, 1: reroute_73},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_93 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_7.outputs["Geometry"]})
    
    reroute_92 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_93})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': separate_components.outputs["Mesh"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_34})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius,
        input_kwargs={'Curve': mesh_to_curve, 'Selection': reroute_4, 'Radius': reroute_35})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_curve_radius_1})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    set_spline_type_1 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': set_curve_radius_1}, attrs={'spline_type': 'NURBS'})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_spline_type_1})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_7, 14: reroute_2, 15: reroute_44})
    
    spline_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': spline_parameter_2.outputs["Factor"]})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_46})
    
    capture_attribute_2 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': switch_1.outputs[6], 2: reroute_45})
    
    reroute_114 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_2.outputs["Geometry"]})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_114})
    
    reroute_119 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_118})
    
    reroute_120 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_119})
    
    reroute_121 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_120})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_21, 'Radius': reroute_27})
    
    reroute_106 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute_107 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_127 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_126})
    
    reroute_128 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_127})
    
    reroute_129 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_128})
    
    arc_1 = nw.new_node('GeometryNodeCurveArc',
        input_kwargs={'Resolution': reroute_106, 'Radius': reroute_107, 'Sweep Angle': reroute_129})
    
    switch_3 = nw.new_node(Nodes.Switch,
        input_kwargs={1: reroute_121, 14: curve_circle_1.outputs["Curve"], 15: arc_1.outputs["Curve"]})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': switch_3.outputs[6], 2: spline_parameter_1.outputs["Factor"]})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs["Geometry"]})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_58})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': reroute_52, 'Profile Curve': reroute_51, 'Fill Caps': reroute_16})
    
    reroute_59 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs[2]})
    
    reroute_57 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_59})
    
    reroute_115 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_2.outputs[2]})
    
    reroute_56 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_115})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_57, 'Y': reroute_56})
    
    capture_attribute_4 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_to_mesh_1, 1: combine_xyz},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_90 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_4.outputs["Geometry"]})
    
    reroute_79 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_90})
    
    reroute_80 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_79})
    
    reroute_75 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_56})
    
    reroute_76 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_75})
    
    equal_2 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_76}, attrs={'operation': 'EQUAL'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_75, 1: 0.9990}, attrs={'operation': 'SUBTRACT'})
    
    equal_3 = nw.new_node(Nodes.Compare, input_kwargs={0: subtract_1}, attrs={'operation': 'EQUAL'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: equal_2, 1: equal_3})
    
    separate_geometry_3 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_80, 'Selection': add_2},
        attrs={'domain': 'FACE'})
    
    reroute_89 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_4.outputs["Attribute"]})
    
    reroute_77 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_89})
    
    reroute_84 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_77})
    
    reroute_83 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_84})
    
    capture_attribute_10 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': separate_geometry_3.outputs["Inverted"], 1: reroute_83},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    separate_geometry_2 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_79, 'Selection': add_2},
        attrs={'domain': 'EDGE'})
    
    uv_unwrap_1 = nw.new_node('GeometryNodeUVUnwrap', input_kwargs={'Seam': add_2})
    
    capture_attribute_9 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': separate_geometry_2.outputs["Selection"], 1: uv_unwrap_1},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [capture_attribute_10.outputs["Geometry"], capture_attribute_9.outputs["Geometry"]]})
    
    reroute_85 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_2})
    
    reroute_81 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_9.outputs["Attribute"]})
    
    reroute_82 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_81})
    
    add_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: capture_attribute_10.outputs["Attribute"], 1: reroute_82})
    
    reroute_88 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_3.outputs["Vector"]})
    
    reroute_87 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_88})
    
    capture_attribute_11 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': reroute_85, 1: reroute_87},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_109 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_11.outputs["Geometry"]})
    
    reroute_108 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_109})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_92, reroute_108]})
    
    reroute_111 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_11.outputs["Attribute"]})
    
    reroute_110 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_111})
    
    reroute_113 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_7.outputs["Attribute"]})
    
    reroute_112 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_113})
    
    add_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_110, 1: reroute_112})
    
    reroute_94 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_59})
    
    reroute_95 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_94})
    
    reroute_97 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_54})
    
    reroute_96 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_97})
    
    add_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_95, 1: reroute_96})
    
    reroute_91 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_5})
    
    reroute_78 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_91})
    
    reroute_104 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_86})
    
    reroute_105 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_115})
    
    add_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_104, 1: reroute_105})
    
    reroute_98 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_6})
    
    reroute_99 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_98})
    
    reroute_100 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_99})
    
    reroute_101 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_100})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': join_geometry, 'UV': add_4.outputs["Vector"], 'Factor': reroute_78, 'Profile Factor': reroute_101},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_show_u_v', singleton=False, type='GeometryNodeTree')
def nodegroup_show_u_v(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketString', 'UV Name', 'uv_#1'),
            ('NodeSocketBool', 'Fill', False),
            ('NodeSocketVectorTranslation', 'Offset', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVectorXYZ', 'Scale', (1.0000, 1.0000, 1.0000))])
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Fill"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    duplicate_elements = nw.new_node(Nodes.DuplicateElements, input_kwargs={'Geometry': reroute_18}, attrs={'domain': 'FACE'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["UV Name"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    named_attribute = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': reroute_16}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': named_attribute.outputs["Attribute"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Offset"]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': duplicate_elements.outputs["Geometry"], 'Position': reroute_15, 'Offset': reroute_12})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': set_position}, attrs={'mode': 'ONLY_FACE'})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': delete_geometry})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: reroute, 14: reroute_20, 15: set_position})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': switch.outputs[6], 'Scale': reroute_3})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_position__normal_store', singleton=False, type='GeometryNodeTree')
def nodegroup_position__normal_store(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Position / Normal', 0),
            ('NodeSocketInt', 'Point / Edge / Face', 0),
            ('NodeSocketString', 'Name', '')])
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Point / Edge / Face"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_21, 1: 1.0000, 2: 2.0000})
    
    position = nw.new_node(Nodes.InputPosition)
    
    normal = nw.new_node(Nodes.InputNormal)
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input.outputs["Position / Normal"], 8: position, 9: normal},
        attrs={'input_type': 'VECTOR'})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Name': group_input.outputs["Name"], 3: switch.outputs[3]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Name': group_input.outputs["Name"], 3: switch.outputs[3]},
        attrs={'domain': 'EDGE', 'data_type': 'FLOAT_VECTOR'})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_21, 14: store_named_attribute_2, 15: store_named_attribute_1})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Name': group_input.outputs["Name"], 3: switch.outputs[3]},
        attrs={'domain': 'FACE', 'data_type': 'FLOAT_VECTOR'})
    
    switch_3 = nw.new_node(Nodes.Switch,
        input_kwargs={1: map_range.outputs["Result"], 14: switch_1.outputs[6], 15: store_named_attribute})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': switch_3.outputs[6]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_position_compare', singleton=False, type='GeometryNodeTree')
def nodegroup_position_compare(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'X / Y / Z', 0),
            ('NodeSocketInt', 'G / GE / L / LE / E / N', 0),
            ('NodeSocketFloat', 'Compare Value', 0.0000)])
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["G / GE / L / LE / E / N"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["X / Y / Z"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    multiswitch_f = nw.new_node(nodegroup_multiswitch__f().name,
        input_kwargs={'Switch': reroute_5, '0': separate_xyz.outputs["X"], '1': separate_xyz.outputs["Y"], '2': separate_xyz.outputs["Z"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Compare Value"]})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: multiswitch_f, 1: reroute})
    
    greater_equal = nw.new_node(Nodes.Compare, input_kwargs={0: multiswitch_f, 1: reroute}, attrs={'operation': 'GREATER_EQUAL'})
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={0: multiswitch_f, 1: reroute}, attrs={'operation': 'LESS_THAN'})
    
    less_equal = nw.new_node(Nodes.Compare, input_kwargs={0: multiswitch_f, 1: reroute}, attrs={'operation': 'LESS_EQUAL'})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={0: multiswitch_f, 1: reroute}, attrs={'operation': 'EQUAL'})
    
    not_equal = nw.new_node(Nodes.Compare, input_kwargs={0: multiswitch_f, 1: reroute}, attrs={'operation': 'NOT_EQUAL'})
    
    multiswitch_f_1 = nw.new_node(nodegroup_multiswitch__f().name,
        input_kwargs={'Switch': reroute_3, '0': greater_than, '1': greater_equal, '2': less_than, '3': less_equal, '4': equal, '5': not_equal})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Output': multiswitch_f_1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_get_scale', singleton=False, type='GeometryNodeTree')
def nodegroup_get_scale(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': group_input.outputs["Geometry"]})
    
    absolute = nw.new_node(Nodes.VectorMath, input_kwargs={0: bounding_box.outputs["Min"]}, attrs={'operation': 'ABSOLUTE'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': bounding_box.outputs["Max"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: absolute.outputs["Vector"], 1: reroute_1})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': add.outputs["Vector"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add.outputs["Vector"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'X': separate_xyz.outputs["X"], 'Y': separate_xyz.outputs["Y"], 'Z': separate_xyz.outputs["Z"], 'Scale': reroute_3},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_color_ramp_math', singleton=False, type='ShaderNodeTree')
def nodegroup_color_ramp_math(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Fac', 0.5000),
            ('NodeSocketColor', 'Color1', (1.0000, 1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloat', 'Pos 1', 1.0000),
            ('NodeSocketColor', 'Color2', (0.0000, 0.0000, 0.0000, 1.0000)),
            ('NodeSocketFloat', 'Pos 2', 0.0000)])
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Pos 2"], 1: group_input.outputs["Pos 1"]},
        attrs={'operation': 'SUBTRACT'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: subtract}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: group_input.outputs["Fac"]}, attrs={'operation': 'MULTIPLY'})
    
    subtract_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Pos 1"], 1: group_input.outputs["Pos 2"]},
        attrs={'operation': 'SUBTRACT'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Pos 1"], 1: subtract_1}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: divide_1})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: add, 6: group_input.outputs["Color1"], 7: group_input.outputs["Color2"]},
        attrs={'data_type': 'RGBA'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Color': mix_2.outputs[2]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_scatter', singleton=False, type='ShaderNodeTree')
def nodegroup_scatter(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Scale Individual', (1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloat', 'Scale Grid', 5.0000),
            ('NodeSocketFloat', 'Scale Uniform', 1.0000),
            ('NodeSocketFloat', 'W', 0.0000),
            ('NodeSocketFloat', 'Min', 1.0000),
            ('NodeSocketFloat', 'Max', 1.0000),
            ('NodeSocketFloat', 'Randomize Rotation Individual', 0.0000),
            ('NodeSocketFloat', 'Rotation All', 0.0000),
            ('NodeSocketFloat', 'Bias', 0.5000)])
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: group_input.outputs["Vector"], 'Scale': group_input.outputs["Scale Grid"]},
        attrs={'operation': 'SCALE'})
    
    fraction = nw.new_node(Nodes.VectorMath, input_kwargs={0: scale.outputs["Vector"]}, attrs={'operation': 'FRACTION'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': -0.5000, 'Y': -0.5000, 'Z': -0.5000})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: fraction.outputs["Vector"], 1: combine_xyz})
    
    ceil = nw.new_node(Nodes.VectorMath, input_kwargs={0: scale.outputs["Vector"]}, attrs={'operation': 'CEIL'})
    
    white_noise_texture = nw.new_node(Nodes.WhiteNoiseTexture,
        input_kwargs={'Vector': ceil.outputs["Vector"], 'W': group_input.outputs["W"]},
        attrs={'noise_dimensions': '4D'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': white_noise_texture.outputs["Value"], 3: group_input.outputs["Min"], 4: group_input.outputs["Max"]})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add.outputs["Vector"], 'Scale': map_range.outputs["Result"]},
        attrs={'operation': 'SCALE'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: white_noise_texture.outputs["Value"], 1: group_input.outputs["Randomize Rotation Individual"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: group_input.outputs["Rotation All"]})
    
    radians = nw.new_node(Nodes.Math, input_kwargs={0: add_1}, attrs={'operation': 'RADIANS'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate, input_kwargs={'Vector': scale_1.outputs["Vector"], 'Angle': radians})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: vector_rotate, 'Scale': group_input.outputs["Scale Uniform"]},
        attrs={'operation': 'SCALE'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale_2.outputs["Vector"], 1: group_input.outputs["Scale Individual"], 'Scale': 0.5900},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: white_noise_texture.outputs["Value"], 1: group_input.outputs["Bias"]},
        attrs={'operation': 'GREATER_THAN'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Vector': multiply_1.outputs["Vector"], 'Bias Clamp': greater_than, 'Bias ': white_noise_texture.outputs["Value"], 'Color': white_noise_texture.outputs["Color"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_inset_faces', singleton=False, type='GeometryNodeTree')
def nodegroup_inset_faces(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Mesh', None),
            ('NodeSocketBool', 'Selection', True),
            ('NodeSocketBool', 'Uniform', True),
            ('NodeSocketFloat', 'Scale', 1.0000),
            ('NodeSocketVector', 'Scale_1', (1.0000, 1.0000, 1.0000))])
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Uniform"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    extrude_mesh_11 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': group_input.outputs["Mesh"], 'Selection': group_input.outputs["Selection"], 'Offset Scale': 0.0000})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale_1"]})
    
    transform_selection = nw.new_node(nodegroup_transform_selection().name,
        input_kwargs={'Geometry': extrude_mesh_11.outputs["Mesh"], 'Selection': extrude_mesh_11.outputs["Top"], 'Scale': reroute})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh_11.outputs["Mesh"], 'Selection': extrude_mesh_11.outputs["Top"], 'Scale': reroute_3, 'Axis': (0.0000, 1.0000, 0.0000)})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: reroute_2, 14: transform_selection.outputs["Geometry"], 15: scale_elements})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': switch.outputs[6], 'Inset': extrude_mesh_11.outputs["Top"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_decorative_pillar', singleton=False, type='GeometryNodeTree')
def nodegroup_decorative_pillar(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketBool', 'Custom Curve', False),
            ('NodeSocketGeometry', 'Custom Curve_1', None),
            ('NodeSocketInt', 'Curve Resolution', 64),
            ('NodeSocketInt', 'Profile Resolution', 32),
            ('NodeSocketInt', 'Style', 0),
            ('NodeSocketFloatDistance', 'Radius', 0.1000),
            ('NodeSocketFloat', 'Height', 1.0000),
            ('NodeSocketFloat', 'Radius Min', 0.5000),
            ('NodeSocketFloat', 'Radius Max', 1.0000),
            ('NodeSocketFloat', 'From Min', 0.0000),
            ('NodeSocketFloat', 'From Max', 1.0000),
            ('NodeSocketFloat', 'Wave Scale', 1.0000),
            ('NodeSocketFloat', 'Variation', 0.0000),
            ('NodeSocketFloat', 'Phase Offset', 0.0000),
            ('NodeSocketFloatAngle', 'Tilt', 0.0000),
            ('NodeSocketString', 'Texture', 'tex_wave'),
            ('NodeSocketBool', 'Shade Smooth', True),
            ('NodeSocketBool', 'Fill Caps', False)])
    
    curve_line_length = nw.new_node(nodegroup_curve_line_length().name,
        input_kwargs={'Length': group_input_1.outputs["Height"], 'Orientation X / Y / Z': 2})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Curve Resolution"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    resample_curve_4 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_length, 'Count': reroute_3})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_1.outputs["Custom Curve"], 14: resample_curve_4, 15: group_input_1.outputs["Custom Curve_1"]})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': switch.outputs[6], 'Tilt': group_input_1.outputs["Tilt"]})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_curve_tilt})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_35})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Radius"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Profile Resolution"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Style"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    position_6 = nw.new_node(Nodes.InputPosition)
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ)
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_6, 1: combine_xyz_7})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Wave Scale"]})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_12, 1: 0.5800})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Variation"]})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Phase Offset"]})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': add.outputs["Vector"], 'Scale': add_1, 'Distortion': reroute_21, 'Phase Offset': reroute_22},
        attrs={'bands_direction': 'Z'})
    
    position_7 = nw.new_node(Nodes.InputPosition)
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ)
    
    add_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_7, 1: combine_xyz_8})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_14, 1: 0.5800})
    
    wave_texture_1 = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': add_2.outputs["Vector"], 'Scale': add_3, 'Distortion': reroute_21, 'Phase Offset': reroute_22},
        attrs={'wave_profile': 'SAW', 'bands_direction': 'Z'})
    
    position_8 = nw.new_node(Nodes.InputPosition)
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ)
    
    add_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_8, 1: combine_xyz_9})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    add_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_13, 1: 0.5800})
    
    wave_texture_2 = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': add_4.outputs["Vector"], 'Scale': add_5, 'Distortion': reroute_21, 'Phase Offset': reroute_22},
        attrs={'wave_profile': 'TRI', 'bands_direction': 'Z'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: wave_texture.outputs["Fac"], 7: wave_texture_1.outputs["Fac"]},
        attrs={'blend_type': 'DIFFERENCE', 'data_type': 'RGBA'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: wave_texture_1.outputs["Fac"], 7: wave_texture_2.outputs["Fac"]},
        attrs={'blend_type': 'DIFFERENCE', 'data_type': 'RGBA'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: wave_texture.outputs["Fac"], 7: wave_texture_1.outputs["Fac"]},
        attrs={'blend_type': 'BURN', 'data_type': 'RGBA'})
    
    multiswitch_f = nw.new_node(nodegroup_multiswitch__f().name,
        input_kwargs={'Switch': reroute_20, '0': wave_texture.outputs["Fac"], '1': wave_texture_1.outputs["Fac"], '2': wave_texture_2.outputs["Fac"], '3': mix.outputs[2], '4': mix_1.outputs[2], '5': mix_3.outputs[2]})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiswitch_f})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': reroute_34, 1: group_input_1.outputs["From Min"], 2: group_input_1.outputs["From Max"], 3: group_input_1.outputs["Radius Min"], 4: group_input_1.outputs["Radius Max"]})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    to_pipe = nw.new_node(nodegroup_to_pipe().name,
        input_kwargs={'Curve': reroute_24, 'Profile Radius': reroute_11, 'Profile Resolution': reroute_7, 'Curve Radius': reroute_31, 'Fill Caps': group_input_1.outputs["Fill Caps"]})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Texture"]})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_38})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': to_pipe.outputs["Mesh"], 'Name': reroute_33, 4: reroute_28})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': store_named_attribute, 'Shade Smooth': group_input_1.outputs["Shade Smooth"]})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': set_shade_smooth, 'Curve': reroute_27, 'Factor': to_pipe.outputs["Factor"], 'Profile Factor': to_pipe.outputs["Profile Factor"], 'UV': to_pipe.outputs["UV"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_cube_unwrap', singleton=False, type='GeometryNodeTree')
def nodegroup_cube_unwrap(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_2 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketString', 'UV Name', 'UV_Cube'),
            ('NodeSocketFloat', 'Margin', 0.0000),
            ('NodeSocketInt', 'Unwrap / Smart UV', 0),
            ('NodeSocketFloat', 'Face 1 UV Rot', 90.0000),
            ('NodeSocketFloat', 'Face 2 UV Rot', 0.0000),
            ('NodeSocketFloat', 'Face 3 UV Rot', 90.0000),
            ('NodeSocketFloat', 'Face 4 UV Rot', 0.0000),
            ('NodeSocketFloat', 'Face 5 UV Rot', 90.0000),
            ('NodeSocketFloat', 'Face 6 UV Rot', 90.0000),
            ('NodeSocketVectorTranslation', 'Show UV Offset', (0.0000, 0.0000, 0.0000))])
    
    reroute_165 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Geometry"]})
    
    reroute_166 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_165})
    
    reroute_222 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_166})
    
    position_compare = nw.new_node(nodegroup_position_compare().name, input_kwargs={'X / Y / Z': 2})
    
    position_compare_1 = nw.new_node(nodegroup_position_compare().name, input_kwargs={'X / Y / Z': 1, 'G / GE / L / LE / E / N': 2})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: position_compare, 1: position_compare_1}, attrs={'operation': 'SUBTRACT'})
    
    position_compare_2 = nw.new_node(nodegroup_position_compare().name, input_kwargs={'X / Y / Z': 2, 'G / GE / L / LE / E / N': 2})
    
    position_compare_3 = nw.new_node(nodegroup_position_compare().name, input_kwargs={'X / Y / Z': 1, 'G / GE / L / LE / E / N': 2})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: position_compare_2, 1: position_compare_3}, attrs={'operation': 'SUBTRACT'})
    
    op_or = nw.new_node(Nodes.BooleanMath, input_kwargs={0: subtract, 1: subtract_1}, attrs={'operation': 'OR'})
    
    position_compare_4 = nw.new_node(nodegroup_position_compare().name)
    
    position_compare_5 = nw.new_node(nodegroup_position_compare().name, input_kwargs={'X / Y / Z': 1, 'G / GE / L / LE / E / N': 3})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: position_compare_4, 1: position_compare_5}, attrs={'operation': 'SUBTRACT'})
    
    op_or_1 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: op_or, 1: subtract_2}, attrs={'operation': 'OR'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Margin"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_132 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_133 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_132})
    
    uv_unwrap = nw.new_node('GeometryNodeUVUnwrap',
        input_kwargs={'Seam': op_or_1, 'Margin': reroute_133},
        attrs={'method': 'CONFORMAL'})
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': reroute_222, 1: uv_unwrap},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs["Attribute"]})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Name': group_input_2.outputs["UV Name"], 3: reroute_2},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_131 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': store_named_attribute_1})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_165})
    
    reroute_60 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    reroute_61 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_60})
    
    reroute_62 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_61})
    
    reroute_64 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_62})
    
    reroute_65 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_64})
    
    reroute_71 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_65})
    
    reroute_73 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_71})
    
    reroute_91 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_73})
    
    reroute_93 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_91})
    
    reroute_114 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_93})
    
    reroute_116 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_114})
    
    reroute_141 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_116})
    
    reroute_142 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_141})
    
    reroute_134 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_142})
    
    get_scale = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_166})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: get_scale.outputs["Z"], 1: -2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract_3 = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: -0.0001}, attrs={'operation': 'SUBTRACT'})
    
    reroute_181 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_3})
    
    reroute_182 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_181})
    
    reroute_183 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_182})
    
    reroute_184 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_183})
    
    position_compare_6 = nw.new_node(nodegroup_position_compare().name,
        input_kwargs={'X / Y / Z': 2, 'G / GE / L / LE / E / N': 2, 'Compare Value': reroute_184})
    
    separate_geometry_5 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_134, 'Selection': position_compare_6},
        attrs={'domain': 'FACE'})
    
    position_normal_store = nw.new_node(nodegroup_position__normal_store().name,
        input_kwargs={'Geometry': separate_geometry_5.outputs["Selection"], 'Name': 'f6-pos#'})
    
    get_scale_1 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_142})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale_1.outputs["Z"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_143 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide_1})
    
    reroute_144 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_143})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_144})
    
    set_position_9 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': position_normal_store, 'Offset': combine_xyz_9})
    
    radians = nw.new_node(Nodes.Math, input_kwargs={0: 180.0000}, attrs={'operation': 'RADIANS'})
    
    radians_1 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0000}, attrs={'operation': 'RADIANS'})
    
    radians_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_2.outputs["Face 6 UV Rot"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_16 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians, 'Y': radians_1, 'Z': radians_2})
    
    reroute_154 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_16})
    
    reroute_164 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_154})
    
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_9, 'Rotation': reroute_164})
    
    bring_to_floor = nw.new_node(nodegroup_bring_to_floor().name,
        input_kwargs={'Geometry': transform_5, 'Axis': (1.0000, 1.0000, 0.0000)})
    
    reroute_90 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_91})
    
    reroute_88 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_90})
    
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale.outputs["X"], 1: -2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract_4 = nw.new_node(Nodes.Math, input_kwargs={0: divide_2, 1: -0.0001}, attrs={'operation': 'SUBTRACT'})
    
    reroute_173 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_4})
    
    reroute_178 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_173})
    
    reroute_179 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_178})
    
    reroute_180 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_179})
    
    position_compare_7 = nw.new_node(nodegroup_position_compare().name,
        input_kwargs={'G / GE / L / LE / E / N': 2, 'Compare Value': reroute_180})
    
    separate_geometry_3 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_88, 'Selection': position_compare_7},
        attrs={'domain': 'FACE'})
    
    position_normal_store_1 = nw.new_node(nodegroup_position__normal_store().name,
        input_kwargs={'Geometry': separate_geometry_3.outputs["Selection"], 'Name': 'f4-pos#'})
    
    get_scale_2 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_90})
    
    divide_3 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale_2.outputs["X"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_89 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide_3})
    
    reroute_98 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_89})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_98})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': position_normal_store_1, 'Offset': combine_xyz_6})
    
    radians_3 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0000}, attrs={'operation': 'RADIANS'})
    
    radians_4 = nw.new_node(Nodes.Math, input_kwargs={0: 90.0000}, attrs={'operation': 'RADIANS'})
    
    radians_5 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_2.outputs["Face 4 UV Rot"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_14 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians_3, 'Y': radians_4, 'Z': radians_5})
    
    reroute_155 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_14})
    
    reroute_162 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_155})
    
    transform_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_5, 'Rotation': reroute_162})
    
    bring_to_floor_1 = nw.new_node(nodegroup_bring_to_floor().name,
        input_kwargs={'Geometry': transform_3, 'Axis': (1.0000, 1.0000, 0.0000)})
    
    reroute_70 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_71})
    
    reroute_68 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_70})
    
    divide_4 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale.outputs["Y"], 1: -2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract_5 = nw.new_node(Nodes.Math, input_kwargs={0: divide_4, 1: -0.0001}, attrs={'operation': 'SUBTRACT'})
    
    reroute_177 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_5})
    
    reroute_174 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_177})
    
    reroute_175 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_174})
    
    reroute_176 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_175})
    
    position_compare_8 = nw.new_node(nodegroup_position_compare().name,
        input_kwargs={'X / Y / Z': 1, 'G / GE / L / LE / E / N': 2, 'Compare Value': reroute_176})
    
    separate_geometry_2 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_68, 'Selection': position_compare_8},
        attrs={'domain': 'FACE'})
    
    position_normal_store_2 = nw.new_node(nodegroup_position__normal_store().name,
        input_kwargs={'Geometry': separate_geometry_2.outputs["Selection"], 'Name': 'f3-pos#'})
    
    get_scale_3 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_70})
    
    divide_5 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale_3.outputs["Y"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_69 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide_5})
    
    reroute_79 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_69})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute_79})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': position_normal_store_2, 'Offset': combine_xyz_3})
    
    radians_6 = nw.new_node(Nodes.Math, input_kwargs={0: -90.0000}, attrs={'operation': 'RADIANS'})
    
    radians_7 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0000}, attrs={'operation': 'RADIANS'})
    
    radians_8 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_2.outputs["Face 3 UV Rot"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_13 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians_6, 'Y': radians_7, 'Z': radians_8})
    
    reroute_156 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_13})
    
    reroute_161 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_156})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_3, 'Rotation': reroute_161})
    
    bring_to_floor_2 = nw.new_node(nodegroup_bring_to_floor().name,
        input_kwargs={'Geometry': transform_2, 'Axis': (1.0000, 1.0000, 0.0000)})
    
    reroute_63 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_64})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_63})
    
    divide_6 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale.outputs["X"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract_6 = nw.new_node(Nodes.Math, input_kwargs={0: divide_6, 1: 0.0001}, attrs={'operation': 'SUBTRACT'})
    
    reroute_169 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_6})
    
    reroute_170 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_169})
    
    reroute_171 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_170})
    
    reroute_172 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_171})
    
    position_compare_9 = nw.new_node(nodegroup_position_compare().name, input_kwargs={'Compare Value': reroute_172})
    
    separate_geometry_1 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_38, 'Selection': position_compare_9},
        attrs={'domain': 'FACE'})
    
    position_normal_store_3 = nw.new_node(nodegroup_position__normal_store().name,
        input_kwargs={'Geometry': separate_geometry_1.outputs["Selection"], 'Name': 'f2-pos#'})
    
    get_scale_4 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_63})
    
    divide_7 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale_4.outputs["X"], 1: -2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide_7})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_40})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_41})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': position_normal_store_3, 'Offset': combine_xyz_1})
    
    radians_9 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0000}, attrs={'operation': 'RADIANS'})
    
    radians_10 = nw.new_node(Nodes.Math, input_kwargs={0: -90.0000}, attrs={'operation': 'RADIANS'})
    
    radians_11 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_2.outputs["Face 2 UV Rot"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_12 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians_9, 'Y': radians_10, 'Z': radians_11})
    
    reroute_157 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_12})
    
    reroute_160 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_157})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_1, 'Rotation': reroute_160})
    
    bring_to_floor_3 = nw.new_node(nodegroup_bring_to_floor().name,
        input_kwargs={'Geometry': transform_1, 'Axis': (1.0000, 1.0000, 0.0000)})
    
    divide_8 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale.outputs["Y"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract_7 = nw.new_node(Nodes.Math, input_kwargs={0: divide_8, 1: 0.0001}, attrs={'operation': 'SUBTRACT'})
    
    reroute_167 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_7})
    
    reroute_168 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_167})
    
    position_compare_10 = nw.new_node(nodegroup_position_compare().name, input_kwargs={'X / Y / Z': 1, 'Compare Value': reroute_168})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_33, 'Selection': position_compare_10},
        attrs={'domain': 'FACE'})
    
    position_normal_store_4 = nw.new_node(nodegroup_position__normal_store().name,
        input_kwargs={'Geometry': separate_geometry.outputs["Selection"], 'Name': 'f1-pos#'})
    
    get_scale_5 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_60})
    
    divide_9 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale_5.outputs["Y"], 1: -2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide_9})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_35})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute_32})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': position_normal_store_4, 'Offset': combine_xyz})
    
    radians_12 = nw.new_node(Nodes.Math, input_kwargs={0: 90.0000}, attrs={'operation': 'RADIANS'})
    
    radians_13 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0000}, attrs={'operation': 'RADIANS'})
    
    radians_14 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_2.outputs["Face 1 UV Rot"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_11 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians_12, 'Y': radians_13, 'Z': radians_14})
    
    reroute_153 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_11})
    
    reroute_159 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_153})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position, 'Rotation': reroute_159})
    
    bring_to_floor_4 = nw.new_node(nodegroup_bring_to_floor().name,
        input_kwargs={'Geometry': transform, 'Axis': (1.0000, 1.0000, 0.0000)})
    
    get_scale_6 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': bring_to_floor_4})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': get_scale_6.outputs["X"]})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_132})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_52})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_51})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_50})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_34, 1: reroute_44})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': bring_to_floor_3, 'Offset': combine_xyz_2})
    
    reroute_67 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_2})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': bring_to_floor_4})
    
    reroute_59 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_58})
    
    reroute_66 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_59})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_67, reroute_66]})
    
    reroute_82 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_1})
    
    reroute_83 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_82})
    
    reroute_86 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_83})
    
    reroute_87 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_86})
    
    get_scale_7 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_87})
    
    reroute_75 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': get_scale_7.outputs["X"]})
    
    reroute_80 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_75})
    
    reroute_78 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_52})
    
    reroute_77 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_78})
    
    reroute_76 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_77})
    
    reroute_81 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_76})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_80, 1: reroute_81})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_1})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': bring_to_floor_2, 'Offset': combine_xyz_4})
    
    reroute_84 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_4})
    
    reroute_85 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_82})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_84, reroute_85]})
    
    reroute_106 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_2})
    
    reroute_107 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_106})
    
    reroute_108 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_107})
    
    reroute_109 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_108})
    
    get_scale_8 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_109})
    
    reroute_103 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': get_scale_8.outputs["Y"]})
    
    reroute_96 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_103})
    
    reroute_102 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_78})
    
    reroute_95 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_102})
    
    reroute_94 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_95})
    
    reroute_97 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_94})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_96, 1: reroute_97})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': add_2})
    
    set_position_6 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': bring_to_floor_1, 'Offset': combine_xyz_5})
    
    reroute_124 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_6})
    
    reroute_105 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_124})
    
    reroute_113 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_114})
    
    reroute_104 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_113})
    
    divide_10 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale.outputs["Z"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract_8 = nw.new_node(Nodes.Math, input_kwargs={0: divide_10, 1: 0.0001}, attrs={'operation': 'SUBTRACT'})
    
    reroute_185 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_8})
    
    reroute_186 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_185})
    
    reroute_187 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_186})
    
    reroute_188 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_187})
    
    position_compare_11 = nw.new_node(nodegroup_position_compare().name, input_kwargs={'X / Y / Z': 2, 'Compare Value': reroute_188})
    
    separate_geometry_4 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_104, 'Selection': position_compare_11},
        attrs={'domain': 'FACE'})
    
    position_normal_store_5 = nw.new_node(nodegroup_position__normal_store().name,
        input_kwargs={'Geometry': separate_geometry_4.outputs["Selection"], 'Name': 'f5-pos#'})
    
    get_scale_9 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_113})
    
    divide_11 = nw.new_node(Nodes.Math, input_kwargs={0: get_scale_9.outputs["Z"], 1: -2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_112 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide_11})
    
    reroute_121 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_112})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_121})
    
    set_position_8 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': position_normal_store_5, 'Offset': combine_xyz_7})
    
    radians_15 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0000}, attrs={'operation': 'RADIANS'})
    
    radians_16 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0000}, attrs={'operation': 'RADIANS'})
    
    radians_17 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_2.outputs["Face 5 UV Rot"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_15 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians_15, 'Y': radians_16, 'Z': radians_17})
    
    reroute_158 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_15})
    
    reroute_163 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_158})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_8, 'Rotation': reroute_163})
    
    bring_to_floor_5 = nw.new_node(nodegroup_bring_to_floor().name,
        input_kwargs={'Geometry': transform_4, 'Axis': (1.0000, 1.0000, 0.0000)})
    
    get_scale_10 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': set_position_6})
    
    reroute_130 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': get_scale_10.outputs["X"]})
    
    reroute_101 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_130})
    
    reroute_111 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_102})
    
    reroute_118 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_111})
    
    reroute_117 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_118})
    
    reroute_99 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_117})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_101, 1: reroute_99})
    
    reroute_123 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_103})
    
    reroute_119 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_123})
    
    reroute_120 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_99})
    
    add_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_119, 1: reroute_120})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_3, 'Y': add_4})
    
    set_position_7 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': bring_to_floor_5, 'Offset': combine_xyz_8})
    
    reroute_125 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_7})
    
    reroute_110 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_125})
    
    join_geometry_8 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_105, reroute_110]})
    
    get_scale_11 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': join_geometry_8})
    
    reroute_151 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': get_scale_11.outputs["X"]})
    
    reroute_152 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_151})
    
    reroute_147 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_152})
    
    reroute_146 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_147})
    
    reroute_128 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_111})
    
    reroute_137 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_128})
    
    reroute_138 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_137})
    
    reroute_145 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_138})
    
    add_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_146, 1: reroute_145})
    
    reroute_148 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_103})
    
    reroute_136 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_148})
    
    reroute_135 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_145})
    
    add_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_136, 1: reroute_135})
    
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_5, 'Y': add_6})
    
    set_position_10 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': bring_to_floor, 'Offset': combine_xyz_10})
    
    reroute_149 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_10})
    
    reroute_127 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_106})
    
    join_geometry_5 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_105, reroute_127]})
    
    reroute_129 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_5})
    
    join_geometry_7 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_110, reroute_129]})
    
    reroute_126 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_7})
    
    join_geometry_6 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_149, reroute_126]})
    
    reroute_210 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_6})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    reroute_189 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["X"]})
    
    reroute_198 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_189})
    
    reroute_199 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_198})
    
    reroute_200 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_199})
    
    reroute_201 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_200})
    
    reroute_191 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_210})
    
    reroute_190 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_189})
    
    attribute_statistic = nw.new_node(Nodes.AttributeStatistic, input_kwargs={'Geometry': reroute_191, 2: reroute_190})
    
    reroute_202 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': attribute_statistic.outputs["Max"]})
    
    reroute_203 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_202})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_201, 2: reroute_203})
    
    reroute_206 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    reroute_207 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_206})
    
    reroute_197 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["Y"]})
    
    reroute_196 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_197})
    
    reroute_195 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_196})
    
    reroute_194 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_195})
    
    reroute_192 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_191})
    
    get_scale_12 = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_210})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: get_scale_12.outputs["X"], 1: get_scale_12.outputs["Y"]})
    
    reroute_193 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_189})
    
    switch_3 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than, 2: reroute_197, 3: reroute_193},
        attrs={'input_type': 'FLOAT'})
    
    attribute_statistic_1 = nw.new_node(Nodes.AttributeStatistic, input_kwargs={'Geometry': reroute_192, 2: switch_3.outputs["Output"]})
    
    reroute_204 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': attribute_statistic_1.outputs["Max"]})
    
    reroute_205 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_204})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_194, 2: reroute_205})
    
    reroute_209 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_1.outputs["Result"]})
    
    reroute_208 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_209})
    
    combine_xyz_17 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_207, 'Y': reroute_208})
    
    reroute_211 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_17})
    
    reroute_225 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_211})
    
    reroute_223 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_225})
    
    reroute_212 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_223})
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input_2.outputs["Unwrap / Smart UV"], 8: reroute_3, 9: reroute_212},
        attrs={'input_type': 'VECTOR'})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': reroute_210, 'Name': group_input_2.outputs["UV Name"], 3: switch_1.outputs[3]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_246 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': store_named_attribute})
    
    reroute_282 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_246})
    
    reroute_283 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_282})
    
    reroute_284 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_283})
    
    reroute_285 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_284})
    
    reroute_286 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_285})
    
    reroute_287 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_286})
    
    reroute_288 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_287})
    
    reroute_221 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_288})
    
    index_6 = nw.new_node(Nodes.Index)
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: index_6}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    separate_geometry_11 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_221, 'Selection': equal},
        attrs={'domain': 'FACE'})
    
    named_attribute_5 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'f6-pos#'}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position_16 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': separate_geometry_11.outputs["Selection"], 'Position': named_attribute_5.outputs["Attribute"]})
    
    reroute_220 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_287})
    
    index_5 = nw.new_node(Nodes.Index)
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={2: index_5, 3: 1}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    separate_geometry_10 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_220, 'Selection': equal_1},
        attrs={'domain': 'FACE'})
    
    named_attribute_4 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'f5-pos#'}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position_15 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': separate_geometry_10.outputs["Selection"], 'Position': named_attribute_4.outputs["Attribute"]})
    
    reroute_219 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_286})
    
    index_4 = nw.new_node(Nodes.Index)
    
    equal_2 = nw.new_node(Nodes.Compare, input_kwargs={2: index_4, 3: 2}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    separate_geometry_9 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_219, 'Selection': equal_2},
        attrs={'domain': 'FACE'})
    
    named_attribute_3 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'f4-pos#'}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position_14 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': separate_geometry_9.outputs["Selection"], 'Position': named_attribute_3.outputs["Attribute"]})
    
    index_1 = nw.new_node(Nodes.Index)
    
    separate_geometry_6 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_282, 'Selection': index_1},
        attrs={'domain': 'FACE'})
    
    named_attribute = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'f1-pos#'}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position_11 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': separate_geometry_6.outputs["Selection"], 'Position': named_attribute.outputs["Attribute"]})
    
    reroute_247 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_11})
    
    reroute_215 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_284})
    
    index_2 = nw.new_node(Nodes.Index)
    
    equal_3 = nw.new_node(Nodes.Compare, input_kwargs={2: index_2, 3: 4}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    separate_geometry_7 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_215, 'Selection': equal_3},
        attrs={'domain': 'FACE'})
    
    named_attribute_1 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'f2-pos#'}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position_12 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': separate_geometry_7.outputs["Selection"], 'Position': named_attribute_1.outputs["Attribute"]})
    
    reroute_214 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_12})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_247, reroute_214]})
    
    reroute_218 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_285})
    
    index_3 = nw.new_node(Nodes.Index)
    
    equal_4 = nw.new_node(Nodes.Compare, input_kwargs={2: index_3, 3: 3}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    separate_geometry_8 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_218, 'Selection': equal_4},
        attrs={'domain': 'FACE'})
    
    named_attribute_2 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'f3-pos#'}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position_13 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': separate_geometry_8.outputs["Selection"], 'Position': named_attribute_2.outputs["Attribute"]})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry_3, set_position_13]})
    
    join_geometry_9 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_14, join_geometry_4]})
    
    join_geometry_10 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_15, join_geometry_9]})
    
    join_geometry_11 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_16, join_geometry_10]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_11})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_2.outputs["Unwrap / Smart UV"], 14: reroute_131, 15: merge_by_distance})
    
    equal_5 = nw.new_node(Nodes.Compare,
        input_kwargs={2: group_input_2.outputs["Unwrap / Smart UV"], 3: 1},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': equal_5})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    show_uv = nw.new_node(nodegroup_show_u_v().name,
        input_kwargs={'Geometry': switch.outputs[6], 'UV Name': group_input_2.outputs["UV Name"], 'Fill': True, 'Offset': group_input_2.outputs["Show UV Offset"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': show_uv})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_288})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_14, 14: reroute_16, 15: reroute_8})
    
    named_attribute_6 = nw.new_node(Nodes.NamedAttribute,
        input_kwargs={'Name': group_input_2.outputs["UV Name"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': named_attribute_6.outputs["Attribute"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': switch.outputs[6], 'Show UV': switch_2.outputs[6], 'UV': reroute_7},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_bring_to_floor', singleton=False, type='GeometryNodeTree')
def nodegroup_bring_to_floor(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_2 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketVector', 'Axis', (0.0000, 0.0000, 1.0000))])
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Geometry"]})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    get_scale = nw.new_node(nodegroup_get_scale().name, input_kwargs={'Geometry': reroute_2})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': group_input_2.outputs["Axis"]})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"], 1: 0.0000}, attrs={'operation': 'GREATER_THAN'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': greater_than, 3: -1.0000})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: get_scale.outputs["X"], 1: map_range.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    map_range_3 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz.outputs["X"], 1: -1.0000, 3: -2.0000, 4: 2.0000})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: map_range_3.outputs["Result"]}, attrs={'operation': 'DIVIDE'})
    
    greater_than_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: 0.0000}, attrs={'operation': 'GREATER_THAN'})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': greater_than_1, 3: -1.0000})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: get_scale.outputs["Y"], 1: map_range_1.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    map_range_4 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz.outputs["Y"], 1: -1.0000, 3: -2.0000, 4: 2.0000})
    
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_1, 1: map_range_4.outputs["Result"]},
        attrs={'operation': 'DIVIDE'})
    
    greater_than_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: 0.0000}, attrs={'operation': 'GREATER_THAN'})
    
    map_range_2 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': greater_than_2, 3: -1.0000})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: get_scale.outputs["Z"], 1: map_range_2.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    map_range_5 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz.outputs["Z"], 1: -1.0000, 3: -2.0000, 4: 2.0000})
    
    divide_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_2, 1: map_range_5.outputs["Result"]},
        attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide, 'Y': divide_1, 'Z': divide_2})
    
    multiply_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_xyz_1, 1: group_input_2.outputs["Axis"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute, 'Offset': multiply_3.outputs["Vector"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_position}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_complex_noise', singleton=False, type='ShaderNodeTree')
def nodegroup_complex_noise(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'W', 0.0000),
            ('NodeSocketFloat', 'Detail', 2.0000),
            ('NodeSocketFloat', 'Scale', 5.0000),
            ('NodeSocketFloatFactor', 'Roughness', 0.5000),
            ('NodeSocketFloat', 'Distortion', 0.0000),
            ('NodeSocketColor', 'Color1', (1.0000, 1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloat', 'Pos 1', 1.0000),
            ('NodeSocketColor', 'Color2', (0.0000, 0.0000, 0.0000, 1.0000)),
            ('NodeSocketFloat', 'Pos 2', 0.0000),
            ('NodeSocketFloatFactor', 'Darken Fac', 0.8000),
            ('NodeSocketFloatFactor', 'Lighten Fac', 0.5500)])
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Vector"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["W"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Detail"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Roughness"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Distortion"]})
    
    noise_texture_6 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_1, 'W': reroute_2, 'Scale': reroute_4, 'Detail': reroute_3, 'Roughness': reroute_5, 'Distortion': reroute_6},
        attrs={'noise_dimensions': '4D'})
    
    group_1 = nw.new_node(nodegroup_color_ramp_math().name,
        input_kwargs={'Fac': noise_texture_6.outputs["Color"], 'Pos 1': 0.8000, 'Pos 2': 0.3300})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2})
    
    noise_texture_7 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_1, 'W': add, 'Scale': reroute_4, 'Detail': reroute_3, 'Roughness': reroute_5, 'Distortion': reroute_6},
        attrs={'noise_dimensions': '4D'})
    
    group_2 = nw.new_node(nodegroup_color_ramp_math().name,
        input_kwargs={'Fac': noise_texture_7.outputs["Color"], 'Pos 1': 0.8900, 'Pos 2': 0.5000})
    
    mix_12 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["Darken Fac"], 6: group_1, 7: group_2},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: add})
    
    noise_texture_8 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_1, 'W': add_1, 'Scale': reroute_4, 'Detail': reroute_3, 'Roughness': reroute_5, 'Distortion': reroute_6},
        attrs={'noise_dimensions': '4D'})
    
    group_3 = nw.new_node(nodegroup_color_ramp_math().name,
        input_kwargs={'Fac': noise_texture_8.outputs["Fac"], 'Pos 1': 0.7000, 'Pos 2': 0.5000})
    
    mix_13 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["Lighten Fac"], 6: mix_12.outputs[2], 7: group_3},
        attrs={'blend_type': 'LIGHTEN', 'data_type': 'RGBA'})
    
    group_4 = nw.new_node(nodegroup_color_ramp_math().name,
        input_kwargs={'Fac': mix_13.outputs[2], 'Color1': group_input.outputs["Color1"], 'Pos 1': group_input.outputs["Pos 1"], 'Color2': group_input.outputs["Color2"], 'Pos 2': group_input.outputs["Pos 2"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Height': group_4}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_edge_mask', singleton=False, type='ShaderNodeTree')
def nodegroup_edge_mask(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'To Min', 6.7400),
            ('NodeSocketFloat', 'To Max', -0.1800),
            ('NodeSocketFloat', 'Bevel Radius', 0.0900),
            ('NodeSocketVector', 'Normal', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Noise Scale', 5.0000),
            ('NodeSocketFloatFactor', 'Darken', 0.9000),
            ('NodeSocketFloatFactor', 'Second Layer', 0.3000),
            ('NodeSocketFloatFactor', 'Invert', 0.0000)])
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Second Layer"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Darken"]})
    
    bevel = nw.new_node('ShaderNodeBevel',
        input_kwargs={'Radius': group_input.outputs["Bevel Radius"], 'Normal': group_input.outputs["Normal"]},
        attrs={'samples': 12})
    
    geometry = nw.new_node(Nodes.NewGeometry)
    
    dot_product = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bevel, 1: geometry.outputs["True Normal"]},
        attrs={'operation': 'DOT_PRODUCT'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': dot_product.outputs["Value"], 3: group_input.outputs["To Min"], 4: group_input.outputs["To Max"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Vector"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Noise Scale"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_3, 'Scale': reroute, 'Detail': 15.0000, 'Roughness': 0.7667})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.5236
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.6182
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_1, 6: map_range.outputs["Result"], 7: colorramp.outputs["Color"]},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: 3.0000}, attrs={'operation': 'MULTIPLY'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_3, 'Scale': multiply, 'Detail': 15.0000, 'Roughness': 0.8400, 'Distortion': 0.0500})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.5055
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.5564
    colorramp_1.color_ramp.elements[1].color = [3.0000, 3.0000, 3.0000, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_1.outputs["Color"], 7: map_range.outputs["Result"]},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_2, 6: mix.outputs[2], 7: mix_1.outputs[2]},
        attrs={'blend_type': 'LIGHTEN', 'data_type': 'RGBA'})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_2.outputs[2]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5000
    colorramp_2.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["Invert"], 6: mix_2.outputs[2], 7: colorramp_2.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Fac': mix_3.outputs[2]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_scratch_map', singleton=False, type='ShaderNodeTree')
def nodegroup_scratch_map(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Location', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Scratches Scale', 30.0000),
            ('NodeSocketFloat', 'Bias', 0.5000),
            ('NodeSocketFloat', 'Randomize', 1.0000),
            ('NodeSocketFloat', 'Randomize Rotation', 9999.0000),
            ('NodeSocketFloatFactor', 'Dots Presence', 1.0000),
            ('NodeSocketFloatFactor', 'Invert', 0.0000)])
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: group_input.outputs["Vector"], 1: group_input.outputs["Location"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add.outputs["Vector"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute, 'Scale': 10.8500, 'Detail': 7.0000, 'Roughness': 0.9133, 'Distortion': -0.1800})
    
    mix_11 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0070, 6: reroute_4, 7: noise_texture_1.outputs["Fac"]},
        attrs={'data_type': 'RGBA'})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_11.outputs[2]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scratches Scale"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Randomize"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Randomize Rotation"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': group_input.outputs["Bias"], 3: 0.8000})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    group_2 = nw.new_node(nodegroup_scatter().name,
        input_kwargs={'Vector': reroute_8, 'Scale Individual': (24.2200, 0.4300, 1.0000), 'Scale Grid': reroute_7, 'Scale Uniform': 0.5000, 'W': reroute_31, 'Min': 0.3000, 'Max': 4.3200, 'Randomize Rotation Individual': reroute_2, 'Bias': reroute_1})
    
    gradient_texture_2 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_2.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_2.outputs["Bias Clamp"]})
    
    mix_14 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_2.outputs["Color"], 7: reroute_29},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: 1.0280}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_31, 1: 99.8500}, attrs={'operation': 'MULTIPLY'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.0700})
    
    group_3 = nw.new_node(nodegroup_scatter().name,
        input_kwargs={'Vector': reroute_22, 'Scale Individual': (24.2200, -0.5200, 1.0000), 'Scale Grid': multiply, 'Scale Uniform': 0.5000, 'W': multiply_1, 'Min': 0.3000, 'Max': 3.6700, 'Randomize Rotation Individual': reroute_14, 'Rotation All': 78.7000, 'Bias': add_1})
    
    gradient_texture_1 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_3.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_3.outputs["Bias Clamp"]})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_1.outputs["Color"], 7: reroute_28},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    mix_6 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1533, 6: mix_14.outputs[2], 7: mix_4.outputs[2]},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: 0.3200}, attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_31, 1: 155.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    group_5 = nw.new_node(nodegroup_scatter().name,
        input_kwargs={'Vector': reroute_20, 'Scale Individual': (24.2200, -0.5200, 1.0000), 'Scale Grid': multiply_2, 'Scale Uniform': 0.5000, 'W': multiply_3, 'Min': 0.3000, 'Max': 3.6700, 'Randomize Rotation Individual': reroute_10, 'Rotation All': 78.7000, 'Bias': reroute_9})
    
    gradient_texture_4 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_5.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_5.outputs["Bias Clamp"]})
    
    mix_13 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_4.outputs["Color"], 7: reroute_27},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.3600, 6: mix_6.outputs[2], 7: mix_13.outputs[2]},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_19, 1: 1.3000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_32, 1: 155.7000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.0500})
    
    group_4 = nw.new_node(nodegroup_scatter().name,
        input_kwargs={'Vector': reroute_18, 'Scale Individual': (24.2200, -0.5200, 1.0000), 'Scale Grid': multiply_4, 'Scale Uniform': 0.5000, 'W': multiply_5, 'Min': 0.3000, 'Max': 3.6700, 'Randomize Rotation Individual': reroute_12, 'Rotation All': 78.7000, 'Bias': add_2})
    
    gradient_texture_3 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_4.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_4.outputs["Bias Clamp"]})
    
    mix_12 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_3.outputs["Color"], 7: reroute_26},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1993, 6: mix_5.outputs[2], 7: mix_12.outputs[2]},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: -0.7500}, attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': reroute_5, 'W': reroute_31, 'Scale': multiply_6},
        attrs={'voronoi_dimensions': '4D', 'feature': 'DISTANCE_TO_EDGE'})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Distance"]})
    colorramp_4.color_ramp.elements[0].position = 0.0000
    colorramp_4.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.0026
    colorramp_4.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': multiply_6, 'Detail': 5.0000, 'Roughness': 0.8467, 'Distortion': -0.0900})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_5.color_ramp.elements[0].position = 0.5455
    colorramp_5.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.6982
    colorramp_5.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_10 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_25, 6: colorramp_5.outputs["Color"], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    mix_8 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_4.outputs["Color"], 7: mix_10.outputs[2]},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_8.outputs[2]})
    
    mix_9 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_7.outputs[2], 7: reroute_23},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': noise_texture_1.outputs["Fac"]})
    
    mix_16 = nw.new_node(Nodes.Mix, input_kwargs={0: 0.0143, 6: reroute_38, 7: reroute_39}, attrs={'data_type': 'RGBA'})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_44})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_40, 1: 4.0000}, attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture_1 = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mix_16.outputs[2], 'W': reroute_45, 'Scale': multiply_7},
        attrs={'voronoi_dimensions': '4D'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_1.outputs["Distance"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.0463
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_40, 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture_2 = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mix_16.outputs[2], 'W': reroute_43, 'Scale': multiply_8},
        attrs={'voronoi_dimensions': '4D'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_2.outputs["Distance"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.0693
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp.outputs["Color"], 7: colorramp_1.outputs["Color"]},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    mix_17 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["Dots Presence"], 6: mix_9.outputs[2], 7: mix_1.outputs[2]},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Fac': group_input.outputs["Invert"], 'Color': mix_17.outputs[2]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Height': invert}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_table', singleton=False, type='GeometryNodeTree')
def nodegroup_table(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_2 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatDistance', 'Size X', 2.0000),
            ('NodeSocketFloatDistance', 'Size Y', 1.4500),
            ('NodeSocketInt', 'Curve Resolution', 32),
            ('NodeSocketInt', 'Profile Resolution', 32),
            ('NodeSocketInt', 'Legx X', 2),
            ('NodeSocketInt', 'Legs Y', 2),
            ('NodeSocketInt', 'Style', 0),
            ('NodeSocketFloatDistance', 'Radius', 0.1000),
            ('NodeSocketFloat', 'Height', 1.0000),
            ('NodeSocketFloat', 'Radius Min', 0.2400),
            ('NodeSocketFloat', 'Radius Max', 0.4900),
            ('NodeSocketFloat', 'From Min', -0.0400),
            ('NodeSocketFloat', 'From Max', 0.5200),
            ('NodeSocketFloat', 'Wave Scale', 0.4900),
            ('NodeSocketFloat', 'Variation', 54.2000),
            ('NodeSocketFloat', 'Phase Offset', 5.2600),
            ('NodeSocketFloat', 'Legs Offset X', 0.7000),
            ('NodeSocketFloat', 'Legs Offset Y', 0.7000),
            ('NodeSocketFloatDistance', 'Tabletop Thickness', 0.0600),
            ('NodeSocketFloat', 'Apron Offset', 0.1100),
            ('NodeSocketString', 'UV', 'UV_Table'),
            ('NodeSocketString', 'Texture', 'tex_wave'),
            ('NodeSocketMaterial', 'Material', None)]) #surface.shaderfunc_to_material(shader_table)
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Size X"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Size Y"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Tabletop Thickness"]})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_8, 'Y': reroute_11, 'Z': reroute_18})
    
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz_2})
    
    store_named_attribute_4 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    cube_unwrap = nw.new_node(nodegroup_cube_unwrap().name,
        input_kwargs={'Geometry': store_named_attribute_4, 'Unwrap / Smart UV': 1, 'Face 2 UV Rot': 90.0000, 'Face 4 UV Rot': 90.0000, 'Face 6 UV Rot': 0.0000})
    
    bring_to_floor = nw.new_node(nodegroup_bring_to_floor().name, input_kwargs={'Geometry': cube_unwrap.outputs["Geometry"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Height"]})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_40})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_41})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_43})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': bring_to_floor, 'Offset': combine_xyz})
    
    reroute_65 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position})
    
    reroute_64 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_65})
    
    store_named_attribute_3 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': reroute_64, 'Name': 'tabletop', 5: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'FLOAT_COLOR'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Legx X"]})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Legs Y"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    grid_1 = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': reroute_4, 'Size Y': reroute_5, 'Vertices X': reroute_14, 'Vertices Y': reroute_16})
    
    store_named_attribute_5 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid_1.outputs["Mesh"], 'Name': 'uv_map', 3: grid_1.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': store_named_attribute_5})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input_2.outputs["Legs Offset X"], 'Y': group_input_2.outputs["Legs Offset Y"], 'Z': 1.0000})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': reroute_3, 'Rotation': (0.0000, -0.0000, 0.0000), 'Scale': combine_xyz_1})
    
    reroute_63 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform})
    
    reroute_62 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_63})
    
    reroute_61 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_62})
    
    reroute_60 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_61})
    
    decorative_pillar = nw.new_node(nodegroup_decorative_pillar().name,
        input_kwargs={'Curve Resolution': group_input_2.outputs["Curve Resolution"], 'Profile Resolution': group_input_2.outputs["Profile Resolution"], 'Style': group_input_2.outputs["Style"], 'Radius': group_input_2.outputs["Radius"], 'Height': reroute_31, 'Radius Min': group_input_2.outputs["Radius Min"], 'Radius Max': group_input_2.outputs["Radius Max"], 'From Min': group_input_2.outputs["From Min"], 'From Max': group_input_2.outputs["From Max"], 'Wave Scale': group_input_2.outputs["Wave Scale"], 'Variation': group_input_2.outputs["Variation"], 'Phase Offset': group_input_2.outputs["Phase Offset"], 'Texture': group_input_2.outputs["Texture"], 'Fill Caps': True})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': decorative_pillar.outputs["Mesh"]})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    bring_to_floor_1 = nw.new_node(nodegroup_bring_to_floor().name, input_kwargs={'Geometry': reroute_38})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': reroute_60, 'Instance': bring_to_floor_1})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': realize_instances})
    
    reroute_59 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_58})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': reroute_59, 'Name': 'legs', 5: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'FLOAT_COLOR'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_1})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_2, 'Scale': reroute})
    
    vector = nw.new_node(Nodes.Vector)
    vector.vector = (0.0000, 0.0000, -1.0000)
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Apron Offset"]})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_46})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_47})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_48})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': transform_1, 'Offset': vector, 'Offset Scale': reroute_49})
    
    cube_unwrap_1 = nw.new_node(nodegroup_cube_unwrap().name,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'UV Name': 'UV_Cube1'})
    
    inset_faces = nw.new_node(nodegroup_inset_faces().name,
        input_kwargs={'Mesh': cube_unwrap_1.outputs["Geometry"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': 0.9500})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': inset_faces.outputs["Mesh"], 'Selection': inset_faces.outputs["Inset"], 'Offset Scale': 0.0900, 'Individual': False})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Offset': reroute_23})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position_1})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': flip_faces, 'Name': 'apron', 5: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'FLOAT_COLOR'})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [store_named_attribute_3, store_named_attribute_2, store_named_attribute_1]})
    
    reroute_67 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_1})
    
    reroute_66 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_67})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': cube_unwrap.outputs["UV"]})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_44})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_50})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_51})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': decorative_pillar.outputs["UV"]})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_37})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_35})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_34})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_52, 1: reroute_33})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': cube_unwrap_1.outputs["UV"]})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: add.outputs["Vector"], 1: reroute_36})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': reroute_66, 'Name': group_input_2.outputs["UV"], 3: add_1.outputs["Vector"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': store_named_attribute})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Material"]})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    set_material = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': reroute_45, 'Material': reroute_28})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})

def shader_table(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'UV_Table'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': attribute.outputs["Vector"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    group_2 = nw.new_node(nodegroup_scratch_map().name,
        input_kwargs={'Vector': reroute_9, 'Scratches Scale': 45.0000, 'Bias': 0.8800})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': group_2})
    colorramp_5.color_ramp.elements[0].position = 0.0909
    colorramp_5.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.5018
    colorramp_5.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'apron'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': attribute_1.outputs["Fac"], 4: 30.0000})
    
    attribute_2 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'tabletop'})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': attribute_2.outputs["Fac"], 4: 10.7400})
    
    mix_11 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: map_range.outputs["Result"], 7: map_range_1.outputs["Result"]},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    attribute_3 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'legs'})
    
    map_range_2 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': attribute_3.outputs["Fac"], 4: 8.0000})
    
    mix_12 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_11.outputs[2], 7: map_range_2.outputs["Result"]},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_12.outputs[2]})
    
    wave_texture_2 = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': reroute_5, 'Scale': reroute_2, 'Distortion': 0.6800, 'Detail': 12.1000, 'Detail Scale': 11.5800, 'Detail Roughness': 0.5926},
        attrs={'bands_direction': 'Y'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': wave_texture_2.outputs["Color"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_13})
    colorramp_3.color_ramp.elements.new(0)
    colorramp_3.color_ramp.elements[0].position = 0.0327
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.0836
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_3.color_ramp.elements[2].position = 0.1164
    colorramp_3.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_8, 'Scale': 15.6000, 'Detail': 11.2000, 'Roughness': 0.7067})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp_4.color_ramp.elements[0].position = 0.5455
    colorramp_4.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.6036
    colorramp_4.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_3.outputs["Color"], 7: colorramp_4.outputs["Color"]},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_1})
    colorramp_2.color_ramp.interpolation = "CONSTANT"
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.0218
    colorramp_2.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': colorramp_2.outputs["Color"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    group = nw.new_node(nodegroup_edge_mask().name,
        input_kwargs={'Vector': reroute_4, 'Bevel Radius': 0.0550, 'Darken': 0.9400, 'Second Layer': 0.0000})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': reroute, 'Scale': 3.0000, 'Distortion': 9.7700, 'Detail': 10.3000, 'Detail Scale': 1.0800, 'Detail Roughness': 0.5926},
        attrs={'bands_direction': 'Y'})
    
    wave_texture_1 = nw.new_node(Nodes.WaveTexture, input_kwargs={'Vector': wave_texture.outputs["Color"], 'Scale': 1.0600})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': wave_texture_1.outputs["Color"]})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_14, 6: (0.0396, 0.0209, 0.0115, 1.0000), 7: (0.0496, 0.0262, 0.0126, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group, 6: mix.outputs[2], 7: (0.3283, 0.2369, 0.1872, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_3, 6: mix_1.outputs[2], 7: (0.0156, 0.0097, 0.0060, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_4.outputs[2], 6: mix_3.outputs[2], 7: (0.3594, 0.2611, 0.2055, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_10 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_5.outputs["Color"], 6: mix_5.outputs[2], 7: (0.3283, 0.2369, 0.1872, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = -0.3400
    
    mix_13 = nw.new_node(Nodes.Mix, input_kwargs={6: reroute_10, 7: value}, attrs={'blend_type': 'SUBTRACT', 'data_type': 'RGBA'})
    
    brick_texture = nw.new_node(Nodes.BrickTexture,
        input_kwargs={'Vector': reroute_6, 'Color1': (1.0000, 1.0000, 1.0000, 1.0000), 'Color2': (0.5564, 0.5564, 0.5564, 1.0000), 'Scale': mix_13.outputs[2], 'Mortar Size': 0.0000, 'Mortar Smooth': 1.0000, 'Brick Width': 99.9000})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': brick_texture.outputs["Color"]})
    
    mix_14 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_10.outputs[2], 7: reroute_11},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    mix_6 = nw.new_node(Nodes.Mix, input_kwargs={0: reroute_3, 2: 0.1327})
    
    group_1 = nw.new_node(nodegroup_complex_noise().name,
        input_kwargs={'Vector': reroute_7, 'Detail': 12.8000, 'Roughness': 0.7667, 'Color1': (0.7478, 0.7478, 0.7478, 1.0000), 'Pos 1': 0.5800, 'Color2': (0.3442, 0.3442, 0.3442, 1.0000)})
    
    mix_8 = nw.new_node(Nodes.Mix, input_kwargs={0: reroute_3, 2: 1.0000})
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: group_1, 7: mix_8.outputs["Result"]},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_15})
    colorramp.color_ramp.elements[0].position = 0.1236
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.7673
    colorramp.color_ramp.elements[1].color = [0.0020, 0.0020, 0.0020, 1.0000]
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_12})
    colorramp_1.color_ramp.elements[0].position = 0.0909
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.1636
    colorramp_1.color_ramp.elements[1].color = [0.1182, 0.1182, 0.1182, 1.0000]
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.5467, 6: colorramp.outputs["Color"], 7: colorramp_1.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    mix_9 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_5.outputs["Color"], 2: mix_2.outputs[2], 3: -1.0000, 7: (0.0000, 0.0000, 0.0000, 1.0000)})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.3500, 'Height': mix_9.outputs["Result"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_14.outputs[2], 'Specular': mix_6.outputs["Result"], 'Roughness': mix_7.outputs[2], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatDistance', 'Size X', 2.0000),
            ('NodeSocketFloatDistance', 'Size Y', 1.4500),
            ('NodeSocketInt', 'Curve Resolution', 32),
            ('NodeSocketInt', 'Profile Resolution', 32),
            ('NodeSocketInt', 'Legx X', 2),
            ('NodeSocketInt', 'Legs Y', 2),
            ('NodeSocketInt', 'Style', 0),
            ('NodeSocketFloatDistance', 'Radius', 0.1000),
            ('NodeSocketFloat', 'Height', 1.0000),
            ('NodeSocketFloat', 'Radius Min', 0.2400),
            ('NodeSocketFloat', 'Radius Max', 0.4900),
            ('NodeSocketFloat', 'From Min', -0.0400),
            ('NodeSocketFloat', 'From Max', 0.5200),
            ('NodeSocketFloat', 'Wave Scale', 0.4900),
            ('NodeSocketFloat', 'Variation', 54.2000),
            ('NodeSocketFloat', 'Phase Offset', 5.2600),
            ('NodeSocketFloat', 'Legs Offset X', 0.8800),
            ('NodeSocketFloat', 'Legs Offset Y', 0.8800),
            ('NodeSocketFloatDistance', 'Tabletop Thickness', 0.0600),
            ('NodeSocketFloat', 'Apron Offset', 0.1100),
            ('NodeSocketString', 'UV', 'UV_Table'),
            ('NodeSocketString', 'Texture', 'tex_wave'),
            ('NodeSocketMaterial', 'Material', None)]) #surface.shaderfunc_to_material(shader_table)
    
    table = nw.new_node(nodegroup_table().name,
        input_kwargs={'Size X': group_input.outputs["Size X"], 'Size Y': group_input.outputs["Size Y"], 'Curve Resolution': group_input.outputs["Curve Resolution"], 'Profile Resolution': group_input.outputs["Profile Resolution"], 'Legx X': group_input.outputs["Legx X"], 'Legs Y': group_input.outputs["Legs Y"], 'Style': group_input.outputs["Style"], 'Radius': group_input.outputs["Radius"], 'Height': group_input.outputs["Height"], 'Radius Min': group_input.outputs["Radius Min"], 'Radius Max': group_input.outputs["Radius Max"], 'From Min': group_input.outputs["From Min"], 'From Max': group_input.outputs["From Max"], 'Wave Scale': group_input.outputs["Wave Scale"], 'Variation': group_input.outputs["Variation"], 'Phase Offset': group_input.outputs["Phase Offset"], 'Legs Offset X': group_input.outputs["Legs Offset X"], 'Legs Offset Y': group_input.outputs["Legs Offset Y"], 'Tabletop Thickness': group_input.outputs["Tabletop Thickness"], 'Apron Offset': group_input.outputs["Apron Offset"], 'UV': group_input.outputs["UV"], 'Texture': group_input.outputs["Texture"], 'Material': group_input.outputs["Material"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': table}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_table, selection=selection)


import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_a_s_t_rotate_x_y_z_001', singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_rotate_x_y_z_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Direction', 0),
            ('NodeSocketString', '#', '0=X, 1=Y and 2=Z')])
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Direction"]})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_2, 1: 1.0000}, attrs={'operation': 'EQUAL'})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 90.0000
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': value})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={0: equal, 3: reroute_1}, attrs={'input_type': 'FLOAT'})
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_2}, attrs={'operation': 'EQUAL'})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={0: equal_1, 3: reroute_1}, attrs={'input_type': 'FLOAT'})
    
    equal_2 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_2, 1: 2.0000}, attrs={'operation': 'EQUAL'})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={0: equal_2, 3: reroute_1}, attrs={'input_type': 'FLOAT'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': switch.outputs["Output"], 'Y': switch_2.outputs["Output"], 'Z': switch_1.outputs["Output"]})
    
    divide = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_xyz_3, 1: (57.2958, 57.2958, 57.2958)},
        attrs={'operation': 'DIVIDE'})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Rotation': divide.outputs["Vector"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_a_s_t_mono_directional_bezier_001', singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_mono_directional_bezier_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketIntUnsigned', 'Resolution', 16),
            ('NodeSocketVectorEuler', 'Start', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Center', 0.0000),
            ('NodeSocketFloat', 'Middle X', 0.0000),
            ('NodeSocketFloat', 'Middle Y', 0.0000),
            ('NodeSocketFloat', 'Length', 1.0000),
            ('NodeSocketFloat', 'End X', 0.0000),
            ('NodeSocketFloat', 'End Y', 0.0000),
            ('NodeSocketInt', 'Direction', 0)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Length"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Center"], 1: 2.0000})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: add}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Middle X"], 'Y': group_input.outputs["Middle Y"], 'Z': divide})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["End X"], 'Y': group_input.outputs["End Y"], 'Z': reroute})
    
    quadratic_bezier = nw.new_node(Nodes.QuadraticBezier,
        input_kwargs={'Resolution': group_input.outputs["Resolution"], 'Start': group_input.outputs["Start"], 'Middle': combine_xyz_1, 'End': combine_xyz})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': quadratic_bezier, 2: spline_parameter.outputs["Length"]})
    
    ast_rotate_xyz_001 = nw.new_node(nodegroup_a_s_t_rotate_x_y_z_001().name,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Direction': group_input.outputs["Direction"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Curve': ast_rotate_xyz_001, 'Length': capture_attribute.outputs[2], 'Factor': spline_parameter.outputs["Factor"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup("nodegroup_a_s_t_abhays_round_curve_001", singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_abhays_round_curve_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketIntUnsigned', 'Resolution', 64),
            ('NodeSocketFloatFactor', 'Length', 1.0000),
            ('NodeSocketFloatDistance', 'Radius', 1.0000),
            ('NodeSocketBool', 'Fill', False),
            ('NodeSocketInt', 'Cut', 0),
            ('NodeSocketFloat', 'Rotation', 6.2832),
            ('NodeSocketFloat', 'Edge Scale', 1.0000),
            ('NodeSocketFloat', 'Even Index Z offset', 0.0000)])
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Length"]})
    
    ast_mono_directional_bezier_001 = nw.new_node(nodegroup_a_s_t_mono_directional_bezier_001().name,
        input_kwargs={'Resolution': group_input.outputs["Resolution"], 'Length': reroute_4})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: group_input.outputs["Cut"]})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_4, 1: spline_parameter.outputs["Factor"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute, 1: group_input.outputs["Rotation"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1}, attrs={'operation': 'SINE'})
    
    sine_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1}, attrs={'operation': 'SINE', 'use_clamp': True})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={0: greater_than, 2: sine, 3: sine_1}, attrs={'input_type': 'FLOAT'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: switch_1.outputs["Output"], 1: reroute}, attrs={'operation': 'SUBTRACT'})
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={0: group_input.outputs["Cut"], 1: 1.0000})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    cosine = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2}, attrs={'operation': 'COSINE'})
    
    cosine_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2}, attrs={'operation': 'COSINE', 'use_clamp': True})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={0: greater_than_1, 2: cosine, 3: cosine_1}, attrs={'input_type': 'FLOAT'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract, 'Y': switch_2.outputs["Output"]})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': ast_mono_directional_bezier_001.outputs["Curve"], 'Offset': combine_xyz})
    
    ast_index_selection_001 = nw.new_node(nodegroup_a_s_t_index_selection_001().name)
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Even Index Z offset"]})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': ast_index_selection_001.outputs["Even Selection"], 'Offset': combine_xyz_1})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_1, 'Scale': group_input.outputs["Radius"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': transform})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': curve_to_mesh, 'Selection': ast_index_selection_001.outputs["Even Selection"], 'Scale': group_input.outputs["Edge Scale"], 'Axis': (0.0000, 0.0000, 0.0000)},
        attrs={'domain': 'EDGE'})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': scale_elements})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': merge_by_distance})
    
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': mesh_to_curve}, attrs={'mode': 'NGONS'})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Fill"], 14: mesh_to_curve, 15: fill_curve})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Curve': switch.outputs[6], 'Length': ast_mono_directional_bezier_001.outputs["Length"], 'Mesh': merge_by_distance},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_vecter_curve_circle', singleton=False, type='GeometryNodeTree')
def nodegroup_vecter_curve_circle(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatDistance', 'Radius', 1.0000),
            ('NodeSocketInt', 'Turns', 6)])
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 512, 'Radius': group_input.outputs["Radius"]})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_parameter.outputs["Factor"], 1: group_input.outputs["Turns"]},
        attrs={'operation': 'MULTIPLY'})
    
    fract = nw.new_node(Nodes.Math, input_kwargs={0: multiply}, attrs={'operation': 'FRACT'})
    
    sample_curve = nw.new_node(Nodes.SampleCurve, input_kwargs={'Curves': curve_circle_1.outputs["Curve"], 'Factor': fract})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Vecter': sample_curve.outputs["Position"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_recurve', singleton=False, type='GeometryNodeTree')
def nodegroup_recurve(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketBool', 'Merge by Distance', True),
            ('NodeSocketFloatDistance', 'Distance', 0.0010)])
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': group_input.outputs["Curve"]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance,
        input_kwargs={'Geometry': curve_to_mesh, 'Distance': group_input.outputs["Distance"]})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["Merge by Distance"], 14: curve_to_mesh, 15: merge_by_distance})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': switch.outputs[6]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Curve': mesh_to_curve}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_a_s_t_index_selection_001', singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_index_selection_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    index_2 = nw.new_node(Nodes.Index)
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: index_2, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    less_equal = nw.new_node(Nodes.Compare, input_kwargs={0: modulo}, attrs={'operation': 'LESS_EQUAL'})
    
    greater_equal = nw.new_node(Nodes.Compare, input_kwargs={0: modulo, 1: 1.0000}, attrs={'operation': 'GREATER_EQUAL'})
    
    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketInt', '%', 2)])
    
    modulo_1 = nw.new_node(Nodes.Math, input_kwargs={0: index_2, 1: group_input.outputs["%"]}, attrs={'operation': 'MODULO'})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: modulo_1}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_1 = nw.new_node(Nodes.Compare,
        input_kwargs={1: 1.0000, 2: modulo_1, 3: 1},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_2 = nw.new_node(Nodes.Compare,
        input_kwargs={1: 1.0000, 2: modulo_1, 3: 2},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_3 = nw.new_node(Nodes.Compare,
        input_kwargs={1: 1.0000, 2: modulo_1, 3: 3},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_4 = nw.new_node(Nodes.Compare,
        input_kwargs={1: 1.0000, 2: modulo_1, 3: 4},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Even Selection': less_equal, 'Odd Selection': greater_equal, '1st': equal, '2nd': equal_1, '3rd': equal_2, '4th': equal_3, '5th': equal_4},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_delete_vertices_in_centre', singleton=False, type='GeometryNodeTree')
def nodegroup_delete_vertices_in_centre(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={4: position_1}, attrs={'operation': 'EQUAL', 'data_type': 'VECTOR'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': equal})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': delete_geometry}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_change_spline_type_001', singleton=False, type='GeometryNodeTree')
def nodegroup_change_spline_type_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketInt', 'Select', 0)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Select"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_1}, attrs={'data_type': 'INT'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Curve"]})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': reroute_4})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_2, 3: 1}, attrs={'data_type': 'INT'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    set_spline_type_1 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': reroute_5}, attrs={'spline_type': 'CATMULL_ROM'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    greater_than_2 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_3, 3: 2}, attrs={'data_type': 'INT'})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    set_spline_type_2 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': reroute_6}, attrs={'spline_type': 'NURBS'})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    set_spline_type_3 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': reroute_7}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type_3})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than_2, 14: set_spline_type_2, 15: set_handle_type})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than_1, 14: set_spline_type_1, 15: switch_2.outputs[6]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than, 14: set_spline_type, 15: switch_1.outputs[6]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Curve': switch.outputs[6]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_a_s_t_curve_to_circular_mesh_001', singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_curve_to_circular_mesh_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketInt', 'Resolution', 32),
            ('NodeSocketFloatDistance', 'Radius', 1.0000),
            ('NodeSocketBool', 'Fill Caps', True),
            ('NodeSocketBool', 'Shade Smooth', True),
            ('NodeSocketString', 'UVMap', 'UVMap')])
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': group_input.outputs["Curve"], 2: spline_parameter.outputs["Length"]})
    
    ast_abhay_s_round_curve_001 = nw.new_node(nodegroup_a_s_t_abhays_round_curve_001().name,
        input_kwargs={'Resolution': group_input.outputs["Resolution"], 'Radius': group_input.outputs["Radius"]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': capture_attribute.outputs["Geometry"], 'Profile Curve': ast_abhay_s_round_curve_001.outputs["Curve"], 'Fill Caps': group_input.outputs["Fill Caps"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Shade Smooth': group_input.outputs["Shade Smooth"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': capture_attribute.outputs[2], 'Y': ast_abhay_s_round_curve_001.outputs["Length"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': set_shade_smooth, 'Name': group_input.outputs["UVMap"], 3: combine_xyz},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': store_named_attribute})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': flip_faces})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': merge_by_distance, 'UV': combine_xyz},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_dicircle_pattern', singleton=False, type='GeometryNodeTree')
def nodegroup_dicircle_pattern(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Resolution', 512),
            ('NodeSocketFloatDistance', 'Major Radius', 0.0100),
            ('NodeSocketInt', 'Major Turns', 7),
            ('NodeSocketFloatDistance', 'Minor Radius', 0.5000),
            ('NodeSocketInt', 'Minor Turns', 60)])
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': group_input.outputs["Resolution"]})
    
    vecter_curve_circle = nw.new_node(nodegroup_vecter_curve_circle().name,
        input_kwargs={'Radius': group_input.outputs["Major Radius"], 'Turns': group_input.outputs["Major Turns"]})
    
    vecter_curve_circle_1 = nw.new_node(nodegroup_vecter_curve_circle().name,
        input_kwargs={'Radius': group_input.outputs["Minor Radius"], 'Turns': group_input.outputs["Minor Turns"]})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: vecter_curve_circle, 1: vecter_curve_circle_1})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Position': add.outputs["Vector"]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_position})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': curve_to_mesh_1})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Max"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Curve ': set_position, 'Mesh': curve_to_mesh_1, 'Radius': separate_xyz.outputs["X"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_projec__funnel', singleton=False, type='GeometryNodeTree')
def nodegroup_projec__funnel(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    curve_line = nw.new_node(Nodes.CurveLine)
    
    index = nw.new_node(Nodes.Index)
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Inner Radius', 0.0000),
            ('NodeSocketFloat', 'Outer Radius', 0.0000),
            ('NodeSocketInt', 'Resolution vertically', 32),
            ('NodeSocketInt', 'Resolution hozontally', 128),
            ('NodeSocketFloatFactor', 'Profile Fac', 1.0000),
            ('NodeSocketString', 'UVMap', 'UVMap')])
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Inner Radius"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Outer Radius"]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={0: index, 2: reroute_4, 3: reroute}, attrs={'input_type': 'FLOAT'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': curve_line, 'Radius': switch.outputs["Output"]})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_curve_radius, 'Count': group_input.outputs["Resolution vertically"]})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': spline_parameter.outputs["Length"]})
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': resample_curve_1, 2: reroute_1})
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': group_input.outputs["Resolution hozontally"], 'Rotations': 1.0000, 'End Radius': 1.0000, 'Height': 0.0000})
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': spiral, 2: reroute_1})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': capture_attribute.outputs["Geometry"], 'Profile Curve': capture_attribute_1.outputs["Geometry"]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': curve_to_mesh})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': capture_attribute.outputs[2], 'Y': capture_attribute_1.outputs[2]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_1})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': merge_by_distance, 'Name': group_input.outputs["UVMap"], 3: reroute_2},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position, 1: (1.0000, 1.0000, 0.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    length = nw.new_node(Nodes.VectorMath, input_kwargs={0: multiply.outputs["Vector"]}, attrs={'operation': 'LENGTH'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': length.outputs["Value"], 1: reroute_4, 2: reroute})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve,
        input_kwargs={'Factor': group_input.outputs["Profile Fac"], 'Value': map_range.outputs["Result"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0000), (0.8864, 0.0062), (0.9682, 0.0688), (0.9864, 0.2062), (1.0000, 1.0000)])
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': float_curve_1})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute, 'Position': multiply.outputs["Vector"], 'Offset': combine_xyz})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position_2})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': flip_faces, 'Vector': reroute_2},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_align_to_3_d_plane', singleton=False, type='GeometryNodeTree')
def nodegroup_align_to_3_d_plane(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    bounding_box_1 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': group_input.outputs["Geometry"]})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_1.outputs["Min"]})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: 0.0000, 1: separate_xyz_1.outputs["Z"]}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': subtract})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Offset': combine_xyz_1})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_position_4}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Resolution', 512),
            ('NodeSocketInt', 'Major Turns1', 7),
            ('NodeSocketInt', 'Minor Turns1', 60),
            ('NodeSocketVector', 'Scale', (1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloatFactor', 'Factor', 0.0000),
            ('NodeSocketBool', 'Base', True),
            ('NodeSocketInt', 'Base Resolution vertically', 32),
            ('NodeSocketInt', 'Base Resolution hozontally', 128),
            ('NodeSocketFloatFactor', 'Caos', 0.5000),
            ('NodeSocketFloatDistance', 'Distance', 0.0250),
            ('NodeSocketBool', 'Caos Align', False),
            ('NodeSocketInt', 'Spline Smoothness', 3),
            ('NodeSocketFloatDistance', 'Resample Length', 0.1000),
            ('NodeSocketInt', 'Skinning Resolution', 4),
            ('NodeSocketFloatDistance', 'Skinning Radius', 0.0100),
            ('NodeSocketBool', 'Shade Smooth', False),
            ('NodeSocketBool', 'Normal Direction Z UP', False),
            ('NodeSocketString', 'Buttom Controls', ''),
            ('NodeSocketInt', 'Major Turns', 22),
            ('NodeSocketInt', 'Minor Turns', 60),
            ('NodeSocketString', 'UVMap Wire', 'Map Skinning'),
            ('NodeSocketString', 'UVMap Base', 'Map Base'),
            ('NodeSocketMaterial', 'Wire Material', None),
            ('NodeSocketMaterial', 'Base Material', None)])
    
    mix = nw.new_node(Nodes.Mix, input_kwargs={0: group_input.outputs["Factor"], 3: 0.5000})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Resolution"]})
    
    di_circle_pattern = nw.new_node(nodegroup_dicircle_pattern().name,
        input_kwargs={'Resolution': reroute_2, 'Major Turns': group_input.outputs["Major Turns"], 'Minor Turns': group_input.outputs["Minor Turns"]})
    
    projec_funnel = nw.new_node(nodegroup_projec__funnel().name,
        input_kwargs={'Inner Radius': mix.outputs["Result"], 'Outer Radius': di_circle_pattern.outputs["Radius"], 'Resolution vertically': group_input.outputs["Base Resolution vertically"], 'Resolution hozontally': group_input.outputs["Base Resolution hozontally"], 'UVMap': group_input.outputs["UVMap Base"]})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Base"], 15: projec_funnel.outputs["Geometry"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    transform_geometry_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': switch_1.outputs[6], 'Scale': reroute_1})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': transform_geometry_2, 'Offset Scale': -0.0100, 'Individual': False})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Side"], 'Shade Smooth': False})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_shade_smooth})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces, transform_geometry_2]})
    
    merge_by_distance_1 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_2})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Base Material"]})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': merge_by_distance_1, 'Material': reroute_21})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Caos Align"]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': projec_funnel.outputs["Geometry"], 'Ray Direction': (0.0000, 0.0000, 1.0000)})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': di_circle_pattern.outputs["Mesh"], 'Position': raycast.outputs["Hit Position"]})
    
    delete_vertices_in_centre = nw.new_node(nodegroup_delete_vertices_in_centre().name, input_kwargs={'Geometry': set_position_1})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Distance"]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': delete_vertices_in_centre, 'Distance': reroute_5})
    
    ast_index_selection_001 = nw.new_node(nodegroup_a_s_t_index_selection_001().name)
    
    mix_1 = nw.new_node(Nodes.Mix, input_kwargs={0: group_input.outputs["Caos"], 2: 1.0000, 3: 1.2500})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': merge_by_distance, 'Selection': ast_index_selection_001.outputs["Even Selection"], 'Scale': mix_1.outputs["Result"]},
        attrs={'domain': 'EDGE'})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': scale_elements})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Spline Smoothness"]})
    
    change_spline_type_001 = nw.new_node(nodegroup_change_spline_type_001().name, input_kwargs={'Curve': mesh_to_curve, 'Select': reroute_4})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Resample Length"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': change_spline_type_001, 'Count': 32, 'Length': reroute},
        attrs={'mode': 'LENGTH'})
    
    align_to_3d_plane = nw.new_node(nodegroup_align_to_3_d_plane().name, input_kwargs={'Geometry': resample_curve})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_11, 14: resample_curve, 15: align_to_3d_plane})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_2.outputs[6]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs[19]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs[20]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    di_circle_pattern_1 = nw.new_node(nodegroup_dicircle_pattern().name,
        input_kwargs={'Resolution': reroute_3, 'Major Radius': 1.0000, 'Major Turns': reroute_6, 'Minor Radius': 1.0000, 'Minor Turns': reroute_7})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': resample_curve})
    
    divide_by_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box.outputs["Max"], 1: (2.0000, 2.0000, 2.0000)},
        label='Divide by 2',
        attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: divide_by_2.outputs["Vector"], 1: (0.0100, 0.0100, 0.0000)},
        attrs={'operation': 'SUBTRACT'})
    
    transform_geometry = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': di_circle_pattern_1.outputs["Curve "], 'Scale': subtract.outputs["Vector"]})
    
    re_curve = nw.new_node(nodegroup_recurve().name, input_kwargs={'Curve': transform_geometry, 'Distance': reroute_5})
    
    gradient_texture = nw.new_node(Nodes.GradientTexture, attrs={'gradient_type': 'SPHERICAL'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': gradient_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5227
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': colorramp.outputs["Color"]})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': re_curve, 'Offset': combine_xyz})
    
    change_spline_type_001_1 = nw.new_node(nodegroup_change_spline_type_001().name, input_kwargs={'Curve': set_position, 'Select': reroute_4})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': change_spline_type_001_1, 'Count': 32, 'Length': reroute},
        attrs={'mode': 'LENGTH'})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': resample_curve_1})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_14, reroute_13]})
    
    transform_geometry_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_1, 'Scale': reroute_1})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_geometry_1})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    set_curve_normal = nw.new_node('GeometryNodeSetCurveNormal', input_kwargs={'Curve': reroute_16}, attrs={'mode': 'Z_UP'})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["Normal Direction Z UP"], 14: reroute_17, 15: set_curve_normal})
    
    ast_curve_to_circular_mesh_001 = nw.new_node(nodegroup_a_s_t_curve_to_circular_mesh_001().name,
        input_kwargs={'Curve': switch.outputs[6], 'Resolution': group_input.outputs["Skinning Resolution"], 'Radius': group_input.outputs["Skinning Radius"], 'Shade Smooth': group_input.outputs["Shade Smooth"], 'UVMap': group_input.outputs["UVMap Wire"]})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wire Material"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': ast_curve_to_circular_mesh_001.outputs["Mesh"], 'Material': reroute_19})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_1, set_material]})
    
    align_to_3d_plane_1 = nw.new_node(nodegroup_align_to_3_d_plane().name, input_kwargs={'Geometry': join_geometry})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': align_to_3d_plane_1, 'Base': projec_funnel.outputs["Geometry"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
apply(bpy.context.active_object)
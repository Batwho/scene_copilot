import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



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

@node_utils.to_nodegroup('nodegroup_shape', singleton=False, type='GeometryNodeTree')
def nodegroup_shape(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Fac', 0.6400),
            ('NodeSocketIntUnsigned', 'Amount', 32),
            ('NodeSocketInt', 'Spline type', 2),
            ('NodeSocketFloatDistance', 'Radius', 1.0000),
            ('NodeSocketInt', 'Resolution', 16)])
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': group_input.outputs["Amount"], 'Rotations': 1.0000, 'End Radius': 1.0000, 'Height': 0.0000})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': spiral, 2: spline_parameter.outputs["Length"]})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 1.0000), (0.5000, 0.0000), (1.0000, 1.0000)])
    
    subtract_from_0 = nw.new_node(Nodes.Math,
        input_kwargs={0: 0.0000, 1: float_curve},
        label='subtract from 0',
        attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: subtract_from_0, 1: group_input.outputs["Fac"]},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Offset': combine_xyz})
    
    change_spline_type_001 = nw.new_node(nodegroup_change_spline_type_001().name,
        input_kwargs={'Curve': set_position, 'Select': group_input.outputs["Spline type"]})
    
    transform_geometry = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': change_spline_type_001, 'Scale': group_input.outputs["Radius"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': transform_geometry, 'Count': group_input.outputs["Resolution"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Curve': resample_curve, 'Length': capture_attribute.outputs[2]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_curve_merge_001', singleton=False, type='GeometryNodeTree')
def nodegroup_curve_merge_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketFloatDistance', 'Distance', 0.0010)])
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': group_input.outputs["Curve"]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance,
        input_kwargs={'Geometry': curve_to_mesh, 'Distance': group_input.outputs["Distance"]})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': merge_by_distance})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Curve': mesh_to_curve}, attrs={'is_active_output': True})

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

@node_utils.to_nodegroup('nodegroup_aloe_vera_leaf_gen', singleton=False, type='GeometryNodeTree')
def nodegroup_aloe_vera_leaf_gen(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketIntUnsigned', 'Resolution V', 16),
            ('NodeSocketInt', 'Resolution U', 32),
            ('NodeSocketFloat', 'Fac', 0.7500),
            ('NodeSocketFloat', 'Middle X', 0.0000),
            ('NodeSocketFloat', 'Middle Y', 0.0000),
            ('NodeSocketFloat', 'Length', 1.0000),
            ('NodeSocketFloatDistance', 'Radius', 0.1500),
            ('NodeSocketFloat', 'End X', 0.0000),
            ('NodeSocketFloat', 'End Y', 0.0000),
            ('NodeSocketIntUnsigned', 'Amount', 6),
            ('NodeSocketInt', 'Spline type', 1),
            ('NodeSocketBool', 'Fill Caps', False)])
    
    ast_mono_directional_bezier_001 = nw.new_node(nodegroup_a_s_t_mono_directional_bezier_001().name,
        input_kwargs={'Resolution': group_input.outputs["Resolution V"], 'Middle X': group_input.outputs["Middle X"], 'Middle Y': group_input.outputs["Middle Y"], 'Length': group_input.outputs["Length"], 'End X': group_input.outputs["End X"], 'End Y': group_input.outputs["End Y"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: ast_mono_directional_bezier_001.outputs["Factor"], 1: 1.5708},
        attrs={'operation': 'MULTIPLY'})
    
    cosine = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 0.0300}, attrs={'operation': 'COSINE'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius,
        input_kwargs={'Curve': ast_mono_directional_bezier_001.outputs["Curve"], 'Radius': cosine})
    
    shape = nw.new_node(nodegroup_shape().name,
        input_kwargs={'Fac': group_input.outputs["Fac"], 'Amount': group_input.outputs["Amount"], 'Spline type': group_input.outputs["Spline type"], 'Radius': group_input.outputs["Radius"], 'Resolution': group_input.outputs["Resolution U"]})
    
    curve_merge_001 = nw.new_node(nodegroup_curve_merge_001().name, input_kwargs={'Curve': shape.outputs["Curve"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': curve_merge_001, 'Fill Caps': group_input.outputs["Fill Caps"]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': curve_to_mesh})
    
    transform_geometry = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': merge_by_distance, 'Rotation': (0.0000, -1.5708, 0.0000)})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': ast_mono_directional_bezier_001.outputs["Length"], 'Y': shape.outputs["Length"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': transform_geometry, 'UVMap': combine_xyz},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_a_s_t_phyllotaxis', singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_phyllotaxis(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Vertices', 500),
            ('NodeSocketFloatAngle', 'Angle', 2.3998),
            ('NodeSocketFloatDistance', 'Radius', 1.0000),
            ('NodeSocketFloat', 'Expand', 0.0000),
            ('NodeSocketFloatDistance', 'Depth', 0.0000),
            ('NodeSocketFloat', 'Exponent', 1.0000)])
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Vertices"]})
    
    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': reroute_13})
    
    index = nw.new_node(Nodes.Index)
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': index})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Angle"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_12, 1: reroute_11}, attrs={'operation': 'MULTIPLY'})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: multiply}, attrs={'operation': 'SINE'})
    
    cosine = nw.new_node(Nodes.Math, input_kwargs={0: multiply}, attrs={'operation': 'COSINE'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': sine, 'Y': cosine})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': index})
    
    sqrt = nw.new_node(Nodes.Math, input_kwargs={0: reroute_9}, attrs={'operation': 'SQRT'})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Expand"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: sqrt, 1: reroute_8})
    
    maximum = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: 0.0000}, attrs={'operation': 'MAXIMUM'})
    
    scale = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz, 'Scale': maximum}, attrs={'operation': 'SCALE'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_line, 'Position': scale.outputs["Vector"]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': set_position}, attrs={'legacy_behavior': True})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': realize_instances})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Min"]})
    
    maximum_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["X"], 1: separate_xyz.outputs["Y"]},
        attrs={'operation': 'MAXIMUM'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute_14, 1: maximum_1}, attrs={'operation': 'DIVIDE'})
    
    scale_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 'Scale': divide}, attrs={'operation': 'SCALE'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position, 'Position': scale_1.outputs["Vector"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': position_1}, attrs={'axis': 'Y'})
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': set_position_1, 1: align_euler_to_vector},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs["Geometry"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': index})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Vertices"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_3, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: subtract}, attrs={'operation': 'DIVIDE'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: divide_1}, attrs={'operation': 'SUBTRACT'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Exponent"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: subtract_1, 1: reroute}, attrs={'operation': 'POWER'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Depth"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: power, 1: reroute_1}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_1})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_1})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_19, 'Offset': reroute_18})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': set_position_2})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Vertices"]})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide_1})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs["Attribute"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Points': mesh_to_points, 'Size': reroute_15, 'Falloff': reroute_17, 'Rotation': reroute_16},
        attrs={'is_active_output': True})

def shader_aloen_leaves(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'ALOE_VERA'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': attribute.outputs["Vector"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_xyz.outputs["X"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.2773
    colorramp.color_ramp.elements[0].color = [0.4723, 1.0000, 0.0500, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.4227
    colorramp.color_ramp.elements[1].color = [0.0669, 0.4166, 0.0008, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.9045
    colorramp.color_ramp.elements[2].color = [0.0065, 0.1328, 0.0000, 1.0000]
    
    ambient_occlusion = nw.new_node(Nodes.AmbientOcclusion)
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={6: colorramp.outputs["Color"], 7: ambient_occlusion.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': attribute.outputs["Vector"], 'Scale': (5.0000, 1.0000, 1.0000)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 2.5000, 'Detail': 5.0000})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Hue': 0.0000, 'Saturation': 2.0000, 'Color': noise_texture.outputs["Color"]})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.4000, 6: mix.outputs[2], 7: hue_saturation_value},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_1.outputs[2]})
    
    fresnel = nw.new_node(Nodes.Fresnel)
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': fresnel})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5455
    colorramp_2.color_ramp.elements[1].color = [0.1000, 0.1000, 0.1000, 1.0000]
    
    geometry = nw.new_node(Nodes.NewGeometry)
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': geometry.outputs["Pointiness"]})
    colorramp_3.color_ramp.elements[0].position = 0.5273
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.6000
    colorramp_3.color_ramp.elements[1].color = [0.1000, 0.1000, 0.1000, 1.0000]
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_2.outputs["Color"], 7: colorramp_3.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'SCREEN'})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_xyz.outputs["X"]})
    colorramp_4.color_ramp.interpolation = "EASE"
    colorramp_4.color_ramp.elements.new(0)
    colorramp_4.color_ramp.elements[0].position = 0.2773
    colorramp_4.color_ramp.elements[0].color = [1.0000, 0.0500, 0.0500, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.4227
    colorramp_4.color_ramp.elements[1].color = [0.4166, 0.0008, 0.0008, 1.0000]
    colorramp_4.color_ramp.elements[2].position = 0.9045
    colorramp_4.color_ramp.elements[2].color = [0.1328, 0.0000, 0.0000, 1.0000]
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_xyz.outputs["X"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [0.6000, 0.6000, 0.6000, 1.0000]
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': attribute.outputs["Vector"]})
    
    bump_1 = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.1000, 'Height': noise_texture_1.outputs["Fac"]})
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.1000, 'Height': noise_texture.outputs["Fac"], 'Normal': bump_1})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': reroute, 'Subsurface': mix_2.outputs[2], 'Subsurface Radius': (1.0000, 0.2500, 0.2000), 'Subsurface Color': colorramp_4.outputs["Color"], 'Specular': 0.4900, 'Roughness': colorramp_1.outputs["Color"], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Quality', 1),
            ('NodeSocketString', 'Plant COntrols', ''),
            ('NodeSocketInt', 'Leaves Count', 16),
            ('NodeSocketFloat', 'Length', 1.0000),
            ('NodeSocketFloatDistance', 'Leaves Radius', 0.1500),
            ('NodeSocketFloatDistance', 'Radius', 0.1000),
            ('NodeSocketFloatFactor', 'Depth', 0.3000),
            ('NodeSocketFloatFactor', 'Depth 2', 1.0000),
            ('NodeSocketFloat', 'Depth align', 0.0000),
            ('NodeSocketFloat', 'Angle', 0.0000),
            ('NodeSocketFloat', 'Tilt', -6.0000),
            ('NodeSocketFloat', 'Fac', 0.7500),
            ('NodeSocketIntUnsigned', 'Amount', 6),
            ('NodeSocketInt', 'Spline type', 1),
            ('NodeSocketString', 'Shape Leaves', ''),
            ('NodeSocketFloat', 'Middle X', 0.0000),
            ('NodeSocketFloat', 'Middle Y', 0.0300),
            ('NodeSocketFloat', 'End X', 0.0000),
            ('NodeSocketFloat', 'End Y', 0.6100),
            ('NodeSocketMaterial', 'Material', None), #surface.shaderfunc_to_material(shader_aloen_leaves)
            ('NodeSocketString', 'UVMAP', 'ALOE_VERA')])
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Leaves Count"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Depth"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    mix = nw.new_node(Nodes.Mix, input_kwargs={0: reroute_8, 2: -0.1000, 3: 0.2500})
    
    ast_phyllotaxis = nw.new_node(nodegroup_a_s_t_phyllotaxis().name,
        input_kwargs={'Vertices': reroute_10, 'Radius': group_input.outputs["Radius"], 'Depth': mix.outputs["Result"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Quality"]})
    
    times16 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 16.0000}, label='times16', attrs={'operation': 'MULTIPLY'})
    
    times32 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 32.0000}, label='times32', attrs={'operation': 'MULTIPLY'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': times32})
    
    aloe_vera_leaf_gen = nw.new_node(nodegroup_aloe_vera_leaf_gen().name,
        input_kwargs={'Resolution V': times16, 'Resolution U': reroute_2, 'Fac': group_input.outputs["Fac"], 'Middle X': group_input.outputs["Middle X"], 'Middle Y': group_input.outputs["Middle Y"], 'Length': group_input.outputs["Length"], 'Radius': group_input.outputs["Leaves Radius"], 'End X': group_input.outputs["End X"], 'End Y': group_input.outputs["End Y"], 'Amount': group_input.outputs["Amount"], 'Spline type': group_input.outputs["Spline type"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': ast_phyllotaxis.outputs["Falloff"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.4000, 0.4000, 0.4000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.0273
    colorramp.color_ramp.elements[1].color = [0.6000, 0.6000, 0.6000, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.3000
    colorramp.color_ramp.elements[2].color = [0.7000, 0.7000, 0.7000, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.4000
    colorramp.color_ramp.elements[3].color = [0.8000, 0.8000, 0.8000, 1.0000]
    colorramp.color_ramp.elements[4].position = 1.0000
    colorramp.color_ramp.elements[4].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': ast_phyllotaxis.outputs["Points"], 'Instance': aloe_vera_leaf_gen.outputs["Geometry"], 'Rotation': ast_phyllotaxis.outputs["Rotation"], 'Scale': colorramp.outputs["Color"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: ast_phyllotaxis.outputs["Falloff"], 1: 50.0000},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: group_input.outputs["Angle"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tilt"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add, 'Y': reroute_9})
    
    divide = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_xyz, 1: (-57.2958, -57.2958, -57.2958)},
        attrs={'operation': 'DIVIDE'})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': instance_on_points, 'Rotation': divide.outputs["Vector"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': rotate_instances})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': realize_instances, 'Name': group_input.outputs["UVMAP"], 3: aloe_vera_leaf_gen.outputs["UVMap"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': store_named_attribute, 'Material': group_input.outputs["Material"]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': set_material})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_aloen_leaves, selection=selection)
apply(bpy.context.active_object)
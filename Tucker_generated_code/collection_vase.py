import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_a_s_t_index_selection', singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_index_selection(nw: NodeWrangler):
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

@node_utils.to_nodegroup('nodegroup_a_s_t_rotate_x_y_z', singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_rotate_x_y_z(nw: NodeWrangler):
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

@node_utils.to_nodegroup("nodegroup_a_s_t_abhays_round_curve", singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_abhays_round_curve(nw: NodeWrangler):
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
    
    ast_mono_directional_bezier = nw.new_node(nodegroup_a_s_t_mono_directional_bezier().name,
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
        input_kwargs={'Geometry': ast_mono_directional_bezier.outputs["Curve"], 'Offset': combine_xyz})
    
    ast_index_selection = nw.new_node(nodegroup_a_s_t_index_selection().name)
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Even Index Z offset"]})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': ast_index_selection.outputs["Even Selection"], 'Offset': combine_xyz_1})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_1, 'Scale': group_input.outputs["Radius"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': transform})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': curve_to_mesh, 'Selection': ast_index_selection.outputs["Even Selection"], 'Scale': group_input.outputs["Edge Scale"], 'Axis': (0.0000, 0.0000, 0.0000)},
        attrs={'domain': 'EDGE'})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': scale_elements})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': merge_by_distance})
    
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': mesh_to_curve}, attrs={'mode': 'NGONS'})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Fill"], 14: mesh_to_curve, 15: fill_curve})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Curve': switch.outputs[6], 'Length': ast_mono_directional_bezier.outputs["Length"], 'Mesh': merge_by_distance},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_if_u_v_not_exists_use_generative_001', singleton=False, type='ShaderNodeTree')
def nodegroup_if_u_v_not_exists_use_generative_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vecter', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Threshold', 0.0001)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Vecter"]})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute, 1: group_input.outputs["Threshold"]},
        attrs={'operation': 'GREATER_THAN'})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: greater_than, 4: texture_coordinate.outputs["Generated"], 5: reroute},
        attrs={'data_type': 'VECTOR'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vecter': mix_1.outputs[1]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_ceramic-4', singleton=False, type='ShaderNodeTree')
def nodegroup_ceramic4(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vecter', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Hue', 0.5000),
            ('NodeSocketFloat', 'Saturation', 1.0000),
            ('NodeSocketFloat', 'Value', 1.0000),
            ('NodeSocketFloatFactor', 'Specular', 0.5000),
            ('NodeSocketFloatFactor', 'Clearcoat', 0.0000),
            ('NodeSocketFloatFactor', 'Clearcoat Roughness', 0.0300),
            ('NodeSocketFloat', 'Displacement', 0.0010),
            ('NodeSocketFloat', 'Scale', 1.0000),
            ('NodeSocketFloatFactor', 'Fac', 0.0000)])
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: group_input_1.outputs["Vecter"], 'Scale': group_input_1.outputs["Scale"]},
        attrs={'operation': 'SCALE'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale.outputs["Vector"]})
    
    base_color = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Base Color',
        attrs={'image': bpy.data.images['ceramic_4_basecolor-2K.png']})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': base_color.outputs["Color"]})
    colorramp.color_ramp.interpolation = "CONSTANT"
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.1455
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Hue': group_input_1.outputs["Hue"], 'Saturation': group_input_1.outputs["Saturation"], 'Value': group_input_1.outputs["Value"], 'Fac': colorramp.outputs["Color"], 'Color': base_color.outputs["Color"]})
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Fac': group_input_1.outputs["Fac"], 'Color': hue_saturation_value})
    
    metallic = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Metallic',
        attrs={'image': bpy.data.images['ceramic_4_metallic-2K.jpg']})
    
    roughness = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Roughness',
        attrs={'image': bpy.data.images['ceramic_4_roughness-2K.jpg']})
    
    normal = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Normal',
        attrs={'image': bpy.data.images['ceramic_4_normal-2K.png']})
    
    separate_rgb = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': normal.outputs["Color"]})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: separate_rgb.outputs["Green"]},
        attrs={'operation': 'SUBTRACT', 'use_clamp': True})
    
    combine_rgb = nw.new_node(Nodes.CombineColor,
        input_kwargs={'Red': separate_rgb.outputs["Red"], 'Green': subtract, 'Blue': separate_rgb.outputs["Blue"]})
    
    normal_map = nw.new_node(Nodes.ShaderNodeNormalMap, input_kwargs={'Color': combine_rgb})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': invert, 'Metallic': metallic.outputs["Color"], 'Specular': group_input_1.outputs["Specular"], 'Roughness': roughness.outputs["Color"], 'Clearcoat': group_input_1.outputs["Clearcoat"], 'Clearcoat Roughness': group_input_1.outputs["Clearcoat Roughness"], 'Normal': normal_map})
    
    displacement = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Displacement',
        attrs={'image': bpy.data.images['ceramic_4_height-2K.jpg']})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Displacement"], 1: group_input_1.outputs["Scale"]},
        attrs={'operation': 'DIVIDE'})
    
    displacement_1 = nw.new_node(Nodes.Displacement, input_kwargs={'Height': displacement.outputs["Color"], 'Scale': divide})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'BSDF': principled_bsdf, 'Displacement': displacement_1, 'tmp_viewer': principled_bsdf},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_penta_selection', singleton=False, type='GeometryNodeTree')
def nodegroup_penta_selection(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketInt', 'nTH selection', 1)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["nTH selection"]})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: reroute, 3: 1}, attrs={'data_type': 'INT'})
    
    ast_index_selection = nw.new_node(nodegroup_a_s_t_index_selection().name, input_kwargs={'%': reroute})
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute, 3: 2}, attrs={'data_type': 'INT'})
    
    greater_than_2 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute, 3: 3}, attrs={'data_type': 'INT'})
    
    greater_than_3 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute, 3: 4}, attrs={'data_type': 'INT'})
    
    switch_3 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than_3, 1: True, 6: ast_index_selection.outputs["4th"], 7: ast_index_selection.outputs["5th"]},
        attrs={'input_type': 'BOOLEAN'})
    
    switch_2 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than_2, 1: True, 6: ast_index_selection.outputs["3rd"], 7: switch_3.outputs[2]},
        attrs={'input_type': 'BOOLEAN'})
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than_1, 1: True, 6: ast_index_selection.outputs["2nd"], 7: switch_2.outputs[2]},
        attrs={'input_type': 'BOOLEAN'})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than, 1: True, 6: ast_index_selection.outputs["1st"], 7: switch_1.outputs[2]},
        attrs={'input_type': 'BOOLEAN'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Selection': switch.outputs[2]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_vecter_circle', singleton=False, type='GeometryNodeTree')
def nodegroup_vecter_circle(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Factor', 0.5000),
            ('NodeSocketFloat', 'Radius', 1.0000),
            ('NodeSocketInt', 'Turns', 1)])
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Turns"], 1: -6.2832}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Factor"], 1: multiply},
        attrs={'operation': 'MULTIPLY'})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1}, attrs={'operation': 'SINE'})
    
    cosine = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1}, attrs={'operation': 'COSINE'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': sine, 'Y': cosine})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_xyz, 'Scale': group_input.outputs["Radius"]},
        attrs={'operation': 'SCALE'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Vector': scale.outputs["Vector"], 'Radius': group_input.outputs["Radius"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_change_spline_type', singleton=False, type='GeometryNodeTree')
def nodegroup_change_spline_type(nw: NodeWrangler):
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

@node_utils.to_nodegroup('nodegroup_curve_merge', singleton=False, type='GeometryNodeTree')
def nodegroup_curve_merge(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketFloatDistance', 'Distance', 0.0010)])
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': group_input.outputs["Curve"]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance,
        input_kwargs={'Geometry': curve_to_mesh, 'Distance': group_input.outputs["Distance"]})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': merge_by_distance})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Curve': mesh_to_curve}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_a_s_t_mono_directional_bezier', singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_mono_directional_bezier(nw: NodeWrangler):
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
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 2: spline_parameter.outputs["Factor"]})
    
    ast_rotate_xyz = nw.new_node(nodegroup_a_s_t_rotate_x_y_z().name,
        input_kwargs={'Geometry': capture_attribute_1.outputs["Geometry"], 'Direction': group_input.outputs["Direction"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Curve': ast_rotate_xyz, 'Length': capture_attribute.outputs[2], 'Factor': capture_attribute_1.outputs[2]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_a_s_t_curve_to_circular_mesh', singleton=False, type='GeometryNodeTree')
def nodegroup_a_s_t_curve_to_circular_mesh(nw: NodeWrangler):
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
    
    ast_abhay_s_round_curve = nw.new_node(nodegroup_a_s_t_abhays_round_curve().name,
        input_kwargs={'Resolution': group_input.outputs["Resolution"], 'Radius': group_input.outputs["Radius"]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': capture_attribute.outputs["Geometry"], 'Profile Curve': ast_abhay_s_round_curve.outputs["Curve"], 'Fill Caps': group_input.outputs["Fill Caps"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Shade Smooth': group_input.outputs["Shade Smooth"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': capture_attribute.outputs[2], 'Y': ast_abhay_s_round_curve.outputs["Length"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': set_shade_smooth, 'Name': group_input.outputs["UVMap"], 3: combine_xyz},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': store_named_attribute})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': merge_by_distance, 'UV': combine_xyz},
        attrs={'is_active_output': True})

def shader_pot_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'cage_uv'})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: attribute_1.outputs["Fac"], 1: 0.0001}, attrs={'operation': 'GREATER_THAN'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': greater_than})
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'pot_uv'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: greater_than, 4: attribute.outputs["Vector"], 5: attribute_1.outputs["Vector"]},
        attrs={'data_type': 'VECTOR'})
    
    group = nw.new_node(nodegroup_if_u_v_not_exists_use_generative_001().name, input_kwargs={'Vecter': mix.outputs[1]})
    
    group_1 = nw.new_node(nodegroup_ceramic4().name,
        input_kwargs={'Vecter': group, 'Hue': 0.8250, 'Saturation': 2.0000, 'Value': 0.0000, 'Clearcoat': 1.0000, 'Clearcoat Roughness': 0.2000, 'Scale': 0.5000})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.8000, 0.7201, 0.0264, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.0000, 'Clearcoat': 1.0000})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': reroute_2, 1: group_1.outputs["BSDF"], 2: principled_bsdf_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_1.outputs["Displacement"]})
    
    mix_1 = nw.new_node(Nodes.Mix, input_kwargs={0: reroute_2, 5: reroute_1}, attrs={'data_type': 'VECTOR'})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': mix_shader, 'Displacement': mix_1.outputs[1]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_uplift_z', singleton=False, type='GeometryNodeTree')
def nodegroup_uplift_z(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Min"]})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: 0.0000, 1: separate_xyz.outputs["Z"]}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': subtract})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute, 'Translation': combine_xyz_3})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform_1}, attrs={'is_active_output': True})

def shader_pot_material_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'cage_uv'})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: attribute_1.outputs["Fac"], 1: 0.0001}, attrs={'operation': 'GREATER_THAN'})
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'pot_uv'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: greater_than, 4: attribute.outputs["Vector"], 5: attribute_1.outputs["Vector"]},
        attrs={'data_type': 'VECTOR'})
    
    group = nw.new_node(nodegroup_if_u_v_not_exists_use_generative_001().name, input_kwargs={'Vecter': mix.outputs[1]})
    
    group_1 = nw.new_node(nodegroup_ceramic4().name,
        input_kwargs={'Vecter': group, 'Hue': 0.8250, 'Saturation': 2.0000, 'Value': 0.0000, 'Clearcoat': 1.0000, 'Clearcoat Roughness': 0.2000, 'Scale': 0.5000, 'Fac': 1.0000})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': greater_than})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_1.outputs["Displacement"]})
    
    mix_1 = nw.new_node(Nodes.Mix, input_kwargs={0: reroute_2, 5: reroute_1}, attrs={'data_type': 'VECTOR'})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': group_1.outputs["tmp_viewer"], 'Displacement': mix_1.outputs[1]},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketIntUnsigned', 'Resolution U', 16),
            ('NodeSocketFloat', 'Height', 1.0000),
            ('NodeSocketInt', 'Resolution V', 128),
            ('NodeSocketFloat', 'Radius', 0.5000),
            ('NodeSocketIntUnsigned', 'Folds', 32),
            ('NodeSocketInt', 'nTH selection', 4),
            ('NodeSocketFloat', 'Fold Amount', 0.8500),
            ('NodeSocketFloat', 'Thickness', 0.0100),
            ('NodeSocketFloat', 'Pot Base Scale', 0.5000),
            ('NodeSocketBool', 'cage mesh', False),
            ('NodeSocketFloatDistance', 'Pattern Size', 0.0750),
            ('NodeSocketFloatDistance', 'Patterin Radius', 0.0100),
            ('NodeSocketInt', 'Pattern Resolution', 6),
            ('NodeSocketMaterial', 'Material', None)]) #surface.shaderfunc_to_material(shader_pot_material)
    
    ast_mono_directional_bezier = nw.new_node(nodegroup_a_s_t_mono_directional_bezier().name,
        input_kwargs={'Resolution': group_input.outputs["Resolution U"], 'Length': group_input.outputs["Height"], 'Direction': 2})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': ast_mono_directional_bezier.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.5000), (0.1000, 0.2375), (0.3818, 0.8438), (0.8409, 0.4500), (0.9136, 0.7438), (0.9591, 0.8125), (1.0000, 1.0000)])
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius,
        input_kwargs={'Curve': ast_mono_directional_bezier.outputs["Curve"], 'Radius': float_curve})
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Folds"], 1: 4.0000}, attrs={'operation': 'MODULO'})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={0: modulo, 1: 3.0000}, attrs={'operation': 'EQUAL'})
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal, 4: group_input.outputs["Folds"], 5: 32},
        attrs={'input_type': 'INT'})
    
    ast_mono_directional_bezier_1 = nw.new_node(nodegroup_a_s_t_mono_directional_bezier().name, input_kwargs={'Resolution': switch_1.outputs[1]})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={0: equal, 4: 1, 5: 2}, attrs={'input_type': 'INT'})
    
    vecter_circle = nw.new_node(nodegroup_vecter_circle().name,
        input_kwargs={'Factor': ast_mono_directional_bezier_1.outputs["Factor"], 'Radius': group_input.outputs["Radius"], 'Turns': switch_2.outputs[1]})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': ast_mono_directional_bezier_1.outputs["Curve"], 'Position': vecter_circle.outputs["Vector"]})
    
    penta_selection = nw.new_node(nodegroup_penta_selection().name, input_kwargs={'nTH selection': group_input.outputs["nTH selection"]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position, 'Scale': group_input.outputs["Fold Amount"]},
        attrs={'operation': 'SCALE'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': penta_selection, 'Position': scale.outputs["Vector"], 'Offset': (0.0000, 0.0000, 0.1000)})
    
    change_spline_type = nw.new_node(nodegroup_change_spline_type().name, input_kwargs={'Curve': set_position_1, 'Select': 2})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': change_spline_type, 2: spline_parameter.outputs["Length"]})
    
    curve_merge = nw.new_node(nodegroup_curve_merge().name, input_kwargs={'Curve': capture_attribute.outputs["Geometry"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_merge, 'Count': group_input.outputs["Resolution V"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': resample_curve})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_curve_radius, 'Profile Curve': reroute})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance,
        input_kwargs={'Geometry': curve_to_mesh, 'Distance': group_input.outputs["Pattern Size"]})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': merge_by_distance})
    
    ast_curve_to_circular_mesh = nw.new_node(nodegroup_a_s_t_curve_to_circular_mesh().name,
        input_kwargs={'Curve': mesh_to_curve, 'Resolution': group_input.outputs["Pattern Resolution"], 'Radius': group_input.outputs["Patterin Radius"], 'UVMap': 'cage_uv'})
    
    flip_faces_1 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': ast_curve_to_circular_mesh.outputs["Mesh"]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["cage mesh"], 15: flip_faces_1})
    
    multiply_add = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: ast_curve_to_circular_mesh.outputs["UV"], 1: (4.0000, 0.2000, 1.0000), 2: (0.5200, 0.5200, 0.5200)},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': switch.outputs[6], 'Name': 'cage_uv', 3: multiply_add.outputs["Vector"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': ast_mono_directional_bezier.outputs["Length"], 'Y': capture_attribute.outputs[2]})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': combine_xyz_1, 'Axis': (0.0000, 1.0000, 0.0000), 'Angle': 3.1416})
    
    vector_rotate_1 = nw.new_node(Nodes.VectorRotate, input_kwargs={'Vector': vector_rotate, 'Angle': -1.5708})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: vector_rotate_1, 1: (1.0000, 1.5000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': curve_to_mesh, 'Name': 'pot_uv', 3: multiply.outputs["Vector"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': store_named_attribute})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': reroute_1})
    
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': reroute})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: 0.0000, 1: group_input.outputs["Thickness"]},
        attrs={'operation': 'SUBTRACT'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': subtract})
    
    transform_geometry_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': fill_curve, 'Translation': combine_xyz})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': transform_geometry_1, 'Scale': group_input.outputs["Pot Base Scale"]})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_1, scale_elements]})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': join_geometry_1, 'Offset Scale': group_input.outputs["Thickness"], 'Individual': False})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Side"]})
    
    flip_faces_2 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': scale_elements})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces, set_shade_smooth, flip_faces_2]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [store_named_attribute_1, join_geometry_2]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': group_input.outputs["Material"]})
    
    uplift_z = nw.new_node(nodegroup_uplift_z().name, input_kwargs={'Geometry': set_material})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': uplift_z}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_pot_material_001, selection=selection)
apply(bpy.context.active_object)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_scatter_proxy_preview(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.1836, 0.2957, 0.0694, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_trunk_proxy_preview(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.8000, 0.3955, 0.2097, 1.0000), 'Roughness': 0.8000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_rotation', singleton=False, type='GeometryNodeTree')
def nodegroup_rotation(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'rotation angle', 0.0000),
            ('NodeSocketFloat', 'randomness', 0.0000),
            ('NodeSocketInt', 'Seed', 0)])
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 3.1416, 1: 180.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["rotation angle"], 1: divide},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["randomness"]})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_40, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_1, 'Y': multiply_1})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_40, 'Y': reroute_40, 'Z': 6.2832})
    
    random_value_3 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: combine_xyz_3, 1: combine_xyz_2, 'Seed': group_input.outputs["Seed"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz_1, 1: random_value_3.outputs["Value"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': add.outputs["Vector"]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_second_rotation', singleton=False, type='GeometryNodeTree')
def nodegroup_second_rotation(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Grow Rotation Angle', 3.1416),
            ('NodeSocketFloat', 'Randomness', 0.0000),
            ('NodeSocketFloatAngle', 'Grow Direction', 0.0000)])
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 3.1416, 1: 180.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Grow Rotation Angle"], 1: divide},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Randomness"]})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_40, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_1, 'Y': multiply_1})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_40, 'Y': reroute_40, 'Z': 6.2832})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: combine_xyz_3, 1: combine_xyz_2},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz_4, 1: random_value_1.outputs["Value"]})
    
    rotate_euler = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': add.outputs["Vector"], 'Axis': (1.0000, 0.0000, 0.0000), 'Angle': group_input.outputs["Grow Direction"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': rotate_euler}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_leaves_rotation', singleton=False, type='GeometryNodeTree')
def nodegroup_leaves_rotation(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Randomness', 0.0000),
            ('NodeSocketFloat', 'Spread Angle', 0.0000),
            ('NodeSocketFloatFactor', 'Aling Vertical', 0.0000),
            ('NodeSocketBool', 'up Flip Direction', False),
            ('NodeSocketFloatFactor', 'Aling Horizontal', 0.0000),
            ('NodeSocketBool', 'back Flip Direction', False)])
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Randomness"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_40, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 3.1416, 1: 180.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Spread Angle"], 1: divide},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_1})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply, 'Y': multiply, 'Z': multiply_2})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_40, 'Y': reroute_40, 'Z': reroute_5})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: combine_xyz_3, 1: combine_xyz_2},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Aling Vertical"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input.outputs["up Flip Direction"], 2: 1.0000, 3: -1.0000},
        attrs={'input_type': 'FLOAT'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': switch.outputs["Output"]})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': random_value_2.outputs["Value"], 'Factor': reroute_3, 'Vector': combine_xyz},
        attrs={'axis': 'Y'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Aling Horizontal"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input.outputs[5], 2: 1.0000, 3: -1.0000},
        attrs={'input_type': 'FLOAT'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': switch_1.outputs["Output"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_1})
    
    align_euler_to_vector_1 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': align_euler_to_vector, 'Factor': reroute_2, 'Vector': reroute_4},
        attrs={'axis': 'Z'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Rotation': align_euler_to_vector_1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_proxy_geometry', singleton=False, type='GeometryNodeTree')
def nodegroup_proxy_geometry(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketGeometry', 'branchGeometry', None),
            ('NodeSocketGeometry', 'twigGeometry', None)])
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 3, 'Radius': 0.0600})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': group_input.outputs["Curve"], 'Profile Curve': curve_circle.outputs["Curve"]})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': curve_to_mesh_1})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': bounding_box.outputs["Bounding Box"], 'Material': surface.shaderfunc_to_material(shader_trunk_proxy_preview)})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [group_input.outputs["twigGeometry"], group_input.outputs[2]]})
    
    convex_hull = nw.new_node(Nodes.ConvexHull, input_kwargs={'Geometry': join_geometry_2})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': convex_hull, 'Material': surface.shaderfunc_to_material(shader_scatter_proxy_preview)})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, set_material_1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_3}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_trunk_resoltion__u_vmap', singleton=False, type='GeometryNodeTree')
def nodegroup_trunk_resoltion__u_vmap(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Resolution', 6)])
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 2: curve_parameter.outputs["Factor"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs["Geometry"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Resolution"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute, 'Radius': 0.0600})
    
    curve_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 2: curve_parameter_1.outputs["Factor"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs["Geometry"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': capture_attribute.outputs[2], 'Y': capture_attribute_1.outputs[2]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'curve': reroute_1, 'profile': reroute_3, 'Vector': combine_xyz},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_w_i_n_d_leaves', singleton=False, type='GeometryNodeTree')
def nodegroup_w_i_n_d_leaves(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 1.0000
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Wind Speed', 15.0000),
            ('NodeSocketFloat', 'Wind Strength', 4.0000),
            ('NodeSocketFloat', 'Wind Offset', 0.0000),
            ('NodeSocketObject', 'Object', None)])# bpy.data.objects['Wind_Multiplier_Example_Object'])])
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: value, 1: group_input.outputs["Wind Speed"]}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: group_input.outputs["Wind Offset"]})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': add, 'Scale': 0.2000, 'Detail': 3.0000, 'Roughness': 0.6833, 'Distortion': 1.0000},
        attrs={'noise_dimensions': '4D'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture_2.outputs["Color"], 1: (3.0000, 2.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply.outputs["Vector"], 1: (1.5000, 1.0000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    position_6 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_6 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_6})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': reroute_34}, attrs={'legacy_behavior': True})
    
    bounding_box_1 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': realize_instances})
    
    separate_xyz_7 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_1.outputs["Max"]})
    
    divide_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_6.outputs["X"], 1: separate_xyz_7.outputs["X"]},
        attrs={'operation': 'DIVIDE'})
    
    separate_xyz_8 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_1.outputs["Min"]})
    
    divide_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_6.outputs["X"], 1: separate_xyz_8.outputs["X"]},
        attrs={'operation': 'DIVIDE'})
    
    multiply_add = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: divide_1.outputs["Vector"], 1: divide_2.outputs["Vector"], 2: (1.0000, 1.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    divide_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_6.outputs["Y"], 1: separate_xyz_7.outputs["Y"]},
        attrs={'operation': 'DIVIDE'})
    
    divide_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_6.outputs["Y"], 1: separate_xyz_8.outputs["Y"]},
        attrs={'operation': 'DIVIDE'})
    
    multiply_add_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: divide_3.outputs["Vector"], 1: divide_4.outputs["Vector"], 2: (1.0000, 1.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_add.outputs["Vector"], 1: multiply_add_1.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    divide_5 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_6.outputs["Z"], 1: separate_xyz_7.outputs["Z"]},
        attrs={'operation': 'DIVIDE'})
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': divide_5.outputs["Vector"]})
    colorramp_6.color_ramp.interpolation = "B_SPLINE"
    colorramp_6.color_ramp.elements[0].position = 0.0000
    colorramp_6.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 1.0000
    colorramp_6.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    multiply_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_1.outputs["Vector"], 1: colorramp_6.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    colorramp_7 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': multiply_2.outputs["Vector"]})
    colorramp_7.color_ramp.interpolation = "B_SPLINE"
    colorramp_7.color_ramp.elements[0].position = 0.0045
    colorramp_7.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_7.color_ramp.elements[1].position = 1.0000
    colorramp_7.color_ramp.elements[1].color = [0.2135, 0.2135, 0.2135, 1.0000]
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wind Strength"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Object"]})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': reroute_2}, attrs={'transform_space': 'RELATIVE'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': object_info.outputs["Location"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz.outputs["Z"], 2: 5.0000, 4: 2.0000})
    
    multiply_add_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_9, 1: map_range.outputs["Result"], 2: reroute_9},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_add_2})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_1, 'Y': reroute_1, 'Z': reroute_1})
    
    multiply_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: colorramp_7.outputs["Color"], 1: combine_xyz},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: multiply_3.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Vector': multiply_4.outputs["Vector"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_w_i_n_d_tree', singleton=False, type='GeometryNodeTree')
def nodegroup_w_i_n_d_tree(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Wind Speed', 15.0000),
            ('NodeSocketFloat', 'Wind Strength', 1.5000),
            ('NodeSocketFloat', 'Wind Offset', 0.0000),
            ('NodeSocketBool', 'Wind On / Off', False),
            ('NodeSocketObject', 'Wind Multiplier Object', None)])# bpy.data.objects['Wind_Multiplier_Example_Object'])])
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wind On / Off"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    position_4 = nw.new_node(Nodes.InputPosition)
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': position_4})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 1.0000
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wind Speed"]})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: value, 1: reroute_7}, attrs={'operation': 'DIVIDE'})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wind Offset"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: reroute_6})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': position_4, 'W': reroute_8, 'Scale': 0.2000, 'Detail': 1.0000, 'Distortion': 1.0000},
        attrs={'noise_dimensions': '4D'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture_1.outputs["Color"], 1: (2.0000, 2.0000, 0.5000)},
        attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply.outputs["Vector"], 1: (1.0000, 1.0000, 0.2500)},
        attrs={'operation': 'SUBTRACT'})
    
    position_5 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_5})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': group_input.outputs["Geometry"]})
    
    separate_xyz_4 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Max"]})
    
    divide_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_3.outputs["X"], 1: separate_xyz_4.outputs["X"]},
        attrs={'operation': 'DIVIDE'})
    
    separate_xyz_5 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Min"]})
    
    divide_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_3.outputs["X"], 1: separate_xyz_5.outputs["X"]},
        attrs={'operation': 'DIVIDE'})
    
    multiply_add = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: divide_1.outputs["Vector"], 1: divide_2.outputs["Vector"], 2: (1.0000, 1.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    divide_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_3.outputs["Y"], 1: separate_xyz_4.outputs["Y"]},
        attrs={'operation': 'DIVIDE'})
    
    divide_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_3.outputs["Y"], 1: separate_xyz_5.outputs["Y"]},
        attrs={'operation': 'DIVIDE'})
    
    multiply_add_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: divide_3.outputs["Vector"], 1: divide_4.outputs["Vector"], 2: (1.0000, 1.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_add.outputs["Vector"], 1: multiply_add_1.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    divide_5 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz_3.outputs["Z"], 1: separate_xyz_4.outputs["Z"]},
        attrs={'operation': 'DIVIDE'})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': divide_5.outputs["Vector"]})
    colorramp_5.color_ramp.interpolation = "B_SPLINE"
    colorramp_5.color_ramp.elements[0].position = 0.2091
    colorramp_5.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 1.0000
    colorramp_5.color_ramp.elements[1].color = [0.9230, 0.9230, 0.9230, 1.0000]
    
    multiply_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_1.outputs["Vector"], 1: colorramp_5.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': multiply_2.outputs["Vector"]})
    colorramp_4.color_ramp.interpolation = "B_SPLINE"
    colorramp_4.color_ramp.elements[0].position = 0.0045
    colorramp_4.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.9409
    colorramp_4.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wind Strength"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    object_info = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': group_input.outputs["Wind Multiplier Object"]},
        attrs={'transform_space': 'RELATIVE'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': object_info.outputs["Location"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz.outputs["Z"], 2: 5.0000, 4: 2.0000})
    
    multiply_add_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_9, 1: map_range.outputs["Result"], 2: reroute_9},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_add_2})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_1, 'Y': reroute_1, 'Z': reroute_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz})
    
    multiply_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: colorramp_4.outputs["Color"], 1: reroute},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: multiply_3.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_4, 1: multiply_4.outputs["Vector"]})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={0: reroute_4, 8: reroute_3, 9: add_1.outputs["Vector"]},
        attrs={'input_type': 'VECTOR'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': switch.outputs[3]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_noise_branches', singleton=False, type='GeometryNodeTree')
def nodegroup_noise_branches(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    position_3 = nw.new_node(Nodes.InputPosition)
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatFactor', 'Fac', 0.5000),
            ('NodeSocketFloat', 'Noise Offset', 2.5000),
            ('NodeSocketFloat', 'Noise Scale', 0.6700),
            ('NodeSocketFloat', 'Noise Detail', 2.0000),
            ('NodeSocketFloat', 'Noise Amount', 0.0000)])
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input.outputs["Noise Offset"], 'Scale': group_input.outputs["Noise Scale"], 'Detail': group_input.outputs["Noise Detail"], 'Roughness': 0.3500},
        attrs={'noise_dimensions': '4D'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (2.0000, 2.0000, 2.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply.outputs["Vector"], 1: (1.0000, 1.0000, 1.0000)},
        attrs={'operation': 'SUBTRACT'})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': group_input.outputs["Fac"]})
    colorramp_3.color_ramp.elements.new(0)
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.1500
    colorramp_3.color_ramp.elements[1].color = [0.4389, 0.4389, 0.4389, 1.0000]
    colorramp_3.color_ramp.elements[2].position = 1.0000
    colorramp_3.color_ramp.elements[2].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: colorramp_3.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Noise Amount"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_40, 'Y': reroute_40, 'Z': 1.0000})
    
    multiply_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_1.outputs["Vector"], 1: combine_xyz_1},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_3, 1: multiply_2.outputs["Vector"]})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add.outputs["Vector"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': reroute_30}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_noise_trunk', singleton=False, type='GeometryNodeTree')
def nodegroup_noise_trunk(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    position_3 = nw.new_node(Nodes.InputPosition)
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatFactor', 'Fac', 0.5000),
            ('NodeSocketFloat', 'Noise Offset', 2.5000),
            ('NodeSocketFloat', 'Noise Scale', 0.6700),
            ('NodeSocketFloat', 'Noise Detail', 2.0000),
            ('NodeSocketFloat', 'Noise Amount', 0.0000)])
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input.outputs["Noise Offset"], 'Scale': group_input.outputs["Noise Scale"], 'Detail': group_input.outputs["Noise Detail"], 'Roughness': 0.3500},
        attrs={'noise_dimensions': '4D'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (2.0000, 2.0000, 2.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply.outputs["Vector"], 1: (1.0000, 1.0000, 1.0000)},
        attrs={'operation': 'SUBTRACT'})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': group_input.outputs["Fac"]})
    colorramp_3.color_ramp.elements.new(0)
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.2364
    colorramp_3.color_ramp.elements[1].color = [0.4389, 0.4389, 0.4389, 1.0000]
    colorramp_3.color_ramp.elements[2].position = 1.0000
    colorramp_3.color_ramp.elements[2].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: colorramp_3.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Noise Amount"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_40, 'Y': reroute_40, 'Z': 1.0000})
    
    multiply_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_1.outputs["Vector"], 1: combine_xyz_1},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_3, 1: multiply_2.outputs["Vector"]})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add.outputs["Vector"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': reroute_30}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_z_01', singleton=False, type='GeometryNodeTree')
def nodegroup_z_01(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketFloat', 'From Max', 1.0000)])
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["From Max"]})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_1.outputs["Z"], 2: reroute_5},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Result': map_range_1.outputs["Result"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_main_radius_by_height', singleton=False, type='GeometryNodeTree')
def nodegroup_main_radius_by_height(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatFactor', 'Fac', 0.5000),
            ('NodeSocketFloat', 'Radius Scale', 1.0000)])
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': group_input.outputs["Fac"]})
    colorramp_1.color_ramp.interpolation = "B_SPLINE"
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.0001
    colorramp_1.color_ramp.elements[1].color = [0.6631, 0.6631, 0.6631, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 0.2500
    colorramp_1.color_ramp.elements[2].color = [0.6482, 0.6482, 0.6482, 1.0000]
    colorramp_1.color_ramp.elements[3].position = 0.7886
    colorramp_1.color_ramp.elements[3].color = [0.3762, 0.3762, 0.3762, 1.0000]
    colorramp_1.color_ramp.elements[4].position = 1.0000
    colorramp_1.color_ramp.elements[4].color = [0.1035, 0.1035, 0.1035, 1.0000]
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_1.outputs["Color"], 1: group_input.outputs["Radius Scale"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': reroute_8}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_main_trunk', singleton=False, type='GeometryNodeTree')
def nodegroup_main_trunk(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Height In', 1.0000),
            ('NodeSocketFloat', 'Radius In', 0.5000),
            ('NodeSocketVector', 'Noise In', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Radius', 1.7500),
            ('NodeSocketInt', 'Resolution', 30)])
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Height In"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': group_input.outputs["Resolution"]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Noise In"]})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': resample_curve, 'Position': reroute_29})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_2})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Radius In"], 1: group_input.outputs["Radius"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_26, 'Radius': multiply})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Height In"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius In"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'geo0': set_curve_radius, 'geo_branches': reroute_26, 'Path': curve_line, 'Height Out': reroute_1, 'Radius Out': reroute_3},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_main_branches', singleton=False, type='GeometryNodeTree')
def nodegroup_main_branches(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketGeometry', 'Path', None),
            ('NodeSocketFloat', 'Height In', 1.0000),
            ('NodeSocketFloat', 'radius in', 0.5000),
            ('NodeSocketVector', 'Noise In', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Radius', 1.0000),
            ('NodeSocketInt', 'Density', 10),
            ('NodeSocketInt', 'Resolution', 10),
            ('NodeSocketFloat', 'Length', 0.4000),
            ('NodeSocketFloat', 'Grow Angle', 45.0000),
            ('NodeSocketFloat', 'Rotation Random', 0.2000),
            ('NodeSocketFloatFactor', 'Grow Height', 0.1850),
            ('NodeSocketVector', 'Extra Shape', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketInt', 'Seed', 0)])
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': reroute_4, 'Count': group_input.outputs["Density"]})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Grow Height"]})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': resample_curve, 2: reroute_21, 5: 5.2000})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': trim_curve})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Resolution"]})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': group_input.outputs["Path"], 'Count': reroute_8})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': resample_curve_1})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Noise In"]})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_3, 'Position': reroute_28})
    
    position_9 = nw.new_node(Nodes.InputPosition)
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Height In"]})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz.outputs["Z"], 2: reroute_35},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    colorramp_9 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range.outputs["Result"]})
    colorramp_9.color_ramp.interpolation = "B_SPLINE"
    colorramp_9.color_ramp.elements[0].position = 0.5000
    colorramp_9.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_9.color_ramp.elements[1].position = 1.0000
    colorramp_9.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Extra Shape"]})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: colorramp_9.outputs["Color"], 1: reroute_20},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_9, 1: multiply.outputs["Vector"]})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_3, 'Position': add.outputs["Vector"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Grow Angle"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rotation Random"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Seed"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    rotation = nw.new_node(nodegroup_rotation().name,
        input_kwargs={'rotation angle': reroute_16, 'randomness': reroute_15, 'Seed': reroute_19})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.8000, 3: 1.2000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range.outputs["Result"]})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.4234, 0.4234, 0.4234, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.3364
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[2].position = 1.0000
    colorramp.color_ramp.elements[2].color = [0.4939, 0.4939, 0.4939, 1.0000]
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Length"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"], 1: reroute_11}, attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: random_value.outputs[1], 1: multiply_1}, attrs={'operation': 'MULTIPLY'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_36, 'Instance': set_position_5, 'Rotation': rotation, 'Scale': multiply_2})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["radius in"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: reroute_2}, attrs={'operation': 'MULTIPLY'})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_3})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_22, 'Radius': reroute_7})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': set_curve_radius_1}, attrs={'legacy_behavior': True})
    
    radius = nw.new_node(Nodes.Radius)
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_3})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: radius, 1: reroute_6}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius_2 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': realize_instances_1, 'Radius': multiply_4})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Height In"]})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["radius in"]})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'geo0': set_curve_radius_2, 'geotwig': reroute_17, 'Path': group_input.outputs["Path"], 'Height Out': reroute_23, 'radius Out': reroute_26},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_main_twigs', singleton=False, type='GeometryNodeTree')
def nodegroup_main_twigs(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketGeometry', 'Path', None),
            ('NodeSocketFloat', 'Height In', 1.0000),
            ('NodeSocketFloat', 'Radius In', 0.5000),
            ('NodeSocketVector', 'Noise In', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Radius', 0.5000),
            ('NodeSocketInt', 'Density', 10),
            ('NodeSocketInt', 'Resolution', 12),
            ('NodeSocketFloat', 'Length', 0.5000),
            ('NodeSocketFloatAngle', 'Grow Angle', 0.0000),
            ('NodeSocketFloat', 'Grow Spread Angle', 25.7000),
            ('NodeSocketFloat', 'Rotation Random', 0.1000),
            ('NodeSocketFloatFactor', 'Grow Distance', 0.3500)])
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Density"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': reroute_9, 'Count': reroute_17})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Grow Distance"]})
    
    trim_curve_1 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': resample_curve, 2: reroute_6})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': trim_curve_1})
    
    resample_curve_3 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': group_input.outputs["Path"], 'Count': group_input.outputs["Resolution"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': resample_curve_3})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Noise In"]})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_10, 'Position': reroute_32})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Grow Spread Angle"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rotation Random"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Grow Angle"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    second_rotation = nw.new_node(nodegroup_second_rotation().name,
        input_kwargs={'Grow Rotation Angle': reroute_8, 'Randomness': reroute_7, 'Grow Direction': reroute_13})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.8000, 3: 1.2000})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_2.outputs["Z"], 2: group_input.outputs["Height In"]},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range_2.outputs["Result"]})
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.1537, 0.1537, 0.1537, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.3364
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[2].position = 1.0000
    colorramp_2.color_ramp.elements[2].color = [0.4939, 0.4939, 0.4939, 1.0000]
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Length"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_2.outputs["Color"], 1: reroute_4},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_1.outputs[1], 1: multiply}, attrs={'operation': 'MULTIPLY'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_37, 'Instance': set_position_4, 'Rotation': second_rotation, 'Scale': multiply_1})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_1})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius In"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: reroute_2}, attrs={'operation': 'MULTIPLY'})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_2})
    
    set_curve_radius_3 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_23, 'Radius': reroute_12})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': set_curve_radius_3}, attrs={'legacy_behavior': True})
    
    radius_1 = nw.new_node(Nodes.Radius)
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_2})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: radius_1, 1: reroute_11}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius_4 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': realize_instances_2, 'Radius': multiply_3})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_curve_radius_4}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_leaves', singleton=False, type='GeometryNodeTree')
def nodegroup_leaves(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Points', None),
            ('NodeSocketVector', 'Wind In', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketInt', 'Density', 10),
            ('NodeSocketFloat', 'Spread Angle', 0.0000),
            ('NodeSocketFloat', 'Rotation Random', 0.2500),
            ('NodeSocketFloatFactor', 'Aling Vertical', 0.0000),
            ('NodeSocketBool', 'back Flip Direction', False),
            ('NodeSocketFloatFactor', 'Aling Horizontal', 0.0000),
            ('NodeSocketBool', 'up Flip Direction', False),
            ('NodeSocketFloat', 'Leaves Scale', 0.5000),
            ('NodeSocketObject', 'Object', None),#bpy.data.objects['leaf_2']),
            ('NodeSocketBool', 'Wind On / Off', False),
            ('NodeSocketBool', 'Selection', True)])
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Points"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Density"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': reroute_16, 'Count': reroute_15})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Object"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': reroute_14})
    
    position = nw.new_node(Nodes.InputPosition)
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': position})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: reroute_17, 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: reroute_17, 1: multiply.outputs["Vector"]},
        attrs={'operation': 'SUBTRACT'})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': subtract.outputs["Vector"]}, attrs={'axis': 'Y'})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wind On / Off"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rotation Random"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Spread Angle"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Aling Vertical"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["up Flip Direction"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Aling Horizontal"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["back Flip Direction"]})
    
    leaves_rotation = nw.new_node(nodegroup_leaves_rotation().name,
        input_kwargs={'Randomness': reroute_10, 'Spread Angle': reroute_19, 'Aling Vertical': reroute_9, "up Flip Direction": reroute_8, 'Aling Horizontal': reroute_7, "back Flip Direction": reroute_6})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': leaves_rotation})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wind In"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: leaves_rotation, 1: reroute_1})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={0: reroute_4, 8: reroute_5, 9: add.outputs["Vector"]},
        attrs={'input_type': 'VECTOR'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: align_euler_to_vector, 1: switch.outputs[3]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Leaves Scale"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_11, 'Y': reroute_11, 'Z': reroute_11})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': resample_curve, 'Selection': group_input.outputs["Selection"], 'Instance': object_info.outputs["Geometry"], 'Rotation': add_1.outputs["Vector"], 'Scale': reroute_12})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Instances': instance_on_points_2}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_proxy_switch', singleton=False, type='GeometryNodeTree')
def nodegroup_proxy_switch(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'False', None),
            ('NodeSocketGeometry', 'True', None),
            ('NodeSocketBool', 'Switch', False)])
    
    is_viewport = nw.new_node(Nodes.IsViewport)
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input.outputs["Switch"], 7: is_viewport},
        attrs={'input_type': 'BOOLEAN'})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: switch_1.outputs[2], 14: group_input.outputs["False"], 15: group_input.outputs["True"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Output': switch.outputs[6]}, attrs={'is_active_output': True})

def shader_trunk_dark_prev(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'UVMap'})
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': attribute.outputs["Vector"], 'Scale': (5.0000, 1.0000, 1.0000)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 15.0000, 'Detail': 4.0000, 'Roughness': 0.6767})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0922, 0.0352, 0.0115, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.1909
    colorramp.color_ramp.elements[1].color = [0.0472, 0.0300, 0.0177, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.4386
    colorramp.color_ramp.elements[2].color = [0.1098, 0.0654, 0.0388, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.4852
    colorramp.color_ramp.elements[3].color = [0.2597, 0.1492, 0.0857, 1.0000]
    colorramp.color_ramp.elements[4].position = 0.6591
    colorramp.color_ramp.elements[4].color = [0.3297, 0.1906, 0.1103, 1.0000]
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.1000, 'Height': noise_texture.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': colorramp.outputs["Color"], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Tree Height', 5.0000),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketFloat', 'Wind Offset', 0.0000),
            ('NodeSocketFloat', 'Radius Scale', 1.0000),
            ('NodeSocketFloat', 'Noise Offset', 2.5000),
            ('NodeSocketBool', 'Proxy Preview in Viewport', False),
            ('NodeSocketObject', 'Wind Multiplier Object',None)])# bpy.data.objects['Wind_Multiplier_Example_Object'])])
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tree Height"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    z_0_1 = nw.new_node(nodegroup_z_01().name, input_kwargs={'From Max': reroute_4})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': z_0_1})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius Scale"]})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    main_radius_by_height = nw.new_node(nodegroup_main_radius_by_height().name, input_kwargs={'Fac': reroute_19, 'Radius Scale': reroute_32})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_radius_by_height})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    noise_trunk = nw.new_node(nodegroup_noise_trunk().name,
        input_kwargs={'Fac': reroute_9, 'Noise Offset': group_input.outputs["Noise Offset"], 'Noise Scale': 0.2500, 'Noise Amount': 0.2500})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': noise_trunk})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    main_trunk = nw.new_node(nodegroup_main_trunk().name,
        input_kwargs={'Height In': reroute_5, 'Radius In': reroute_8, 'Noise In': reroute_7, 'Radius': 2.0000, 'Resolution': 25})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_trunk.outputs['geo_branches']})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_trunk.outputs["Path"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_trunk.outputs["Height Out"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_trunk.outputs["Radius Out"]})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    noise_branches = nw.new_node(nodegroup_noise_branches().name, input_kwargs={'Fac': reroute_18, 'Noise Amount': 1.6000})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': noise_branches})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_40})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Seed"]})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    main_branches = nw.new_node(nodegroup_main_branches().name,
        input_kwargs={'Geometry': reroute_22, 'Path': reroute_17, 'Height In': reroute_16, 'radius in': reroute_15, 'Noise In': reroute_41, 'Density': 30, 'Resolution': 7, 'Grow Angle': 35.8400, 'Grow Height': 0.3022, 'Extra Shape': (0.0000, 0.7300, 0.0000), 'Seed': reroute_3})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branches.outputs['geotwig']})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branches.outputs["Path"]})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branches.outputs["Height Out"]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branches.outputs["radius Out"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_34})
    
    main_twigs = nw.new_node(nodegroup_main_twigs().name,
        input_kwargs={'Geometry': reroute_14, 'Path': reroute_13, 'Height In': reroute_12, 'Radius In': reroute_11, 'Noise In': reroute_35, 'Resolution': 3, 'Length': 0.4100, 'Grow Angle': 0.0297, 'Grow Spread Angle': 27.5600})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_twigs})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_trunk.outputs["geo0"]})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_37})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branches.outputs["geo0"]})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_36, reroute_20, reroute_21]})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wind Offset"]})
    
    wind_tree = nw.new_node(nodegroup_w_i_n_d_tree().name,
        input_kwargs={'Geometry': reroute_33, 'Wind Strength': 1.0000, 'Wind Offset': reroute_23, 'Wind On / Off': True, 'Wind Multiplier Object': group_input.outputs["Wind Multiplier Object"]})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': wind_tree})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_42, 'Position': reroute_45})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_1})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Wind Multiplier Object"]})
    
    wind_leaves = nw.new_node(nodegroup_w_i_n_d_leaves().name,
        input_kwargs={'Geometry': reroute_26, 'Wind Strength': 2.0000, 'Wind Offset': reroute_29, 'Object': reroute_50})
    
    leaves = nw.new_node(nodegroup_leaves().name,
        input_kwargs={'Points': reroute_44, 'Wind In': wind_leaves, 'Density': 12, 'Spread Angle': 145.0000, 'Rotation Random': 1.2700, 6: True, 'Aling Horizontal': 0.8114, 'Leaves Scale': 0.9600, 'Wind On / Off': True})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': leaves})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': join_geometry, 'Position': reroute_45})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position})
    
    trunk_resoltion_uvmap = nw.new_node(nodegroup_trunk_resoltion__u_vmap().name, input_kwargs={'Geometry': reroute_46, 'Resolution': 5})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': trunk_resoltion_uvmap.outputs["curve"], 'Profile Curve': trunk_resoltion_uvmap.outputs["profile"], 'Fill Caps': True})
    
    assign_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_trunk_dark_prev)})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': assign_material})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_38, reroute_43]})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_37})
    
    proxygeometry = nw.new_node(nodegroup_proxy_geometry().name, input_kwargs={'Curve': reroute_49, 1: reroute_20, 2: reroute_21})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': proxygeometry})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_47})
    
    proxyswitch = nw.new_node(nodegroup_proxy_switch().name,
        input_kwargs={'False': join_geometry_1, 'True': reroute_48, 'Switch': group_input.outputs["Proxy Preview in Viewport"]})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': trunk_resoltion_uvmap.outputs["Vector"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': proxyswitch, 'UVMap': reroute_28},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_trunk_dark_prev, selection=selection)
apply(bpy.context.active_object)
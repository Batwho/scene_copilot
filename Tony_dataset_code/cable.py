import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_subdivide_curve', singleton=False, type='GeometryNodeTree')
def nodegroup_subdivide_curve(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketInt', 'Level', 3)])
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': group_input.outputs["Curve"]})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': curve_to_mesh, 'Level': group_input.outputs["Level"]})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': subdivision_surface})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Curve': mesh_to_curve}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Value', 0.5000),
            ('NodeSocketFloat', 'Value1', 0.5000)])
    
    compare = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Value"], 1: -1.0000, 2: 0.0000},
        attrs={'operation': 'COMPARE'})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={0: compare, 5: -1}, attrs={'input_type': 'INT'})
    
    compare_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Value1"], 1: 1.0000, 2: 0.0000},
        attrs={'operation': 'COMPARE'})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={0: compare_1, 5: 1}, attrs={'input_type': 'INT'})
    
    op_and = nw.new_node(Nodes.BooleanMath, input_kwargs={0: switch_1.outputs[1], 1: switch.outputs[1]})
    
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: op_and}, attrs={'operation': 'NOT'})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={0: op_not, 5: 1}, attrs={'input_type': 'INT'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: switch_1.outputs[1], 1: switch_2.outputs[1]})
    
    switch_3 = nw.new_node(Nodes.Switch, input_kwargs={0: op_not, 5: -1}, attrs={'input_type': 'INT'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: switch.outputs[1], 1: switch_3.outputs[1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={"multiply_2": add, "multiply_3": add_1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_curve_to_mesh_(with_u_v)', singleton=False, type='GeometryNodeTree')
def nodegroup_curve_to_mesh_with_u_v(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketGeometry', 'Profile', None)])
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': group_input.outputs["Curve"], 2: curve_parameter.outputs["Factor"]})
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': group_input.outputs["Profile"], 2: curve_parameter.outputs["Factor"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': capture_attribute_1.outputs["Geometry"], 'Profile Curve': capture_attribute.outputs["Geometry"], 'Fill Caps': True})
    
    curve_length = nw.new_node(Nodes.CurveLength, input_kwargs={'Curve': capture_attribute_1.outputs["Geometry"]})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: capture_attribute_1.outputs[2], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: curve_length, 1: divide}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply, 'Y': capture_attribute.outputs[2]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': curve_to_mesh, 'UV Map': combine_xyz_3},
        attrs={'is_active_output': True})

def shader_corner_rings_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Metallic': 1.0000, 'Roughness': 0.2227})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_cables_material_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    cable_color = nw.new_node(Nodes.Attribute, label='Cable Color', attrs={'attribute_name': 'color'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': cable_color.outputs["Color"]})
    colorramp.color_ramp.interpolation = "CONSTANT"
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.2464
    colorramp.color_ramp.elements[1].color = [0.0057, 0.7083, 0.0000, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.5000
    colorramp.color_ramp.elements[2].color = [0.6100, 0.0089, 0.0000, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.7500
    colorramp.color_ramp.elements[3].color = [0.0039, 0.0000, 0.5640, 1.0000]
    colorramp.color_ramp.elements[4].position = 1.0000
    colorramp.color_ramp.elements[4].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    musgrave_texture = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Scale': 340.3000, 'Detail': 1.6600, 'Dimension': 0.0000, 'Lacunarity': 11.4000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.2500, 'Height': musgrave_texture})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Roughness': 0.7605, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_cables_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    cable_color = nw.new_node(Nodes.Attribute, label='Cable Color', attrs={'attribute_name': 'color'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': cable_color.outputs["Color"]})
    colorramp.color_ramp.interpolation = "CONSTANT"
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.2464
    colorramp.color_ramp.elements[1].color = [0.0057, 0.7083, 0.0000, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.5000
    colorramp.color_ramp.elements[2].color = [0.6100, 0.0089, 0.0000, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.7500
    colorramp.color_ramp.elements[3].color = [0.0039, 0.0000, 0.5640, 1.0000]
    colorramp.color_ramp.elements[4].position = 1.0000
    colorramp.color_ramp.elements[4].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    musgrave_texture = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Scale': 340.3000, 'Detail': 1.6600, 'Dimension': 0.0000, 'Lacunarity': 11.4000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.2500, 'Height': musgrave_texture})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Roughness': 0.7605, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_6 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Segment Length', 0.0500),
            ('NodeSocketInt', 'Resolution', 4),
            ('NodeSocketBool', 'Smooth Curve', False),
            ('NodeSocketFloatDistance', 'Cables Radius', 0.0070),
            ('NodeSocketFloat', 'Max Drip', 2.0000),
            ('NodeSocketFloatFactor', 'Drip Randomness', 1.0000),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketFloat', 'Max Random Drip', 1.0000),
            ('NodeSocketFloat', 'Separation', 0.1000),
            ('NodeSocketInt', 'Direction', 0),
            ('NodeSocketInt', 'Count', 4),
            ('NodeSocketFloatDistance', 'Ends Radius', 0.0200),
            ('NodeSocketBool', 'Parallel', False),
            ('NodeSocketInt', 'Sub-Count', 1),
            ('NodeSocketFloatDistance', 'Sub-Radius', 0.0000),
            ('NodeSocketFloat', 'Twist', 0.0000),
            ('NodeSocketCollection', 'Connectors Collection', None),
            ('NodeSocketInt', 'Connectors Amount', 0),
            ('NodeSocketFloat', "Connector's Scale", 0.0200),
            ('NodeSocketInt', 'fake Seed', 0),
            ('NodeSocketBool', 'Corner Rings', False),
            ('NodeSocketFloatDistance', 'Radius', 0.1200),
            ('NodeSocketFloatDistance', 'Height', 0.1000),
            ('NodeSocketMaterial', 'Cable Material', None),#surface.shaderfunc_to_material(shader_cables_material_001)),
            ('NodeSocketMaterial', 'Corner Rings Material', None),#surface.shaderfunc_to_material(shader_corner_rings_001)),
            ('NodeSocketBool', 'Animated', False),
            ('NodeSocketFloat', 'Frequency', 20.0000)])
    
    mesh_to_curve_1 = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': group_input_6.outputs["Geometry"]})
    
    set_spline_type_1 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': mesh_to_curve_1}, attrs={'spline_type': 'BEZIER'})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': 8, 'Radius': group_input_6.outputs["Radius"], 'Depth': group_input_6.outputs["Height"]},
        attrs={'fill_type': 'NONE'})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': transform})
    
    instance_on_points_3 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': set_spline_type_1, 'Instance': set_shade_smooth})
    
    realize_instances_3 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_3}, attrs={'legacy_behavior': True})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': realize_instances_3, 'Material': group_input_6.outputs["Corner Rings Material"]})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_6.outputs["Corner Rings"], 15: set_material})
    
    less_than = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_6.outputs["Count"], 1: 3.0000},
        attrs={'operation': 'LESS_THAN'})
    
    op_or = nw.new_node(Nodes.BooleanMath,
        input_kwargs={0: group_input_6.outputs["Parallel"], 1: less_than},
        attrs={'operation': 'OR'})
    
    mesh_circle = nw.new_node(Nodes.MeshCircle,
        input_kwargs={'Vertices': group_input_6.outputs["Count"], 'Radius': group_input_6.outputs["Ends Radius"]})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_6.outputs["Ends Radius"]})
    
    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': group_input_6.outputs["Count"], 'Offset': combine_xyz_2})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': mesh_line, 'Rotation': (1.5708, 0.0000, 0.7854)})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: op_or, 14: mesh_circle, 15: transform_1})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': group_input_6.outputs["Geometry"]})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': mesh_to_curve}, attrs={'spline_type': 'BEZIER'})
    
    set_spline_resolution = nw.new_node(Nodes.SetSplineResolution, input_kwargs={'Geometry': set_spline_type, 'Resolution': 64})
    
    curve_handle_positions = nw.new_node('GeometryNodeInputCurveHandlePositions')
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={3: group_input_6.outputs["Max Drip"], 'Seed': group_input_6.outputs["Seed"]})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_6.outputs["Drip Randomness"], 6: group_input_6.outputs["Max Drip"], 7: random_value.outputs[1]},
        attrs={'data_type': 'RGBA'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': mix.outputs[2]})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: curve_handle_positions.outputs["Left"], 1: combine_xyz},
        attrs={'operation': 'SUBTRACT'})
    
    set_handle_positions = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_spline_resolution, 'Position': subtract.outputs["Vector"]})
    
    subtract_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: curve_handle_positions.outputs["Right"], 1: combine_xyz},
        attrs={'operation': 'SUBTRACT'})
    
    set_handle_positions_1 = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_handle_positions, 'Position': subtract_1.outputs["Vector"]},
        attrs={'mode': 'RIGHT'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': switch.outputs[6], 'Instance': set_handle_positions_1})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points}, attrs={'legacy_behavior': True})
    
    index_2 = nw.new_node(Nodes.Index)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': realize_instances, 2: index_2},
        attrs={'domain': 'CURVE'})
    
    curve_handle_positions_1 = nw.new_node('GeometryNodeInputCurveHandlePositions')
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 1.0000
    
    pingpong = nw.new_node(Nodes.Math,
        input_kwargs={0: value, 1: group_input_6.outputs["Frequency"]},
        attrs={'operation': 'PINGPONG'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': pingpong, 2: group_input_6.outputs["Frequency"], 3: -5.0000, 4: 5.0000})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_6.outputs["Count"], 1: group_input_6.outputs["Sub-Count"]},
        attrs={'operation': 'MULTIPLY'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"], 1: multiply}, attrs={'operation': 'DIVIDE'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_6.outputs["Separation"], 1: divide},
        attrs={'operation': 'MULTIPLY'})
    
    switch_3 = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input_6.outputs["Animated"], 2: group_input_6.outputs["Separation"], 3: multiply_1},
        attrs={'input_type': 'FLOAT'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_3.outputs["Output"]})
    
    nodegroup = nw.new_node(nodegroup_node_group().name,
        input_kwargs={0: group_input_6.outputs["Direction"], 1: group_input_6.outputs["Direction"]})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: nodegroup.outputs["multiply_2"]}, attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: nodegroup.outputs["multiply_3"]}, attrs={'operation': 'MULTIPLY'})
    
    id = nw.new_node(Nodes.InputID)
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={2: multiply_2, 3: multiply_3, 'Seed': id})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: id, 1: 2.0000})
    
    random_value_4 = nw.new_node(Nodes.RandomValue, input_kwargs={2: multiply_2, 3: multiply_3, 'Seed': add})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={3: group_input_6.outputs["Max Random Drip"], 'Seed': 2})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': random_value_2.outputs[1], 'Y': random_value_4.outputs[1], 'Z': random_value_1.outputs[1]})
    
    subtract_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: curve_handle_positions_1.outputs["Left"], 1: combine_xyz_1},
        attrs={'operation': 'SUBTRACT'})
    
    set_handle_positions_2 = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': capture_attribute.outputs["Geometry"], 'Position': subtract_2.outputs["Vector"]})
    
    subtract_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: curve_handle_positions_1.outputs["Right"], 1: combine_xyz_1},
        attrs={'operation': 'SUBTRACT'})
    
    set_handle_positions_3 = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_handle_positions_2, 'Position': subtract_3.outputs["Vector"]},
        attrs={'mode': 'RIGHT'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_handle_positions_3})
    
    subdivide_curve = nw.new_node(nodegroup_subdivide_curve().name, input_kwargs={'Curve': reroute})
    
    switch_2 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_6.outputs["Smooth Curve"], 14: reroute, 15: subdivide_curve})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': switch_2.outputs[6], 'Length': group_input_6.outputs["Segment Length"]},
        attrs={'mode': 'LENGTH'})
    
    index = nw.new_node(Nodes.Index)
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: group_input_6.outputs["Twist"]}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': resample_curve, 'Tilt': multiply_4})
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': group_input_6.outputs["Sub-Count"], 'Rotations': 1.0000, 'Start Radius': group_input_6.outputs["Sub-Radius"], 'End Radius': group_input_6.outputs["Sub-Radius"], 'Height': 0.0000})
    
    index_1 = nw.new_node(Nodes.Index)
    
    less_than_1 = nw.new_node(Nodes.Math, input_kwargs={0: index_1, 1: 1.0000}, attrs={'operation': 'LESS_THAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': spiral, 'Selection': less_than_1})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_6.outputs["Resolution"], 'Radius': group_input_6.outputs["Cables Radius"]})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': delete_geometry, 'Instance': curve_circle.outputs["Curve"]})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_2}, attrs={'legacy_behavior': True})
    
    curve_to_mesh_with_uv = nw.new_node(nodegroup_curve_to_mesh_with_u_v().name,
        input_kwargs={'Curve': set_curve_tilt, 'Profile': realize_instances_1})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_with_uv.outputs["Mesh"], 'Material': group_input_6.outputs["Cable Material"]})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_handle_positions_3, 'Length': 0.2000},
        attrs={'mode': 'LENGTH'})
    
    random_value_3 = nw.new_node(Nodes.RandomValue, input_kwargs={'Seed': group_input_6.outputs[20]})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_6.outputs["Connectors Amount"], 1: 100.0000})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: 100.0000}, attrs={'operation': 'DIVIDE'})
    
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: divide_1}, attrs={'operation': 'DIVIDE'})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: random_value_3.outputs[1], 1: divide_2},
        attrs={'operation': 'GREATER_THAN'})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': group_input_6.outputs["Connectors Collection"], 'Separate Children': True, 'Reset Children': True})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent}, attrs={'axis': 'Z'})
    
    add_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_6.outputs["Connector's Scale"], 1: group_input_6.outputs["Cables Radius"]})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': resample_curve_1, 'Selection': greater_than, 'Instance': collection_info, 'Pick Instance': True, 'Rotation': align_euler_to_vector, 'Scale': add_2})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1}, attrs={'legacy_behavior': True})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [switch_1.outputs[6], set_material_1, realize_instances_2]})
    
    white_noise_texture = nw.new_node(Nodes.WhiteNoiseTexture, input_kwargs={'Vector': capture_attribute.outputs[2]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry_1, 'UV Map': curve_to_mesh_with_uv.outputs["UV Map"], 'Color': white_noise_texture.outputs["Color"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_cables_material, selection=selection)
apply(bpy.context.active_object)
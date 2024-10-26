import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_shelf_caps', singleton=False, type='GeometryNodeTree')
def nodegroup_shelf_caps(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Points', None),
            ('NodeSocketInt', 'ShelfStacks', 0),
            ('NodeSocketInt', 'ShelfHeight', 0),
            ('NodeSocketMaterial', 'Cap Material', None)]) #surface.shaderfunc_to_material(shader_shelf_caps)
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['StrutFoot']})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': group_input.outputs["Points"], 'Instance': object_info.outputs["Geometry"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cap Material"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    set_material = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': instance_on_points, 'Material': reroute_2})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances, input_kwargs={'Instances': reroute, 'Rotation': (0.0000, 3.1416, 0.0000)})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 0.1000
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: value, 1: group_input.outputs["ShelfHeight"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply, 1: group_input.outputs["ShelfStacks"]},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_1})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': rotate_instances, 'Offset': combine_xyz})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'ShelfTop': set_position, 'ShelfFoot': reroute},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_shelving', singleton=False, type='GeometryNodeTree')
def nodegroup_shelving(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketMaterial', 'ShelfMetal2', None), #surface.shaderfunc_to_material(shader_shelf_metal)
            ('NodeSocketBool', 'ShelfWoodPanel', False),
            ('NodeSocketMaterial', 'ShelfPanelMaterial', None), #surface.shaderfunc_to_material(shader_shelf_wood)
            ('NodeSocketInt', 'MeshSubdivisions', 3)])
    
    index = nw.new_node(Nodes.Index)
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: index}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': equal, 'Offset': (0.0500, 0.0500, 0.0000)})
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={2: index, 3: 1}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': equal_1, 'Offset': (0.0500, -0.0500, 0.0000)})
    
    equal_2 = nw.new_node(Nodes.Compare, input_kwargs={2: index, 3: 2}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_1, 'Selection': equal_2, 'Offset': (-0.0500, 0.0500, 0.0000)})
    
    equal_3 = nw.new_node(Nodes.Compare, input_kwargs={2: index, 3: 3}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_2, 'Selection': equal_3, 'Offset': (-0.0500, -0.0500, 0.0000)})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_3, 'Offset': (0.0000, 0.0000, 0.0500)})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["MeshSubdivisions"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    subdivide_mesh_1 = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': set_position_4, 'Level': reroute_4})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': subdivide_mesh_1})
    
    quadrilateral = nw.new_node('GeometryNodeCurvePrimitiveQuadrilateral', input_kwargs={'Width': 0.0050, 'Height': 0.0050})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': mesh_to_curve, 'Profile Curve': quadrilateral})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfMetal2"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    set_material = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': curve_to_mesh, 'Material': reroute})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_4, 'Offset': (0.0000, 0.0000, 0.0025)})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': set_position_5, 'Offset Scale': 0.0200})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position_5})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [extrude_mesh.outputs["Mesh"], flip_faces]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_2})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': merge_by_distance, 'Material': group_input.outputs["ShelfPanelMaterial"]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["ShelfWoodPanel"], 15: set_material_1})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, switch.outputs[6]]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_strut_pos', singleton=False, type='GeometryNodeTree')
def nodegroup_strut_pos(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'StrutPos', 0)])
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["StrutPos"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Offset': combine_xyz})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_position}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_strut_horizontal', singleton=False, type='GeometryNodeTree')
def nodegroup_strut_horizontal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketMaterial', 'ShelfMetal2', None)]) #surface.shaderfunc_to_material(shader_shelf_metal2)
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': group_input.outputs["Geometry"]},
        attrs={'mode': 'ONLY_FACE'})
    
    split_edges = nw.new_node(Nodes.SplitEdges, input_kwargs={'Mesh': delete_geometry})
    
    index = nw.new_node(Nodes.Index)
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: index, 3: 4}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={2: index, 3: 6}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    op_or = nw.new_node(Nodes.BooleanMath, input_kwargs={0: equal, 1: equal_1}, attrs={'operation': 'OR'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': split_edges, 'Selection': op_or, 'Offset': (0.0000, 0.0500, 0.0000)})
    
    index_1 = nw.new_node(Nodes.Index)
    
    equal_2 = nw.new_node(Nodes.Compare, input_kwargs={2: index_1, 3: 1}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_3 = nw.new_node(Nodes.Compare, input_kwargs={2: index_1}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    op_or_1 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: equal_2, 1: equal_3}, attrs={'operation': 'OR'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': op_or_1, 'Offset': (0.0500, 0.0000, 0.0000)})
    
    index_2 = nw.new_node(Nodes.Index)
    
    equal_4 = nw.new_node(Nodes.Compare, input_kwargs={2: index_2, 3: 5}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_5 = nw.new_node(Nodes.Compare, input_kwargs={2: index_2, 3: 7}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    op_or_2 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: equal_4, 1: equal_5}, attrs={'operation': 'OR'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_1, 'Selection': op_or_2, 'Offset': (0.0000, -0.0500, 0.0000)})
    
    index_3 = nw.new_node(Nodes.Index)
    
    equal_6 = nw.new_node(Nodes.Compare, input_kwargs={2: index_3, 3: 3}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_7 = nw.new_node(Nodes.Compare, input_kwargs={2: index_3, 3: 2}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    op_or_3 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: equal_6, 1: equal_7}, attrs={'operation': 'OR'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_2, 'Selection': op_or_3, 'Offset': (-0.0500, 0.0000, 0.0000)})
    
    index_4 = nw.new_node(Nodes.Index)
    
    equal_8 = nw.new_node(Nodes.Compare, input_kwargs={2: index_4, 3: 4}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_9 = nw.new_node(Nodes.Compare, input_kwargs={2: index_4, 3: 5}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    op_or_4 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: equal_8, 1: equal_9}, attrs={'operation': 'OR'})
    
    set_position_5 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_3, 'Selection': op_or_4, 'Offset': (0.0300, 0.0000, 0.0000)})
    
    index_5 = nw.new_node(Nodes.Index)
    
    equal_10 = nw.new_node(Nodes.Compare, input_kwargs={2: index_5, 3: 6}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_11 = nw.new_node(Nodes.Compare, input_kwargs={2: index_5, 3: 7}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    op_or_5 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: equal_10, 1: equal_11}, attrs={'operation': 'OR'})
    
    set_position_6 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_5, 'Selection': op_or_5, 'Offset': (-0.0300, 0.0000, 0.0000)})
    
    index_6 = nw.new_node(Nodes.Index)
    
    equal_12 = nw.new_node(Nodes.Compare, input_kwargs={2: index_6}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_13 = nw.new_node(Nodes.Compare, input_kwargs={2: index_6, 3: 2}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    op_or_6 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: equal_12, 1: equal_13}, attrs={'operation': 'OR'})
    
    set_position_7 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_6, 'Selection': op_or_6, 'Offset': (0.0000, 0.0300, 0.0000)})
    
    index_7 = nw.new_node(Nodes.Index)
    
    equal_14 = nw.new_node(Nodes.Compare, input_kwargs={2: index_7, 3: 1}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    equal_15 = nw.new_node(Nodes.Compare, input_kwargs={2: index_7, 3: 3}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    op_or_7 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: equal_14, 1: equal_15}, attrs={'operation': 'OR'})
    
    set_position_8 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_7, 'Selection': op_or_7, 'Offset': (0.0000, -0.0300, 0.0000)})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_8, 'Offset': (0.0000, 0.0000, 0.0500)})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': set_position_4})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['SideBars']})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': mesh_to_curve, 'Profile Curve': object_info.outputs["Geometry"], 'Fill Caps': True})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh, 'Shade Smooth': False})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfMetal2"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    set_material = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': set_shade_smooth, 'Material': reroute})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_grid', singleton=False, type='GeometryNodeTree')
def nodegroup_grid(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketInt', 'X', 0),
            ('NodeSocketInt', 'Y', 0)])
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["X"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: 0.2000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Y"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.2000}, attrs={'operation': 'MULTIPLY'})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': multiply, 'Size Y': multiply_1, 'Vertices X': 2, 'Vertices Y': 2})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': grid.outputs["Mesh"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'pVert': mesh_to_points, 'MeshDissolved': grid.outputs["Mesh"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_vert_struts', singleton=False, type='GeometryNodeTree')
def nodegroup_vert_struts(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'StrutCount', 10),
            ('NodeSocketInt', 'StrutPos', 0),
            ('NodeSocketMaterial', 'ShelfMetal2', None), #surface.shaderfunc_to_material(shader_shelf_metal2)
            ('NodeSocketMaterial', 'ShelfMetal', None)]) #surface.shaderfunc_to_material(shader_shelf_metal)
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["StrutCount"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': reroute_7, 'Offset': (0.0000, 0.0000, 0.1000)})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': reroute_13, 'Instance': mesh_line})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_2})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    index = nw.new_node(Nodes.Index)
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: index}, attrs={'data_type': 'INT'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': reroute_20, 'Selection': greater_than})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['StrutClamp']})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': delete_geometry, 'Instance': object_info_1.outputs["Geometry"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_1})
    
    index_1 = nw.new_node(Nodes.Index)
    
    sample_index = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': instance_on_points_1, 2: index_1, 'Index': index_1},
        attrs={'domain': 'INSTANCE', 'data_type': 'INT'})
    
    equal = nw.new_node(Nodes.Compare,
        input_kwargs={2: sample_index.outputs[1], 3: 1},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': reroute_1, 'Selection': equal, 'Rotation': (0.0000, 0.0000, -1.5708)})
    
    equal_1 = nw.new_node(Nodes.Compare,
        input_kwargs={2: sample_index.outputs[1], 3: 2},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    rotate_instances_1 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': rotate_instances, 'Selection': equal_1, 'Rotation': (0.0000, 0.0000, -4.7124)})
    
    equal_2 = nw.new_node(Nodes.Compare,
        input_kwargs={2: sample_index.outputs[1], 3: 3},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    rotate_instances_2 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': rotate_instances_1, 'Selection': equal_2, 'Rotation': (0.0000, 0.0000, -3.1416)})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["StrutPos"]})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_17, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': rotate_instances_2, 'Offset': reroute_2})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfMetal2"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    set_material = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': set_position, 'Material': reroute_5})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['StrutVert']})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_19, 'Instance': object_info.outputs["Geometry"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': realize_instances})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfMetal"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': merge_by_distance, 'Material': reroute_6})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'StrutCount': reroute_9, 'StrutClamp': set_material, 'StrutVert': set_material_1},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_stacker', singleton=False, type='GeometryNodeTree')
def nodegroup_stacker(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'StrutCount', 0),
            ('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'ShelfStacks', 5)])
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["StrutCount"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply})
    
    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': group_input.outputs["ShelfStacks"], 'Offset': combine_xyz})
    
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': group_input.outputs["Geometry"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_line, 'Instance': geometry_to_instance})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Instances': instance_on_points}, attrs={'is_active_output': True})

def shader_shelf_caps(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Object"]})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': mapping, 'Scale': 1000.0000})
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Distance': 0.0005, 'Height': voronoi_texture.outputs["Distance"]},
        attrs={'invert': True})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0291, 0.0291, 0.0291, 1.0000), 'Emission Strength': 0.0000, 'Normal': bump},
        attrs={'distribution': 'MULTI_GGX', 'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_shelf_wood(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: texture_coordinate.outputs["Object"], 1: (0.1000, 1.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': multiply.outputs["Vector"], 'Scale': 20.0000, 'Detail': 5.0000, 'Roughness': 0.8000})
    
    color_ramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    color_ramp.color_ramp.elements[0].position = 0.2974
    color_ramp.color_ramp.elements[0].color = [0.1437, 0.0973, 0.0600, 1.0000]
    color_ramp.color_ramp.elements[1].position = 1.0000
    color_ramp.color_ramp.elements[1].color = [0.3574, 0.2939, 0.2193, 1.0000]
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: texture_coordinate.outputs["Object"], 1: (1.0000, 0.1000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': multiply_1.outputs["Vector"], 'Detail': 5.0000, 'Roughness': 1.0000})
    
    color_ramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    color_ramp_1.color_ramp.elements[0].position = 0.3500
    color_ramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp_1.color_ramp.elements[1].position = 0.7500
    color_ramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.2500, 6: color_ramp.outputs["Color"], 7: color_ramp_1.outputs["Color"]},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    color_ramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix.outputs[2]})
    color_ramp_2.color_ramp.interpolation = "B_SPLINE"
    color_ramp_2.color_ramp.elements[0].position = 0.0000
    color_ramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    color_ramp_2.color_ramp.elements[1].position = 0.2615
    color_ramp_2.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Roughness': color_ramp_2.outputs["Color"], 'Emission Strength': 0.0000},
        attrs={'distribution': 'MULTI_GGX', 'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_shelf_metal2(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Scale': 0.5000, 'Detail': 9.0000, 'Roughness': 0.7830})
    
    color_ramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    color_ramp.color_ramp.interpolation = "B_SPLINE"
    color_ramp.color_ramp.elements[0].position = 0.4923
    color_ramp.color_ramp.elements[0].color = [0.3000, 0.3000, 0.3000, 1.0000]
    color_ramp.color_ramp.elements[1].position = 1.0000
    color_ramp.color_ramp.elements[1].color = [0.5000, 0.5000, 0.5000, 1.0000]
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: texture_coordinate_1.outputs["Object"], 1: (1.0000, 1.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': multiply.outputs["Vector"], 'Scale': 50.0000, 'Detail': 5.0000, 'Roughness': 1.0000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0005, 'Height': noise_texture_1.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.1784, 0.1788, 0.1790, 1.0000), 'Metallic': 1.0000, 'Roughness': color_ramp.outputs["Color"], 'Emission Strength': 0.0000, 'Normal': bump},
        attrs={'distribution': 'MULTI_GGX', 'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_shelf_metal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Scale': 0.5000, 'Detail': 9.0000, 'Roughness': 0.7830})
    
    color_ramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    color_ramp.color_ramp.interpolation = "B_SPLINE"
    color_ramp.color_ramp.elements[0].position = 0.4923
    color_ramp.color_ramp.elements[0].color = [0.3000, 0.3000, 0.3000, 1.0000]
    color_ramp.color_ramp.elements[1].position = 1.0000
    color_ramp.color_ramp.elements[1].color = [0.5000, 0.5000, 0.5000, 1.0000]
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: texture_coordinate_1.outputs["Object"], 1: (1.0000, 1.0000, 0.0250)},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': multiply.outputs["Vector"], 'Scale': 50.0000, 'Detail': 5.0000, 'Roughness': 1.0000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0025, 'Height': noise_texture_1.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Metallic': 1.0000, 'Roughness': color_ramp.outputs["Color"], 'Emission Strength': 0.0000, 'Normal': bump},
        attrs={'distribution': 'MULTI_GGX', 'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'X', 12),
            ('NodeSocketInt', 'Y', 6),
            ('NodeSocketInt', 'ShelfHeight', 5),
            ('NodeSocketInt', 'ShelfPos', 0),
            ('NodeSocketInt', 'ShelfStacks', 3),
            ('NodeSocketInt', 'Shelf Support Divisions', 3),
            ('NodeSocketBool', 'ShelfWoodPanel', False),
            ('NodeSocketMaterial', 'Cap Material', None), #surface.shaderfunc_to_material(shader_shelf_caps)
            ('NodeSocketMaterial', 'ShelfMetal1', None), #surface.shaderfunc_to_material(shader_shelf_metal)
            ('NodeSocketMaterial', 'ShelfMetal2', None), #surface.shaderfunc_to_material(shader_shelf_metal)
            ('NodeSocketMaterial', 'ShelfPanelMaterial', None)]) #surface.shaderfunc_to_material(shader_shelf_wood)
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["X"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Y"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    grid = nw.new_node(nodegroup_grid().name, input_kwargs={'X': reroute_9, 'Y': reroute_10})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfHeight"]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_43})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfPos"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_41})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfMetal2"]})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_48})
    
    reroute_55 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_49})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfMetal1"]})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_53})
    
    vertstruts = nw.new_node(nodegroup_vert_struts().name,
        input_kwargs={'Geometry': grid.outputs["pVert"], 'StrutCount': reroute_14, 'StrutPos': reroute, 'ShelfMetal2': reroute_55, 'ShelfMetal': reroute_54})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': vertstruts.outputs["StrutCount"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': vertstruts.outputs["StrutVert"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    strutpos = nw.new_node(nodegroup_strut_pos().name,
        input_kwargs={'Geometry': grid.outputs["MeshDissolved"], 'StrutPos': reroute})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_49})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_50})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_51})
    
    struthorizontal = nw.new_node(nodegroup_strut_horizontal().name, input_kwargs={'Geometry': strutpos, 'ShelfMetal2': reroute_52})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': struthorizontal})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': vertstruts.outputs["StrutClamp"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfWoodPanel"]})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_40})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_36})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_37})
    
    reroute_56 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfPanelMaterial"]})
    
    reroute_57 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_56})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_57})
    
    reroute_59 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_58})
    
    reroute_60 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shelf Support Divisions"]})
    
    reroute_61 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_60})
    
    reroute_62 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_61})
    
    reroute_63 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_62})
    
    shelving = nw.new_node(nodegroup_shelving().name,
        input_kwargs={'Geometry': strutpos, 'ShelfMetal2': reroute_52, 'ShelfWoodPanel': reroute_38, 'ShelfPanelMaterial': reroute_59, 'MeshSubdivisions': reroute_63})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': shelving})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_4, reroute_24, reroute_6, reroute_25]})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["ShelfStacks"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_44})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    stacker = nw.new_node(nodegroup_stacker().name,
        input_kwargs={'StrutCount': reroute_5, 'Geometry': join_geometry, 'ShelfStacks': reroute_21})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cap Material"]})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_45})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_46})
    
    shelfcaps = nw.new_node(nodegroup_shelf_caps().name,
        input_kwargs={'Points': grid.outputs["pVert"], 'ShelfStacks': reroute_34, 'ShelfHeight': reroute_35, 'Cap Material': reroute_47})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': shelfcaps.outputs["ShelfFoot"]})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': shelfcaps.outputs["ShelfTop"]})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [stacker, reroute_27, reroute_29]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_1}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_shelf_metal, selection=selection)
    surface.add_material(obj, shader_shelf_metal2, selection=selection)
    surface.add_material(obj, shader_shelf_wood, selection=selection)
    surface.add_material(obj, shader_shelf_caps, selection=selection)


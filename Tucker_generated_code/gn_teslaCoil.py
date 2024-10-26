import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_node_group', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    mesh_circle = nw.new_node(Nodes.MeshCircle, input_kwargs={'Vertices': 4, 'Radius': 0.0800})
    
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': mesh_circle})
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Offset Scale', 1.7300)])
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': group_input.outputs["Geometry"]})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Max"]})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': separate_xyz.outputs["Z"]})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': transform_5, 'Offset': combine_xyz_3})
    
    is_shade_smooth = nw.new_node('GeometryNodeInputShadeSmooth')
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': set_position, 4: is_shade_smooth},
        attrs={'data_type': 'BOOLEAN', 'domain': 'FACE'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': capture_attribute.outputs["Geometry"], 'Offset Scale': 0.1300},
        attrs={'mode': 'EDGES'})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Shade Smooth': capture_attribute.outputs[4]})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': set_shade_smooth, 'Offset Scale': group_input.outputs["Offset Scale"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': extrude_mesh_1.outputs["Mesh"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_main_coil', singleton=False, type='GeometryNodeTree')
def nodegroup_main_coil(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatDistance', 'Radius', 5.2000),
            ('NodeSocketFloatDistance', 'thickness', 1.0000),
            ('NodeSocketInt', 'radius resolution', 8),
            ('NodeSocketInt', 'thickness resolution', 8),
            ('NodeSocketInt', 'coil resolution', 8),
            ('NodeSocketFloatDistance', 'coil thickness', 1.0000)])
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["radius resolution"], 'Point 1': (3.7000, 0.0000, 0.0000), 'Radius': group_input.outputs["Radius"]})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["thickness resolution"], 'Radius': group_input.outputs["thickness"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_circle.outputs["Curve"], 'Profile Curve': curve_circle_1.outputs["Curve"], 'Fill Caps': True})
    
    delete_geometry_2 = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': curve_to_mesh},
        attrs={'mode': 'ONLY_FACE', 'domain': 'EDGE'})
    
    index_1 = nw.new_node(Nodes.Index)
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["radius resolution"], 1: group_input.outputs["thickness resolution"]},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: index_1, 3: multiply}, attrs={'data_type': 'INT'})
    
    delete_geometry_3 = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': delete_geometry_2, 'Selection': greater_than},
        attrs={'domain': 'EDGE'})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': delete_geometry_3})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["coil resolution"], 'Radius': group_input.outputs["coil thickness"]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': mesh_to_curve, 'Profile Curve': curve_circle_2.outputs["Curve"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': curve_to_mesh_1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_top', singleton=False, type='GeometryNodeTree')
def nodegroup_top(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Value', 0.5000),
            ('NodeSocketFloatDistance', 'Radius', 0.5500)])
    
    cylinder_1 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Radius': group_input.outputs["Radius"], 'Depth': group_input.outputs["Value"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder_1.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide})
    
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Translation': combine_xyz_4})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': group_input.outputs["Geometry"]})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Max"]})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': separate_xyz.outputs["Z"]})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': transform_5, 'Offset': combine_xyz_3})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_position}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_concentric_rings', singleton=False, type='GeometryNodeTree')
def nodegroup_concentric_rings(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'RIng count', 10),
            ('NodeSocketInt', 'Ring resolution', 32),
            ('NodeSocketFloatDistance', 'Ring Radius', 1.0000),
            ('NodeSocketFloat', 'Ring Spread', 1.2200),
            ('NodeSocketInt', 'Subtract from center', 0),
            ('NodeSocketInt', 'Resolution', 12),
            ('NodeSocketFloatDistance', 'Radius', 0.3950)])
    
    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': group_input.outputs["RIng count"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Ring resolution"], 'Radius': group_input.outputs["Ring Radius"]})
    
    index = nw.new_node(Nodes.Index)
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: index, 1: group_input.outputs["Ring Spread"]},
        attrs={'operation': 'MULTIPLY'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': mesh_line, 'Instance': curve_circle.outputs["Curve"], 'Scale': multiply})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ)
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': instance_on_points, 'Position': combine_xyz})
    
    index_1 = nw.new_node(Nodes.Index)
    
    less_than = nw.new_node(Nodes.Compare,
        input_kwargs={0: index_1, 1: group_input.outputs["Subtract from center"]},
        attrs={'operation': 'LESS_THAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': set_position, 'Selection': less_than},
        attrs={'domain': 'INSTANCE'})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': delete_geometry})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Resolution"], 'Radius': group_input.outputs["Radius"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': realize_instances, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': curve_to_mesh}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_platformplatform', singleton=False, type='GeometryNodeTree')
def nodegroup_platformplatform(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    grid = nw.new_node(Nodes.MeshGrid)
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketBool', 'Selection', True),
            ('NodeSocketGeometry', 'Points', None),
            ('NodeSocketFloat', 'Y', 0.0000),
            ('NodeSocketFloatDistance', 'Depth', 1.0000),
            ('NodeSocketGeometry', 'Target Geometry', None),
            ('NodeSocketFloat', 'Z', 0.0000),
            ('NodeSocketFloat', 'plateSize', 0.0000),
            ('NodeSocketFloat', 'Z_1', 0.0000)])
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Y"], 'Y': group_input.outputs["Y"], 'Z': 1.0000})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': group_input.outputs["Points"], 'Scale': combine_xyz_3})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': 16, 'Radius': group_input.outputs["Depth"], 'Depth': 0.4000})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': transform_2, 'Selection': group_input.outputs["Selection"], 'Instance': transform_1})
    
    translate_instances = nw.new_node(Nodes.TranslateInstances,
        input_kwargs={'Instances': instance_on_points, 'Translation': (0.0000, 0.0000, 2.0000)})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': translate_instances})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': group_input.outputs["Target Geometry"], 2: cylinder.outputs["Bottom"], 'Ray Length': 104.4000})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances, 'Selection': cylinder.outputs["Bottom"], 'Position': raycast.outputs["Hit Position"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Z"]})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_1, 'Selection': cylinder.outputs["Top"], 'Offset': combine_xyz})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_2, 'Material': surface.shaderfunc_to_material(shader_red_coil)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': set_material})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': join_geometry})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box.outputs["Max"], 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute_1, 'Offset': multiply.outputs["Vector"]})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': set_position, 'Offset Scale': 0.0800, 'Individual': False})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_rubber)})
    
    grid_1 = nw.new_node(Nodes.MeshGrid, input_kwargs={'Size X': 0.8700, 'Size Y': 0.0300, 'Vertices X': 2, 'Vertices Y': 2})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid_1.outputs["Mesh"], 'Name': 'uv_map', 3: grid_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    bounding_box_1 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"]})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box_1.outputs["Max"], 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute_2, 'Offset': multiply_1.outputs["Vector"]})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': set_position_3, 'Offset Scale': 0.2200, 'Individual': False})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Rotation': (0.0000, 0.0000, 1.5708)})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': transform, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_2, set_material_3]})
    
    transform_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_2, 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry_2, transform_3]})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_4, join_geometry, join_geometry_3]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_1})
    
    mesh_circle_1 = nw.new_node(Nodes.MeshCircle, input_kwargs={'Radius': 0.4000})
    
    is_shade_smooth = nw.new_node('GeometryNodeInputShadeSmooth')
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': mesh_circle_1, 4: is_shade_smooth},
        attrs={'data_type': 'BOOLEAN', 'domain': 'FACE'})
    
    extrude_mesh_3 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': capture_attribute.outputs["Geometry"], 'Offset Scale': 0.1000},
        attrs={'mode': 'EDGES'})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': extrude_mesh_3.outputs["Mesh"], 'Shade Smooth': capture_attribute.outputs[4]})
    
    extrude_mesh_2 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': set_shade_smooth, 'Offset Scale': 0.1000, 'Individual': False})
    
    index = nw.new_node(Nodes.Index)
    
    integer = nw.new_node(Nodes.Integer)
    integer.integer = 95
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: index, 1: integer})
    
    cube = nw.new_node(Nodes.MeshCube)
    
    store_named_attribute_3 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Rotation': normal, 'Vector': (1.0000, 1.0000, 0.0000)})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': align_euler_to_vector})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz.outputs["X"], 'Y': separate_xyz.outputs["Y"], 'Z': 0.1000})
    
    raycast_1 = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': store_named_attribute_3, 'Ray Direction': combine_xyz_1})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': extrude_mesh_2.outputs["Mesh"], 'Selection': greater_than, 'Position': raycast_1.outputs["Hit Position"]})
    
    index_1 = nw.new_node(Nodes.Index)
    
    integer_1 = nw.new_node(Nodes.Integer)
    integer_1.integer = 64
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={0: index_1, 1: integer_1}, attrs={'operation': 'LESS_THAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': set_position_4, 'Selection': less_than})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': separate_xyz_1.outputs["X"], 'Y': separate_xyz_1.outputs["Y"]})
    
    set_position_6 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': delete_geometry, 'Position': combine_xyz_2})
    
    extrude_mesh_4 = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': set_position_6, 'Offset Scale': 0.3600, 'Individual': False})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["plateSize"], 'Y': group_input.outputs["plateSize"], 'Z': group_input.outputs["Z_1"]})
    
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': extrude_mesh_4.outputs["Mesh"], 'Scale': combine_xyz_5})
    
    bounding_box_2 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute})
    
    multiply_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box_2.outputs["Max"], 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': transform_5, 'Offset': multiply_2.outputs["Vector"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["plateSize"], 'Y': group_input.outputs["plateSize"], 'Z': 1.0000})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_5, 'Scale': combine_xyz_4})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': transform_4, 'Material': surface.shaderfunc_to_material(shader_rubber)})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute, set_material_1]})
    
    bounding_box_3 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': transform_3})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry_4, 'Max': bounding_box_3.outputs["Max"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_box', singleton=False, type='GeometryNodeTree')
def nodegroup_box(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Mesh', None)])
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': group_input.outputs["Mesh"], 'Offset Scale': 0.0000})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': 0.9100})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': scale_elements, 'Selection': extrude_mesh.outputs["Top"]},
        attrs={'mode': 'ONLY_FACE', 'domain': 'FACE'})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': delete_geometry, 'Offset Scale': 0.0100, 'Individual': False})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': group_input.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_speaker)})
    
    subdivide_mesh_1 = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': set_material_1, 'Level': 3})
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': subdivide_mesh_1})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, subdivision_surface_1]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Mesh"]})
    
    cube = nw.new_node(Nodes.MeshCube)
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Scale': (0.2000, 0.2000, 0.2000)})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': reroute, 'Instance': transform})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': instance_on_points, 'Translation': (0.0000, 0.0000, 0.0700), 'Scale': (0.8900, 0.8900, 0.8900)})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': transform_1})
    
    subdivision_surface_2 = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': realize_instances, 'Level': 2, 'Edge Crease': 0.3846})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': subdivision_surface_2, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material_2})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_shade_smooth, set_shade_smooth_1]})
    
    transform_2 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': join_geometry_1, 'Translation': (0.0000, 0.0000, 0.0200), 'Scale': (0.9300, 0.9300, 0.9300)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Mesh': transform_2}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_wheels', singleton=False, type='GeometryNodeTree')
def nodegroup_wheels(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_2 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Taper', 0.3000),
            ('NodeSocketFloatDistance', 'Thicccc', 0.0100),
            ('NodeSocketFloat', 'width', 0.0000),
            ('NodeSocketFloat', 'height', 0.0000),
            ('NodeSocketFloat', 'extrusion', 0.0100),
            ('NodeSocketFloat', 'wheel thickness', 1.0000),
            ('NodeSocketFloat', 'wheel size', 1.0000),
            ('NodeSocketFloat', 'wheel position Y', 0.0000),
            ('NodeSocketFloat', 'Wheel position Z', 0.0000),
            ('NodeSocketFloat', 'Final offsetY', 0.0000),
            ('NodeSocketInt', 'Wheel resolution', 16)])
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_2.outputs["Wheel resolution"], 'Radius': 0.0500})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_2.outputs["Wheel resolution"], 1: 2.0000},
        attrs={'operation': 'DIVIDE'})
    
    float_to_integer = nw.new_node(Nodes.FloatToInt, input_kwargs={'Float': divide})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': float_to_integer, 'Radius': 0.0100})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_circle_1.outputs["Curve"], 'Profile Curve': curve_circle_2.outputs["Curve"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': surface.shaderfunc_to_material(shader_rubber)})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Radius': 0.0500, 'Depth': group_input_2.outputs["extrusion"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': store_named_attribute, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_2.outputs["extrusion"], 1: 4.4300},
        attrs={'operation': 'MULTIPLY'})
    
    cylinder_1 = nw.new_node('GeometryNodeMeshCylinder', input_kwargs={'Radius': 0.0050, 'Depth': multiply})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder_1.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': store_named_attribute_1, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, set_material_1, set_material_3]})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input_2.outputs["wheel size"], 'Y': group_input_2.outputs["wheel size"], 'Z': group_input_2.outputs["wheel thickness"]})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': join_geometry_1, 'Translation': (0.0000, 0.0100, -0.0200), 'Rotation': (0.0000, 1.5708, 0.0000), 'Scale': combine_xyz_5})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'Y': group_input_2.outputs["wheel position Y"], 'Z': group_input_2.outputs["Wheel position Z"]})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_1, 'Translation': combine_xyz_6})
    
    arc = nw.new_node('GeometryNodeCurveArc', input_kwargs={'Resolution': 4, 'Radius': 0.0500, 'Sweep Angle': 4.7124})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': arc.outputs["Curve"], 'Rotation': (1.5708, 0.7854, 3.1416)})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input_2.outputs["width"], 'Z': group_input_2.outputs["height"]})
    
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_4, 'Scale': combine_xyz_1})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': group_input_2.outputs["Thicccc"], 2: 100.0000})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': map_range_1.outputs["Result"]})
    
    transform_6 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': transform_5, 'Profile Curve': transform_6, 'Fill Caps': True})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    greater_than = nw.new_node(Nodes.Compare,
        input_kwargs={3: 6, 4: separate_xyz_1.outputs["Y"]},
        attrs={'mode': 'AVERAGE', 'data_type': 'VECTOR'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    multiply_add = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: separate_xyz.outputs["Z"], 1: (0.0000, 1.0600, 0.0000), 2: (0.0000, 0.0200, 0.0000)},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': group_input_2.outputs["extrusion"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': group_input_2.outputs["Taper"]})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Vector': multiply_add.outputs["Vector"], 8: (0.0000, 1.1300, 1.2600), 9: combine_xyz_2, 10: combine_xyz},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_to_mesh, 'Selection': greater_than, 'Offset': map_range.outputs["Vector"]})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_2, set_material_2]})
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ)
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': join_geometry})
    
    faceforward = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box.outputs["Max"], 1: bounding_box.outputs["Min"]},
        attrs={'operation': 'FACEFORWARD'})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': faceforward.outputs["Vector"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_3.outputs["X"], 'Y': separate_xyz_3.outputs["Y"], 'Z': separate_xyz_2.outputs["Z"]})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': join_geometry, 'Offset': combine_xyz_4})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': group_input_2.outputs["Final offsetY"]})
    
    transform_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_1, 'Translation': combine_xyz_7})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform_3}, attrs={'is_active_output': True})

def shader_red_coil(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.2738, 0.0000, 0.0131, 1.0000), 'Metallic': 1.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_speaker(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0272, 0.0272, 0.0272, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_rubber(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0072, 0.0072, 0.0072, 1.0000), 'Specular Tint': 0.5000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_metal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Metallic': 1.0000, 'Specular Tint': 0.5000, 'Roughness': 0.3667})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    cube = nw.new_node(Nodes.MeshCube)
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute_1, 'Translation': (0.0000, 0.0000, 0.5000)})
    
    group_input_6 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Base height', 1.0000),
            ('NodeSocketFloat', 'Base width', 1.0000),
            ('NodeSocketFloat', 'Wheel Placement', 0.5000),
            ('NodeSocketFloat', 'Wheel Taper', 0.9000),
            ('NodeSocketFloatDistance', 'Wheel Thicccc', 1.4600),
            ('NodeSocketFloat', 'Wheel width', 0.7200),
            ('NodeSocketFloat', 'Wheel height', 1.1200),
            ('NodeSocketFloat', 'Wheel extrusion', 0.0100),
            ('NodeSocketFloat', 'wheel thickness', 1.8400),
            ('NodeSocketFloat', 'wheel size', 0.7800),
            ('NodeSocketFloat', 'wheel position Y', 0.0000),
            ('NodeSocketFloat', 'Wheel position Z', 0.0000),
            ('NodeSocketFloat', 'Wheel Final offsetY', -0.0300),
            ('NodeSocketInt', 'Wheel resolution', 16),
            ('NodeSocketFloat', 'Platform Y', 0.4300),
            ('NodeSocketFloatDistance', 'Platform Depth', 0.0900),
            ('NodeSocketFloat', 'Platform Z', -1.1800),
            ('NodeSocketFloat', 'Platform plateSize', 1.1700),
            ('NodeSocketFloat', 'Platform Z #2', 0.2600),
            ('NodeSocketInt', 'RIng count', 11),
            ('NodeSocketInt', 'Ring resolution', 32),
            ('NodeSocketFloatDistance', 'Ring Radius', 0.0300),
            ('NodeSocketFloat', 'Ring Spread', 1.5300),
            ('NodeSocketInt', 'Ring Subtract from center', 7),
            ('NodeSocketInt', 'Ring gauge Resolution', 32),
            ('NodeSocketFloatDistance', 'Ring gauge Radius', 0.0200),
            ('NodeSocketFloat', 'Coil Radius', 1.266),
            ('NodeSocketFloatDistance', 'Coil thickness', 0.1300),
            ('NodeSocketInt', 'Coil radius resolution', 32),
            ('NodeSocketInt', 'Coil thickness resolution', 16),
            ('NodeSocketInt', 'coil resolution', 3),
            ('NodeSocketFloatDistance', 'coil thickness', 0.0200)])
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_6.outputs["Base width"]})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': reroute_6, 'Y': reroute_6, 'Z': group_input_6.outputs["Base height"]})
    
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform, 'Scale': combine_xyz_3})
    
    transform_6 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_5})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_6})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_6.outputs["Wheel Placement"], 1: 0.9000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply, 'Y': multiply, 'Z': 1.0000})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_5, 'Scale': combine_xyz_1})
    
    index = nw.new_node(Nodes.Index)
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={2: index, 3: 4}, attrs={'data_type': 'INT', 'operation': 'LESS_THAN'})
    
    wheels = nw.new_node(nodegroup_wheels().name,
        input_kwargs={'Taper': group_input_6.outputs["Wheel Taper"], 'Thicccc': group_input_6.outputs["Wheel Thicccc"], 'width': group_input_6.outputs["Wheel width"], 'height': group_input_6.outputs["Wheel height"], 'extrusion': group_input_6.outputs["Wheel extrusion"], 'wheel thickness': group_input_6.outputs["wheel thickness"], 'wheel size': group_input_6.outputs["wheel size"], 'wheel position Y': group_input_6.outputs["wheel position Y"], 'Wheel position Z': group_input_6.outputs["Wheel position Z"], 'Final offsetY': group_input_6.outputs["Wheel Final offsetY"], 'Wheel resolution': group_input_6.outputs["Wheel resolution"]},
        label='Wheels')
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': transform_1, 'Selection': less_than, 'Instance': wheels, 'Rotation': (0.0000, 0.0000, 0.7679)})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: -24.0000, 3: 23.4000})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': random_value.outputs[1]})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz, 1: (0.0000, 0.0000, 13.8416)})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': instance_on_points, 'Rotation': add.outputs["Vector"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': rotate_instances})
    
    box = nw.new_node(nodegroup_box().name, input_kwargs={'Mesh': reroute_5}, label='box')
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': box})
    
    index_1 = nw.new_node(Nodes.Index)
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: index_1, 3: 3}, attrs={'data_type': 'INT'})
    
    platform = nw.new_node(nodegroup_platformplatform().name,
        input_kwargs={'Selection': greater_than, 'Points': store_named_attribute_1, 'Y': group_input_6.outputs["Platform Y"], 'Depth': group_input_6.outputs["Platform Depth"], 'Target Geometry': box, 'Z': group_input_6.outputs["Platform Z"], 'plateSize': group_input_6.outputs["Platform plateSize"], 'Z_1': group_input_6.outputs["Platform Z #2"]},
        label='platform')
    
    concentric_rings = nw.new_node(nodegroup_concentric_rings().name,
        input_kwargs={'RIng count': group_input_6.outputs["RIng count"], 'Ring resolution': group_input_6.outputs["Ring resolution"], 'Ring Radius': group_input_6.outputs["Ring Radius"], 'Ring Spread': group_input_6.outputs["Ring Spread"], 'Subtract from center': group_input_6.outputs["Ring Subtract from center"], 'Resolution': group_input_6.outputs["Ring gauge Resolution"], 'Radius': group_input_6.outputs["Ring gauge Radius"]},
        label='concentric rings')
    
    bounding_box_2 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': platform.outputs["Geometry"]})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box_2.outputs["Max"], 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': concentric_rings, 'Offset': multiply_1.outputs["Vector"]})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_5, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    value_1 = nw.new_node(Nodes.Value)
    value_1.outputs[0].default_value = 0.2200
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 2.0200
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder', input_kwargs={'Radius': value_1, 'Depth': value})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: value, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Translation': combine_xyz_2})
    
    multiply_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: platform.outputs["Max"], 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_6 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': transform_4, 'Offset': multiply_2.outputs["Vector"]})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_6, 'Material': surface.shaderfunc_to_material(shader_red_coil)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [platform.outputs["Geometry"], set_material_3, set_material_4]})
    
    top = nw.new_node(nodegroup_top().name, input_kwargs={'Geometry': join_geometry_1, 'Value': -0.0600, 'Radius': 0.2700})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': top, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry_1, set_material_2]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [realize_instances, reroute, join_geometry_2]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_6.outputs["Coil Radius"]})
    
    coil = nw.new_node(nodegroup_main_coil().name,
        input_kwargs={'Radius': reroute_4, 'thickness': group_input_6.outputs["Coil thickness"], 'radius resolution': group_input_6.outputs["Coil radius resolution"], 'thickness resolution': group_input_6.outputs["Coil thickness resolution"], 'coil resolution': group_input_6.outputs["coil resolution"], 'coil thickness': group_input_6.outputs["coil thickness"]},
        label='coil')
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': coil, 'Translation': (0.0000, 0.0000, 3.9400)})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_2})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_1, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    nodegroup = nw.new_node(nodegroup_node_group().name, input_kwargs={'Geometry': join_geometry_1, 'Offset Scale': reroute_4})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': nodegroup})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_1, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_2, set_material_1, reroute_3]})
    
    bounding_box_1 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': join_geometry_3})
    
    faceforward = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box_1.outputs["Min"], 1: bounding_box_1.outputs["Max"]},
        attrs={'operation': 'FACEFORWARD'})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': faceforward.outputs["Vector"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': separate_xyz_1.outputs["Z"]})
    
    transform_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_3, 'Translation': combine_xyz_4})
    
    group_output_1 = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform_3}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_metal, selection=selection)
    surface.add_material(obj, shader_rubber, selection=selection)
    surface.add_material(obj, shader_speaker, selection=selection)
    surface.add_material(obj, shader_red_coil, selection=selection)


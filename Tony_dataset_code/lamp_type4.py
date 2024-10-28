import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_light(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Emission': (0.9636, 1.0000, 0.2728, 1.0000), 'Emission Strength': 96.2000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_chrom(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Metallic': 1.0000, 'Roughness': 0.0436})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Base', 0.0000),
            ('NodeSocketFloat', 'Dep', 0.0000),
            ('NodeSocketFloat', 'Lengh', 0.0000),
            ('NodeSocketFloat', 'Radious', 0.0000),
            ('NodeSocketFloat', 'Light radious', 0.0000),
            ('NodeSocketFloat', 'Sides len', 0.5000),
            ('NodeSocketFloatFactor', 'Start', 0.8547),
            ('NodeSocketFloatFactor', 'End', 0.0833),
            ('NodeSocketFloat', 'Position Y', 0.0000),
            ('NodeSocketFloat', 'position Z', 0.0000),
            ('NodeSocketFloat', 'Bend Position Y', 0.0000),
            ('NodeSocketFloat', 'Bend Position Z', 0.0000),
            ('NodeSocketFloat', 'thk', 0.0000),
            ('NodeSocketFloat', 'Light Rotarion ', 0.5000),
            ('NodeSocketFloatAngle', 'Cover rotation ', 2.7276),
            ('NodeSocketFloat', 'Light trim ', 0.1900),
            ('NodeSocketFloat', 'Light position ', -0.1000),
            ('NodeSocketFloat', 'Z', 1.6800)])
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Base"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_9, 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Dep"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply, 'Y': reroute, 'Z': group_input.outputs["Z"]})
    
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': divide})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Translation': combine_xyz_1})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_1})
    
    set_material_5 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_2, 'Material': surface.shaderfunc_to_material(shader_chrom)})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_9})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_xyz_2, 1: (-1.0000, -1.0000, -1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_2, 'End': multiply_1.outputs["Vector"]})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_line, 'Translation': combine_xyz_3})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': transform_2, 'Count': 4})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection)
    
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: endpoint_selection}, attrs={'operation': 'NOT'})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'Y': group_input.outputs["Position Y"], 'Z': group_input.outputs["position Z"]})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_8})
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_2, 'Count': 3})
    
    endpoint_selection_2 = nw.new_node(Nodes.EndpointSelection)
    
    op_not_1 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: endpoint_selection_2}, attrs={'operation': 'NOT'})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'Y': group_input.outputs["Bend Position Y"], 'Z': group_input.outputs["Bend Position Z"]})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': resample_curve_2, 'Selection': op_not_1, 'Offset': combine_xyz_9})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': set_position}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type, 'Selection': op_not_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_handle_type})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': resample_curve, 'Selection': op_not, 'Instance': reroute_1})
    
    transform_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': instance_on_points})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radious"]})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_11, 1: 0.0900}, attrs={'operation': 'MULTIPLY'})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': multiply_2})
    
    curve_to_mesh_3 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': transform_3, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_3, 'Material': surface.shaderfunc_to_material(shader_chrom)})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': transform_2, 'Count': 3})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': resample_curve_1, 'Selection': op_not, 'Instance': reroute_1})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Lengh"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_10})
    
    multiply_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_xyz_4, 1: (-1.0000, -1.0000, -1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_4, 'End': multiply_3.outputs["Vector"]})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': instance_on_points_1, 'Selection': endpoint_selection_1, 'Instance': curve_line_1})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': instance_on_points_2})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_11, 1: 0.8000}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': transform_4, 'Radius': multiply_4})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Light radious"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': reroute_12})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_circle.outputs["Curve"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_1.outputs["Y"], 1: group_input.outputs["Light trim "]})
    
    delete_geometry_1 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': reroute_7, 'Selection': greater_than})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': delete_geometry_1, 'Fill Caps': True})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh_1})
    
    set_material_6 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_8, 'Material': surface.shaderfunc_to_material(shader_light)})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': instance_on_points_2, 'Radius': reroute_11})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["thk"]})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_13, 1: 3.7600}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: multiply_5})
    
    set_curve_radius_3 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_curve_radius, 'Radius': add})
    
    arc = nw.new_node('GeometryNodeCurveArc',
        input_kwargs={'Radius': reroute_12, 'Start Angle': group_input.outputs["Cover rotation "], 'Sweep Angle': 3.9479})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_3, 'Profile Curve': arc.outputs["Curve"], 'Fill Caps': True})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_13, 1: -1.0300}, attrs={'operation': 'MULTIPLY'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': curve_to_mesh, 'Offset Scale': multiply_6, 'Individual': False})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': extrude_mesh.outputs["Mesh"]})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces, curve_to_mesh]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_2})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': merge_by_distance, 'Material': surface.shaderfunc_to_material(shader_chrom)})
    
    multiply_7 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Sides len"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_rgb = nw.new_node('FunctionNodeCombineColor', input_kwargs={'Red': multiply_7})
    
    curve_line_3 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_rgb})
    
    endpoint_selection_3 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    instance_on_points_3 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': transform_4, 'Instance': curve_line_3, 'Pick Instance': endpoint_selection_3})
    
    resample_curve_3 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': instance_on_points_3, 'Count': 20})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 1.0000), (0.5848, 1.0000), (0.6731, 0.8300), (0.7848, 1.0000), (1.0000, 1.0000)])
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_11, 1: float_curve}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius_2 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve_3, 'Radius': multiply_8})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_2, 'Profile Curve': reroute_5, 'Fill Caps': True})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh_2})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_4, 'Material': surface.shaderfunc_to_material(shader_chrom)})
    
    scale_instances = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': reroute_4, 'Scale': (-1.0000, 1.0000, 1.0000)})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': scale_instances, 'Material': surface.shaderfunc_to_material(shader_chrom)})
    
    instance_on_points_4 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': resample_curve, 'Selection': op_not, 'Instance': set_handle_type})
    
    resample_curve_4 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': instance_on_points_4, 'Count': 30})
    
    set_spline_type_1 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': resample_curve_4})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': set_spline_type_1, 3: group_input.outputs["End"]})
    
    trim_curve_1 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': set_spline_type_1, 2: group_input.outputs["Start"]})
    
    resample_curve_5 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': trim_curve_1, 'Count': 53})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    multiply_9 = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_parameter_1.outputs["Factor"], 1: 27.6800},
        attrs={'operation': 'MULTIPLY'})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: multiply_9}, attrs={'operation': 'SINE'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': sine, 1: -0.4700, 2: 0.2600, 3: 0.3600, 4: 0.4600})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"]})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_11, 1: 0.2600})
    
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: add_2}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius_4 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve_5, 'Radius': multiply_10})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [trim_curve, set_curve_radius_4]})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': 0.0800})
    
    curve_to_mesh_4 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': join_geometry_1, 'Profile Curve': curve_circle_2.outputs["Curve"], 'Fill Caps': True})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh_4})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_3, 'Material': surface.shaderfunc_to_material(shader_chrom)})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Area'], 'As Instance': True})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Light position "]})
    
    radians = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Light Rotarion "]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians})
    
    multiply_11 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_10, 1: 1.9700}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_11, 'Y': 0.1300, 'Z': 1.0000})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': object_info.outputs["Geometry"], 'Translation': combine_xyz_5, 'Rotation': combine_xyz_7, 'Scale': combine_xyz_6})
    
    instance_on_points_5 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': instance_on_points_1, 'Selection': endpoint_selection_1, 'Instance': transform})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [set_material_5, set_material_4, set_material_6, set_material_2, set_material_1, set_material, set_material_3, instance_on_points_5]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_chrom, selection=selection)
    surface.add_material(obj, shader_light, selection=selection)
apply(bpy.context.active_object)
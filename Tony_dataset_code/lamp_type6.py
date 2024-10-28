import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_l_g_h_t(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    fresnel = nw.new_node(Nodes.Fresnel)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': fresnel})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [1.0000, 0.8620, 0.5174, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.0818
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"], 1: 20.0000}, attrs={'operation': 'MULTIPLY'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Emission': multiply, 'Emission Strength': 123.9000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_b_l(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0000, 0.0000, 0.0000, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Hight', 0.0000),
            ('NodeSocketFloat', 'L_Hight', 0.0000),
            ('NodeSocketFloatDistance', 'B_Radious', 0.4100),
            ('NodeSocketFloat', 'B_Hight', 0.0000),
            ('NodeSocketFloat', 'P_Radious', 0.0000),
            ('NodeSocketInt', 'L_Count', 3),
            ('NodeSocketFloat', 'L_RotationR', 6.9500),
            ('NodeSocketFloat', 'L_Rotation', 3.2700),
            ('NodeSocketFloat', 'L_Locar-rotation', 0.0000),
            ('NodeSocketFloat', 'L_Radious', 0.0000),
            ('NodeSocketInt', 'L_Selection', 0),
            ('NodeSocketBool', 'Eevee', False)])
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["B_Hight"]})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Radius': group_input_1.outputs["B_Radious"], 'Depth': reroute_1})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Translation': combine_xyz_7})
    
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': transform_1})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': geometry_to_instance, 'Material': surface.shaderfunc_to_material(shader_b_l)})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Hight"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_3})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': 0.2600})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz, 1: combine_xyz_3})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': add.outputs["Vector"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["P_Radious"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: 1.2900}, attrs={'operation': 'MULTIPLY'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': multiply})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': surface.shaderfunc_to_material(shader_b_l)})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["L_Hight"]})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_3, 1: reroute_4}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': subtract})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_5, 'End': combine_xyz})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_2, 'Count': group_input_1.outputs["L_Count"]})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine,
        input_kwargs={'End': (0.0000, 4.0000, 0.0000), 'Direction': (1.0000, 0.0000, 0.0000), 'Length': 0.3000},
        attrs={'mode': 'DIRECTION'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': resample_curve, 'Instance': curve_line_1})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["L_Radious"]})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: 0.2600}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_1})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: 0.9100}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_2})
    
    curve_line_3 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_9, 'End': combine_xyz_1})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_3})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: 1.8600}, attrs={'operation': 'MULTIPLY'})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.2500), (0.4294, 1.0000), (0.8397, 0.4500), (1.0000, 0.4500)])
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: float_curve})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve_1, 'Radius': add_1})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': 0.0500})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': curve_circle_2.outputs["Curve"], 'Fill Caps': True})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_l_g_h_t)})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Eevee"]})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': set_material_4, 'Selection': reroute_6},
        attrs={'domain': 'FACE'})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Radius': reroute_2})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    less_than = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_1.outputs["Z"], 1: -0.0200},
        attrs={'operation': 'LESS_THAN'})
    
    delete_geometry_1 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': store_named_attribute_1, 'Selection': less_than})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': delete_geometry_1})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': delete_geometry_1, 'Offset Scale': -0.0100, 'Individual': False})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces, extrude_mesh.outputs["Mesh"]]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_4})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': merge_by_distance, 'Material': surface.shaderfunc_to_material(shader_b_l)})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material_3})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Point'], 'As Instance': True})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': object_info.outputs["Geometry"], 'Translation': (0.0000, 0.0000, 0.1000)})
    
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: reroute_6}, attrs={'operation': 'NOT'})
    
    delete_geometry_2 = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': transform_3, 'Selection': op_not},
        attrs={'domain': 'INSTANCE'})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [delete_geometry, set_shade_smooth, delete_geometry_2]})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: -0.0200})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_2, 'Z': -0.0800})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_3, 'Translation': combine_xyz_4})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': instance_on_points, 'Selection': endpoint_selection_1, 'Instance': transform})
    
    index_1 = nw.new_node(Nodes.Index)
    
    modulo = nw.new_node(Nodes.Math,
        input_kwargs={0: index_1, 1: group_input_1.outputs["L_Selection"]},
        attrs={'operation': 'MODULO'})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input_1.outputs["L_Locar-rotation"]})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    rotate_instances_1 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': instance_on_points_1, 'Selection': modulo, 'Rotation': combine_xyz_6, 'Pivot Point': position_2, 'Local Space': False})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': reroute_5})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': reroute, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_2, 'Material': surface.shaderfunc_to_material(shader_b_l)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [rotate_instances_1, set_material_2]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["Z"], 1: group_input_1.outputs["L_RotationR"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_4, 1: group_input_1.outputs["L_Rotation"]})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_3})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': join_geometry_1, 'Rotation': combine_xyz_2, 'Local Space': False})
    
    join_geometry_2 = nw.new_node(Nodes.QJoinGeometry, input_kwargs={'Geometry': [set_material_1, rotate_instances]})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_1})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_2, 'Translation': combine_xyz_8})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, transform_2]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_b_l, selection=selection)
    surface.add_material(obj, shader_l_g_h_t, selection=selection)
apply(bpy.context.active_object)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_d_r(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0032, 0.0032, 0.0032, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_l_i_g_h_t(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Emission': (1.0000, 1.0000, 1.0000, 1.0000), 'Emission Strength': 19.7000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Lamp_Length', 0.0000),
            ('NodeSocketFloat', 'Hight', -0.0500),
            ('NodeSocketFloat', 'Base_z', 0.2000),
            ('NodeSocketFloat', 'Base_len', 4.0000),
            ('NodeSocketFloat', 'Base_TH', 0.0000),
            ('NodeSocketFloat', 'Hase_hight', 1.0000)])
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Hight"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_5})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': reroute_7})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: 145.2500}, attrs={'operation': 'DIVIDE'})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': divide})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    object_info = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Lamp_14_Ref']},
        attrs={'transform_space': 'RELATIVE'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: reroute_7, 1: object_info.outputs["Location"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: (-1.0000, -1.0000, -1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Lamp_Length"]})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine,
        input_kwargs={'Start': reroute_7, 'End': (0.0000, 0.0000, 0.1700), 'Direction': multiply.outputs["Vector"], 'Length': reroute_4},
        attrs={'mode': 'DIRECTION'})
    
    value_5 = nw.new_node(Nodes.Value)
    value_5.outputs[0].default_value = 3.1500
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: value_5, 1: 100.0000}, attrs={'operation': 'DIVIDE'})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': divide_1})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line_1, 'Profile Curve': curve_circle_2.outputs["Curve"]})
    
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: -0.2600, 1: 100.0000}, attrs={'operation': 'DIVIDE'})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': curve_to_mesh_1, 'Offset Scale': divide_2, 'Individual': False})
    
    flip_faces_2 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': extrude_mesh_1.outputs["Mesh"]})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_to_mesh_1, flip_faces_2]})
    
    merge_by_distance_1 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_3})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': merge_by_distance_1, 'Selection': extrude_mesh_1.outputs["Side"], 'Shade Smooth': False})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_4, 1: 0.0900}, attrs={'operation': 'MULTIPLY'})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine,
        input_kwargs={'Start': reroute_7, 'End': (0.0000, 0.0000, 0.1700), 'Direction': multiply.outputs["Vector"], 'Length': multiply_1},
        attrs={'mode': 'DIRECTION'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: value_5, 1: 1.0900}, attrs={'operation': 'MULTIPLY'})
    
    divide_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: 100.0000}, attrs={'operation': 'DIVIDE'})
    
    curve_circle_3 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': divide_3})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line_2, 'Profile Curve': curve_circle_3.outputs["Curve"], 'Fill Caps': True})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_to_mesh, set_shade_smooth, curve_to_mesh_2]})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': surface.shaderfunc_to_material(shader_d_r)})
    
    divide_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Hase_hight"], 1: 31.1700},
        attrs={'operation': 'DIVIDE'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: divide_4, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_3})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_material_1, 'Translation': combine_xyz_3})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Base_z"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': reroute_1})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Base_len"]})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    divide_5 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_4, 1: 100.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': divide_5})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Base_TH"]})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: reroute}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_6, 'Y': multiply_5, 'Z': 1.0000})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': transform, 'Translation': combine_xyz_1, 'Scale': combine_xyz_2})
    
    divide_6 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: 200.0000}, attrs={'operation': 'DIVIDE'})
    
    fillet_curve = nw.new_node(Nodes.FilletCurve,
        input_kwargs={'Curve': transform_1, 'Count': 6, 'Radius': divide_6},
        attrs={'mode': 'POLY'})
    
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': fillet_curve}, attrs={'mode': 'NGONS'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': fill_curve, 'Offset Scale': multiply_3})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': extrude_mesh.outputs["Mesh"]})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [fill_curve, flip_faces]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_2})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_3})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_10})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_line_2, 'Translation': combine_xyz_5})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_4})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': endpoint_selection})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Spot'], 'As Instance': True})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': object_info_1.outputs["Geometry"], 'Translation': (0.0000, 0.0000, -0.0500)})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': subtract.outputs["Vector"]}, attrs={'axis': 'Z'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_2, 'Selection': reroute_3, 'Instance': transform_3, 'Rotation': align_euler_to_vector})
    
    multiply_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Lamp_Length"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_6})
    
    multiply_7 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_xyz_6, 1: (1.0000, 1.0000, 0.7800)},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: multiply_7.outputs["Vector"], 1: (0.0000, 0.0000, 0.0800)})
    
    translate_instances = nw.new_node(Nodes.TranslateInstances,
        input_kwargs={'Instances': instance_on_points, 'Translation': add.outputs["Vector"]})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Radius': 0.0200})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_2, 'Selection': reroute_3, 'Instance': store_named_attribute, 'Rotation': align_euler_to_vector})
    
    translate_instances_1 = nw.new_node(Nodes.TranslateInstances,
        input_kwargs={'Instances': instance_on_points_1, 'Translation': multiply_7.outputs["Vector"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': translate_instances_1, 'Material': surface.shaderfunc_to_material(shader_l_i_g_h_t)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [transform_2, merge_by_distance, translate_instances, set_material]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_1}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_l_i_g_h_t, selection=selection)
    surface.add_material(obj, shader_d_r, selection=selection)
apply(bpy.context.active_object)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_g_o_l_d(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.8000, 0.6837, 0.5713, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.1909})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_m_a_t_002(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0000, 0.0000, 0.0000, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_m_at_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    fresnel = nw.new_node(Nodes.Fresnel)
    
    emission = nw.new_node(Nodes.Emission, input_kwargs={'Color': (1.0000, 0.9982, 0.8921, 1.0000), 'Strength': 139.3000})
    
    glass_bsdf = nw.new_node(Nodes.GlassBSDF)
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': fresnel, 1: emission, 2: glass_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_5 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketBool', 'Inputbool', False),
            ('NodeSocketBool', 'Selection', True),
            ('NodeSocketInt', 'Seed1', 1),
            ('NodeSocketFloat', 'Max1', 0.5000),
            ('NodeSocketFloatDistance', 'Radius', 1.3700),
            ('NodeSocketFloat', 'Max2', 8.5800),
            ('NodeSocketInt', 'Count', 34),
            ('NodeSocketFloat', 'Input', 0.0000),
            ('NodeSocketInt', 'Seed2', 5)])
    
    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': group_input_5.outputs["Count"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 18, 'Radius': group_input_5.outputs["Radius"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_5.outputs["Radius"], 1: 5.7400},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: group_input_5.outputs[6]})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={3: add})
    
    sample_curve = nw.new_node(Nodes.SampleCurve,
        input_kwargs={'Curves': curve_circle.outputs["Curve"], 'Length': random_value.outputs[1]},
        attrs={'mode': 'LENGTH', 'use_all_curves': True})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_line, 'Position': sample_curve.outputs["Position"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_5.outputs[9]})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={2: -0.5000, 3: 0.5000, 'Seed': reroute_10})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_5.outputs[8]})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_1.outputs[1], 1: reroute_9}, attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_10, 1: 1.0000})
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={2: -0.5000, 3: 0.5000, 'Seed': add_1})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_2.outputs[1], 1: reroute_9}, attrs={'operation': 'MULTIPLY'})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_5.outputs["Max1"]})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_8, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    random_value_3 = nw.new_node(Nodes.RandomValue, input_kwargs={2: multiply_3, 3: reroute_8, 'Seed': group_input_5.outputs["Seed1"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_1, 'Y': multiply_2, 'Z': random_value_3.outputs[1]})
    
    scale = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz, 'Scale': 1.3700}, attrs={'operation': 'SCALE'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position, 'Offset': scale.outputs["Vector"]})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine)
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': set_position_1, 'Instance': curve_line_1})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['roof'], 'Separate Children': True},
        attrs={'transform_space': 'RELATIVE'})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': collection_info})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': realize_instances_1, 'Ray Direction': (0.0000, 0.0000, 1.0000)})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances, 'Selection': endpoint_selection, 'Position': raycast.outputs["Hit Position"]})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 6, 'Radius': 0.0100})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_position_2, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_m_a_t_002)})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_5.outputs["Input"]})
    
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: reroute_7}, attrs={'operation': 'NOT'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': op_not})
    
    delete_geometry_1 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': set_material_3, 'Selection': reroute_4})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': delete_geometry_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_1})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Radius': 0.0300})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"], 1: 2.0000}, attrs={'operation': 'POWER'})
    
    value_1 = nw.new_node(Nodes.Value)
    value_1.outputs[0].default_value = -3.6400
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: power, 1: value_1}, attrs={'operation': 'MULTIPLY'})
    
    power_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: 2.0000}, attrs={'operation': 'POWER'})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: power_1, 1: value_1}, attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_4, 1: multiply_5})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: add_2, 1: 9.4500}, attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_6, 1: separate_xyz.outputs["Z"]})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz.outputs["X"], 'Y': separate_xyz.outputs["Y"], 'Z': add_3})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': store_named_attribute, 'Position': combine_xyz_1})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': reroute, 'Instance': set_position_3})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points, 'Material': surface.shaderfunc_to_material(shader_m_a_t_002)})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["Z"], 1: -1.4100}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_1.outputs["X"], 'Y': separate_xyz_1.outputs["Y"], 'Z': multiply_7})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': -0.0900})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_3, 'Position': combine_xyz_3, 'Offset': combine_xyz_2})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute, 'Instance': set_position_4, 'Scale': (0.8700, 0.8700, 0.8700)})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points_2, 'Material': surface.shaderfunc_to_material(shader_m_at_001)})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material_1})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Z"], 1: -0.4400}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_2.outputs["X"], 'Y': separate_xyz_2.outputs["Y"], 'Z': multiply_8})
    
    set_position_5 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_3, 'Position': combine_xyz_4, 'Offset': (0.0000, 0.0000, -0.0100)})
    
    instance_on_points_3 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_2, 'Selection': endpoint_selection_1, 'Instance': set_position_5, 'Scale': (0.7200, 0.7200, 0.7200)})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points_3, 'Material': surface.shaderfunc_to_material(shader_m_a_t_002)})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': set_material_4, 'Selection': reroute_4})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': delete_geometry})
    
    endpoint_selection_2 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ)
    
    set_position_6 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances, 'Selection': endpoint_selection_2, 'Position': combine_xyz_5})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_position_6, 'Radius': 1.0000})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine)
    
    endpoint_selection_3 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    set_position_7 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_line_2, 'Selection': endpoint_selection_3, 'Position': raycast.outputs["Hit Position"]})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_position_7, 'Radius': 1.5000})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_curve_radius, set_curve_radius_1]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': join_geometry_1, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    set_material_5 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': surface.shaderfunc_to_material(shader_g_o_l_d)})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    delete_geometry_2 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': set_material_5, 'Selection': reroute_5})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': delete_geometry_2})
    
    endpoint_selection_4 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    instance_on_points_4 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_curve_radius_1, 'Selection': endpoint_selection_4, 'Instance': set_position_5, 'Scale': (1.4200, 1.4200, 1.4200)})
    
    set_material_6 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points_4, 'Material': surface.shaderfunc_to_material(shader_m_a_t_002)})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    delete_geometry_3 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': set_material_6, 'Selection': reroute_6})
    
    uv_sphere_1 = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Radius': 0.0600})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere_1.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    set_material_7 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': store_named_attribute_1, 'Material': surface.shaderfunc_to_material(shader_g_o_l_d)})
    
    delete_geometry_4 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': set_material_7, 'Selection': reroute_6})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': delete_geometry_4})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [reroute_3, set_material_2, set_shade_smooth_1, reroute_1, reroute_2, delete_geometry_3, set_shade_smooth]})
    
    convex_hull = nw.new_node(Nodes.ConvexHull, input_kwargs={'Geometry': delete_geometry_2})
    
    subdivide_mesh = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': convex_hull})
    
    triangulate_1 = nw.new_node('GeometryNodeTriangulate',
        input_kwargs={'Mesh': subdivide_mesh},
        attrs={'ngon_method': 'CLIP', 'quad_method': 'BEAUTY'})
    
    dual_mesh = nw.new_node(Nodes.DualMesh, input_kwargs={'Mesh': triangulate_1})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': dual_mesh})
    
    set_curve_radius_2 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': mesh_to_curve, 'Radius': 0.2500})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': 0.0200})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_2, 'Profile Curve': curve_circle_2.outputs["Curve"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_2, 'Material': surface.shaderfunc_to_material(shader_m_a_t_002)})
    
    delete_geometry_5 = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': set_material, 'Selection': group_input_5.outputs["Selection"]})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry, delete_geometry_5]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_2}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_m_at_001, selection=selection)
    surface.add_material(obj, shader_m_a_t_002, selection=selection)
    surface.add_material(obj, shader_g_o_l_d, selection=selection)
apply(bpy.context.active_object)
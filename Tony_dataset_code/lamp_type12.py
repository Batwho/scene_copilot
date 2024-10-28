import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_lamp11(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'M2'})
    
    separate_rgb = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': attribute.outputs["Vector"]})
    
    less_than = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_rgb.outputs["Green"], 1: separate_rgb.outputs["Red"]},
        attrs={'operation': 'LESS_THAN'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: less_than, 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (0.5089, 0.2874, 0.1620, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': mix.outputs[2], 'Metallic': 1.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_2 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Perfil', 2.0000),
            ('NodeSocketFloat', 'Radious_1', 5.0000),
            ('NodeSocketFloat', 'Radious_2', 2.5000),
            ('NodeSocketFloat', 'Radious 3', 1.0000),
            ('NodeSocketFloat', 'Top_Radious', -0.7500),
            ('NodeSocketFloat', 'Top_Light', -0.2000),
            ('NodeSocketFloat', 'Hight', 2.0000),
            ('NodeSocketInt', 'Count', 36),
            ('NodeSocketFloat', "Light Hight'", -0.2000)])
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Top_Light"]})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_8})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_1, 'End': combine_xyz_1})
    
    collection_info_1 = nw.new_node(Nodes.CollectionInfo, input_kwargs={'Collection': bpy.data.collections['LIGHT']})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': curve_line_1, 'Instance': collection_info_1})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_2.outputs["Light Hight'"]})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': instance_on_points_1, 'Translation': combine_xyz_3})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Top_Radious"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Radious 3"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: reroute_6})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_8, 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder', input_kwargs={'Radius': add, 'Depth': multiply})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': group_input_2.outputs["Count"]})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_2.outputs["Hight"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_1})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_2})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': 30})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_circle.outputs["Curve"], 'Instance': resample_curve})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': instance_on_points, 'Rotation': (0.0000, 0.0000, 0.0297), 'Local Space': False})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': rotate_instances})
    
    position = nw.new_node(Nodes.InputPosition)
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': spline_parameter.outputs["Factor"], 3: 1.0000, 4: 0.0000})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"], 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_2})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Perfil"]})
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: reroute_3}, attrs={'operation': 'POWER'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Radious_1"]})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: power, 1: reroute_4}, attrs={'operation': 'MULTIPLY'})
    
    power_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: reroute_3}, attrs={'operation': 'POWER'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: power_1, 1: 1.1900})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Radious_2"]})
    
    power_2 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: reroute_5}, attrs={'operation': 'POWER'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: power_2}, attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: reroute_6}, attrs={'operation': 'SUBTRACT'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute, 'Y': reroute, 'Z': 1.0000})
    
    multiply_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 1: combine_xyz}, attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances, 'Position': multiply_4.outputs["Vector"]})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': 0.0300})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_circle_1.outputs["Curve"], 1: normal},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_position, 'Profile Curve': transform_1, 'Fill Caps': True})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh, 'Shade Smooth': False})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['ceiling'], 'Reset Children': True},
        attrs={'transform_space': 'RELATIVE'})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': collection_info})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': realize_instances_1, 'Ray Direction': (0.0000, 0.0000, 1.0000)})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_line_1, 'Selection': endpoint_selection, 'Position': raycast.outputs["Hit Position"]})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 12, 'Radius': 0.0400})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_position_1, 'Profile Curve': curve_circle_2.outputs["Curve"], 'Fill Caps': True})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [store_named_attribute, set_shade_smooth, curve_to_mesh_1]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': surface.shaderfunc_to_material(shader_lamp11)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_2, set_material]})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate, input_kwargs={'Vector': capture_attribute.outputs["Attribute"], 'Angle': 1.5708})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry_1, 'Attribute': vector_rotate},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_lamp11, selection=selection)
apply(bpy.context.active_object)
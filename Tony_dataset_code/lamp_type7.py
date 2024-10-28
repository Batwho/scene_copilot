import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_m_i_o_noise', singleton=False, type='GeometryNodeTree')
def nodegroup_m_i_o_noise(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Scale', 5.0000),
            ('NodeSocketFloat', 'Detail', 2.0000),
            ('NodeSocketFloatFactor', 'Roughness', 0.5000),
            ('NodeSocketFloat', 'Distortion', 0.0000),
            ('NodeSocketFloat', 'Intens', 0.5000)])
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': group_input.outputs["Scale"], 'Detail': group_input.outputs["Detail"], 'Roughness': group_input.outputs["Roughness"], 'Distortion': group_input.outputs["Distortion"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': noise_texture.outputs["Fac"], 3: -0.5000, 4: 0.5000})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range.outputs["Result"], 1: group_input.outputs["Intens"]},
        attrs={'operation': 'MULTIPLY'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': multiply}, attrs={'is_active_output': True})

def shader_metal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Metallic': 1.0000, 'Roughness': 0.2136})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_body(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0080, 0.0080, 0.0080, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'LIGHT'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': attribute.outputs["Vector"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_xyz.outputs["X"]})
    colorramp.color_ramp.elements[0].position = 0.5864
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.6045
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"], 1: 16.2600}, attrs={'operation': 'MULTIPLY'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0207, 0.0207, 0.0207, 1.0000), 'Emission': (1.0000, 0.6936, 0.3929, 1.0000), 'Emission Strength': multiply})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Start_radious', 0.0000),
            ('NodeSocketFloat', 'Rotations', 2.3100),
            ('NodeSocketFloatDistance', 'End Radius', 0.2100),
            ('NodeSocketFloat', 'Hight', 0.0000),
            ('NodeSocketFloat', 'Base_Hight', 0.0000),
            ('NodeSocketFloat', 'Lamp_Radious', 0.0000),
            ('NodeSocketFloat', 'Cable_Noise', -0.0300),
            ('NodeSocketFloat', 'Plug Hight', 0.0000),
            ('NodeSocketFloat', 'Sphere', 0.0000)])
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Base_Hight"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_2})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Start_radious"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': reroute_6})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_body)})
    
    value_5 = nw.new_node(Nodes.Value)
    value_5.outputs[0].default_value = 67.6500
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Hight"]})
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': value_5, 'Rotations': group_input.outputs["Rotations"], 'Start Radius': reroute_6, 'End Radius': group_input.outputs["End Radius"], 'Height': reroute})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz.outputs["Z"], 2: reroute})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range.outputs["Result"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0000), (0.5074, 0.3313), (1.0000, 1.0000)])
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: -5.4500}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 0.0400})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': spiral, 'Tilt': add})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range.outputs["Result"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.1647, 0.0125), (1.0000, 1.0000)], handles=['AUTO', 'VECTOR', 'AUTO'])
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 1.0000, 'Z': float_curve})
    
    multiply_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 1: combine_xyz_1}, attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_curve_tilt, 'Position': multiply_1.outputs["Vector"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Lamp_Radious"]})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.0800}, attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: multiply_2})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_1})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position, 'Offset': combine_xyz_2})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_position_1, 'Radius': reroute_1})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': 0.1000})
    
    transform_2 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle_1.outputs["Curve"], 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': transform_2, 1: normal},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': capture_attribute.outputs["Geometry"], 'Fill Caps': True})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh_1, 'Shade Smooth': False})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_material)})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_4, 'Z': divide})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['Wall'], 'Reset Children': True},
        attrs={'transform_space': 'RELATIVE'})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': collection_info})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': realize_instances, 'Source Position': combine_xyz_3, 'Ray Direction': (1.0000, 0.0000, 0.0000)})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Plug Hight"]})
    
    add_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: raycast.outputs["Hit Position"], 1: combine_xyz_6})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_3, 'End': add_2.outputs["Vector"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_1, 'Count': 117})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.0000, 1.0000), (0.0142, 1.0000), (0.1279, 0.0000), (0.4768, 0.0000), (0.7162, 0.0000), (0.9779, 1.0000), (1.0000, 1.0000)])
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 1.0000, 'Z': float_curve_2})
    
    multiply_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_1, 1: combine_xyz_4}, attrs={'operation': 'MULTIPLY'})
    
    mio_noise = nw.new_node(nodegroup_m_i_o_noise().name,
        input_kwargs={'Scale': 0.9800, 'Intens': group_input.outputs["Cable_Noise"]})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': float_curve_2, 3: 1.0000, 4: 0.0000})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_1.outputs["Result"], 1: 0.9900},
        attrs={'operation': 'GREATER_THAN'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: mio_noise, 1: greater_than}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_4})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': resample_curve, 'Position': multiply_3.outputs["Vector"], 'Offset': combine_xyz_5})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_position_2, 'Radius': 0.0600})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': 0.1000})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': curve_circle_2.outputs["Curve"], 'Fill Caps': True})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_2, 'Material': surface.shaderfunc_to_material(shader_body)})
    
    curve_circle_3 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': 0.0700})
    
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': curve_circle_3.outputs["Curve"]})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': fill_curve, 'Offset Scale': 0.0100})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Rotation': (0.0000, 0.0000, 0.7854), 'Scale': (1.0000, 1.0000, 1.5400)})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': transform, 'Rotation': (0.0000, 1.5708, 0.0000), 'Scale': (1.6800, 1.0000, -1.0000)})
    
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': transform_1})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_2.outputs["Vector"]})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': geometry_to_instance, 'Position': reroute_5})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_3, 'Material': surface.shaderfunc_to_material(shader_body)})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Sphere"]})
    
    uv_sphere_1 = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Radius': reroute_3})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere_1.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_line, 'Selection': endpoint_selection_1, 'Instance': store_named_attribute_1})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_3, 1: 0.6600}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_5})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': instance_on_points, 'Offset': combine_xyz_7})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_4, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material_4})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [set_material_1, set_material, set_material_2, set_material_3, set_shade_smooth_1]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry_1, 'Normal': capture_attribute.outputs["Attribute"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material, selection=selection)
    surface.add_material(obj, shader_body, selection=selection)
    surface.add_material(obj, shader_metal, selection=selection)
apply(bpy.context.active_object)
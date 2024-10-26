import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'uv_one'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': attribute.outputs["Vector"]})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: 0.6800}, attrs={'operation': 'GREATER_THAN'})
    
    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'temp'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute_1.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [1.0000, 0.2177, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.0174, 0.6051, 1.0000, 1.0000]
    
    attribute_2 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'stren'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: attribute_2.outputs["Color"], 1: 500.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: greater_than, 1: multiply}, attrs={'operation': 'MULTIPLY'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': greater_than, 'Metallic': 1.0000, 'Roughness': 0.4000, 'Emission': colorramp.outputs["Color"], 'Emission Strength': multiply_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Hight', 0.0000),
            ('NodeSocketInt', 'Count', 3),
            ('NodeSocketFloatDistance', 'Size X', 0.6100),
            ('NodeSocketFloatDistance', 'Size Y', 1.0000),
            ('NodeSocketFloat', 'Scale', 0.6800),
            ('NodeSocketFloat', 'Differenc', 0.2900),
            ('NodeSocketFloat', 'Noise s', -0.2000),
            ('NodeSocketFloat', 'W', 0.0000),
            ('NodeSocketFloat', 'Sc', 0.5000),
            ('NodeSocketFloat', 'Top Sc', 0.7400),
            ('NodeSocketFloat', 'Offset Scale', 0.0010),
            ('NodeSocketFloatFactor', 'Light_Temp', 0.5000),
            ('NodeSocketFloatFactor', 'Strength', 0.5000)])
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_1.outputs["Hight"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_2})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': group_input_1.outputs["Count"]})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': group_input_1.outputs["Size X"], 'Size Y': group_input_1.outputs["Size Y"], 'Vertices X': 2, 'Vertices Y': 2})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    index = nw.new_node(Nodes.Index)
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: group_input_1.outputs["Scale"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: add, 1: group_input_1.outputs["Differenc"]},
        attrs={'operation': 'MULTIPLY'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': resample_curve, 'Instance': store_named_attribute, 'Scale': multiply})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input_1.outputs["W"], 'Scale': 1.4700, 'Detail': 0.0000, 'Roughness': 0.0000},
        attrs={'noise_dimensions': '4D'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Fac"]}, attrs={'operation': 'SUBTRACT'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: subtract, 1: group_input_1.outputs["Noise s"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_1})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_2, 'Y': reroute_2})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': realize_instances_2, 'Offset': combine_xyz_3})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_1})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': reroute_1})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input_1.outputs["Sc"], 1: 5.0000}, attrs={'operation': 'DIVIDE'})
    
    quadrilateral = nw.new_node('GeometryNodeCurvePrimitiveQuadrilateral', input_kwargs={'Width': divide, 'Height': divide})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': quadrilateral, 1: normal},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': mesh_to_curve, 'Profile Curve': capture_attribute.outputs["Geometry"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh, 'Shade Smooth': False})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': set_shade_smooth})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_line, 'Scale': (1.0000, 1.0000, 0.0000)})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': reroute_1, 'Instance': transform_1})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    object_info = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Plane']},
        attrs={'transform_space': 'RELATIVE'})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': object_info.outputs["Geometry"], 'Ray Direction': (0.0000, 0.0000, 1.0000)})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances, 'Selection': endpoint_selection, 'Position': raycast.outputs["Hit Position"]})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_position, 'Radius': 0.0800})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': 0.0100})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: divide, 1: group_input_1.outputs["Top Sc"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_2})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute})
    
    multiply_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_xyz, 1: (-1.0000, -1.0000, -1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz, 'End': multiply_3.outputs["Vector"]})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': mesh_to_curve, 'Profile Curve': curve_line_1})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide_1})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_to_mesh_2, 'Translation': combine_xyz_1})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': transform})
    
    divide_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Offset Scale"], 1: 10.0000},
        attrs={'operation': 'DIVIDE'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': transform, 'Offset Scale': divide_2})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces, extrude_mesh.outputs["Mesh"]]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_1})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': merge_by_distance, 'Shade Smooth': False})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Radius': 0.0200})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz.outputs["Z"]})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': store_named_attribute_1, 'Selection': greater_than})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position, 'Selection': endpoint_selection_1, 'Instance': delete_geometry, 'Scale': (0.3500, 0.3500, 0.3500)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [realize_instances_1, curve_to_mesh_1, set_shade_smooth_1, instance_on_points_2]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': surface.shaderfunc_to_material(shader_material)})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_1.outputs["Light_Temp"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_1.outputs["Strength"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': set_material, 'Attribute': capture_attribute.outputs["Attribute"], 2: mix.outputs[2], 3: mix_1.outputs[2]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material, selection=selection)
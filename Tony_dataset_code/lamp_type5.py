import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_bk(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0049, 0.0049, 0.0049, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_light(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'mio1'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute_1.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [1.0000, 0.4606, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.5421, 1.0000, 1.0000]
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'mio'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"], 1: 243.4000}, attrs={'operation': 'MULTIPLY'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Emission': colorramp_1.outputs["Color"], 'Emission Strength': multiply})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_metal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.8000, 0.6060, 0.2528, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.0773})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_3 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Top_Angle', -0.2000),
            ('NodeSocketFloat', 'Top_angle_2', 0.0000),
            ('NodeSocketFloat', 'Top_Hight', 0.0000),
            ('NodeSocketFloat', 'Lamp', 0.5000),
            ('NodeSocketFloat', 'Cone_angle', -0.7000),
            ('NodeSocketFloat', 'Base_Hight', 0.0000),
            ('NodeSocketFloatDistance', 'Base_Radius', 0.1900),
            ('NodeSocketFloatDistance', 'Radius', 0.0100),
            ('NodeSocketFloatFactor', 'Light_Strenghth', 0.5000),
            ('NodeSocketFloatFactor', 'Fac', 0.5000)])
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'Y': group_input_3.outputs["Top_Angle"], 'Z': group_input_3.outputs["Top_Hight"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_5})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': reroute_5})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'Y': group_input_3.outputs["Top_angle_2"], 'Z': separate_xyz.outputs["Z"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': (0.0000, 0.0000, -0.2300), 'End': combine_xyz})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': 6})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': separate_xyz.outputs["Y"]})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': resample_curve, 'Selection': endpoint_selection, 'Offset': combine_xyz_1})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': endpoint_selection_1, 'Offset': (0.0000, -0.1300, 0.2400)})
    
    fillet_curve = nw.new_node(Nodes.FilletCurve,
        input_kwargs={'Curve': set_position_1, 'Count': 3, 'Radius': 0.0800},
        attrs={'mode': 'POLY'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input_3.outputs["Radius"], 1: 10.0000}, attrs={'operation': 'DIVIDE'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': divide})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': fillet_curve, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_metal)})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': fillet_curve})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': endpoint_selection})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_3.outputs["Lamp"]})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder', input_kwargs={'Radius': 0.1100, 'Depth': reroute})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: divide_1, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 0.0500}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_1})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Translation': combine_xyz_2})
    
    position = nw.new_node(Nodes.InputPosition)
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_3.outputs["Cone_angle"]})
    
    multiply_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 1: reroute_1}, attrs={'operation': 'MULTIPLY'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': transform, 'Selection': cylinder.outputs["Top"], 'Offset': multiply_2.outputs["Vector"]})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': set_position_2, 'Selection': cylinder.outputs["Bottom"], 'Offset Scale': 0.0000})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': 0.7900})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements, 'Selection': extrude_mesh.outputs["Top"], 'Scale': 1.0700})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': scale_elements_1, 'Selection': extrude_mesh.outputs["Top"], 'Offset Scale': -0.1300})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_1, 1: -1.0000, 2: 0.1000})
    
    scale_elements_2 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Selection': extrude_mesh_1.outputs["Top"], 'Scale': map_range.outputs["Result"]})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': group_input_3.outputs["Top_angle_2"]})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_5, 1: combine_xyz_6})
    
    object_info = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Empty'], 'As Instance': True},
        attrs={'transform_space': 'RELATIVE'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add.outputs["Vector"], 1: object_info.outputs["Location"]},
        attrs={'operation': 'SUBTRACT'})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': subtract.outputs["Vector"]}, attrs={'axis': 'Z'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_3, 'Selection': reroute_2, 'Instance': scale_elements_2, 'Rotation': align_euler_to_vector})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points, 'Material': surface.shaderfunc_to_material(shader_bk)})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material_1, 'Selection': cylinder.outputs["Side"]})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Radius': 0.0500})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_3, 'Selection': reroute_2, 'Instance': store_named_attribute_2, 'Rotation': align_euler_to_vector})
    
    translate_instances = nw.new_node(Nodes.TranslateInstances,
        input_kwargs={'Instances': instance_on_points_1, 'Translation': (0.0000, 0.0000, -0.1800)})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': translate_instances})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': realize_instances, 'Material': surface.shaderfunc_to_material(shader_light)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_2, set_shade_smooth, set_material]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_3.outputs["Base_Hight"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': -0.0700, 'Z': reroute_4})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_1, 'Translation': combine_xyz_4})
    
    cylinder_1 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Radius': group_input_3.outputs["Base_Radius"], 'Depth': reroute_4})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder_1.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_4, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': -0.1700, 'Z': divide_2})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_1, 'Translation': combine_xyz_3})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': transform_1, 1: position_1},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Material': surface.shaderfunc_to_material(shader_bk)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_2, set_material_3]})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["Light_Strenghth"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input_3.outputs["Fac"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry, 1: mix.outputs[2], 2: mix_1.outputs[2]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_metal, selection=selection)
    surface.add_material(obj, shader_light, selection=selection)
    surface.add_material(obj, shader_bk, selection=selection)
apply(bpy.context.active_object)
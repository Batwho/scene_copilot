import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_inverter', singleton=False, type='GeometryNodeTree')
def nodegroup_inverter(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketFloat', 'Value', 0.0000)])
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Value"]})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_2})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_1})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_2})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'X': combine_xyz_6, '-X': combine_xyz_7, 'Y': combine_xyz_3, '-Y': combine_xyz_2, 'Z': combine_xyz_5, '-Z': combine_xyz_4},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketFloat', 'Y', 1.0000)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Y"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'vectorend': combine_xyz_2, 'vectorstart': combine_xyz_3}, attrs={'is_active_output': True})

def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.8000, 0.6797, 0.4425, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.0455})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_light(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Emission': (1.0000, 1.0000, 1.0000, 1.0000), 'Emission Strength': 7.9000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    value_2 = nw.new_node(Nodes.Value)
    value_2.outputs[0].default_value = 0.7100
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': value_2})
    
    curve_line_3 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_1})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_3, 'Count': 5})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': (0.0000, 0.0000, 1.0000), 'End': (0.0000, 0.0000, 0.0000)})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    delete_geometry_2 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': curve_line_1, 'Selection': endpoint_selection})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 0.4500
    
    nodegroup = nw.new_node(nodegroup_node_group().name, input_kwargs={'Y': value})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': nodegroup.outputs['vectorstart'], 'End': nodegroup.outputs["vectorend"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': delete_geometry_2, 'Instance': curve_line})
    
    scale_instances = nw.new_node(Nodes.ScaleInstances,
        input_kwargs={'Instances': instance_on_points, 'Scale': (1.0000, 3.5000, 1.0000)})
    
    inverter = nw.new_node(nodegroup_inverter().name, input_kwargs={'Value': 0.0400})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': inverter.outputs["Z"], 'End': inverter.outputs["-Z"]})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': scale_instances, 'Instance': curve_line_2})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': realize_instances})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_1.outputs["Y"], 1: 0.0000},
        attrs={'operation': 'GREATER_THAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': reroute_1, 'Selection': greater_than})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: 0.0000}, attrs={'operation': 'LESS_THAN'})
    
    value_1 = nw.new_node(Nodes.Value)
    value_1.outputs[0].default_value = 0.3900
    
    inverter_1 = nw.new_node(nodegroup_inverter().name, input_kwargs={'Value': value_1})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': delete_geometry, 'Selection': less_than, 'Offset': inverter_1.outputs["-Y"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': value_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_circle.outputs["Curve"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_position, 'Profile Curve': reroute})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': curve_to_mesh, 'Offset Scale': 0.0500, 'Individual': False})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_material)})
    
    delete_geometry_1 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': reroute_1, 'Selection': less_than})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': delete_geometry_1, 'Offset': inverter_1.outputs["Y"]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_position_1, 'Profile Curve': reroute})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': surface.shaderfunc_to_material(shader_material)})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_instances})
    
    value_3 = nw.new_node(Nodes.Value)
    value_3.outputs[0].default_value = 0.0500
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': value_3})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': reroute_3, 'Profile Curve': curve_circle_1.outputs["Curve"], 'Fill Caps': True})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh_2})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_2, 'Material': surface.shaderfunc_to_material(shader_material)})
    
    curve_to_mesh_5 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_position_1, 'Profile Curve': reroute, 'Fill Caps': True})
    
    curve_to_mesh_6 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_position, 'Profile Curve': reroute, 'Fill Caps': True})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_to_mesh_5, curve_to_mesh_6]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_2, 'Material': surface.shaderfunc_to_material(shader_light)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [set_material_2, set_material_3, set_material_1, set_material]})
    
    index = nw.new_node(Nodes.Index)
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: 0.6400}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': resample_curve, 'Instance': join_geometry, 'Rotation': combine_xyz})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: value_2, 1: -0.5000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_1})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': instance_on_points_2, 'Offset': combine_xyz_2})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: value_2, 1: value_3})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: -0.5900}, attrs={'operation': 'MULTIPLY'})
    
    inverter_2 = nw.new_node(nodegroup_inverter().name, input_kwargs={'Value': multiply_2})
    
    curve_line_4 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': inverter_2.outputs["Z"], 'End': inverter_2.outputs["-Z"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': value_3})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: 1.5100}, attrs={'operation': 'MULTIPLY'})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': multiply_3})
    
    curve_to_mesh_3 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line_4, 'Profile Curve': curve_circle_2.outputs["Curve"], 'Fill Caps': True})
    
    set_material_5 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_3, 'Material': surface.shaderfunc_to_material(shader_material)})
    
    curve_line_5 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 0.1000)})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['ciling'], 'Reset Children': True},
        attrs={'transform_space': 'RELATIVE'})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': collection_info})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': realize_instances_1, 'Ray Direction': (0.0000, 0.0000, 1.0000)})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_line_5, 'Selection': endpoint_selection_1, 'Position': raycast.outputs["Hit Position"]})
    
    curve_circle_3 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': reroute_5})
    
    curve_to_mesh_4 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_position_3, 'Profile Curve': curve_circle_3.outputs["Curve"], 'Fill Caps': True})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_4, 'Material': surface.shaderfunc_to_material(shader_material)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_2, set_material_5, set_material_4]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_1}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_light, selection=selection)
    surface.add_material(obj, shader_material, selection=selection)
apply(bpy.context.active_object)
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

    fresnel = nw.new_node(Nodes.Fresnel, input_kwargs={'IOR': 1.1200})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': fresnel})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.1136
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"], 1: 14.8400}, attrs={'operation': 'MULTIPLY'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Emission': (1.0000, 0.7315, 0.3126, 1.0000), 'Emission Strength': 12.0000})
    
    glass_bsdf = nw.new_node(Nodes.GlassBSDF)
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': multiply, 1: principled_bsdf, 2: glass_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def shader_blk(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0228, 0.0228, 0.0228, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Resolution', 5),
            ('NodeSocketFloatDistance', 'T_Radius', 0.5000),
            ('NodeSocketFloat', 'X_Scale ', 1.0000),
            ('NodeSocketFloat', 'Y_Scale', 1.0000),
            ('NodeSocketFloatDistance', 'Rim_Radious', 0.0300),
            ('NodeSocketInt', 'Rim_Resolition', 6),
            ('NodeSocketInt', 'Count', 0),
            ('NodeSocketFloat', 'Len', 0.0400),
            ('NodeSocketFloat', 'Spiral_S', 1.9100),
            ('NodeSocketFloatDistance', 'Radius', 0.4100),
            ('NodeSocketFloat', 'Ligt_count', 2.5000),
            ('NodeSocketFloat', 'Radious', 1.1900)])
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Resolution"], 'Radius': group_input.outputs["T_Radius"]})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["X_Scale "], 'Y': group_input.outputs["Y_Scale"]})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform, 'Scale': combine_xyz_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Count"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': reroute, 'Count': reroute_5})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, -5.0000)})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': resample_curve, 'Instance': curve_line})
    
    index = nw.new_node(Nodes.Index)
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': index, 2: subtract, 3: 0.0100})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range.outputs["Result"], 1: group_input.outputs["Spiral_S"]},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: group_input.outputs["Len"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 1.0000, 'Z': add})
    
    scale_instances = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': instance_on_points, 'Scale': combine_xyz})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_instances})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': reroute_3})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_6, 1: group_input.outputs["Ligt_count"]},
        attrs={'operation': 'MULTIPLY'})
    
    float_to_integer = nw.new_node(Nodes.FloatToInt, input_kwargs={'Float': multiply_1})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': float_to_integer})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_7, 3: reroute_8}, attrs={'data_type': 'INT'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2})
    
    switch_2 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than, 2: 4.6000, 3: 43.7000, 4: reroute_8, 5: add_1},
        attrs={'input_type': 'INT'})
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': realize_instances, 'Count': switch_2.outputs[1]})
    
    endpoint_selection_2 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: endpoint_selection}, attrs={'operation': 'NOT'})
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than, 6: endpoint_selection_2, 7: op_not},
        attrs={'input_type': 'BOOLEAN'})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, -0.2300)})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_1, 'Count': 25})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.2500), (0.2012, 0.2934), (0.4853, 1.0000), (0.9647, 0.2500), (1.0000, 0.2750)], handles=['AUTO', 'VECTOR', 'AUTO', 'AUTO', 'AUTO'])
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: float_curve, 1: group_input.outputs["Radious"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve_1, 'Radius': multiply_3})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 10, 'Radius': 0.0500})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': curve_circle_2.outputs["Curve"], 'Fill Caps': True})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': resample_curve_2, 'Selection': switch_1.outputs[2], 'Instance': curve_to_mesh_1})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points_1, 'Material': surface.shaderfunc_to_material(shader_light)})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rim_Radious"]})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Rim_Resolition"], 'Radius': reroute_10})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': reroute_1, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh, 'Shade Smooth': False})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_blk)})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_4, 'Radius': group_input.outputs["Radius"]})
    
    curve_circle_4 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': 0.0200})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': curve_circle_4.outputs["Curve"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh_2})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_2, 'Material': surface.shaderfunc_to_material(shader_blk)})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': (0.0000, 0.0000, 0.0100), 'End': (0.0000, 0.0000, -0.0200)})
    
    curve_circle_3 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 18, 'Radius': 0.0200})
    
    curve_to_mesh_3 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line_2, 'Profile Curve': curve_circle_3.outputs["Curve"], 'Fill Caps': True})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': realize_instances, 'Instance': curve_to_mesh_3})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    greater_than_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: -0.0600}, attrs={'operation': 'GREATER_THAN'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_10, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_4})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': instance_on_points_2, 'Selection': greater_than_1, 'Offset': combine_xyz_2})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position, 'Material': surface.shaderfunc_to_material(shader_blk)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [set_material_3, set_material_2, set_material, set_material_1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_blk, selection=selection)
    surface.add_material(obj, shader_light, selection=selection)
apply(bpy.context.active_object)
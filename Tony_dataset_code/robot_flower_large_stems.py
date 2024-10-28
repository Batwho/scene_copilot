import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_bulb_pollen(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'TEST'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute.outputs["Color"]})
    colorramp.color_ramp.interpolation = "B_SPLINE"
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.1167, 0.1239, 0.5070, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.3091
    colorramp.color_ramp.elements[1].color = [0.0139, 0.0016, 0.0082, 1.0000]
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute.outputs["Color"]})
    colorramp_1.color_ramp.interpolation = "B_SPLINE"
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.7030, 1.0000, 0.2316, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.0227
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 0.1591
    colorramp_1.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Subsurface Color': colorramp.outputs["Color"], 'Metallic': 0.6364, 'Roughness': 0.1500, 'Emission': colorramp_1.outputs["Color"], 'Emission Strength': 4.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Amount of Leaves', 7),
            ('NodeSocketInt', 'Curve Resolution', 178),
            ('NodeSocketInt', 'Profile Resolution', 80),
            ('NodeSocketFloatDistance', 'Curve Radius', 0.0300),
            ('NodeSocketFloat', 'Leaf Shape Radius', 12.0000),
            ('NodeSocketFloatDistance', 'Instance Radius', 0.0150),
            ('NodeSocketFloat', 'X Rotation', 73.8000),
            ('NodeSocketFloat', 'Y Rotation', 5.0000),
            ('NodeSocketFloat', 'Z Rotation', 0.0000),
            ('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketVector', 'End Handle Position', (0.0000, -0.3590, 0.0650)),
            ('NodeSocketVector', 'Start Handle Position', (0.0000, -0.0500, 0.8280)),
            ('NodeSocketVectorTranslation', 'End Position', (0.0000, 0.8720, 0.0750)),
            ('NodeSocketVectorTranslation', 'Start Position', (0.0000, 0.0060, -0.0940)),
            ('NodeSocketColor', 'Color1', (0.5000, 0.5000, 0.5000, 1.0000)),
            ('NodeSocketColor', 'Color2', (0.5000, 0.5000, 0.5000, 1.0000))])
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Amount of Leaves"], 'Radius': group_input.outputs["Instance Radius"]})
    
    bezier_segment_1 = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Resolution': 150, 'Start': (0.0000, 0.0000, 0.5000), 'Start Handle': (0.0000, 0.0000, 0.0000), 'End': (0.0000, 0.0000, 0.0000)})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': bezier_segment_1, 'Selection': endpoint_selection, 'Offset': group_input.outputs["End Position"]})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': endpoint_selection_1, 'Offset': group_input.outputs["Start Position"]})
    
    set_handle_positions = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_position_1, 'Selection': endpoint_selection, 'Offset': group_input.outputs["End Handle Position"]},
        attrs={'mode': 'RIGHT'})
    
    set_handle_positions_1 = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_handle_positions, 'Selection': endpoint_selection_1, 'Offset': group_input.outputs["Start Handle Position"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_handle_positions_1, 'Count': group_input.outputs["Curve Resolution"]})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': resample_curve})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: spline_parameter.outputs["Factor"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': trim_curve, 'Name': 'TEST', 5: mix.outputs[2]},
        attrs={'data_type': 'FLOAT_COLOR'})
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': store_named_attribute, 3: mix.outputs[2]},
        attrs={'data_type': 'FLOAT_COLOR'})
    
    curve_tangent_1 = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent_1})
    
    radians = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["X Rotation"]}, attrs={'operation': 'RADIANS'})
    
    radians_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Y Rotation"]}, attrs={'operation': 'RADIANS'})
    
    radians_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Z Rotation"]}, attrs={'operation': 'RADIANS'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': radians, 'Y': radians_1, 'Z': radians_2})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: align_euler_to_vector, 1: combine_xyz_1})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_circle_1.outputs["Curve"], 'Instance': capture_attribute.outputs["Geometry"], 'Rotation': add.outputs["Vector"], 'Scale': (0.1500, 0.1500, 0.1500)})
    
    trim_curve_1 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': instance_on_points, 'Selection': False})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.3750), (0.0251, 0.8375), (0.0418, 0.4125), (0.0557, 0.5438), (0.0641, 0.4000), (0.0919, 0.5438), (0.1058, 0.3875), (0.1253, 0.5125), (0.1476, 0.3500), (0.1588, 0.4937), (0.1699, 0.3500), (0.2591, 0.2813), (0.4039, 0.2125), (0.8844, 0.2341), (1.0000, 0.4937)])
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: -0.0100}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': trim_curve_1, 'Radius': multiply})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 64})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_bulb_pollen)})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': set_shade_smooth_1})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry, 'Rotation': (0.0000, 3.1416, 0.0000)})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': transform})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': set_shade_smooth, 'Attribute': capture_attribute.outputs[3]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
apply(bpy.context.active_object)
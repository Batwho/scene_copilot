import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_ribbon_fluffy(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.8000, 0.4827, 0.2644, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.3172})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_chrome(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Metallic': 1.0000, 'Roughness': 0.2345})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_l_ight_bulb_light(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    emission = nw.new_node(Nodes.Emission, input_kwargs={'Color': (1.0000, 0.7032, 0.4346, 1.0000), 'Strength': 60.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': emission}, attrs={'is_active_output': True})

def shader_l_ight_bulb(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Roughness': 0.0000, 'Transmission': 1.0000, 'Transmission Roughness': 0.6621})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_lights(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF)
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_cords(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0072, 0.0072, 0.0072, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_balls(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': object_info.outputs["Random"]})
    colorramp.color_ramp.interpolation = "CONSTANT"
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.1954, 0.2373, 0.6976, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.2939
    colorramp.color_ramp.elements[1].color = [0.6976, 0.6055, 0.2505, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.6091
    colorramp.color_ramp.elements[2].color = [0.6976, 0.0193, 0.0325, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.8636
    colorramp.color_ramp.elements[3].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Metallic': 1.0000, 'Roughness': 0.1992, 'Clearcoat': 1.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_ribbon(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.8000, 0.0000, 0.0434, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.3345, 'Anisotropic': 0.5241})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_needle(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': object_info.outputs["Random"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0073, 0.0144, 0.0076, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.0684, 0.1697, 0.0719, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Subsurface Radius': (0.1000, 0.1000, 0.1000), 'Subsurface Color': (0.2464, 0.6482, 0.2597, 1.0000), 'Specular': 0.2394, 'Specular Tint': 0.1788, 'Roughness': 0.3727})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_tree(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.2161, 0.0930, 0.0518, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Tree Heigth', 2.7000),
            ('NodeSocketFloat', 'Tree Width', 1.0000),
            ('NodeSocketFloat', 'Branch Rotation', 0.0000),
            ('NodeSocketFloat', 'LIghts Around', 3.0100),
            ('NodeSocketInt', 'Lights Density', 15),
            ('NodeSocketFloat', 'Lights Scale', 1.0000),
            ('NodeSocketFloat', 'Ribbon Around', 5.3100),
            ('NodeSocketFloat', 'Fluffy Ribbon Around', 1.8400),
            ('NodeSocketFloatFactor', 'Xmas Balls', 1.0000),
            ('NodeSocketFloat', 'Xmas Balls Scale', 1.0000),
            ('NodeSocketInt', 'Tree Branches', 112),
            ('NodeSocketInt', 'Needle Density', 25),
            ('NodeSocketFloat', 'Needle Scale', 0.0000),
            ('NodeSocketFloatFactor', 'Trim Lights', 0.3750),
            ('NodeSocketFloatFactor', 'Trim Ribbon', 0.3556),
            ('NodeSocketFloatFactor', 'Trim Fluffy Ribbon', 0.3556)])
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Tree Heigth"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tree Branches"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': reroute_51, 'Length': 0.0400})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': resample_curve, 2: curve_parameter.outputs["Factor"]})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs["Geometry"]})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': reroute_43, 2: 0.2056})
    
    curve_to_points = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': trim_curve}, attrs={'mode': 'EVALUATED'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input.outputs["Tree Width"], 'Z': -0.2700})
    
    quadratic_bezier = nw.new_node(Nodes.QuadraticBezier,
        input_kwargs={'Resolution': 8, 'Start': (0.0000, 0.0000, 0.0000), 'Middle': (0.6400, 0.0000, -0.3400), 'End': combine_xyz_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_points.outputs["Rotation"]})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.1500, -0.1500, -6.2832), 1: (0.1500, 0.1500, 6.2832)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    rotate_euler_1 = nw.new_node(Nodes.RotateEuler, input_kwargs={'Rotation': reroute_1, 'Rotate By': random_value.outputs["Value"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs[2]})
    
    float_curve_7 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute})
    node_utils.assign_curve(float_curve_7.mapping.curves[0], [(0.0000, 0.0000), (0.5242, 0.3642), (1.0000, 0.8000)])
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Rotation': rotate_euler_1, 'Factor': float_curve_7})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': group_input.outputs["Branch Rotation"]})
    
    rotate_euler_6 = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': align_euler_to_vector, 'Rotate By': combine_xyz_4},
        attrs={'space': 'LOCAL'})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 1.0000), (0.5061, 0.4442), (1.0000, 0.0500)])
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.1000, -0.1000, -0.5000), 1: (0.1000, 0.1000, 0.5000), 2: 0.8000, 3: 1.3100})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: float_curve, 1: random_value_1.outputs[1]}, attrs={'operation': 'MULTIPLY'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points.outputs["Points"], 'Instance': quadratic_bezier, 'Rotation': rotate_euler_6, 'Scale': reroute_2})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points})
    
    curve_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter_1.outputs["Factor"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 1.0000), (0.0861, 0.6942), (1.0000, 0.1860)])
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': float_curve_1, 4: 0.8500})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_7, 'Radius': map_range.outputs["Result"]})
    
    curve_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter_2.outputs["Factor"]})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.0000, 1.0000), (0.0673, 0.8275), (0.5082, 0.4575), (1.0000, 0.1443)])
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': float_curve_2, 4: 1.2500})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_43, 'Radius': map_range_1.outputs["Result"]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_curve_radius, set_curve_radius_1]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 8, 'Radius': 0.0300})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': join_geometry, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_tree)})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': reroute_8}, attrs={'legacy_behavior': True})
    
    curve_parameter_4 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_2 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': realize_instances, 2: curve_parameter_4.outputs["Factor"]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    capture_attribute_4 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': capture_attribute_2.outputs["Geometry"], 1: position},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    curve_to_points_2 = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': capture_attribute_4.outputs["Geometry"], 'Count': 6})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine)
    
    curve_parameter_3 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_line_1, 2: curve_parameter_3.outputs["Factor"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs["Geometry"]})
    
    trim_curve_1 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': reroute_3, 2: 0.2111, 3: 0.8536})
    
    curve_to_points_1 = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': trim_curve_1, 'Count': 3})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (1.0000, 0.0000, 1.0000)})
    
    curve_line_3 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (-1.0000, 0.0000, 1.0000)})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_line_2, curve_line_3]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_points_1.outputs["Rotation"]})
    
    random_value_3 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.1400, -0.1400, -0.1400), 1: (0.1100, 0.1100, 0.1100)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    rotate_euler_2 = nw.new_node(Nodes.RotateEuler, input_kwargs={'Rotation': reroute_5, 'Rotate By': random_value_3.outputs["Value"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs[2]})
    
    float_curve_3 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute_4})
    node_utils.assign_curve(float_curve_3.mapping.curves[0], [(0.0000, 0.2783), (0.1994, 0.4333), (0.9879, 0.0000)])
    
    random_value_6 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.1400, -0.1400, -0.1400), 1: (0.1100, 0.1100, 0.1100), 2: 0.8000, 3: 1.2000})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: float_curve_3, 1: random_value_6.outputs[1]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_1})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points_1.outputs["Points"], 'Instance': join_geometry_2, 'Rotation': rotate_euler_2, 'Scale': reroute_6})
    
    curve_parameter_6 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_3 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': instance_on_points_1, 2: curve_parameter_6.outputs["Factor"]})
    
    curve_to_points_4 = nw.new_node(Nodes.CurveToPoints,
        input_kwargs={'Curve': capture_attribute_3.outputs["Geometry"], 'Count': group_input.outputs["Needle Density"]})
    
    grid = nw.new_node(Nodes.MeshGrid, input_kwargs={'Size X': 0.6900, 'Size Y': 0.0800, 'Vertices X': 2, 'Vertices Y': 2})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    transform_2 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute_1, 'Translation': (0.3300, 0.0000, 0.0000)})
    
    rotate_euler_5 = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': curve_to_points_4.outputs["Rotation"], 'Rotate By': (0.0000, -0.8001, 0.0000)},
        attrs={'space': 'LOCAL'})
    
    random_value_4 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.6500, 0.4800, -6.2832), 1: (0.9800, -0.3900, 6.2832)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    rotate_euler_4 = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': rotate_euler_5, 'Rotate By': random_value_4.outputs["Value"]})
    
    float_curve_6 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': capture_attribute_3.outputs[2]})
    node_utils.assign_curve(float_curve_6.mapping.curves[0], [(0.0000, 1.0000), (0.6467, 0.7317), (1.0000, 0.3392)])
    
    map_range_4 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': float_curve_6, 3: 0.5000, 4: 0.7100})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Needle Scale"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_46, 1: 1.0000})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: map_range_4.outputs["Result"], 1: add}, attrs={'operation': 'MULTIPLY'})
    
    instance_on_points_4 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points_4.outputs["Points"], 'Instance': transform_2, 'Rotation': rotate_euler_4, 'Scale': multiply_2})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points_4, 'Material': surface.shaderfunc_to_material(shader_needle)})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_3, instance_on_points_1]})
    
    curve_parameter_5 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_5 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter_5.outputs["Factor"]})
    node_utils.assign_curve(float_curve_5.mapping.curves[0], [(0.0000, 1.0000), (0.0861, 0.6942), (1.0000, 0.3560)])
    
    map_range_3 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': float_curve_5, 4: 1.1100})
    
    set_curve_radius_2 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': join_geometry_4, 'Radius': map_range_3.outputs["Result"]})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': 0.0200})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_2, 'Profile Curve': curve_circle_1.outputs["Curve"], 'Fill Caps': True})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': surface.shaderfunc_to_material(shader_tree)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, set_material_2]})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_1, 'Rotation': (0.0000, 0.7854, 0.0000)})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_1, 'Rotation': (0.0000, -0.7854, 0.0000)})
    
    join_geometry_5 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform, transform_1]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_5})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.2800, -0.2800, -0.2800), 1: (0.1400, 0.1400, 0.1400)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    add_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: curve_to_points_2.outputs["Rotation"], 1: random_value_2.outputs["Value"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_1.outputs["Vector"]})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': capture_attribute_4.outputs["Attribute"]})
    
    map_range_5 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz.outputs["Z"], 2: group_input.outputs["Tree Heigth"], 3: 1.0000, 4: 0.1000},
        attrs={'clamp': False})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_5.outputs["Result"]})
    
    float_curve_4 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': capture_attribute_2.outputs[2]})
    node_utils.assign_curve(float_curve_4.mapping.curves[0], [(0.0000, 0.6308), (0.5952, 0.8567), (1.0000, 0.2400)])
    
    map_range_2 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': float_curve_4, 4: 0.3700})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_2.outputs["Result"]})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_13, 1: reroute_10}, attrs={'operation': 'MULTIPLY'})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points_2.outputs["Points"], 'Instance': reroute_12, 'Rotation': reroute_9, 'Scale': multiply_3})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_2})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Ribbon Around"]})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tree Width"]})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tree Heigth"]})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_37})
    
    spiral_1 = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Rotations': reroute_40, 'Start Radius': reroute_36, 'End Radius': 0.1500, 'Height': reroute_35})
    
    transform_4 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': spiral_1, 'Rotation': (0.0000, 0.0000, 8.9675), 'Scale': (1.0000, -1.0000, 1.0000)})
    
    trim_curve_5 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': transform_4, 2: group_input.outputs["Trim Ribbon"]})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': curve_to_mesh}, attrs={'legacy_behavior': True})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': realize_instances_2})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    geometry_proximity_1 = nw.new_node(Nodes.Proximity, input_kwargs={'Target': reroute_32}, attrs={'target_element': 'POINTS'})
    
    map_range_7 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': geometry_proximity_1.outputs["Distance"], 1: 0.1700, 2: 0.0000},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_7.outputs["Result"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': geometry_proximity_1.outputs["Position"]})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': trim_curve_5, 'Selection': reroute_18, 'Position': reroute_20})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': geometry_proximity_1.outputs["Distance"]})
    colorramp_1.color_ramp.interpolation = "B_SPLINE"
    colorramp_1.color_ramp.elements[0].position = 0.3576
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.9636
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: (0.0000, 0.0000, -2.0000), 1: colorramp_1.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_2, 1: multiply_4.outputs["Vector"]})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_3, 'Position': add_2.outputs["Vector"]})
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position_2, 'Length': 0.1800}, attrs={'mode': 'LENGTH'})
    
    set_spline_type_1 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': resample_curve_2}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type_1 = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type_1})
    
    curve_parameter_7 = nw.new_node(Nodes.SplineParameter)
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Ribbon Around"], 1: 0.0300},
        attrs={'operation': 'DIVIDE'})
    
    map_range_8 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': curve_parameter_7.outputs["Factor"], 4: divide})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': set_handle_type_1, 'Tilt': map_range_8.outputs["Result"]})
    
    curve_line_4 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0100, 0.0400, 0.0400)})
    
    curve_to_mesh_3 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_curve_tilt, 'Profile Curve': curve_line_4})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_3, 'Material': surface.shaderfunc_to_material(shader_ribbon)})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': realize_instances})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    trim_curve_4 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': reroute_31, 2: 0.5333})
    
    position_4 = nw.new_node(Nodes.InputPosition)
    
    capture_attribute_6 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': trim_curve_4, 1: position_4},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    curve_to_points_3 = nw.new_node(Nodes.CurveToPoints,
        input_kwargs={'Curve': capture_attribute_6.outputs["Geometry"], 'Count': 5, 'Length': 0.1900},
        attrs={'mode': 'LENGTH'})
    
    balls = nw.new_node(Nodes.RandomValue,
        input_kwargs={'Probability': group_input.outputs["Xmas Balls"]},
        label='balls',
        attrs={'data_type': 'BOOLEAN'})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': capture_attribute_6.outputs["Attribute"]})
    
    map_range_13 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_1.outputs["Z"], 2: group_input.outputs["Tree Heigth"], 3: 1.0000, 4: -0.1300},
        attrs={'clamp': False})
    
    reroute_57 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_13.outputs["Result"]})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: balls.outputs[3], 1: reroute_57}, attrs={'operation': 'MULTIPLY'})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_5})
    
    curve_circle_3 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': 0.0050})
    
    transform_6 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle_3.outputs["Curve"], 'Rotation': (1.5708, 1.7651, 0.0000)})
    
    set_spline_cyclic = nw.new_node('GeometryNodeSetSplineCyclic', input_kwargs={'Geometry': transform_6})
    
    index = nw.new_node(Nodes.Index)
    
    map_range_12 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': index, 1: 27.8600})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': set_spline_cyclic, 'Selection': map_range_12.outputs["Result"]})
    
    curve_circle_7 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': 0.0015})
    
    curve_to_mesh_7 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': separate_geometry.outputs["Selection"], 'Profile Curve': curve_circle_7.outputs["Curve"], 'Fill Caps': True})
    
    set_material_10 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_7, 'Material': surface.shaderfunc_to_material(shader_chrome)})
    
    curve_line_8 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': (0.0000, 0.0000, -0.0250), 'End': (0.0000, 0.0000, -0.0350)})
    
    resample_curve_4 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_8, 'Count': 4})
    
    curve_parameter_9 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_9 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter_9.outputs["Factor"]})
    node_utils.assign_curve(float_curve_9.mapping.curves[0], [(0.0000, 0.8142), (0.2238, 1.0000), (0.7485, 0.9958), (1.0000, 1.0000)])
    
    set_curve_radius_4 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve_4, 'Radius': float_curve_9})
    
    ball_base = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 12, 'Radius': 0.0110}, label='ball base')
    
    curve_to_mesh_8 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_4, 'Profile Curve': ball_base.outputs["Curve"], 'Fill Caps': True})
    
    set_material_11 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_8, 'Material': surface.shaderfunc_to_material(shader_chrome)})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_11})
    
    ico_sphere = nw.new_node(Nodes.MeshIcoSphere, input_kwargs={'Radius': 0.0350, 'Subdivisions': 3})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': ico_sphere.outputs["Mesh"], 'Name': 'UVMap', 3: ico_sphere.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute_2, 'Translation': (0.0000, 0.0000, -0.0660)})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': transform_3, 'Material': surface.shaderfunc_to_material(shader_balls)})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material_4})
    
    curve_line_10 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': (0.0000, 0.0000, -0.0050), 'End': (0.0000, 0.0000, -0.0350)})
    
    curve_circle_10 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 6, 'Radius': 0.0010})
    
    curve_to_mesh_10 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_line_10, 'Profile Curve': curve_circle_10.outputs["Curve"], 'Fill Caps': True})
    
    set_material_13 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_10, 'Material': surface.shaderfunc_to_material(shader_chrome)})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_13})
    
    join_geometry_7 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [set_material_10, reroute_45, set_shade_smooth, reroute_44]})
    
    align_euler_to_vector_3 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': curve_to_points_3.outputs["Rotation"]},
        attrs={'axis': 'Z'})
    
    random_value_7 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.2400, -0.2400, 0.0000), 1: (0.2300, 0.2300, 0.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    rotate_euler = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': align_euler_to_vector_3, 'Rotate By': random_value_7.outputs["Value"]})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Xmas Balls Scale"], 'Y': group_input.outputs["Xmas Balls Scale"], 'Z': group_input.outputs["Xmas Balls Scale"]})
    
    instance_on_points_3 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points_3.outputs["Points"], 'Selection': reroute_58, 'Instance': join_geometry_7, 'Rotation': rotate_euler, 'Scale': combine_xyz_3})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["LIghts Around"]})
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Rotations': reroute_38, 'Start Radius': reroute_36, 'End Radius': 0.1500, 'Height': reroute_35})
    
    trim_curve_3 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': spiral, 2: group_input.outputs["Trim Lights"]})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    geometry_proximity = nw.new_node(Nodes.Proximity, input_kwargs={'Target': reroute_25}, attrs={'target_element': 'POINTS'})
    
    map_range_6 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': geometry_proximity.outputs["Distance"], 1: 0.1700, 2: 0.0000},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_6.outputs["Result"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': geometry_proximity.outputs["Position"]})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': trim_curve_3, 'Selection': reroute_17, 'Position': reroute_14})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': geometry_proximity.outputs["Distance"]})
    colorramp.color_ramp.interpolation = "B_SPLINE"
    colorramp.color_ramp.elements[0].position = 0.3576
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.9636
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_6 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: (0.0000, 0.0000, -2.2100), 1: colorramp.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_1, 1: multiply_6.outputs["Vector"]})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position, 'Position': add_3.outputs["Vector"]})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position_1, 'Length': 0.1800}, attrs={'mode': 'LENGTH'})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': resample_curve_1}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 3, 'Radius': 0.0035})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_handle_type, 'Profile Curve': curve_circle_2.outputs["Curve"]})
    
    set_material_5 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_2, 'Material': surface.shaderfunc_to_material(shader_cords)})
    
    curve_to_points_5 = nw.new_node(Nodes.CurveToPoints,
        input_kwargs={'Curve': set_handle_type, 'Count': group_input.outputs["Lights Density"]})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_points_5.outputs["Points"]})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_50})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    curve_line_6 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': (0.0000, 0.0000, -0.0100), 'End': (0.0000, 0.0000, 0.0150)})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_points_5.outputs["Rotation"]})
    
    align_euler_to_vector_1 = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Rotation': reroute_47, 'Factor': 0.9056}, attrs={'axis': 'Z'})
    
    random_value_9 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.2500, -0.2500, -0.2500), 1: (0.2500, 0.2500, 0.2500)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    rotate_euler_7 = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': align_euler_to_vector_1, 'Rotate By': random_value_9.outputs["Value"]})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': rotate_euler_7})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Lights Scale"], 'Y': group_input.outputs["Lights Scale"], 'Z': group_input.outputs["Lights Scale"]})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_2})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    instance_on_points_6 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_24, 'Selection': reroute_22, 'Instance': curve_line_6, 'Rotation': reroute_48, 'Scale': reroute_41})
    
    curve_circle_5 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 12, 'Radius': 0.0120})
    
    curve_to_mesh_5 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': instance_on_points_6, 'Profile Curve': curve_circle_5.outputs["Curve"], 'Fill Caps': True})
    
    set_material_6 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_5, 'Material': surface.shaderfunc_to_material(shader_cords)})
    
    curve_line_5 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 0.0800)})
    
    instance_on_points_5 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_50, 'Selection': reroute_22, 'Instance': curve_line_5, 'Rotation': reroute_48, 'Scale': reroute_41})
    
    curve_circle_4 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 12, 'Radius': 0.0100})
    
    curve_circle_9 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 12, 'Radius': 0.0060})
    
    join_geometry_8 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [curve_circle_4.outputs["Curve"], curve_circle_9.outputs["Curve"]]})
    
    curve_to_mesh_4 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': instance_on_points_5, 'Profile Curve': join_geometry_8})
    
    set_material_7 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_4, 'Material': surface.shaderfunc_to_material(shader_lights)})
    
    join_geometry_6 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_6, set_material_7]})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_6})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_5})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    curve_line_7 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 0.0400)})
    
    resample_curve_3 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_7})
    
    instance_on_points_7 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_23, 'Selection': endpoint_selection, 'Instance': resample_curve_3})
    
    curve_parameter_8 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_8 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter_8.outputs["Factor"]})
    node_utils.assign_curve(float_curve_8.mapping.curves[0], [(0.0000, 0.7583), (0.2727, 0.9292), (1.0000, 0.1300)])
    
    map_range_9 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': float_curve_8, 4: 1.3300})
    
    set_curve_radius_3 = nw.new_node(Nodes.SetCurveRadius,
        input_kwargs={'Curve': instance_on_points_7, 'Radius': map_range_9.outputs["Result"]})
    
    curve_circle_6 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 12, 'Radius': 0.0100})
    
    curve_to_mesh_6 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_3, 'Profile Curve': curve_circle_6.outputs["Curve"], 'Fill Caps': True})
    
    set_material_8 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_6, 'Material': surface.shaderfunc_to_material(shader_l_ight_bulb)})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Fluffy Ribbon Around"]})
    
    spiral_2 = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Rotations': reroute_39, 'Start Radius': reroute_36, 'End Radius': 0.1500, 'Height': reroute_35})
    
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': spiral_2, 'Rotation': (0.0000, 0.0000, 2.9234)})
    
    trim_curve_6 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': transform_5, 2: group_input.outputs["Trim Fluffy Ribbon"]})
    
    geometry_proximity_2 = nw.new_node(Nodes.Proximity, input_kwargs={'Target': reroute_33}, attrs={'target_element': 'POINTS'})
    
    map_range_10 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': geometry_proximity_2.outputs["Distance"], 1: 0.1700, 2: 0.0000},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_10.outputs["Result"]})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': geometry_proximity_2.outputs["Position"]})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': trim_curve_6, 'Selection': reroute_28, 'Position': reroute_26})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': geometry_proximity_2.outputs["Distance"]})
    colorramp_2.color_ramp.interpolation = "B_SPLINE"
    colorramp_2.color_ramp.elements[0].position = 0.3576
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.9636
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_7 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: (0.0000, 0.0000, -1.8400), 1: colorramp_2.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_3, 1: multiply_7.outputs["Vector"]})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_4, 'Position': add_4.outputs["Vector"]})
    
    resample_curve_5 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position_5, 'Length': 0.1800}, attrs={'mode': 'LENGTH'})
    
    set_spline_type_2 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': resample_curve_5}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type_2 = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type_2})
    
    curve_parameter_10 = nw.new_node(Nodes.SplineParameter)
    
    map_range_11 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': curve_parameter_10.outputs["Factor"], 4: 106.4000})
    
    set_curve_tilt_1 = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': set_handle_type_2, 'Tilt': map_range_11.outputs["Result"]})
    
    curve_line_9 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 0.0100)})
    
    curve_to_mesh_9 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_curve_tilt_1, 'Profile Curve': curve_line_9})
    
    curve_to_points_6 = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': set_curve_tilt_1, 'Count': 1000})
    
    grid_1 = nw.new_node(Nodes.MeshGrid, input_kwargs={'Size X': 0.0150, 'Size Y': 0.0800, 'Vertices X': 2, 'Vertices Y': 8})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid_1.outputs["Mesh"], 'Name': 'uv_map', 3: grid_1.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 214.5000})
    
    multiply_8 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Fac"], 1: (0.0000, 0.0000, 0.0300)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_6 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute, 'Offset': multiply_8.outputs["Vector"]})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_position_6})
    
    random_value_8 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.5100, -0.5100, -77.2000), 1: (0.3300, 0.3300, 70.8000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    rotate_euler_3 = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': curve_to_points_6.outputs["Rotation"], 'Rotate By': random_value_8.outputs["Value"]},
        attrs={'space': 'LOCAL'})
    
    instance_on_points_8 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points_6.outputs["Points"], 'Instance': set_shade_smooth_1, 'Rotation': rotate_euler_3})
    
    join_geometry_9 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_to_mesh_9, instance_on_points_8]})
    
    set_material_9 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_9, 'Material': surface.shaderfunc_to_material(shader_ribbon_fluffy)})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    curve_line_11 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 0.0200)})
    
    resample_curve_6 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_11})
    
    curve_parameter_11 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_10 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter_11.outputs["Factor"]})
    node_utils.assign_curve(float_curve_10.mapping.curves[0], [(0.0000, 1.0000), (0.5758, 0.7417), (1.0000, 0.0000)])
    
    set_curve_radius_5 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve_6, 'Radius': float_curve_10})
    
    star = nw.new_node('GeometryNodeCurveStar', input_kwargs={'Inner Radius': 1.4300, 'Outer Radius': 1.7100})
    
    transform_8 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': star.outputs["Curve"], 'Scale': (0.0025, 0.0025, 0.0025)})
    
    curve_to_mesh_11 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_curve_radius_5, 'Profile Curve': transform_8})
    
    instance_on_points_9 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_23, 'Selection': endpoint_selection_1, 'Instance': curve_to_mesh_11})
    
    set_material_12 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points_9, 'Material': surface.shaderfunc_to_material(shader_l_ight_bulb_light)})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_line})
    
    index_1 = nw.new_node(Nodes.Index)
    
    capture_attribute_5 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': reroute_49, 2: index_1})
    
    curve_to_points_7 = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': capture_attribute_5.outputs["Geometry"], 'Count': 2})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={0: capture_attribute_5.outputs[2], 1: 1.0000}, attrs={'operation': 'EQUAL'})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': equal})
    
    star_1 = nw.new_node('GeometryNodeCurveStar', input_kwargs={'Points': 5})
    
    transform_7 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': star_1.outputs["Curve"], 'Translation': (0.0000, 0.0000, 0.2500), 'Rotation': (1.5708, -0.3166, 0.0000), 'Scale': (0.1000, 0.1000, 0.1000)})
    
    instance_on_points_10 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points_7.outputs["Points"], 'Selection': reroute_53, 'Instance': transform_7, 'Scale': (0.8000, 0.8000, 0.8000)})
    
    curve_to_points_8 = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': instance_on_points_10, 'Count': 25})
    
    curve_line_12 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.1000, 0.0000)})
    
    instance_on_points_11 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points_8.outputs["Points"], 'Instance': curve_line_12, 'Rotation': curve_to_points_8.outputs["Rotation"]})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances,
        input_kwargs={'Geometry': instance_on_points_11},
        attrs={'legacy_behavior': True})
    
    endpoint_selection_2 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    add_5 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Tree Heigth"], 1: 0.2000})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': -0.0400, 'Z': add_5})
    
    set_position_7 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances_1, 'Selection': endpoint_selection_2, 'Position': combine_xyz_5})
    
    reroute_56 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_points_7.outputs["Points"]})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': equal})
    
    spiral_3 = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Rotations': 6.5000, 'Start Radius': 0.0200, 'End Radius': 0.0000, 'Height': 0.1200})
    
    instance_on_points_12 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_56, 'Selection': reroute_54, 'Instance': spiral_3})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_10})
    
    set_curve_radius_6 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_52, 'Radius': 2.0400})
    
    reroute_55 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_curve_radius_6})
    
    join_geometry_10 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_7, instance_on_points_12, reroute_55]})
    
    curve_circle_11 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 6, 'Radius': 0.0020})
    
    curve_to_mesh_12 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': join_geometry_10, 'Profile Curve': curve_circle_11.outputs["Curve"]})
    
    set_material_14 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_12, 'Material': surface.shaderfunc_to_material(shader_chrome)})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [set_material_1, reroute_15, set_material_3, instance_on_points_3, set_material_5, reroute_34, set_material_8, set_material_9, set_material_12, set_material_14]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_3}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_tree, selection=selection)
    surface.add_material(obj, shader_needle, selection=selection)
    surface.add_material(obj, shader_ribbon, selection=selection)
    surface.add_material(obj, shader_balls, selection=selection)
    surface.add_material(obj, shader_cords, selection=selection)
    surface.add_material(obj, shader_lights, selection=selection)
    surface.add_material(obj, shader_l_ight_bulb, selection=selection)
    surface.add_material(obj, shader_l_ight_bulb_light, selection=selection)
    surface.add_material(obj, shader_chrome, selection=selection)
    surface.add_material(obj, shader_ribbon_fluffy, selection=selection)
apply(bpy.context.active_object)
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_wood(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'truv'})
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': attribute.outputs["Vector"], 'Scale': (0.4000, 19.5600, 1.0000)})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mapping})
    
    base_color = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Base Color',
        attrs={'image': bpy.data.images['Bark001_diffuse.png']})
    
    roughness = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Roughness',
        attrs={'image': bpy.data.images['Bark001_roughness.png']})
    
    normal = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Normal',
        attrs={'image': bpy.data.images['Bark001_normal.png']})
    
    normal_map = nw.new_node(Nodes.ShaderNodeNormalMap, input_kwargs={'Strength': 1.0500, 'Color': normal.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': base_color.outputs["Color"], 'Roughness': roughness.outputs["Color"], 'Normal': normal_map})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_leaf(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'plantuv'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': attribute.outputs["Vector"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"], 1: 10.8000}, attrs={'operation': 'MULTIPLY'})
    
    fract = nw.new_node(Nodes.Math, input_kwargs={0: multiply}, attrs={'operation': 'FRACT'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': fract})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0188, 0.0468, 0.0189, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5136
    colorramp.color_ramp.elements[1].color = [0.0107, 0.0185, 0.0102, 1.0000]
    colorramp.color_ramp.elements[2].position = 1.0000
    colorramp.color_ramp.elements[2].color = [0.0268, 0.0751, 0.0276, 1.0000]
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.8304, 'Distance': 0.7900, 'Height': fract})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Roughness': 1.0000, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'seed', 0.9000),
            ('NodeSocketFloat', 'Hight', 0.0000),
            ('NodeSocketFloat', 'len', 0.0000),
            ('NodeSocketFloat', 'angle', 4.8900),
            ('NodeSocketFloat', 'Hight_2', 0.6500),
            ('NodeSocketFloatFactor', 'Arc', 1.0000),
            ('NodeSocketFloat', 'Gravity', 0.6500),
            ('NodeSocketFloat', 'len 2', 0.4500),
            ('NodeSocketFloat', 'LLen Variatioon', 0.2900),
            ('NodeSocketFloat', 'Input', 0.0000)])
    
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Hight"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_10})
    
    resample_curve_3 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': 16})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input.outputs["seed"], 'Scale': 5.9600, 'Roughness': 0.3833},
        attrs={'noise_dimensions': '4D'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: noise_texture.outputs["Color"], 1: (-0.5000, -0.5000, -0.5000)})
    
    spline_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': spline_parameter_2.outputs["Factor"], 'Y': spline_parameter_2.outputs["Factor"]})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add.outputs["Vector"], 1: combine_xyz_2},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply.outputs["Vector"], 1: (0.4300, 0.4300, 0.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': resample_curve_3, 'Offset': multiply_1.outputs["Vector"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_2})
    
    resample_curve_4 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': reroute_3, 'Count': 552})
    
    spline_parameter_3 = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter_3.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 1.0000), (1.0000, 0.5125)])
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.7100, 'Seed': 1})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_parameter_3.outputs["Factor"], 1: 23.4400},
        attrs={'operation': 'MULTIPLY'})
    
    fract = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2}, attrs={'operation': 'FRACT'})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': fract})
    colorramp_2.color_ramp.interpolation = "EASE"
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5045
    colorramp_2.color_ramp.elements[1].color = [0.6927, 0.6927, 0.6927, 1.0000]
    colorramp_2.color_ramp.elements[2].position = 1.0000
    colorramp_2.color_ramp.elements[2].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve,
        input_kwargs={'Factor': random_value.outputs[1], 'Value': colorramp_2.outputs["Color"]})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.0000, 0.0000), (0.2591, 0.8063), (1.0000, 1.0000)])
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve, 1: float_curve_2})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: 0.4000}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve_4, 'Radius': multiply_3})
    
    spline_parameter_6 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_3 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': set_curve_radius, 2: spline_parameter_6.outputs["Factor"]})
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': 27, 'Rotations': 1.0000, 'Start Radius': 0.0500, 'End Radius': 0.0500, 'Height': 0.0000})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': spiral})
    
    index_2 = nw.new_node(Nodes.Index)
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: index_2, 1: -1.3000}, attrs={'operation': 'SUBTRACT'})
    
    capture_attribute_2 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_to_mesh_2, 5: subtract},
        attrs={'data_type': 'INT'})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': capture_attribute_2.outputs["Geometry"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': capture_attribute_3.outputs["Geometry"], 'Profile Curve': mesh_to_curve, 'Fill Caps': True})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': capture_attribute_2.outputs[5], 'Y': capture_attribute_3.outputs[2]})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': curve_to_mesh, 'Name': 'truv', 3: combine_xyz_7},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': store_named_attribute_1, 'Material': surface.shaderfunc_to_material(shader_wood)})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': reroute_4, 'Count': 683})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    capture_attribute_4 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': resample_curve, 1: position_3},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    spline_parameter_7 = nw.new_node(Nodes.SplineParameter)
    
    greater_than = nw.new_node(Nodes.Compare,
        input_kwargs={0: spline_parameter_7.outputs["Factor"], 1: group_input.outputs["Hight_2"]})
    
    combine_xyz_11 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["len"]})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_11})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_1, 'Count': 36})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter.outputs["Factor"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp.outputs["Color"], 1: group_input.outputs["angle"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_4, 1: 3.8400})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': add_2})
    
    index = nw.new_node(Nodes.Index)
    
    accumulate_field = nw.new_node(Nodes.AccumulateField, input_kwargs={1: index})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: accumulate_field.outputs[1], 1: 2.2100}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': combine_xyz_1, 'Z': multiply_5})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': capture_attribute_4.outputs["Geometry"], 'Selection': greater_than, 'Instance': resample_curve_1, 'Rotation': combine_xyz})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': reroute_1})
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': realize_instances, 'Count': 40})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter_1.outputs["Factor"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    float_curve_3 = nw.new_node(Nodes.FloatCurve,
        input_kwargs={'Factor': group_input.outputs["Arc"], 'Value': colorramp_1.outputs["Color"]})
    node_utils.assign_curve(float_curve_3.mapping.curves[0], [(0.0000, 0.0000), (0.3545, 0.7688), (1.0000, 1.0000)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': float_curve_3})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Gravity"]})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: reroute_6}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_6})
    
    multiply_7 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_2, 1: combine_xyz_9}, attrs={'operation': 'MULTIPLY'})
    
    normal_2 = nw.new_node(Nodes.InputNormal)
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: group_input.outputs["len 2"]})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: add_3}, attrs={'operation': 'MULTIPLY'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': position_2, 'Center': multiply_7.outputs["Vector"], 'Axis': normal_2, 'Angle': multiply_8},
        attrs={'invert': True})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': resample_curve_2, 'Position': vector_rotate})
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={2: group_input.outputs["LLen Variatioon"]})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': set_position, 3: random_value_2.outputs[1]})
    
    spline_parameter_5 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': trim_curve, 2: spline_parameter_5.outputs["Factor"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs["Geometry"]})
    
    spline_parameter_4 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter_4.outputs["Factor"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 1.0000), (0.7136, 0.7250), (1.0000, 0.1313)])
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_5, 'Radius': float_curve_1})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Input"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_7})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_7})
    
    multiply_9 = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz_3}, attrs={'operation': 'MULTIPLY'})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_4, 'End': multiply_9.outputs["Vector"]})
    
    resample_curve_5 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_2, 'Count': 3})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection)
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': resample_curve_5, 'Selection': endpoint_selection, 'Offset': (0.0000, -0.0100, 0.0000)})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': set_position_1}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type})
    
    resample_curve_6 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_handle_type, 'Count': 3})
    
    index_3 = nw.new_node(Nodes.Index)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': resample_curve_6, 5: index_3},
        attrs={'data_type': 'INT'})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': capture_attribute.outputs["Geometry"]})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': capture_attribute_1.outputs[2]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Name': 'plantuv', 3: combine_xyz_6},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': store_named_attribute, 'Material': surface.shaderfunc_to_material(shader_leaf)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_1, set_material]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_leaf, selection=selection)
    surface.add_material(obj, shader_wood, selection=selection)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_flower_stem(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry = nw.new_node(Nodes.NewGeometry)
    
    normal_modifier = nw.new_node(Nodes.VectorMath, input_kwargs={0: geometry.outputs["Normal"]}, label='Normal Modifier')
    
    diffuse_bsdf = nw.new_node(Nodes.DiffuseBSDF, input_kwargs={'Normal': normal_modifier.outputs["Vector"]})
    
    shader_to_rgb = nw.new_node('ShaderNodeShaderToRGB', input_kwargs={'Shader': diffuse_bsdf})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': shader_to_rgb.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0727
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.1091
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    invert = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: colorramp.outputs["Color"]},
        label='Invert',
        attrs={'operation': 'SUBTRACT'})
    
    rgb = nw.new_node(Nodes.RGB)
    rgb.outputs[0].default_value = (0.1529, 0.3712, 0.0802, 1.0000)
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': rgb})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp.outputs["Color"], 7: reroute},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.4417, 6: reroute, 7: (0.0108, 0.0104, 0.6921, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: invert, 6: mix.outputs[2], 7: mix_3.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'LIGHTEN'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_1.outputs[2]}, attrs={'is_active_output': True})

def shader_flower_disk(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Location': (0.0100, 0.0000, 0.0000), 'Rotation': (0.0000, 1.5708, 0.0000)})
    
    gradient_texture = nw.new_node(Nodes.GradientTexture, input_kwargs={'Vector': mapping})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': gradient_texture.outputs["Fac"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.0150
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    geometry_1 = nw.new_node(Nodes.NewGeometry)
    
    normal_modifier = nw.new_node(Nodes.VectorMath, input_kwargs={0: geometry_1.outputs["Normal"]}, label='Normal Modifier')
    
    diffuse_bsdf_1 = nw.new_node(Nodes.DiffuseBSDF, input_kwargs={'Normal': normal_modifier.outputs["Vector"]})
    
    shader_to_rgb_1 = nw.new_node('ShaderNodeShaderToRGB', input_kwargs={'Shader': diffuse_bsdf_1})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': shader_to_rgb_1.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.0727
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.1091
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    invert = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: colorramp_2.outputs["Color"]},
        label='Invert',
        attrs={'operation': 'SUBTRACT'})
    
    rgb_1 = nw.new_node(Nodes.RGB)
    rgb_1.outputs[0].default_value = (0.1529, 0.3712, 0.0802, 1.0000)
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': rgb_1})
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_2.outputs["Color"], 7: reroute_1},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.4417, 6: reroute_1, 7: (0.0108, 0.0104, 0.6921, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    mix_6 = nw.new_node(Nodes.Mix,
        input_kwargs={0: invert, 6: mix_5.outputs[2], 7: mix_7.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'LIGHTEN'})
    
    geometry = nw.new_node(Nodes.NewGeometry)
    
    normal = nw.new_node('ShaderNodeNormal')
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0000, 6: geometry.outputs["Normal"], 7: normal.outputs["Dot"]},
        attrs={'data_type': 'RGBA'})
    
    normal_modifier_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: mix_2.outputs[2]}, label='Normal Modifier')
    
    diffuse_bsdf = nw.new_node(Nodes.DiffuseBSDF, input_kwargs={'Normal': normal_modifier_1.outputs["Vector"]})
    
    shader_to_rgb = nw.new_node('ShaderNodeShaderToRGB', input_kwargs={'Shader': diffuse_bsdf})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': shader_to_rgb.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.0727
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.1091
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    invert_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: colorramp_1.outputs["Color"]},
        label='Invert',
        attrs={'operation': 'SUBTRACT'})
    
    rgb = nw.new_node(Nodes.RGB)
    rgb.outputs[0].default_value = (0.6584, 0.3095, 0.0545, 1.0000)
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': rgb})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_1.outputs["Color"], 7: reroute},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.5583, 6: reroute, 7: (0.0000, 0.0714, 0.4480, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: invert_1, 6: mix_3.outputs[2], 7: mix_4.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'LIGHTEN'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp.outputs["Color"], 6: mix_6.outputs[2], 7: mix_1.outputs[2]},
        attrs={'data_type': 'RGBA'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix.outputs[2]}, attrs={'is_active_output': True})

def shader_flower_petal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry = nw.new_node(Nodes.NewGeometry)
    
    normal = nw.new_node('ShaderNodeNormal')
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0000, 6: geometry.outputs["Normal"], 7: normal.outputs["Dot"]},
        attrs={'data_type': 'RGBA'})
    
    normal_modifier = nw.new_node(Nodes.VectorMath, input_kwargs={0: mix_2.outputs[2]}, label='Normal Modifier')
    
    diffuse_bsdf = nw.new_node(Nodes.DiffuseBSDF, input_kwargs={'Normal': normal_modifier.outputs["Vector"]})
    
    shader_to_rgb = nw.new_node('ShaderNodeShaderToRGB', input_kwargs={'Shader': diffuse_bsdf})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': shader_to_rgb.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0727
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.1091
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    invert = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: colorramp.outputs["Color"]},
        label='Invert',
        attrs={'operation': 'SUBTRACT'})
    
    rgb = nw.new_node(Nodes.RGB)
    rgb.outputs[0].default_value = (0.8469, 0.8469, 0.8469, 1.0000)
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': rgb})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp.outputs["Color"], 7: reroute},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: reroute, 7: (0.2285, 0.2631, 0.3185, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'LINEAR_LIGHT'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: invert, 6: mix.outputs[2], 7: mix_3.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'LIGHTEN'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_1.outputs[2]}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_5 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketMaterial', '---------- PETALS ----------', None),
            ('NodeSocketFloat', 'Petal Length', 3.0000),
            ('NodeSocketFloat', 'Width', 0.3000),
            ('NodeSocketFloat', 'Shape', 0.0000),
            ('NodeSocketFloat', 'Bend', -0.5000),
            ('NodeSocketInt', 'Number ', 16),
            ('NodeSocketFloat', 'Orient Random', 1.0000),
            ('NodeSocketFloat', 'Closing', -5.0000),
            ('NodeSocketBool', 'Wind Petals ?', False),
            ('NodeSocketFloat', 'Wind Speed', 1.5000),
            ('NodeSocketFloat', 'Wind Scale', 2.0000),
            ('NodeSocketFloat', 'Wind Influence', 2.0000),
            ('NodeSocketMaterial', '---------- DISK ----------', None),
            ('NodeSocketFloatDistance', 'Radius', 0.1000),
            ('NodeSocketMaterial', '---------- STEM ----------', None),
            ('NodeSocketFloat', 'Length', 1.0000),
            ('NodeSocketFloat', 'Width_1', 0.1500),
            ('NodeSocketFloat', 'Curvature', 0.0000),
            ('NodeSocketInt', 'Length Res', 8),
            ('NodeSocketInt', 'Profile Res', 4),
            ('NodeSocketFloat', 'Scale Flower', 0.0500),
            ('NodeSocketBool', 'Wind Stem _1', False),
            ('NodeSocketFloat', 'Wind Speed_1', 2.0000),
            ('NodeSocketFloat', 'Wind Influence_1', 1.0000),
            ('NodeSocketFloat', 'Wind Offset', 0.0000)])
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input_5.outputs["Length"], 1: 10.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_8})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': group_input_5.outputs["Length Res"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    index = nw.new_node(Nodes.Index)
    
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_5.outputs["Curvature"], 1: 100.0000},
        attrs={'operation': 'DIVIDE'})
    
    vector = nw.new_node(Nodes.Vector)
    vector.vector = (0.0100, 0.0000, 0.0000)
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input_5.outputs["Wind Offset"]})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: vector, 1: combine_xyz_9})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': add.outputs["Vector"], 'W': 0.0100, 'Scale': group_input_5.outputs["Wind Speed_1"], 'Detail': 0.0000, 'Roughness': 0.0000},
        attrs={'noise_dimensions': '2D'})
    
    divide_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_5.outputs["Curvature"], 1: 100.0000},
        attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input_5.outputs["Wind Influence_1"]}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide_2, 1: multiply}, attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: divide_2, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: multiply}, attrs={'operation': 'MULTIPLY'})
    
    map_range_4 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': noise_texture_1.outputs["Color"], 3: multiply_1, 4: multiply_3},
        attrs={'clamp': False})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide_1, 1: map_range_4.outputs["Result"]})
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input_5.outputs["Wind Stem _1"], 2: divide_1, 3: add_1},
        attrs={'input_type': 'FLOAT'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: switch_1.outputs["Output"]}, attrs={'operation': 'MULTIPLY'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': position_1, 'Angle': multiply_4},
        attrs={'rotation_type': 'X_AXIS'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': resample_curve_1, 'Position': vector_rotate})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    ico_sphere = nw.new_node(Nodes.MeshIcoSphere, input_kwargs={'Radius': group_input_5.outputs["Radius"], 'Subdivisions': 2})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': ico_sphere.outputs["Mesh"], 'Name': 'UVMap', 3: ico_sphere.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Scale': (1.0000, 1.0000, 0.3500)})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': transform, 'Material': group_input_5.outputs["---------- DISK ----------"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_1})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': group_input_5.outputs["Radius"]})
    
    curve_to_points = nw.new_node(Nodes.CurveToPoints,
        input_kwargs={'Curve': curve_circle.outputs["Curve"], 'Count': group_input_5.outputs["Number "]})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input_5.outputs["Petal Length"]})
    
    divide_3 = nw.new_node(Nodes.Math, input_kwargs={1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide_3, 'Z': group_input_5.outputs["Bend"]})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_5.outputs["Shape"], 1: 0.1500}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_11 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_5})
    
    quadratic_bezier = nw.new_node(Nodes.QuadraticBezier,
        input_kwargs={'Resolution': 4, 'Start': combine_xyz_3, 'Middle': combine_xyz_2, 'End': combine_xyz_11})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0136, 0.5688), (0.2864, 0.9312), (0.7273, 0.9312), (1.0000, 0.4937)])
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': quadratic_bezier, 'Radius': float_curve})
    
    multiply_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_5.outputs["Width"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_6})
    
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': group_input_5.outputs["Shape"]})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input_5.outputs["Width"]})
    
    quadratic_bezier_1 = nw.new_node(Nodes.QuadraticBezier,
        input_kwargs={'Resolution': 3, 'Start': combine_xyz, 'Middle': combine_xyz_10, 'End': combine_xyz_1})
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': quadratic_bezier_1, 'Count': 3})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_curve_radius, 'Profile Curve': resample_curve_2})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': curve_to_mesh})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': subdivision_surface, 'Material': group_input_5.outputs["---------- PETALS ----------"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    rotate_euler = nw.new_node(Nodes.RotateEuler, input_kwargs={'Rotation': curve_to_points.outputs["Rotation"]})
    
    multiply_7 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_5.outputs["Orient Random"], 1: -0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_8 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_5.outputs["Closing"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_7, 1: multiply_8})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': -0.2000, 'Y': add_2, 'Z': -0.2000})
    
    multiply_9 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_5.outputs["Orient Random"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_9, 1: multiply_8})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 0.2000, 'Y': add_3, 'Z': 0.2000})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: combine_xyz_6, 1: combine_xyz_7, 2: -0.2000, 3: 0.2000},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    add_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: rotate_euler, 1: random_value.outputs["Value"]})
    
    scale = nw.new_node(Nodes.Value, label='Scale ')
    scale.outputs[0].default_value = 0.1500
    
    add_5 = nw.new_node(Nodes.Math, input_kwargs={0: scale, 1: 0.0500})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={2: scale, 3: add_5})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points.outputs["Points"], 'Instance': reroute_5, 'Rotation': add_4.outputs["Vector"], 'Scale': random_value_1.outputs[1]})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': instance_on_points, 'Rotation': (1.5708, 0.0000, 0.0000)})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': rotate_instances})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    length = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_2}, attrs={'operation': 'LENGTH'})
    
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: length.outputs["Value"], 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 0.0100})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input_5.outputs["Wind Speed"]})
    
    multiply_11 = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz_4, 1: combine_xyz_5}, attrs={'operation': 'MULTIPLY'})
    
    add_6 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 1: multiply_11.outputs["Vector"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': add_6.outputs["Vector"], 'W': 0.0200, 'Scale': group_input_5.outputs["Wind Scale"], 'Detail': 0.0000, 'Roughness': 0.0000})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_12 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: group_input_5.outputs["Wind Influence"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_13 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_10, 1: multiply_12.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances, 'Offset': multiply_13.outputs["Vector"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_1})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_5.outputs["Wind Petals ?"], 14: rotate_instances, 15: reroute_11})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_1, switch.outputs[6]]})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent}, attrs={'axis': 'Z'})
    
    multiply_add = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_5.outputs["Scale Flower"], 1: 0.0100, 2: 0.0500},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute, 'Selection': endpoint_selection_1, 'Instance': join_geometry, 'Rotation': align_euler_to_vector, 'Scale': multiply_add})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter_1.outputs["Factor"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.5000, 0.5000, 0.5000, 1.0000]
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_7, 'Radius': colorramp.outputs["Color"]})
    
    divide_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_5.outputs["Width_1"], 1: 100.0000},
        attrs={'operation': 'DIVIDE'})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_5.outputs["Profile Res"], 'Radius': divide_4})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': curve_circle_1.outputs["Curve"], 'Fill Caps': True})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': group_input_5.outputs["---------- STEM ----------"]})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [instance_on_points_1, set_material_2]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry_1})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_shade_smooth}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_flower_petal, selection=selection)
    surface.add_material(obj, shader_flower_disk, selection=selection)
    surface.add_material(obj, shader_flower_stem, selection=selection)
apply(bpy.context.active_object)
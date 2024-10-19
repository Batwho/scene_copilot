import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_royal-_anime_hair', singleton=False, type='ShaderNodeTree')
def nodegroup_royal_anime_hair(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    diffuse_bsdf = nw.new_node(Nodes.DiffuseBSDF)
    
    shader_to_rgb = nw.new_node('ShaderNodeShaderToRGB', input_kwargs={'Shader': diffuse_bsdf})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': shader_to_rgb.outputs["Color"]})
    colorramp_3.color_ramp.interpolation = "CONSTANT"
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.2180, 0.2180, 0.2180, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.4200
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'OurUV'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': attribute.outputs["Vector"]})
    
    animehairshader = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Position(Offset)', 0.5000),
            ('NodeSocketFloatFactor', 'Spread', 0.5917),
            ('NodeSocketFloat', 'BlotchSize', 24.8000),
            ('NodeSocketFloat', 'Randomize', 0.0000),
            ('NodeSocketFloat', 'Strength', 4.5100),
            ('NodeSocketFloat', 'Stretch', -0.6100),
            ('NodeSocketFloat', 'LowerLimit', 0.0000),
            ('NodeSocketFloat', 'UpperLimit', 0.6500),
            ('NodeSocketFloat', 'Shadow(AREA)', 0.0000)])
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': separate_xyz.outputs["X"], 'Scale': animehairshader.outputs["BlotchSize"], 'Detail': 0.8000, 'Roughness': 0.3000, 'Distortion': animehairshader.outputs["Randomize"]})
    
    bright_contrast_1 = nw.new_node('ShaderNodeBrightContrast',
        input_kwargs={'Color': noise_texture.outputs["Fac"], 'Bright': 0.1500, 'Contrast': animehairshader.outputs["Strength"]})
    
    bright_contrast = nw.new_node('ShaderNodeBrightContrast',
        input_kwargs={'Color': noise_texture.outputs["Fac"], 'Bright': -0.1500, 'Contrast': animehairshader.outputs["Stretch"]})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: bright_contrast, 1: animehairshader.outputs["Position(Offset)"], 2: 0.0000},
        attrs={'operation': 'SUBTRACT'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: separate_xyz.outputs["Y"], 2: 0.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': add})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.1100
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.9800
    colorramp.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    specular_1 = nw.new_node('ShaderNodeEeveeSpecular',
        input_kwargs={'Base Color': (0.0000, 0.0000, 0.0000, 1.0000), 'Specular': (1.0000, 1.0000, 1.0000, 1.0000), 'Roughness': animehairshader.outputs["Spread"], 'Ambient Occlusion': 1.0000})
    
    shader_to_rgb_2 = nw.new_node('ShaderNodeShaderToRGB', input_kwargs={'Shader': specular_1})
    
    separate_rgb_1 = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': shader_to_rgb_2.outputs["Color"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp.outputs["Color"], 1: separate_rgb_1.outputs["Red"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: bright_contrast_1, 7: multiply},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix.outputs[2]})
    colorramp_2.color_ramp.interpolation = "CONSTANT"
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.1894, 0.0426, 0.0087, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.1227
    colorramp_2.color_ramp.elements[1].color = [0.3169, 0.0721, 0.0121, 1.0000]
    colorramp_2.color_ramp.elements[2].position = 0.4773
    colorramp_2.color_ramp.elements[2].color = [1.0000, 0.6535, 0.5094, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_3.outputs["Color"], 7: colorramp_2.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Color': mix_1.outputs[2]}, attrs={'is_active_output': True})

def shader_anime(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    ambient_occlusion = nw.new_node(Nodes.AmbientOcclusion)
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': ambient_occlusion.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.4364
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.6591
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'OurUV'})
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': attribute.outputs["Vector"], 'Scale': (10.2000, 1.0000, 1.0000)},
        attrs={'vector_type': 'VECTOR'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 2.2800, 'Detail': 0.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0257, 0.0069, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.2830
    colorramp.color_ramp.elements[1].color = [0.0084, 0.0031, 0.0009, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.3773
    colorramp.color_ramp.elements[2].color = [0.0999, 0.0462, 0.0168, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.4477
    colorramp.color_ramp.elements[3].color = [1.0000, 0.3658, 0.0837, 1.0000]
    colorramp.color_ramp.elements[4].position = 0.5409
    colorramp.color_ramp.elements[4].color = [0.1475, 0.0721, 0.0320, 1.0000]
    colorramp.color_ramp.elements[5].position = 0.6222
    colorramp.color_ramp.elements[5].color = [1.0000, 0.3405, 0.0957, 1.0000]
    colorramp.color_ramp.elements[6].position = 0.6909
    colorramp.color_ramp.elements[6].color = [0.7154, 0.2992, 0.1272, 1.0000]
    
    hue_saturation_value_1 = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Saturation': 0.7000, 'Value': 0.1800, 'Color': colorramp.outputs["Color"]})
    
    bright_contrast_1 = nw.new_node('ShaderNodeBrightContrast',
        input_kwargs={'Color': hue_saturation_value_1, 'Bright': 0.0100, 'Contrast': 0.0800})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_1.outputs["Color"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: bright_contrast_1},
        attrs={'data_type': 'RGBA'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': mix.outputs[2], 'Roughness': 0.8273})
    
    group = nw.new_node(nodegroup_royal_anime_hair().name,
        input_kwargs={'Position(Offset)': 0.4000, 'BlotchSize': 26.0600, 'Strength': -1.3000, 'Stretch': 1.0000, 'LowerLimit': 0.1100, 'UpperLimit': 0.9800, 'Shadow(AREA)': 0.4200})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Saturation': 0.8500, 'Value': 0.2400, 'Color': group})
    
    bright_contrast = nw.new_node('ShaderNodeBrightContrast',
        input_kwargs={'Color': hue_saturation_value, 'Bright': -0.0400, 'Contrast': -0.0200})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_1.outputs["Color"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: bright_contrast},
        attrs={'data_type': 'RGBA'})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': mix_1.outputs[2], 'Specular': 1.0000})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': bright_contrast})
    
    mix_shader_1 = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': 0.1417, 1: principled_bsdf_1, 2: reroute})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={1: principled_bsdf, 2: mix_shader_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    normal = nw.new_node(Nodes.InputNormal)
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Frequency', 1.0000),
            ('NodeSocketFloat', 'Width', 0.5000),
            ('NodeSocketFloat', 'Thickness', 0.1700),
            ('NodeSocketFloat', 'Offset', 4.7000)])
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: spline_parameter.outputs["Factor"], 1: group_input.outputs["Offset"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Frequency"], 1: 6.2832},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: multiply}, attrs={'operation': 'MULTIPLY'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_1})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: reroute}, attrs={'operation': 'SINE'})
    
    scale = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal, 'Scale': sine}, attrs={'operation': 'SCALE'})
    
    normal_1 = nw.new_node(Nodes.InputNormal)
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    cross_product = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal_1, 1: curve_tangent}, attrs={'operation': 'CROSS_PRODUCT'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    sine_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2}, attrs={'operation': 'SINE'})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: sine_1, 'Scale': group_input.outputs["Width"]},
        attrs={'operation': 'SCALE'})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: cross_product.outputs["Vector"], 'Scale': scale_1.outputs["Vector"]},
        attrs={'operation': 'SCALE'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: scale.outputs["Vector"], 1: scale_2.outputs["Vector"]})
    
    scale_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add_1.outputs["Vector"], 'Scale': group_input.outputs["Thickness"]},
        attrs={'operation': 'SCALE'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': scale_3.outputs["Vector"]}, attrs={'is_active_output': True})

def shader_band(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.2396, 0.0245, 0.0434, 1.0000), 'Roughness': 0.4088})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_hair(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.2298, 0.1097, 0.0829, 1.0000), 'Roughness': 0.1364})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_braidify__performance_update(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketObject', 'Attachment Object', None),#bpy.data.objects['Attachment Object']),
            ('NodeSocketFloat', 'Attachment Object Scale', 0.9000),
            ('NodeSocketFloat', 'Braid Overall Thickness', 1.5840),
            ('NodeSocketFloat', 'Braid Strand Thickness', 1.0000),
            ('NodeSocketFloat', 'Braid Resolution', 0.9860),
            ('NodeSocketFloat', 'Braid Startpoint Scale', 1.8380),
            ('NodeSocketFloat', 'Braid Startpoint Pos', 0.4000),
            ('NodeSocketFloatAngle', 'Braid Overall Rotation', 1.0688),
            ('NodeSocketFloat', 'Frequency', 12.8050),
            ('NodeSocketFloat', 'Width', 1.0220),
            ('NodeSocketFloat', 'Depth', 0.6680),
            ('NodeSocketObject', 'Hairband Object', None),#bpy.data.objects['Hairband']),
            ('NodeSocketFloat', 'Hairband Scale', 0.0200),
            ('NodeSocketVectorTranslation', 'Hairband Position', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVectorEuler', 'Hairband Rotation', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketBool', 'Anime/Realistic Styled', False),
            ('NodeSocketIntUnsigned', 'Anime Resolution', 8),
            ('NodeSocketInt', 'Realistic Hair Amount', 250),
            ('NodeSocketFloat', 'Realistic Hair Strand Thickness', 1.2100),
            ('NodeSocketFloat', 'Realistic Hair Thickness', 0.0270),
            ('NodeSocketFloat', 'Realistic Hair Starting Noise Strength', 0.8100)])
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt,
        input_kwargs={'Curve': group_input.outputs["Geometry"], 'Tilt': group_input.outputs["Braid Overall Rotation"]})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': group_input.outputs["Attachment Object"]},
        attrs={'transform_space': 'RELATIVE'})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': object_info_1.outputs["Geometry"], 'Scale': group_input.outputs["Attachment Object Scale"]})
    
    geometry_proximity = nw.new_node(Nodes.Proximity, input_kwargs={'Target': scale_elements})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_curve_tilt, 'Selection': endpoint_selection_1, 'Position': geometry_proximity.outputs["Position"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_4})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': reroute_4, 1: curve_tangent},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': capture_attribute.outputs["Geometry"]},
        attrs={'mode': 'LENGTH'})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': resample_curve_1, 3: 0.7639})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': group_input.outputs["Hairband Object"]})
    
    transform_geometry = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': object_info.outputs["Geometry"], 'Translation': group_input.outputs["Hairband Position"]})
    
    spline_parameter_4 = nw.new_node(Nodes.SplineParameter)
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_parameter_4.outputs["Length"], 1: group_input.outputs["Hairband Scale"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply, 1: group_input.outputs["Braid Overall Thickness"]},
        attrs={'operation': 'MULTIPLY'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': trim_curve, 'Selection': endpoint_selection, 'Instance': transform_geometry, 'Rotation': group_input.outputs["Hairband Rotation"], 'Scale': multiply_1})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Vector': capture_attribute.outputs["Attribute"]},
        attrs={'axis': 'Z'})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': instance_on_points, 'Rotation': align_euler_to_vector})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': rotate_instances})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_1, 'Material': surface.shaderfunc_to_material(shader_band)})
    
    spline_length = nw.new_node(Nodes.SplineLength)
    
    map_range_4 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': group_input.outputs["Braid Resolution"], 3: 1.0000, 4: 0.0010})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_length.outputs["Length"], 1: map_range_4.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': reroute_4, 'Count': 26, 'Length': multiply_2},
        attrs={'mode': 'LENGTH'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': resample_curve})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Frequency"], 1: group_input.outputs["Braid Overall Thickness"]},
        attrs={'operation': 'DIVIDE'})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter.outputs["Factor"]})
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 1.0000
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: colorramp_3.outputs["Color"]}, attrs={'operation': 'MULTIPLY'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_3})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter_1.outputs["Factor"]})
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.7682
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 1.0000
    colorramp_1.color_ramp.elements[2].color = [0.6566, 0.6566, 0.6566, 1.0000]
    
    multiply_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_4, 1: colorramp_1.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_5})
    
    multiply_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Width"], 1: group_input.outputs["Braid Overall Thickness"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_6})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter_1.outputs["Factor"]})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.3500
    colorramp.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.7227
    colorramp.color_ramp.elements[1].color = [0.3495, 0.3495, 0.3495, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.7932
    colorramp.color_ramp.elements[2].color = [0.1480, 0.1480, 0.1480, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.8409
    colorramp.color_ramp.elements[3].color = [0.6881, 0.6881, 0.6881, 1.0000]
    colorramp.color_ramp.elements[4].position = 0.9500
    colorramp.color_ramp.elements[4].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    spline_length_1 = nw.new_node(Nodes.SplineLength)
    
    multiply_7 = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_length_1.outputs["Length"], 1: 0.0080},
        attrs={'operation': 'MULTIPLY'})
    
    map_range_5 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': multiply_7, 4: group_input.outputs["Width"]})
    
    multiply_8 = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp.outputs["Color"], 1: map_range_5.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_9 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: multiply_8}, attrs={'operation': 'MULTIPLY'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_9})
    
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_4, 1: 3.0000}, attrs={'operation': 'MULTIPLY'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: multiply_10}, attrs={'operation': 'DIVIDE'})
    
    multiply_11 = nw.new_node(Nodes.Math, input_kwargs={0: divide_1, 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    nodegroup = nw.new_node(nodegroup_node_group().name,
        input_kwargs={'Frequency': reroute_2, 'Width': group_input.outputs["Depth"], 'Thickness': reroute, 'Offset': multiply_11})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: (-8.9600, -8.9600, -8.9600), 'Scale': group_input.outputs["Braid Startpoint Scale"]},
        attrs={'operation': 'SCALE'})
    
    spline_parameter_5 = nw.new_node(Nodes.SplineParameter)
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter_5.outputs["Factor"]})
    colorramp_4.color_ramp.elements[0].position = 0.0000
    colorramp_4.color_ramp.elements[0].color = [0.1248, 0.1248, 0.1248, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.1636
    colorramp_4.color_ramp.elements[1].color = [0.7523, 0.7523, 0.7523, 1.0000]
    
    maximum = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_4.outputs["Color"], 1: group_input.outputs["Braid Startpoint Pos"]},
        attrs={'operation': 'MAXIMUM'})
    
    map_range_2 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': maximum, 3: 1.0000, 4: -0.1600})
    
    multiply_12 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale.outputs["Vector"], 1: map_range_2.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_13 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: nodegroup, 1: multiply_12.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_1, 'Offset': multiply_13.outputs["Vector"]})
    
    nodegroup_1 = nw.new_node(nodegroup_node_group().name,
        input_kwargs={'Frequency': reroute_2, 'Width': group_input.outputs["Depth"], 'Thickness': reroute, 'Offset': 0.0000})
    
    multiply_14 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: nodegroup_1, 1: multiply_12.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_1, 'Offset': multiply_14.outputs["Vector"]})
    
    nodegroup_2 = nw.new_node(nodegroup_node_group().name,
        input_kwargs={'Frequency': reroute_2, 'Width': group_input.outputs["Depth"], 'Thickness': reroute, 'Offset': divide_1})
    
    multiply_15 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: nodegroup_2, 1: multiply_12.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_1, 'Offset': multiply_15.outputs["Vector"]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_2, set_position, set_position_1]})
    
    trim_curve_1 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': join_geometry, 2: 0.1212})
    
    endpoint_selection_2 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    set_position_5 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': trim_curve_1, 'Selection': endpoint_selection_2, 'Position': geometry_proximity.outputs["Position"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_5})
    
    set_spline_type_1 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': reroute_3}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type_1 = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type_1})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_length.outputs["Length"], 1: spline_parameter.outputs["Length"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_16 = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: 0.3100}, attrs={'operation': 'MULTIPLY'})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter_1.outputs["Factor"]})
    colorramp_2.color_ramp.interpolation = "B_SPLINE"
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements[0].position = 0.8045
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.8477
    colorramp_2.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[2].position = 0.9318
    colorramp_2.color_ramp.elements[2].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[3].position = 0.9909
    colorramp_2.color_ramp.elements[3].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    multiply_17 = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_parameter_1.outputs["Length"], 1: 0.1400},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_18 = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_2.outputs["Color"], 1: multiply_17},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply_16, 1: multiply_18})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': spline_parameter.outputs["Length"], 1: 4.4900, 2: -1223.0100, 3: add, 4: 2.0000})
    
    multiply_19 = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"], 1: 0.6900}, attrs={'operation': 'MULTIPLY'})
    
    spline_parameter_6 = nw.new_node(Nodes.SplineParameter)
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter_6.outputs["Factor"]})
    colorramp_5.color_ramp.elements.new(0)
    colorramp_5.color_ramp.elements.new(0)
    colorramp_5.color_ramp.elements[0].position = 0.0000
    colorramp_5.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.1636
    colorramp_5.color_ramp.elements[1].color = [0.5684, 0.5684, 0.5684, 1.0000]
    colorramp_5.color_ramp.elements[2].position = 0.8045
    colorramp_5.color_ramp.elements[2].color = [0.5268, 0.5268, 0.5268, 1.0000]
    colorramp_5.color_ramp.elements[3].position = 1.0000
    colorramp_5.color_ramp.elements[3].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    map_range_3 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': colorramp_5.outputs["Color"], 3: 2.3700, 4: 0.0000})
    
    multiply_20 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_19, 1: map_range_3.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_handle_type_1, 'Radius': multiply_20})
    
    spline_parameter_3 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': set_curve_radius, 2: spline_parameter_3.outputs["Factor"]})
    
    braid_strands_thickness = nw.new_node(Nodes.Value, label='Braid Strands Thickness')
    braid_strands_thickness.outputs[0].default_value = 0.0500
    
    multiply_21 = nw.new_node(Nodes.Math,
        input_kwargs={0: braid_strands_thickness, 1: group_input.outputs["Braid Strand Thickness"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_22 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_21, 1: group_input.outputs["Braid Overall Thickness"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_22})
    
    spiral_1 = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': group_input.outputs["Anime Resolution"], 'Rotations': 1.0000, 'Start Radius': reroute_9, 'End Radius': reroute_9, 'Height': 0.0000})
    
    capture_attribute_2 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': spiral_1, 2: spline_parameter_3.outputs["Factor"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': capture_attribute_1.outputs["Geometry"], 'Profile Curve': capture_attribute_2.outputs["Geometry"], 'Fill Caps': True})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_anime)})
    
    duplicate_elements = nw.new_node(Nodes.DuplicateElements,
        input_kwargs={'Geometry': reroute_3, 'Amount': group_input.outputs["Realistic Hair Amount"]},
        attrs={'domain': 'SPLINE'})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={3: 6.2832, 'ID': duplicate_elements.outputs["Duplicate Index"]})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: random_value.outputs[1]}, attrs={'operation': 'SINE'})
    
    scale_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal, 'Scale': sine}, attrs={'operation': 'SCALE'})
    
    normal_1 = nw.new_node(Nodes.InputNormal)
    
    curve_tangent_1 = nw.new_node(Nodes.CurveTangent)
    
    cross_product = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal_1, 1: curve_tangent_1}, attrs={'operation': 'CROSS_PRODUCT'})
    
    cosine = nw.new_node(Nodes.Math, input_kwargs={0: random_value.outputs[1]}, attrs={'operation': 'COSINE'})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: cross_product.outputs["Vector"], 'Scale': cosine},
        attrs={'operation': 'SCALE'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: scale_1.outputs["Vector"], 1: scale_2.outputs["Vector"]})
    
    multiply_23 = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"], 1: 0.0500}, attrs={'operation': 'MULTIPLY'})
    
    scale_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add_1.outputs["Vector"], 'Scale': multiply_23},
        attrs={'operation': 'SCALE'})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={3: group_input.outputs["Realistic Hair Strand Thickness"], 'ID': duplicate_elements.outputs["Duplicate Index"], 'Seed': 21})
    
    scale_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale_3.outputs["Vector"], 'Scale': random_value_1.outputs[1]},
        attrs={'operation': 'SCALE'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': duplicate_elements.outputs["Duplicate Index"], 'Scale': 4.0000, 'Detail': 0.0000, 'Roughness': 0.0000},
        attrs={'noise_dimensions': '4D'})
    
    subtract_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    add_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: subtract_1.outputs["Vector"], 1: (1.0000, 1.0000, 1.0000)})
    
    value_3 = nw.new_node(Nodes.Value)
    value_3.outputs[0].default_value = 1.1500
    
    multiply_24 = nw.new_node(Nodes.VectorMath, input_kwargs={0: add_2.outputs["Vector"], 1: value_3}, attrs={'operation': 'MULTIPLY'})
    
    scale_5 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale_4.outputs["Vector"], 'Scale': multiply_24.outputs["Vector"]},
        attrs={'operation': 'SCALE'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': duplicate_elements.outputs["Geometry"], 'Offset': scale_5.outputs["Vector"]})
    
    spline_parameter_7 = nw.new_node(Nodes.SplineParameter)
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter_7.outputs["Factor"]})
    colorramp_6.color_ramp.elements[0].position = 0.0000
    colorramp_6.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 0.1409
    colorramp_6.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    map_range_6 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': colorramp_6.outputs["Color"], 3: 1.0000, 4: 0.0000})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 30.8000})
    
    subtract_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture_1.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_25 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_6.outputs["Result"], 1: group_input.outputs["Realistic Hair Starting Noise Strength"]},
        attrs={'operation': 'MULTIPLY'})
    
    scale_6 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract_2.outputs["Vector"], 'Scale': multiply_25},
        attrs={'operation': 'SCALE'})
    
    set_position_6 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_3, 'Selection': map_range_6.outputs["Result"], 'Offset': scale_6.outputs["Vector"]})
    
    endpoint_selection_3 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    object_info_2 = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': group_input.outputs["Attachment Object"]},
        attrs={'transform_space': 'RELATIVE'})
    
    geometry_proximity_1 = nw.new_node(Nodes.Proximity, input_kwargs={'Target': object_info_2.outputs["Geometry"]})
    
    set_position_7 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_6, 'Selection': endpoint_selection_3, 'Position': geometry_proximity_1.outputs["Position"]})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': set_position_7}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type})
    
    spline_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter_2.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 1.0000), (0.8063, 0.4519), (0.9261, 0.1538), (1.0000, 0.0000)])
    
    spline_length_2 = nw.new_node(Nodes.SplineLength)
    
    multiply_26 = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_length_2.outputs["Length"], 1: group_input.outputs["Realistic Hair Thickness"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_27 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0040, 1: multiply_26}, attrs={'operation': 'MULTIPLY'})
    
    multiply_28 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0001, 1: multiply_26}, attrs={'operation': 'MULTIPLY'})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': float_curve, 1: 1.0000, 2: 0.0000, 3: multiply_27, 4: multiply_28})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_handle_type, 'Radius': map_range_1.outputs["Result"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_curve_radius_1, 'Material': surface.shaderfunc_to_material(shader_hair)})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["Anime/Realistic Styled"], 14: set_material_2, 15: set_material})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_1, switch.outputs[6]]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': capture_attribute_2.outputs[2], 'Y': capture_attribute_1.outputs[2]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry_2, 'UVs': combine_xyz},
        attrs={'is_active_output': True})

def geometry_surface_deform(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    deform_curves_on_surface = nw.new_node('GeometryNodeDeformCurvesOnSurface', input_kwargs={'Curves': group_input.outputs["Geometry"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': deform_curves_on_surface}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_surface_deform, selection=selection, attributes=[])
    surface.add_geomod(obj, geometry_braidify__performance_update, selection=selection)
    surface.add_material(obj, shader_hair, selection=selection)
apply(bpy.context.active_object)
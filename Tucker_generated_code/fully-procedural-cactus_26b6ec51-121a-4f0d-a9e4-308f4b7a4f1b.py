import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_procedural_rock_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': object_info.outputs["Random"], 'Scale': 7.7000})
    
    color_ramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_3.outputs["Fac"]})
    color_ramp_2.color_ramp.elements[0].position = 0.3727
    color_ramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp_2.color_ramp.elements[1].position = 0.7591
    color_ramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: color_ramp_2.outputs["Color"], 1: 0.8100}, attrs={'operation': 'MULTIPLY'})
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_1, 'Scale': 2000.0000})
    
    color_ramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    color_ramp_1.color_ramp.elements[0].position = 0.3773
    color_ramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp_1.color_ramp.elements[1].position = 1.0000
    color_ramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: color_ramp_1.outputs["Color"], 1: 0.6100}, attrs={'operation': 'MULTIPLY'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_1, 'Scale': 200.0000})
    
    color_ramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    color_ramp.color_ramp.elements[0].position = 0.0000
    color_ramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp.color_ramp.elements[1].position = 1.0000
    color_ramp.color_ramp.elements[1].color = [0.1763, 0.1763, 0.1763, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: multiply_1, 6: color_ramp.outputs["Color"], 7: color_ramp_2.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: multiply, 6: mix.outputs[2], 7: (0.6361, 0.6361, 0.6361, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_1, 'Scale': 2000.0000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.2000, 'Height': noise_texture.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_1.outputs[2], 'Roughness': 0.7227, 'Emission Strength': 0.0000, 'Normal': bump},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS', 'distribution': 'MULTI_GGX'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_procedural_clay(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 31.7000, 'Detail': 3.0000, 'Roughness': 1.0000})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_3.outputs["Fac"]})
    colorramp_4.color_ramp.elements[0].position = 0.0591
    colorramp_4.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.7318
    colorramp_4.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_1, 'Scale': 6.4000, 'Detail': 1.7500})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_3.color_ramp.elements[0].position = 0.2364
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.5000
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Generated"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': 6.5000, 'Detail': 5.4000, 'Roughness': 1.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.5241, 0.1534, 0.0304, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [0.3445, 0.0894, 0.0164, 1.0000]
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Saturation': 0.0000, 'Color': colorramp_1.outputs["Color"]})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_3.outputs["Color"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: hue_saturation_value},
        attrs={'data_type': 'RGBA'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_4.outputs["Color"], 6: (0.3963, 0.3963, 0.3963, 1.0000), 7: mix_1.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    texture_coordinate_2 = nw.new_node(Nodes.TextureCoord)
    
    mapping_2 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_2.outputs["Object"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_2, 'Scale': 15.0000, 'Detail': 7.0000, 'Roughness': 1.0000, 'Distortion': 0.2600})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': colorramp.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 1.0000
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={6: mix_2.outputs[2], 7: colorramp_2.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.0833, 'Height': colorramp.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Roughness': 0.5409, 'Normal': bump},
        attrs={'subsurface_method': 'BURLEY'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_needle(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    ambient_occlusion = nw.new_node(Nodes.AmbientOcclusion)
    
    color_ramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': ambient_occlusion.outputs["Color"]})
    color_ramp_1.color_ramp.elements[0].position = 0.6045
    color_ramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp_1.color_ramp.elements[1].position = 0.7227
    color_ramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    color_ramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': ambient_occlusion.outputs["Color"]})
    color_ramp_2.color_ramp.elements[0].position = 0.1045
    color_ramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    color_ramp_2.color_ramp.elements[1].position = 0.1500
    color_ramp_2.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: color_ramp_1.outputs["Color"], 1: color_ramp_2.outputs["Color"]})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: add, 6: (0.0931, 0.1010, 0.0501, 1.0000), 7: (0.8837, 0.7783, 0.4438, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Roughness': 0.6636, 'Emission Strength': 0.0000},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS', 'distribution': 'MULTI_GGX'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_cactus(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    ambient_occlusion = nw.new_node(Nodes.AmbientOcclusion,
        input_kwargs={'Normal': texture_coordinate.outputs["Normal"]},
        attrs={'samples': 6})
    
    color_ramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': ambient_occlusion.outputs["Color"]})
    color_ramp_1.color_ramp.elements[0].position = 0.9364
    color_ramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp_1.color_ramp.elements[1].position = 1.0000
    color_ramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Object"]})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 5.8000})
    
    color_ramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    color_ramp_3.color_ramp.elements[0].position = 0.3955
    color_ramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp_3.color_ramp.elements[1].position = 0.7136
    color_ramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 50.0000})
    
    color_ramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    color_ramp.color_ramp.elements[0].position = 0.0000
    color_ramp.color_ramp.elements[0].color = [0.1481, 0.1632, 0.0703, 1.0000]
    color_ramp.color_ramp.elements[1].position = 1.0000
    color_ramp.color_ramp.elements[1].color = [0.1244, 0.3186, 0.0531, 1.0000]
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: color_ramp_3.outputs["Color"], 6: color_ramp.outputs["Color"], 7: (0.4997, 0.4580, 0.2116, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    mapping_1 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate_1.outputs["Generated"], 'Scale': (31.6000, 11.6000, 1.0000)})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_1, 'Scale': 3.3000})
    
    color_ramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    color_ramp_2.color_ramp.elements[0].position = 0.3318
    color_ramp_2.color_ramp.elements[0].color = [0.1481, 0.1632, 0.0703, 1.0000]
    color_ramp_2.color_ramp.elements[1].position = 0.7091
    color_ramp_2.color_ramp.elements[1].color = [0.1244, 0.3186, 0.0531, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.5500, 6: mix_2.outputs[2], 7: color_ramp_2.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: color_ramp_1.outputs["Color"], 6: mix_1.outputs[2], 7: (0.3751, 0.4994, 0.0880, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Hue': 0.4800, 'Saturation': 0.8300, 'Value': 0.5000, 'Color': mix.outputs[2]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': hue_saturation_value, 'Subsurface Radius': (1.1100, 1.1800, 1.0000), 'Subsurface Anisotropy': 0.2000, 'Roughness': 0.6955, 'Emission Strength': 0.0000},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS', 'distribution': 'MULTI_GGX'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Cactus resolution', 0),
            ('NodeSocketInt', 'Cactus Ridge amount', 0),
            ('NodeSocketFloat', 'Cactus Thickness', 1.0000),
            ('NodeSocketFloat', 'Radius', 0.5000),
            ('NodeSocketFloat', 'Ridge Filet', 0.0300),
            ('NodeSocketFloat', 'Cactus distortion', 0.0900),
            ('NodeSocketFloat', 'Scale', 3.0000),
            ('NodeSocketFloat', 'Detail', 4.0000),
            ('NodeSocketFloat', 'Roughness', 0.5000),
            ('NodeSocketFloat', 'Lacunarity', 2.0000),
            ('NodeSocketFloat', 'Distortion', 0.0000),
            ('NodeSocketInt', 'Needle Count', 6),
            ('NodeSocketVector', 'Needle Length', (0.0000, 0.0000, 0.7900)),
            ('NodeSocketFloat', 'Needle Thickness', 2.0000),
            ('NodeSocketInt', 'Needle Resolution', 4),
            ('NodeSocketVector', 'Needle Min Pos Rand', (-0.1000, 0.0000, 0.1000)),
            ('NodeSocketVector', 'Needle Max Pos Rand', (0.1000, 10.0000, 0.1000)),
            ('NodeSocketFloat', 'Needle Distribution', 0.1110),
            ('NodeSocketFloat', 'Needle Min size', 0.0000),
            ('NodeSocketFloat', 'Needle Max size', 0.0000),
            ('NodeSocketFloat', 'Needle Density', 10000.0000),
            ('NodeSocketInt', 'Pot Vertical Resolution', 100),
            ('NodeSocketFloat', 'Needle Position', 0.3000),
            ('NodeSocketInt', 'Pot Horizontal Resolution', 138),
            ('NodeSocketVector', 'Pot Position', (0.0000, 0.0000, -0.5300)),
            ('NodeSocketFloat', 'Pot Bottom Size', 0.0000),
            ('NodeSocketFloat', 'Pot Neck Size', 1.0000),
            ('NodeSocketVector', 'Pot Scale', (0.7400, 0.7400, 0.5800)),
            ('NodeSocketFloat', 'Pot Thickness', 0.0700),
            ('NodeSocketFloat', 'Pot Shade Angle', 0.0200),
            ('NodeSocketVector', 'Scale_1', (0.9500, 0.9500, 0.9500)),
            ('NodeSocketVector', 'Translation', (0.0000, 0.0000, -0.0900)),
            ('NodeSocketFloat', 'Pebble Density', 5000.0000),
            ('NodeSocketInt', 'Pebble Segments', 8),
            ('NodeSocketInt', 'Pebble Rings', 4),
            ('NodeSocketFloat', 'Pebble Size', 0.0300),
            ('NodeSocketFloat', 'Pebble Z Randomness', 0.0500),
            ('NodeSocketInt', 'Pebble seed', 0)])
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': group_input.outputs["Geometry"], 'Count': group_input.outputs["Cactus resolution"]})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': spline_parameter.outputs["Factor"], 1: 0.7800, 3: group_input.outputs["Cactus Thickness"], 4: 0.0000})
    
    cactus_top_shape = nw.new_node(Nodes.RGBCurve, input_kwargs={'Color': map_range.outputs["Result"]}, label='Cactus top shape')
    node_utils.assign_curve(cactus_top_shape.mapping.curves[0], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(cactus_top_shape.mapping.curves[1], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(cactus_top_shape.mapping.curves[2], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(cactus_top_shape.mapping.curves[3], [(0.0000, 0.0000), (0.2455, 0.7688), (1.0000, 1.0000)])
    
    color_ramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter.outputs["Factor"]})
    color_ramp.color_ramp.interpolation = "EASE"
    color_ramp.color_ramp.elements.new(0)
    color_ramp.color_ramp.elements[0].position = 0.0000
    color_ramp.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    color_ramp.color_ramp.elements[1].position = 0.5273
    color_ramp.color_ramp.elements[1].color = [1.3000, 1.3000, 1.3000, 1.0000]
    color_ramp.color_ramp.elements[2].position = 1.0000
    color_ramp.color_ramp.elements[2].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: cactus_top_shape, 1: color_ramp.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve, 'Radius': multiply})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cactus Ridge amount"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute, 'Radius': group_input.outputs["Radius"]})
    
    index = nw.new_node(Nodes.Index)
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    scale = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 'Scale': 0.6300}, attrs={'operation': 'SCALE'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Selection': modulo, 'Position': scale.outputs["Vector"]})
    
    fillet_curve = nw.new_node(Nodes.FilletCurve,
        input_kwargs={'Curve': set_position, 'Count': 6, 'Radius': group_input.outputs["Ridge Filet"], 'Limit Radius': True},
        attrs={'mode': 'POLY'})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': fillet_curve, 'Count': 1000})
    
    spline_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_parameter_2.outputs["Factor"], 1: divide},
        attrs={'operation': 'MULTIPLY'})
    
    fract = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1}, attrs={'operation': 'FRACT'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: fract, 1: group_input.outputs["Needle Position"]})
    
    color_ramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': add})
    color_ramp_1.color_ramp.elements.new(0)
    color_ramp_1.color_ramp.elements[0].position = 0.4273
    color_ramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp_1.color_ramp.elements[1].position = 0.4955
    color_ramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    color_ramp_1.color_ramp.elements[2].position = 0.5636
    color_ramp_1.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': resample_curve_1, 2: color_ramp_1.outputs["Color"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': capture_attribute.outputs["Geometry"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': group_input.outputs["Scale"], 'Detail': group_input.outputs["Detail"], 'Roughness': group_input.outputs["Roughness"], 'Distortion': group_input.outputs["Distortion"]})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: noise_texture.outputs["Color"], 1: (-0.5000, -0.5000, -0.5000)})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add_1.outputs["Vector"], 'Scale': group_input.outputs["Cactus distortion"]},
        attrs={'operation': 'SCALE'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': curve_to_mesh, 'Offset': scale_1.outputs["Vector"]})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_1, 'Material': surface.shaderfunc_to_material(shader_cactus)})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs[2]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Needle Density"]})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': set_position_1, 'Selection': reroute_7, 'Density Max': 100000.0000, 'Density': reroute_8, 'Seed': 72})
    
    set_point_radius = nw.new_node(Nodes.SetPointRadius,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Radius': 0.0200})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance,
        input_kwargs={'Geometry': set_point_radius, 'Distance': group_input.outputs["Needle Distribution"]})
    
    points = nw.new_node('GeometryNodePoints', input_kwargs={'Count': group_input.outputs["Needle Count"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': group_input.outputs["Needle Length"]})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={0: (-1.0000, -1.0000, -1.0000)}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={0: (0.6000, 0.6000, 0.6000)}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': points, 'Instance': curve_line, 'Rotation': random_value.outputs["Value"], 'Scale': random_value_1.outputs["Value"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points})
    
    reverse_curve = nw.new_node(Nodes.ReverseCurve, input_kwargs={'Curve': realize_instances})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 1.0000, 3: 2.0000})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: spline_parameter_1.outputs["Factor"], 1: random_value_2.outputs[1]},
        attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reverse_curve, 'Radius': multiply_2})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Needle Thickness"]})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Needle Resolution"], 'Radius': reroute_6})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': surface.shaderfunc_to_material(shader_needle)})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_3})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    random_value_4 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: group_input.outputs["Needle Min Pos Rand"], 1: group_input.outputs["Needle Max Pos Rand"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    add_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: distribute_points_on_faces.outputs["Rotation"], 1: random_value_4.outputs["Value"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Needle Min size"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Needle Max size"]})
    
    random_value_3 = nw.new_node(Nodes.RandomValue, input_kwargs={2: reroute_10, 3: reroute_9})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': merge_by_distance, 'Instance': reroute_5, 'Rotation': add_2.outputs["Vector"], 'Scale': random_value_3.outputs[1]})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': group_input.outputs["Pot Vertical Resolution"], 'Side Segments': group_input.outputs["Pot Horizontal Resolution"], 'Fill Segments': 10})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz.outputs["Z"], 1: -1.0000, 3: group_input.outputs["Pot Bottom Size"], 4: group_input.outputs["Pot Neck Size"]})
    
    pot_shape = nw.new_node(Nodes.RGBCurve, input_kwargs={'Color': map_range_1.outputs["Result"]}, label='Pot shape')
    node_utils.assign_curve(pot_shape.mapping.curves[0], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(pot_shape.mapping.curves[1], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(pot_shape.mapping.curves[2], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(pot_shape.mapping.curves[3], [(0.0000, 0.6312), (0.0273, 0.7000), (0.1000, 0.7312), (0.9182, 0.9438), (1.0000, 0.9687)], handles=['VECTOR', 'AUTO', 'VECTOR', 'VECTOR', 'VECTOR'])
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': pot_shape})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_1, 'Y': reroute_1, 'Z': 1.0000})
    
    multiply_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_1, 1: combine_xyz}, attrs={'operation': 'MULTIPLY'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Position': multiply_3.outputs["Vector"]})
    
    sample_curve = nw.new_node(Nodes.SampleCurve, input_kwargs={'Curves': group_input.outputs["Geometry"]})
    
    add_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: sample_curve.outputs["Position"], 1: group_input.outputs["Pot Position"]})
    
    transform_geometry = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': set_position_2, 'Translation': add_3.outputs["Vector"], 'Scale': group_input.outputs["Pot Scale"]})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    equal = nw.new_node(Nodes.Compare,
        input_kwargs={4: normal, 5: (0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'VECTOR', 'operation': 'EQUAL'})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': transform_geometry, 'Selection': equal},
        attrs={'domain': 'FACE'})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': separate_geometry.outputs["Inverted"]})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': separate_geometry.outputs["Inverted"], 'Offset Scale': group_input.outputs["Pot Thickness"], 'Individual': False})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces, extrude_mesh.outputs["Mesh"]]})
    
    edge_angle = nw.new_node(Nodes.InputEdgeAngle)
    
    add_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: edge_angle.outputs["Unsigned Angle"], 1: group_input.outputs["Pot Shade Angle"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry_1, 'Selection': add_4})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_procedural_clay)})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_geometry.outputs["Selection"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    transform_geometry_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': reroute_3, 'Translation': group_input.outputs["Translation"], 'Scale': group_input.outputs["Scale_1"]})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': transform_geometry_1, 'Density': group_input.outputs["Pebble Density"], 'Seed': group_input.outputs["Pebble seed"]})
    
    random_value_6 = nw.new_node(Nodes.RandomValue, input_kwargs={3: group_input.outputs["Pebble Z Randomness"]})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: distribute_points_on_faces_1.outputs["Normal"], 'Scale': random_value_6.outputs[1]},
        attrs={'operation': 'SCALE'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': distribute_points_on_faces_1.outputs["Points"], 'Offset': scale_2.outputs["Vector"]})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere,
        input_kwargs={'Segments': group_input.outputs["Pebble Segments"], 'Rings': group_input.outputs["Pebble Rings"], 'Radius': group_input.outputs["Pebble Size"]})
    
    random_value_5 = nw.new_node(Nodes.RandomValue, input_kwargs={0: (0.5000, 0.5000, 0.5000)}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_3, 'Instance': uv_sphere.outputs["Mesh"], 'Scale': random_value_5.outputs["Value"]})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': instance_on_points_2})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth_1, 'Material': surface.shaderfunc_to_material(shader_procedural_rock_material)})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, set_material_1]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_2, instance_on_points_1, join_geometry_2]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])

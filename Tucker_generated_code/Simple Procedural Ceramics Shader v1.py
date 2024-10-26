import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_procedural_ceramics', singleton=False, type='ShaderNodeTree')
def nodegroup_procedural_ceramics(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate_2 = nw.new_node(Nodes.TextureCoord)
    
    mapping_2 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_2.outputs["Object"]})
    
    noise_texture_20 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_2, 'Scale': 500.0000, 'Detail': 1.0000, 'Roughness': 0.0000})
    
    colorramp_19 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_20.outputs["Color"]})
    colorramp_19.color_ramp.elements[0].position = 0.0000
    colorramp_19.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_19.color_ramp.elements[1].position = 1.0000
    colorramp_19.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    unglazed = nw.new_node(Nodes.GroupInput,
        label='Unglazed',
        expose_input=[('NodeSocketColor', 'Glaze Colour', (0.0343, 0.0137, 0.0037, 1.0000)),
            ('NodeSocketFloat', 'Glaze Position Adjust', -0.1000),
            ('NodeSocketFloat', 'Glaze Fade', 1.0000),
            ('NodeSocketFloat', 'Glaze Roughness', 0.2500),
            ('NodeSocketFloat', 'Glaze Specular', 0.6000),
            ('NodeSocketColor', 'Unglazed Colour', (0.4179, 0.3140, 0.2159, 1.0000)),
            ('NodeSocketFloat', 'Horizonal Lines Bump', 0.8000),
            ('NodeSocketFloat', 'Glaze Imperfections', 0.2500)])
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': colorramp_19.outputs["Color"], 1: -0.0100, 2: unglazed.outputs["Glaze Imperfections"]})
    
    texture_coordinate_4 = nw.new_node(Nodes.TextureCoord)
    
    value_2 = nw.new_node(Nodes.Value)
    value_2.outputs[0].default_value = 1.2000
    
    mapping_4 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_4.outputs["Object"], 'Scale': value_2})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_4, 'Scale': 400.0000, 'Detail': 8.3000, 'Roughness': 1.0000})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Color"]})
    colorramp_5.color_ramp.elements[0].position = 0.2727
    colorramp_5.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.5061
    colorramp_5.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_4, 'Scale': 886.5300, 'Detail': 1.0000, 'Roughness': 1.0000})
    
    colorramp_8 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_3.outputs["Color"]})
    colorramp_8.color_ramp.elements[0].position = 0.3106
    colorramp_8.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_8.color_ramp.elements[1].position = 0.3894
    colorramp_8.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.8000, 6: colorramp_5.outputs["Color"], 7: colorramp_8.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Color': unglazed.outputs["Unglazed Colour"]})
    
    rgb_curves_4 = nw.new_node(Nodes.RGBCurve, input_kwargs={'Color': hue_saturation_value})
    node_utils.assign_curve(rgb_curves_4.mapping.curves[0], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_4.mapping.curves[1], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_4.mapping.curves[2], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_4.mapping.curves[3], [(0.0000, 0.0000), (0.6697, 0.2917), (1.0000, 1.0000)])
    
    dark_dots = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_1.outputs[2], 6: rgb_curves_4, 7: hue_saturation_value},
        label='Dark Dots',
        attrs={'data_type': 'RGBA'})
    
    ambient_occlusion = nw.new_node(Nodes.AmbientOcclusion, attrs={'only_local': True})
    
    colorramp_7 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': ambient_occlusion.outputs["Color"]})
    colorramp_7.color_ramp.elements[0].position = 0.6545
    colorramp_7.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_7.color_ramp.elements[1].position = 0.9636
    colorramp_7.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    ambient_occlusion_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: dark_dots.outputs[2], 7: colorramp_7.outputs["Color"]},
        label='Ambient Occlusion',
        attrs={'data_type': 'RGBA', 'blend_type': 'SOFT_LIGHT'})
    
    texture_coordinate_6 = nw.new_node(Nodes.TextureCoord)
    
    mapping_6 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_6.outputs["Object"]})
    
    noise_texture_4 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_6, 'Scale': 553.1500, 'Detail': 5.4000})
    
    noise_texture_5 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_6, 'Scale': -12.5500, 'Detail': 0.0000, 'Distortion': 0.6000})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.7556, 6: noise_texture_4.outputs["Fac"], 7: noise_texture_5.outputs["Fac"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    rgb_curves_1 = nw.new_node(Nodes.RGBCurve, input_kwargs={'Color': mix_3.outputs[2]})
    node_utils.assign_curve(rgb_curves_1.mapping.curves[0], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_1.mapping.curves[1], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_1.mapping.curves[2], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_1.mapping.curves[3], [(0.0000, 0.0000), (0.3424, 0.5750), (1.0000, 1.0000)])
    
    noise_texture_18 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_6, 'Scale': 21.3000, 'Detail': 3.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_18.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.9122, 0.9122, 0.9122, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.9939
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    texture_coordinate_7 = nw.new_node(Nodes.TextureCoord)
    
    mapping_7 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate_7.outputs["Object"], 'Scale': (1.0000, 1.0000, 44.9000)})
    
    noise_texture_6 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_7, 'Scale': 1.4300, 'Detail': 0.9000, 'Distortion': 0.6000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_6.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.8342, 0.8342, 0.8342, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_1.outputs["Color"], 7: colorramp.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    bump_1 = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0200, 'Height': mix.outputs[2]})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': ambient_occlusion_1.outputs[2], 'Roughness': rgb_curves_1, 'Normal': bump_1})
    
    texture_coordinate_8 = nw.new_node(Nodes.TextureCoord)
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': unglazed.outputs["Glaze Position Adjust"]})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 1.0000, 'Z': unglazed.outputs["Glaze Fade"]})
    
    mapping_8 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate_8.outputs["Generated"], 'Location': combine_xyz, 'Rotation': (-0.9351, 0.1997, -0.6405), 'Scale': combine_xyz_1})
    
    colorramp_9 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mapping_8})
    colorramp_9.color_ramp.elements[0].position = 0.0000
    colorramp_9.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_9.color_ramp.elements[1].position = 0.0150
    colorramp_9.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    texture_coordinate_10 = nw.new_node(Nodes.TextureCoord)
    
    mapping_9 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_10.outputs["Object"]})
    
    noise_texture_9 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_9, 'Scale': 765.0300, 'Detail': 15.0000, 'Roughness': 1.0000})
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_9.outputs["Color"]})
    colorramp_6.color_ramp.elements[0].position = 0.4394
    colorramp_6.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 0.5394
    colorramp_6.color_ramp.elements[1].color = [1.0000, 0.9779, 0.9471, 1.0000]
    
    hue_saturation_value_1 = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Color': unglazed.outputs["Glaze Colour"]})
    
    rgb_curves_3 = nw.new_node(Nodes.RGBCurve, input_kwargs={'Color': hue_saturation_value_1})
    node_utils.assign_curve(rgb_curves_3.mapping.curves[0], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_3.mapping.curves[1], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_3.mapping.curves[2], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_3.mapping.curves[3], [(0.0000, 0.0000), (0.3364, 0.6958), (1.0000, 1.0000)])
    
    mix_9 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_6.outputs["Color"], 6: rgb_curves_3, 7: hue_saturation_value_1},
        attrs={'data_type': 'RGBA'})
    
    noise_texture_7 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_9, 'Scale': 886.5300, 'Detail': 1.0000, 'Roughness': 1.0000})
    
    colorramp_10 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_7.outputs["Color"]})
    colorramp_10.color_ramp.elements[0].position = 0.3163
    colorramp_10.color_ramp.elements[0].color = [0.3231, 0.3095, 0.3005, 1.0000]
    colorramp_10.color_ramp.elements[1].position = 0.4121
    colorramp_10.color_ramp.elements[1].color = [0.7605, 0.7084, 0.6724, 1.0000]
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.8000, 6: mix_9.outputs[2], 7: colorramp_10.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    ambient_occlusion_1_1 = nw.new_node(Nodes.AmbientOcclusion, attrs={'only_local': True})
    
    colorramp_13 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': ambient_occlusion_1_1.outputs["Color"]})
    colorramp_13.color_ramp.elements[0].position = 0.9667
    colorramp_13.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_13.color_ramp.elements[1].position = 1.0000
    colorramp_13.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    a_o_m_i_x = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.3111, 6: mix_4.outputs[2], 7: colorramp_13.outputs["Color"]},
        label='AO MIX',
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    texture_coordinate_12 = nw.new_node(Nodes.TextureCoord)
    
    mapping_12 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_12.outputs["Object"]})
    
    noise_texture_10 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_12, 'Scale': 553.1500, 'Detail': 5.4000})
    
    noise_texture_11 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_12, 'Scale': -12.5500, 'Detail': 0.0000, 'Distortion': 0.6000})
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.7556, 6: noise_texture_10.outputs["Fac"], 7: noise_texture_11.outputs["Fac"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    mix_8 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_7.outputs[2], 7: unglazed.outputs["Glaze Roughness"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    texture_coordinate_9 = nw.new_node(Nodes.TextureCoord)
    
    mapping_11 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_9.outputs["Object"]})
    
    surface_warp = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping_11, 'Scale': -8.8700}, label='Surface Warp')
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': surface_warp.outputs["Color"]})
    colorramp_4.color_ramp.elements[0].position = 0.0000
    colorramp_4.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 1.0000
    colorramp_4.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': (1.0000, 1.0000, 34.6900)})
    
    horizontal_lines = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': -4.3300, 'Detail': 0.0000, 'Distortion': 0.3200},
        label='Horizontal Lines')
    
    colorramp_11 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': horizontal_lines.outputs["Color"]})
    colorramp_11.color_ramp.elements[0].position = 0.0000
    colorramp_11.color_ramp.elements[0].color = [0.8956, 0.8956, 0.8956, 1.0000]
    colorramp_11.color_ramp.elements[1].position = 1.0000
    colorramp_11.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    lines_mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: unglazed.outputs["Horizonal Lines Bump"], 6: (1.0000, 1.0000, 1.0000, 1.0000), 7: colorramp_11.outputs["Color"]},
        label='Lines Mix',
        attrs={'data_type': 'RGBA'})
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={6: colorramp_4.outputs["Color"], 7: lines_mix.outputs[2]},
        attrs={'data_type': 'RGBA'})
    
    colorramp_20 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range.outputs["Result"]})
    colorramp_20.color_ramp.elements[0].position = 0.0000
    colorramp_20.color_ramp.elements[0].color = [0.9850, 0.9850, 0.9850, 1.0000]
    colorramp_20.color_ramp.elements[1].position = 1.0000
    colorramp_20.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    imperfections_mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: unglazed.outputs["Glaze Imperfections"], 6: mix_5.outputs[2], 7: colorramp_20.outputs["Color"]},
        label='Imperfections Mix',
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    bump_2 = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0400, 'Height': imperfections_mix.outputs[2]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': a_o_m_i_x.outputs[2], 'Specular': unglazed.outputs["Glaze Specular"], 'Roughness': mix_8.outputs[2], 'Clearcoat': 0.0932, 'Clearcoat Roughness': 0.1573, 'Normal': bump_2})
    
    mix_shader = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': colorramp_9.outputs["Color"], 1: principled_bsdf_1, 2: principled_bsdf})
    
    mix_shader_1 = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': map_range.outputs["Result"], 1: principled_bsdf_1, 2: mix_shader})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Shader': mix_shader_1}, attrs={'is_active_output': True})

def shader_material_060(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    procedural_ceramics = nw.new_node(nodegroup_procedural_ceramics().name,
        input_kwargs={'Glaze Colour': (0.4452, 0.4397, 0.3185, 1.0000), 'Glaze Position Adjust': -0.1200, 'Glaze Roughness': 0.4000, 'Unglazed Colour': (0.3654, 0.2747, 0.1893, 1.0000), 'Glaze Imperfections': 0.3200})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': procedural_ceramics}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_material(obj, shader_material_060, selection=selection)
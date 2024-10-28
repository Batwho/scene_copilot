import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_candy_cane01(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': texture_coordinate.outputs["UV"]})
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': reroute, 'Location': (18.2000, 0.0000, 0.0000), 'Rotation': (0.0000, 0.6074, 0.3665)})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': mapping, 'Scale': 6.4170, 'Detail': 0.0000, 'Phase Offset': -18.8000})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': wave_texture.outputs["Color"], 'Scale': 1.8000, 'Detail': 0.9000, 'Roughness': 0.9500})
    
    r_e_d_s_t_r_i_p_e_s = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]}, label='RED STRIPES')
    r_e_d_s_t_r_i_p_e_s.color_ramp.elements[0].position = 0.2591
    r_e_d_s_t_r_i_p_e_s.color_ramp.elements[0].color = [1.0000, 0.0055, 0.0000, 1.0000]
    r_e_d_s_t_r_i_p_e_s.color_ramp.elements[1].position = 0.5000
    r_e_d_s_t_r_i_p_e_s.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mapping_1 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': reroute, 'Location': (0.5000, 0.0000, 0.0000), 'Rotation': (0.0000, 0.5899, 0.3665)})
    
    wave_texture_1 = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 6.4000, 'Detail': 0.0000, 'Phase Offset': 2.9000})
    
    g_r_e_e_n_s_t_r_i_p_e_s = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': wave_texture_1.outputs["Color"]}, label='GREEN STRIPES')
    g_r_e_e_n_s_t_r_i_p_e_s.color_ramp.elements[0].position = 0.0364
    g_r_e_e_n_s_t_r_i_p_e_s.color_ramp.elements[0].color = [0.0310, 0.4480, 0.0000, 1.0000]
    g_r_e_e_n_s_t_r_i_p_e_s.color_ramp.elements[1].position = 0.1000
    g_r_e_e_n_s_t_r_i_p_e_s.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: r_e_d_s_t_r_i_p_e_s.outputs["Color"], 7: g_r_e_e_n_s_t_r_i_p_e_s.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix.outputs[2]})
    
    mapping_2 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': reroute})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_2, 'Scale': 25.0000, 'Detail': 8.0000, 'Roughness': 0.8250})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.3773
    colorramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5500
    colorramp_2.color_ramp.elements[1].color = [0.0140, 0.0140, 0.0140, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': reroute_1, 'Subsurface': 0.1000, 'Subsurface Radius': (0.5000, 0.5000, 0.5000), 'Subsurface Color': reroute_1, 'Specular': 0.7000, 'Roughness': colorramp_2.outputs["Color"], 'Clearcoat': 1.0000},
        attrs={'subsurface_method': 'BURLEY'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_material(obj, shader_candy_cane01, selection=selection)
apply(bpy.context.active_object)
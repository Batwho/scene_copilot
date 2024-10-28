import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_candy_cane06(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': texture_coordinate.outputs["UV"]})
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': reroute, 'Location': (18.2000, 0.0000, 0.0000), 'Rotation': (0.0000, 0.6074, 0.3665)})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': mapping, 'Scale': 6.4170, 'Detail': 0.0000, 'Phase Offset': -13.4000})
    
    red_stripe = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': wave_texture.outputs["Color"]}, label='Red Stripe')
    red_stripe.color_ramp.interpolation = "B_SPLINE"
    red_stripe.color_ramp.elements[0].position = 0.4500
    red_stripe.color_ramp.elements[0].color = [1.0000, 0.0055, 0.0000, 1.0000]
    red_stripe.color_ramp.elements[1].position = 0.6773
    red_stripe.color_ramp.elements[1].color = [0.7184, 0.9077, 1.0000, 1.0000]
    
    mapping_1 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': reroute, 'Location': (0.5000, 0.0000, 0.0000), 'Rotation': (0.0000, 0.5899, 0.3665)})
    
    wave_texture_1 = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 6.4000, 'Detail': 0.0000, 'Phase Offset': -0.7000})
    
    green_stripe = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': wave_texture_1.outputs["Color"]}, label='Green Stripe')
    green_stripe.color_ramp.elements[0].position = 0.4136
    green_stripe.color_ramp.elements[0].color = [0.0619, 1.0000, 0.0000, 1.0000]
    green_stripe.color_ramp.elements[1].position = 0.6591
    green_stripe.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: red_stripe.outputs["Color"], 7: green_stripe.outputs["Color"]},
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
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': texture_coordinate.outputs["Object"]})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': reroute_2, 'W': 3.7000, 'Scale': 87.0000},
        attrs={'feature': 'F2', 'distance': 'MINKOWSKI'})
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Color': voronoi_texture.outputs["Distance"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    mix_1 = nw.new_node(Nodes.Mix, input_kwargs={6: invert, 7: reroute_4}, attrs={'data_type': 'RGBA'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mix_1.outputs[2], 'Scale': 1.7000, 'Roughness': 0.0000},
        attrs={'noise_dimensions': '2D'})
    
    separate_rgb = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': noise_texture_1.outputs["Color"]})
    
    combine_rgb = nw.new_node(Nodes.CombineColor,
        input_kwargs={'Red': separate_rgb.outputs["Red"], 'Green': separate_rgb.outputs["Green"], 'Blue': 1.0000})
    
    normal_map = nw.new_node(Nodes.ShaderNodeNormalMap, input_kwargs={'Color': combine_rgb})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': reroute_1, 'Subsurface': 0.1000, 'Subsurface Radius': (0.5000, 0.5000, 0.5000), 'Subsurface Color': reroute_1, 'Specular': 0.7000, 'Roughness': colorramp_2.outputs["Color"], 'Clearcoat': 1.0000, 'Clearcoat Roughness': 0.2664, 'Clearcoat Normal': normal_map},
        attrs={'subsurface_method': 'BURLEY'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_material(obj, shader_candy_cane06, selection=selection)
apply(bpy.context.active_object)
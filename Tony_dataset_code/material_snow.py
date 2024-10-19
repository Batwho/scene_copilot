import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_5_snow(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry = nw.new_node(Nodes.NewGeometry)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': geometry.outputs["Normal"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: 1.0000})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: add}, attrs={'operation': 'MULTIPLY'})
    
    amount = nw.new_node(Nodes.Value, label='Amount')
    amount.outputs[0].default_value = 0.4000
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: amount, 1: 1.0000}, attrs={'operation': 'POWER'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: power}, attrs={'operation': 'SUBTRACT'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: subtract})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Object"]})
    
    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: object_info.outputs["Random"], 1: 32.0000}, attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'W': multiply_1, 'Scale': 4.0000, 'Detail': 4.0000, 'Distortion': 0.2500},
        attrs={'noise_dimensions': '4D'})
    
    power_1 = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Fac"], 1: 0.2700}, attrs={'operation': 'POWER'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: power_1, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: subtract_1})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': add_2})
    colorramp.color_ramp.elements[0].position = 0.4150
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5650
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    power_2 = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"]}, attrs={'operation': 'POWER'})
    
    power_3 = nw.new_node(Nodes.Math, input_kwargs={0: power_2}, attrs={'operation': 'POWER'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': power_3})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.1671, 0.1631, 0.1710, 1.0000), 'Roughness': 0.4000},
        attrs={'subsurface_method': 'BURLEY'})
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 512.0000, 'Smoothness': 0.5000},
        attrs={'voronoi_dimensions': '4D', 'feature': 'SMOOTH_F1'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1852, 6: voronoi_texture.outputs["Color"], 7: (0.5000, 0.5000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    normalize = nw.new_node(Nodes.VectorMath, input_kwargs={0: mix.outputs[2]}, attrs={'operation': 'NORMALIZE'})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.9551, 0.9551, 0.9551, 1.0000), 'Subsurface': 0.5000, 'Subsurface Radius': (1.0000, 1.0000, 1.0000), 'Subsurface Color': (0.6955, 0.7385, 0.8000, 1.0000), 'Roughness': 0.2000, 'Normal': normalize.outputs["Vector"]},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': reroute_2, 1: principled_bsdf, 2: principled_bsdf_1})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': add_2})
    colorramp_1.color_ramp.elements[0].position = 0.4500
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    power_4 = nw.new_node(Nodes.Math, input_kwargs={0: colorramp_1.outputs["Color"], 1: 2.0000}, attrs={'operation': 'POWER'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: power_4, 1: power_1}, attrs={'operation': 'MULTIPLY'})
    
    displacement_amount = nw.new_node(Nodes.Value, label='Displacement amount')
    displacement_amount.outputs[0].default_value = 0.5000
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: displacement_amount}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_3})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': mix_shader, 'Displacement': reroute},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_material(obj, shader_5_snow, selection=selection)
apply(bpy.context.active_object)
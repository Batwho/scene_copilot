import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_mat_meat(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': texture_coordinate.outputs["Generated"]})
    
    gradient_texture = nw.new_node(Nodes.GradientTexture, input_kwargs={'Vector': reroute_4})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': gradient_texture.outputs["Fac"]})
    colorramp_4.color_ramp.elements[0].position = 0.0773
    colorramp_4.color_ramp.elements[0].color = [0.4600, 0.4600, 0.4600, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.3273
    colorramp_4.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    voronoi_texture_1 = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': reroute_3, 'Scale': 200.0000},
        attrs={'feature': 'SMOOTH_F1'})
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_1.outputs["Color"]})
    colorramp_6.color_ramp.elements[0].position = 0.0500
    colorramp_6.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 0.0727
    colorramp_6.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': reroute_3, 'Scale': 10.0000},
        attrs={'feature': 'SMOOTH_F1'})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Color"]})
    colorramp_5.color_ramp.elements[0].position = 0.0500
    colorramp_5.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.0727
    colorramp_5.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_6.outputs["Color"], 7: colorramp_5.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'SCREEN'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute, 'Scale': 1.0000, 'Detail': 1.4000, 'Roughness': 0.6333})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp_1.color_ramp.interpolation = "B_SPLINE"
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.2409
    colorramp_1.color_ramp.elements[0].color = [0.0967, 0.0430, 0.0113, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.7045
    colorramp_1.color_ramp.elements[1].color = [0.0255, 0.0049, 0.0048, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 1.0000
    colorramp_1.color_ramp.elements[2].color = [0.3852, 0.0989, 0.0198, 1.0000]
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute, 'Scale': 16.0000, 'Detail': 3.5000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_2.color_ramp.interpolation = "B_SPLINE"
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0471, 0.0150, 0.0011, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.2539
    colorramp_2.color_ramp.elements[1].color = [0.9238, 0.1983, 0.0680, 1.0000]
    colorramp_2.color_ramp.elements[2].position = 0.5500
    colorramp_2.color_ramp.elements[2].color = [0.2219, 0.0577, 0.0094, 1.0000]
    colorramp_2.color_ramp.elements[3].position = 0.9136
    colorramp_2.color_ramp.elements[3].color = [0.1344, 0.0403, 0.0141, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.2590, 6: colorramp_1.outputs["Color"], 7: colorramp_2.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_5, 'Scale': 25.0000, 'Detail': 5.1000, 'Roughness': 0.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.interpolation = "B_SPLINE"
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0471, 0.0150, 0.0011, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.2818
    colorramp.color_ramp.elements[1].color = [0.6623, 0.1708, 0.0577, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.5500
    colorramp.color_ramp.elements[2].color = [0.0969, 0.0273, 0.0054, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.9136
    colorramp.color_ramp.elements[3].color = [0.3199, 0.1237, 0.0417, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.3500, 6: mix.outputs[2], 7: colorramp.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute_1, 'Scale': 10.0000})
    
    colorramp_7 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_3.outputs["Fac"]})
    colorramp_7.color_ramp.interpolation = "CONSTANT"
    colorramp_7.color_ramp.elements.new(0)
    colorramp_7.color_ramp.elements.new(0)
    colorramp_7.color_ramp.elements[0].position = 0.0000
    colorramp_7.color_ramp.elements[0].color = [0.1986, 0.3906, 0.0524, 1.0000]
    colorramp_7.color_ramp.elements[1].position = 0.4091
    colorramp_7.color_ramp.elements[1].color = [0.2426, 0.1358, 0.0284, 1.0000]
    colorramp_7.color_ramp.elements[2].position = 0.6091
    colorramp_7.color_ramp.elements[2].color = [0.0925, 0.1782, 0.0266, 1.0000]
    colorramp_7.color_ramp.elements[3].position = 1.0000
    colorramp_7.color_ramp.elements[3].color = [0.0854, 0.1864, 0.0266, 1.0000]
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Saturation': 0.9000, 'Value': 0.5000, 'Color': colorramp_7.outputs["Color"]})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_5.outputs[2], 6: mix_1.outputs[2], 7: hue_saturation_value},
        attrs={'data_type': 'RGBA'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_4.outputs["Color"], 6: mix_4.outputs[2], 7: (0.2270, 0.0324, 0.0210, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_1.outputs[2]})
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.5136
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.7000, 6: mix_2.outputs[2], 7: colorramp_3.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_3.outputs[2]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 0.2500, 'Z': 0.1000})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 0.2500
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: combine_xyz, 1: value, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: colorramp_3.outputs["Color"], 2: 0.0000}, attrs={'use_clamp': True})
    
    power = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_3.outputs["Color"], 1: 1.5000, 2: 0.0000},
        attrs={'operation': 'POWER'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0500, 'Height': power})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': reroute_6, 'Subsurface': 1.0000, 'Subsurface Radius': multiply, 'Subsurface Color': reroute_2, 'Roughness': add, 'Normal': bump},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    noise_texture_4 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_5, 'Scale': 15.0000, 'Detail': 4.0000, 'Distortion': 0.2000})
    
    displacement = nw.new_node(Nodes.Displacement, input_kwargs={'Height': noise_texture_4.outputs["Fac"], 'Scale': 0.0500})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': principled_bsdf, 'Displacement': displacement},
        attrs={'is_active_output': True})

def shader_mat_sauce(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': texture_coordinate.outputs["Object"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute, 'Scale': 10.0000, 'Detail': 1.7000, 'Distortion': 1.4000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.7669, 0.0516, 0.0144, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.9822
    colorramp_1.color_ramp.elements[1].color = [0.2624, 0.0414, 0.0354, 1.0000]
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Color': colorramp_1.outputs["Color"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 0.2500, 'Z': 0.1000})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 0.7500
    
    multiply = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz, 1: value}, attrs={'operation': 'MULTIPLY'})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute, 'Scale': 250.0000, 'Detail': 10.3000, 'Distortion': 0.1000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 1.0000
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump_1 = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0020, 'Height': colorramp_2.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': hue_saturation_value, 'Subsurface': 1.0000, 'Subsurface Radius': multiply.outputs["Vector"], 'Subsurface Color': hue_saturation_value, 'Roughness': 0.4000, 'Transmission': 0.2500, 'Transmission Roughness': 1.0000, 'Normal': bump_1},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute, 'Distortion': 1.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    displacement = nw.new_node(Nodes.Displacement, input_kwargs={'Height': colorramp.outputs["Color"], 'Scale': 0.0200})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': principled_bsdf, 'Displacement': displacement},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Moon Height', 2.0000),
            ('NodeSocketFloat', 'Moon Radius', 0.3000)])
    
    ico_sphere_1 = nw.new_node(Nodes.MeshIcoSphere, input_kwargs={'Radius': group_input.outputs["Moon Radius"], 'Subdivisions': 7})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': ico_sphere_1.outputs["Mesh"], 'Name': 'UVMap', 3: ico_sphere_1.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    noise_texture_8 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 0.5000, 'Detail': 5.0000})
    
    separate_rgb_1 = nw.new_node('FunctionNodeSeparateColor', input_kwargs={'Color': noise_texture_8.outputs["Color"]})
    
    map_range_10 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_rgb_1.outputs["Red"], 3: -1.0000})
    
    map_range_11 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_rgb_1.outputs["Green"], 3: -1.0000})
    
    map_range_12 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_rgb_1.outputs["Blue"], 3: -1.0000})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': map_range_10.outputs["Result"], 'Y': map_range_11.outputs["Result"], 'Z': map_range_12.outputs["Result"]})
    
    value_2 = nw.new_node(Nodes.Value)
    value_2.outputs[0].default_value = 0.2000
    
    multiply = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz_3, 1: value_2}, attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute, 'Offset': multiply.outputs["Vector"]})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    noise_texture_18 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 12.2000, 'Detail': 1.5000, 'Roughness': 1.0000})
    
    map_range_18 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': noise_texture_18.outputs["Fac"]})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_18.outputs["Result"], 1: 0.0300, 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_1})
    
    multiply_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal, 1: reroute}, attrs={'operation': 'MULTIPLY'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position, 'Offset': multiply_2.outputs["Vector"]})
    
    noise_texture_15 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 0.3300, 'Detail': 4.9000, 'Roughness': 1.0000, 'Distortion': 1.0000})
    
    noise_texture_16 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': noise_texture_15.outputs["Color"], 'Detail': 3.0000, 'Roughness': 0.0000})
    
    map_range_17 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': noise_texture_16.outputs["Fac"], 3: -1.0000})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_17.outputs["Result"], 1: 0.0300, 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal, 1: multiply_3}, attrs={'operation': 'MULTIPLY'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_1, 'Offset': multiply_4.outputs["Vector"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_position_2})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_mat_meat)})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Moon Height"]})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_1})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_material, 'Translation': combine_xyz_5})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_mat_sauce, selection=selection)
apply(bpy.context.active_object)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_sidewalk_corner', singleton=False, type='ShaderNodeTree')
def nodegroup_sidewalk_corner(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 0.3000, 'Detail': 15.0000, 'Roughness': 0.6436})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Color"]})
    colorramp_4.color_ramp.elements[0].position = 0.3263
    colorramp_4.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 1.0000
    colorramp_4.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketColor', 'sidewalk_color', (0.1914, 0.1319, 0.1000, 1.0000)),
            ('NodeSocketFloat', 'brick_scale', 0.7500),
            ('NodeSocketFloatFactor', 'wet', 0.5691)])
    
    mix_10 = nw.new_node(Nodes.Mix, input_kwargs={0: group_input.outputs["wet"], 2: 0.4000, 3: -0.4000})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: colorramp_4.outputs["Color"], 1: mix_10.outputs["Result"]})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': add})
    colorramp_5.color_ramp.elements[0].position = 0.0544
    colorramp_5.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.2447
    colorramp_5.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    texture_coordinate_2 = nw.new_node(Nodes.TextureCoord, attrs={'object': bpy.data.objects['RoadCurve']})
    
    mapping_2 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate_2.outputs["Object"], 'Location': (0.6200, -0.1500, 0.0000), 'Rotation': (0.0000, 0.0000, 0.6545)})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={1: group_input.outputs["brick_scale"]}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 0.7900}, attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: 0.2500, 1: group_input.outputs["brick_scale"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: 1.6000}, attrs={'operation': 'MULTIPLY'})
    
    brick_texture = nw.new_node(Nodes.BrickTexture,
        input_kwargs={'Vector': mapping_2, 'Color2': (0.6261, 0.6261, 0.6261, 1.0000), 'Mortar': (0.0298, 0.0298, 0.0298, 1.0000), 'Scale': 0.9500, 'Mortar Size': 0.0030, 'Brick Width': multiply_1, 'Row Height': multiply_3})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: brick_texture.outputs["Color"], 7: group_input.outputs["sidewalk_color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Object"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': 0.7000, 'Detail': 15.0000, 'Roughness': 0.8867})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]})
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 1.0000
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix.outputs[2], 7: colorramp_3.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    mix_9 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_5.outputs["Color"], 6: mix_7.outputs[2], 7: (0.5586, 0.5586, 0.5586, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': brick_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.5710
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.6254
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp.outputs["Color"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: add},
        attrs={'data_type': 'RGBA'})
    
    layer_weight = nw.new_node(Nodes.LayerWeight, input_kwargs={'Blend': 0.8000})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 66.8000
    
    mix_2 = nw.new_node(Nodes.Mix, input_kwargs={0: layer_weight.outputs["Facing"], 2: value})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 70.0000, 'Detail': 15.0000, 'Roughness': 0.8039})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0200, 6: colorramp.outputs["Color"], 7: noise_texture.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': mix_2.outputs["Result"], 'Height': mix_1.outputs[2]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_9.outputs[2], 'Roughness': mix_3.outputs[2], 'Normal': bump})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'BSDF': principled_bsdf, 'tmp_viewer': principled_bsdf},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_sidewalk', singleton=False, type='ShaderNodeTree')
def nodegroup_sidewalk(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 0.3000, 'Detail': 15.0000, 'Roughness': 0.6436})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Color"]})
    colorramp_4.color_ramp.elements[0].position = 0.3263
    colorramp_4.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 1.0000
    colorramp_4.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketColor', 'brick_color', (0.1914, 0.1319, 0.1000, 1.0000)),
            ('NodeSocketFloat', 'brick_scale', 0.5000),
            ('NodeSocketFloatFactor', 'wet', 0.5691)])
    
    mix_10 = nw.new_node(Nodes.Mix, input_kwargs={0: group_input.outputs["wet"], 2: 0.4000, 3: -0.4000})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: colorramp_4.outputs["Color"], 1: mix_10.outputs["Result"]})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': add})
    colorramp_5.color_ramp.elements[0].position = 0.0544
    colorramp_5.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.2447
    colorramp_5.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Gradient X2'})
    
    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Gradient Y2'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': attribute.outputs["Fac"], 'Y': attribute_1.outputs["Fac"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={1: group_input.outputs["brick_scale"]}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: 0.2500, 1: group_input.outputs["brick_scale"]},
        attrs={'operation': 'MULTIPLY'})
    
    brick_texture = nw.new_node(Nodes.BrickTexture,
        input_kwargs={'Vector': combine_xyz, 'Color2': (0.6261, 0.6261, 0.6261, 1.0000), 'Mortar': (0.0298, 0.0298, 0.0298, 1.0000), 'Scale': -0.6000, 'Mortar Size': 0.0020, 'Brick Width': multiply, 'Row Height': multiply_1})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: brick_texture.outputs["Color"], 7: group_input.outputs["brick_color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Object"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': 0.7000, 'Detail': 15.0000, 'Roughness': 0.8867})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]})
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 1.0000
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix.outputs[2], 7: colorramp_3.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    mix_9 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_5.outputs["Color"], 6: mix_7.outputs[2], 7: (0.5586, 0.5586, 0.5586, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': brick_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.5710
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.6254
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp.outputs["Color"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: add},
        attrs={'data_type': 'RGBA'})
    
    layer_weight = nw.new_node(Nodes.LayerWeight, input_kwargs={'Blend': 0.8000})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 66.8000
    
    mix_2 = nw.new_node(Nodes.Mix, input_kwargs={0: layer_weight.outputs["Facing"], 2: value})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 70.0000, 'Detail': 15.0000, 'Roughness': 0.8039})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0200, 6: colorramp.outputs["Color"], 7: noise_texture.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': mix_2.outputs["Result"], 'Height': mix_1.outputs[2]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_9.outputs[2], 'Roughness': mix_3.outputs[2], 'Normal': bump})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'BSDF': principled_bsdf, 'tmp_viewer': principled_bsdf},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_asphalt', singleton=False, type='ShaderNodeTree')
def nodegroup_asphalt(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord, attrs={'object': bpy.data.objects['RoadCurve']})
    
    value_1 = nw.new_node(Nodes.Value)
    value_1.outputs[0].default_value = 1.0000
    
    mapping_2 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"], 'Scale': value_1})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_2, 'Scale': 0.3000, 'Detail': 15.0000, 'Roughness': 0.6436})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Color"]})
    colorramp_4.color_ramp.elements[0].position = 0.3263
    colorramp_4.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 1.0000
    colorramp_4.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketColor', 'middleLine_color', (1.0000, 0.4267, 0.0000, 1.0000)),
            ('NodeSocketColor', 'sideLine_color', (0.5249, 0.5249, 0.5249, 1.0000)),
            ('NodeSocketFloat', 'line_width', 0.0300),
            ('NodeSocketFloat', 'sideLine_margin', 0.5000),
            ('NodeSocketFloat', 'dashLine_spacing', 0.2500),
            ('NodeSocketFloat', 'dashLine_length', 1.0000),
            ('NodeSocketFloat', 'middleLine', 0.0200),
            ('NodeSocketFloatFactor', 'wet', 0.2735),
            ('NodeSocketFloatFactor', 'is_intersection', 0.5000),
            ('NodeSocketColor', 'pedestrian_crossing_color', (0.5000, 0.5000, 0.5000, 1.0000)),
            ('NodeSocketFloat', 'pedestrian_crossing_dash', 0.7500)])
    
    mix_10 = nw.new_node(Nodes.Mix, input_kwargs={0: group_input.outputs["wet"], 2: 0.4000, 3: -0.4000})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: colorramp_4.outputs["Color"], 1: mix_10.outputs["Result"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute})
    colorramp_5.color_ramp.elements[0].position = 0.0544
    colorramp_5.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.2447
    colorramp_5.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord, attrs={'object': bpy.data.objects['RoadCurve']})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 1.0000
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': value})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mapping_1})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_1, 'Scale': 0.8000, 'Detail': 8.1000, 'Roughness': 0.8978})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': noise_texture.outputs["Color"], 'Scale': 40.0000})
    
    voronoi_texture_1 = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': reroute_1, 'Scale': 60.0000})
    
    mix_21 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.6575, 6: voronoi_texture.outputs["Distance"], 7: voronoi_texture_1.outputs["Distance"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_21.outputs[2]})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_3})
    colorramp_2.color_ramp.elements[0].position = 0.3263
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.7311
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    invert_1 = nw.new_node(Nodes.Invert, input_kwargs={'Color': colorramp_2.outputs["Color"]})
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Gradient X'})
    
    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Gradient Y'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': attribute.outputs["Fac"], 'Y': attribute_1.outputs["Fac"]})
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': combine_xyz, 'Rotation': (0.0000, 0.0000, 1.5708), 'Scale': (-0.3000, 0.0000, 1.0000)})
    
    brick_texture = nw.new_node(Nodes.BrickTexture,
        input_kwargs={'Vector': mapping, 'Color2': (1.0000, 1.0000, 1.0000, 1.0000), 'Scale': group_input.outputs["dashLine_length"], 'Mortar Size': 0.0250, 'Row Height': group_input.outputs["dashLine_spacing"]})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': brick_texture.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.0272
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    attribute_6 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Gradient X'})
    
    attribute_5 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Gradient Y intersection2'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': attribute_6.outputs["Fac"], 'Y': attribute_5.outputs["Fac"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["pedestrian_crossing_dash"]})
    
    brick_texture_1 = nw.new_node(Nodes.BrickTexture,
        input_kwargs={'Vector': combine_xyz_2, 'Color2': (1.0000, 1.0000, 1.0000, 1.0000), 'Scale': reroute_2, 'Mortar Size': 0.0010})
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': brick_texture_1.outputs["Color"]})
    colorramp_6.color_ramp.elements[0].position = 0.0000
    colorramp_6.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 0.4622
    colorramp_6.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    attribute_3 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Gradient X'})
    
    attribute_4 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Gradient Y intersection'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': attribute_3.outputs["Fac"], 'Y': attribute_4.outputs["Fac"]})
    
    attribute_2 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'roadlane_width'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: attribute_2.outputs["Fac"], 1: 3.0000}, attrs={'operation': 'DIVIDE'})
    
    compare = nw.new_node(Nodes.Math, input_kwargs={0: combine_xyz_1, 1: 0.0000, 2: divide}, attrs={'operation': 'COMPARE'})
    
    mix_14 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_6.outputs["Color"], 6: compare, 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mapping_3 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': combine_xyz_1, 'Location': (0.0000, 0.2000, 0.0000)})
    
    brick_texture_2 = nw.new_node(Nodes.BrickTexture,
        input_kwargs={'Vector': mapping_3, 'Color2': (1.0000, 1.0000, 1.0000, 1.0000), 'Scale': reroute_2, 'Mortar Size': 0.0010},
        attrs={'offset': 0.5765})
    
    colorramp_7 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': brick_texture_2.outputs["Color"]})
    colorramp_7.color_ramp.elements[0].position = 0.3746
    colorramp_7.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_7.color_ramp.elements[1].position = 0.5166
    colorramp_7.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    attribute_7 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'sidewalk_width'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: attribute_7.outputs["Fac"], 1: attribute_2.outputs["Fac"]})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: 3.0000}, attrs={'operation': 'DIVIDE'})
    
    compare_1 = nw.new_node(Nodes.Math, input_kwargs={0: combine_xyz_2, 1: divide_1, 2: divide}, attrs={'operation': 'COMPARE'})
    
    mix_18 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_7.outputs["Color"], 6: compare_1, 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_19 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_14.outputs[2], 7: mix_18.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_20 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: compare_1, 7: compare},
        attrs={'data_type': 'RGBA', 'blend_type': 'SCREEN'})
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Color': mix_20.outputs[2]})
    
    mix_22 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_19.outputs[2], 7: invert},
        attrs={'data_type': 'RGBA', 'blend_type': 'SCREEN'})
    
    mix_12 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["is_intersection"], 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: mix_22.outputs[2]},
        attrs={'data_type': 'RGBA'})
    
    mix_13 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_1.outputs["Color"], 6: mix_12.outputs[2], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_24 = nw.new_node(Nodes.Mix,
        input_kwargs={0: invert_1, 6: mix_13.outputs[2], 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    colorramp_8 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_24.outputs[2]})
    colorramp_8.color_ramp.elements[0].position = 0.9819
    colorramp_8.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_8.color_ramp.elements[1].position = 1.0000
    colorramp_8.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': combine_xyz})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: 0.0000})
    
    compare_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: add_2, 1: group_input.outputs["middleLine"], 2: group_input.outputs["line_width"]},
        attrs={'operation': 'COMPARE'})
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_1.outputs["Color"], 6: compare_2, 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_6 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_2.outputs["Color"], 6: mix_5.outputs[2], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Y"], 1: 0.0000})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["sideLine_margin"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    add_4 = nw.new_node(Nodes.Math, input_kwargs={0: attribute_2.outputs["Fac"], 1: multiply})
    
    compare_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: add_3, 1: add_4, 2: group_input.outputs["line_width"]},
        attrs={'operation': 'COMPARE'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: compare_3, 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'SCREEN'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_3.outputs[2], 7: invert_1},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_3})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.1851, 0.1851, 0.1851, 1.0000]
    
    mix_11 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.3000, 6: colorramp.outputs["Color"], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_2.outputs[2], 6: mix_11.outputs[2], 7: group_input.outputs["sideLine_color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'SCREEN'})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_6.outputs[2], 6: mix_1.outputs[2], 7: group_input.outputs["middleLine_color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'SCREEN'})
    
    compare_4 = nw.new_node(Nodes.Math, input_kwargs={0: combine_xyz_2, 1: divide_1, 2: divide}, attrs={'operation': 'COMPARE'})
    
    mix_23 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: compare_4, 7: compare},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_17 = nw.new_node(Nodes.Mix,
        input_kwargs={0: invert_1, 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: mix_23.outputs[2]},
        attrs={'data_type': 'RGBA'})
    
    mix_15 = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_17.outputs[2], 6: group_input.outputs["pedestrian_crossing_color"], 7: mix_1.outputs[2]},
        attrs={'data_type': 'RGBA'})
    
    mix_16 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["is_intersection"], 6: mix_4.outputs[2], 7: mix_15.outputs[2]},
        attrs={'data_type': 'RGBA'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_8.outputs["Color"], 6: mix_16.outputs[2], 7: mix_1.outputs[2]},
        attrs={'data_type': 'RGBA'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_1, 'Scale': 0.3000, 'Detail': 15.0000, 'Roughness': 0.8867})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]})
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 1.0000
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix.outputs[2], 7: colorramp_3.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'OVERLAY'})
    
    mix_9 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_5.outputs["Color"], 6: mix_7.outputs[2], 7: (0.6425, 0.6425, 0.6425, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_8 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute, 6: (0.0000, 0.0000, 0.0000, 1.0000), 7: colorramp.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Height': mix_8.outputs[2]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_9.outputs[2], 'Specular': 0.4909, 'Roughness': reroute, 'Normal': bump})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'BSDF': principled_bsdf, 'tmp_viewer': principled_bsdf},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_main_road_geometry_nodes', singleton=False, type='GeometryNodeTree')
def nodegroup_main_road_geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'curve', None),
            ('NodeSocketFloat', 'width_roadlane', 0.0000),
            ('NodeSocketFloat', 'width_sidewalk', 0.0000),
            ('NodeSocketFloatFactor', 'wet', 0.5000),
            ('NodeSocketColor', 'color_sideline', (0.5029, 0.5029, 0.5029, 1.0000)),
            ('NodeSocketColor', 'color_middleline', (1.0000, 0.2748, 0.0000, 1.0000)),
            ('NodeSocketColor', 'color_pedestrial', (0.7399, 0.7399, 0.7399, 1.0000)),
            ('NodeSocketColor', 'color_sidewalk', (0.0000, 0.0000, 0.0000, 1.0000)),
            ('NodeSocketFloat', 'brick_scale', 0.0000),
            ('NodeSocketFloatFactor', 'endpoint intersection', 1.0000)])
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["curve"]})
    
    spline_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    store_named_attribute_3 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': reroute_2, 'Name': 'Gradient X2', 4: spline_parameter_2.outputs["Length"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["width_roadlane"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["width_sidewalk"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: reroute_11})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_4, 'End': combine_xyz_6})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_1})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_7, 'End': combine_xyz_5})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_line_1, curve_line_2]})
    
    spline_parameter_3 = nw.new_node(Nodes.SplineParameter)
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': join_geometry, 'Name': 'Gradient Y2', 4: spline_parameter_3.outputs["Length"]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': store_named_attribute_3, 'Profile Curve': store_named_attribute_2})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': surface.shaderfunc_to_material(shader_sidewalk)})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    mix_2 = nw.new_node(Nodes.Mix, input_kwargs={0: group_input.outputs["endpoint intersection"], 3: 1.0000})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0, 'End Size': mix_2.outputs["Result"]})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: reroute_11})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_3})
    
    curve_line_4 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_8, 'End': (0.0000, 0.0000, 0.0000)})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    store_named_attribute_5 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': curve_line_4, 'Name': 'Gradient Y intersection2', 4: spline_parameter.outputs["Length"]})
    
    combine_xyz_12 = nw.new_node(Nodes.CombineXYZ)
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_4, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: multiply_4})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_2})
    
    curve_line_6 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_12, 'End': combine_xyz_9})
    
    combine_xyz_11 = nw.new_node(Nodes.CombineXYZ)
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: reroute_4})
    
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_3})
    
    curve_line_5 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_11, 'End': combine_xyz_10})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_line_6, curve_line_5]})
    
    store_named_attribute_4 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': join_geometry_3, 'Name': 'Gradient Y intersection', 4: spline_parameter.outputs["Length"]})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': store_named_attribute_5, 'Profile Curve': store_named_attribute_4})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_3, 'Selection': endpoint_selection, 'Instance': curve_to_mesh_2, 'Rotation': align_euler_to_vector})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': reroute_5})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mesh_to_points})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    combine_xyz_13 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': separate_xyz.outputs["X"], 'Y': separate_xyz.outputs["Y"]})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={1: combine_xyz_13})
    
    arc = nw.new_node('GeometryNodeCurveArc',
        input_kwargs={'Radius': group_input.outputs["width_sidewalk"], 'Sweep Angle': 1.5708, 'Connect Center': True})
    
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': arc.outputs["Curve"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': fill_curve})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_7, 'Selection': greater_than, 'Instance': reroute_6})
    
    add_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["width_roadlane"], 1: group_input.outputs["width_sidewalk"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_4})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    less_than = nw.new_node(Nodes.Compare,
        input_kwargs={0: reroute_1, 1: separate_xyz_2.outputs["X"]},
        attrs={'operation': 'LESS_THAN'})
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={0: 1.0000, 1: separate_xyz_2.outputs["Y"]})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: less_than, 1: greater_than_1}, attrs={'operation': 'SUBTRACT'})
    
    instance_on_points_3 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_7, 'Selection': subtract, 'Instance': reroute_6, 'Rotation': (0.0000, 0.0000, 3.1416)})
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    greater_than_2 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_3.outputs["X"]})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: add_4, 1: 0.7500}, attrs={'use_clamp': True, 'operation': 'MULTIPLY'})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_5, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    greater_than_3 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_3.outputs["Y"], 1: multiply_6})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: greater_than_2, 1: greater_than_3}, attrs={'operation': 'SUBTRACT'})
    
    instance_on_points_4 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_7, 'Selection': subtract_1, 'Instance': reroute_6, 'Rotation': (0.0000, 0.0000, 1.5708)})
    
    separate_xyz_4 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    greater_than_4 = nw.new_node(Nodes.Compare, input_kwargs={0: multiply_5, 1: separate_xyz_4.outputs["X"]})
    
    greater_than_5 = nw.new_node(Nodes.Compare, input_kwargs={0: multiply_5, 1: separate_xyz_4.outputs["Y"]})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: greater_than_4, 1: greater_than_5}, attrs={'operation': 'SUBTRACT'})
    
    instance_on_points_5 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_7, 'Selection': subtract_2, 'Instance': reroute_6, 'Rotation': (0.0000, 0.0000, -1.5708)})
    
    join_geometry_7 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [instance_on_points_1, instance_on_points_3, instance_on_points_4, instance_on_points_5]})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_7, 'Material': surface.shaderfunc_to_material(shader_sidewalk_corner)})
    
    join_geometry_6 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_2, set_material_3]})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': join_geometry_6})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': realize_instances_1, 'Offset Scale': 0.0500})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Shade Smooth': False})
    
    join_geometry_5 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': instance_on_points})
    
    set_material_5 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_5, 'Material': surface.shaderfunc_to_material(shader_intersection)})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': reroute_2, 'Name': 'Gradient X', 4: spline_parameter.outputs["Length"]})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ)
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_1})
    
    curve_line_3 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_3, 'End': combine_xyz_2})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ)
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': combine_xyz_1, 'End': combine_xyz})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_line_3, curve_line]})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': join_geometry_2, 'Name': 'Gradient Y', 4: spline_parameter_1.outputs["Length"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': store_named_attribute, 'Profile Curve': store_named_attribute_1})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_road)})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_5, set_material_4]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': join_geometry_4})
    
    set_shade_smooth_2 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': realize_instances})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_shade_smooth, set_shade_smooth_2]})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': join_geometry_1})
    
    mix = nw.new_node(Nodes.Mix, input_kwargs={0: group_input.outputs["wet"], 3: 1.0000})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': realize_instances_2, 'widthRoad': reroute, 'widthSidewalk': reroute_11, 'wet': mix.outputs["Result"], 'color_sideline': group_input.outputs["color_sideline"], 'color_middleline': group_input.outputs["color_middleline"], 'color_pedestrial': group_input.outputs["color_pedestrial"], 'color_sidewalk': group_input.outputs["color_sidewalk"], 'brick_scale': group_input.outputs["brick_scale"], 'intersection rotation': align_euler_to_vector},
        attrs={'is_active_output': True})

def shader_sidewalk_corner(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'color_sidewalk'})
    
    attribute_2 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'brick_scale'})
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'wet'})
    
    group = nw.new_node(nodegroup_sidewalk_corner().name,
        input_kwargs={'sidewalk_color': attribute_1.outputs["Color"], 'brick_scale': attribute_2.outputs["Fac"], 'wet': attribute.outputs["Fac"]})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': group.outputs["tmp_viewer"]},
        attrs={'is_active_output': True})

def shader_intersection(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'wet'})
    
    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'color_pedestrial'})
    
    group = nw.new_node(nodegroup_asphalt().name,
        input_kwargs={'middleLine_color': (1.0000, 0.3610, 0.0000, 1.0000), 'sideLine_margin': 0.5100, 'dashLine_spacing': 0.2400, 'dashLine_length': 1.0200, 'wet': attribute.outputs["Fac"], 'is_intersection': 1.0000, 'pedestrian_crossing_color': attribute_1.outputs["Color"]})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': group.outputs["tmp_viewer"]},
        attrs={'is_active_output': True})

def shader_sidewalk(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'color_sidewalk'})
    
    attribute_2 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'brick_scale'})
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'wet'})
    
    group = nw.new_node(nodegroup_sidewalk().name,
        input_kwargs={'brick_color': attribute_1.outputs["Color"], 'brick_scale': attribute_2.outputs["Fac"], 'wet': attribute.outputs["Fac"]})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': group.outputs["tmp_viewer"]},
        attrs={'is_active_output': True})

def shader_road(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'color_middle'})
    
    attribute_2 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'color_sideline'})
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'wet'})
    
    group = nw.new_node(nodegroup_asphalt().name,
        input_kwargs={'middleLine_color': attribute_1.outputs["Color"], 'sideLine_color': attribute_2.outputs["Color"], 'line_width': 0.0400, 'sideLine_margin': 0.7300, 'dashLine_spacing': 0.4200, 'dashLine_length': 1.2400, 'wet': attribute.outputs["Fac"], 'is_intersection': 0.0000, 'pedestrian_crossing_dash': 0.5500})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': group.outputs["BSDF"]}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    main_road_geometry_nodes = nw.new_node(nodegroup_main_road_geometry_nodes().name,
        input_kwargs={'curve': group_input.outputs["Geometry"], 'width_roadlane': 6.5000, 'width_sidewalk': 3.8200, 'wet': 0.6250, 'color_sideline': (0.7365, 0.7365, 0.7365, 1.0000), 'color_middleline': (1.0000, 0.2330, 0.0000, 1.0000), 'color_pedestrial': (0.5029, 0.5029, 0.5029, 1.0000), 'color_sidewalk': (0.1912, 0.1329, 0.0999, 1.0000), 'brick_scale': 1.5900})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': main_road_geometry_nodes.outputs["Geometry"], 'widthRoad': main_road_geometry_nodes.outputs["widthRoad"], 'widthSidewalk': main_road_geometry_nodes.outputs["widthSidewalk"], 'wet': main_road_geometry_nodes.outputs["wet"], 'color_sideline': main_road_geometry_nodes.outputs["color_sideline"], 'color_middleline': main_road_geometry_nodes.outputs["color_middleline"], 'color_pedestrial': main_road_geometry_nodes.outputs["color_pedestrial"], 'color_sidewalk': main_road_geometry_nodes.outputs["color_sidewalk"], 'brick_scale': main_road_geometry_nodes.outputs["brick_scale"], 'intersection rotation': main_road_geometry_nodes.outputs["intersection rotation"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_road, selection=selection)
    surface.add_material(obj, shader_sidewalk, selection=selection)
    surface.add_material(obj, shader_intersection, selection=selection)
    surface.add_material(obj, shader_sidewalk_corner, selection=selection)
apply(bpy.context.active_object)
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_scatter_001', singleton=False, type='ShaderNodeTree')
def nodegroup_scatter_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Scale Individual', (1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloat', 'Scale Grid', 5.0000),
            ('NodeSocketFloat', 'Scale Uniform', 1.0000),
            ('NodeSocketFloat', 'W', 0.0000),
            ('NodeSocketFloat', 'Min', 1.0000),
            ('NodeSocketFloat', 'Max', 1.0000),
            ('NodeSocketFloat', 'Randomize Rotation Individual', 0.0000),
            ('NodeSocketFloat', 'Rotation All', 0.0000),
            ('NodeSocketFloat', 'Bias', 0.5000)])
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: group_input.outputs["Vector"], 'Scale': group_input.outputs["Scale Grid"]},
        attrs={'operation': 'SCALE'})
    
    fraction = nw.new_node(Nodes.VectorMath, input_kwargs={0: scale.outputs["Vector"]}, attrs={'operation': 'FRACTION'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': -0.5000, 'Y': -0.5000, 'Z': -0.5000})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: fraction.outputs["Vector"], 1: combine_xyz})
    
    ceil = nw.new_node(Nodes.VectorMath, input_kwargs={0: scale.outputs["Vector"]}, attrs={'operation': 'CEIL'})
    
    white_noise_texture = nw.new_node(Nodes.WhiteNoiseTexture,
        input_kwargs={'Vector': ceil.outputs["Vector"], 'W': group_input.outputs["W"]},
        attrs={'noise_dimensions': '4D'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': white_noise_texture.outputs["Value"], 3: group_input.outputs["Min"], 4: group_input.outputs["Max"]})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add.outputs["Vector"], 'Scale': map_range.outputs["Result"]},
        attrs={'operation': 'SCALE'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: white_noise_texture.outputs["Value"], 1: group_input.outputs["Randomize Rotation Individual"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: group_input.outputs["Rotation All"]})
    
    radians = nw.new_node(Nodes.Math, input_kwargs={0: add_1}, attrs={'operation': 'RADIANS'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate, input_kwargs={'Vector': scale_1.outputs["Vector"], 'Angle': radians})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: vector_rotate, 'Scale': group_input.outputs["Scale Uniform"]},
        attrs={'operation': 'SCALE'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale_2.outputs["Vector"], 1: group_input.outputs["Scale Individual"], 'Scale': 0.5900},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: white_noise_texture.outputs["Value"], 1: group_input.outputs["Bias"]},
        attrs={'operation': 'GREATER_THAN'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Vector': multiply_1.outputs["Vector"], 'Bias Clamp': greater_than, 'Bias ': white_noise_texture.outputs["Value"], 'Color': white_noise_texture.outputs["Color"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_color_ramp_math_001', singleton=False, type='ShaderNodeTree')
def nodegroup_color_ramp_math_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Fac', 0.5000),
            ('NodeSocketColor', 'Color1', (1.0000, 1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloat', 'Pos 1', 1.0000),
            ('NodeSocketColor', 'Color2', (0.0000, 0.0000, 0.0000, 1.0000)),
            ('NodeSocketFloat', 'Pos 2', 0.0000)])
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Pos 2"], 1: group_input.outputs["Pos 1"]},
        attrs={'operation': 'SUBTRACT'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: subtract}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: group_input.outputs["Fac"]}, attrs={'operation': 'MULTIPLY'})
    
    subtract_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Pos 1"], 1: group_input.outputs["Pos 2"]},
        attrs={'operation': 'SUBTRACT'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Pos 1"], 1: subtract_1}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: divide_1})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: add, 6: group_input.outputs["Color1"], 7: group_input.outputs["Color2"]},
        attrs={'data_type': 'RGBA'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Color': mix_2.outputs[2]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_uber_mapping__tile_rotation_001', singleton=False, type='ShaderNodeTree')
def nodegroup_uber_mapping__tile_rotation_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'UV', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Scale', 1.0000),
            ('NodeSocketFloat', 'Aspect Ratio', 1.0000),
            ('NodeSocketFloat', 'Translate X', 0.0000),
            ('NodeSocketFloat', 'Translate Y', 0.0000),
            ('NodeSocketFloat', 'Global Rotation', 0.0000),
            ('NodeSocketFloat', 'Mosaic Rotation', 0.0000),
            ('NodeSocketFloat', 'Mosaic Noise', 0.0000)])
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["UV"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': reroute})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["X"], 1: reroute_3, 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_44})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: reroute_34, 1: reroute_9, 2: 0.0000}, attrs={'operation': 'MODULO'})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Mosaic Noise"]})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_47})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_48})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_49})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_51})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 0.5000, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_43})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute_42, 'Scale': reroute_44})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': noise_texture.outputs["Fac"]})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_45})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_52})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_50, 6: subtract, 7: reroute_46},
        attrs={'data_type': 'RGBA', 'blend_type': 'DIFFERENCE'})
    
    round = nw.new_node(Nodes.Math, input_kwargs={0: mix_2.outputs[2], 1: 1.3000, 2: 0.0000}, attrs={'operation': 'ROUND'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["Y"], 1: reroute_5, 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: 0.5000, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_51, 6: subtract_1, 7: reroute_52},
        attrs={'data_type': 'RGBA', 'blend_type': 'DIFFERENCE'})
    
    round_1 = nw.new_node(Nodes.Math, input_kwargs={0: mix_3.outputs[2], 1: 1.3000, 2: 0.0000}, attrs={'operation': 'ROUND'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': round, 'Y': round_1, 'Z': 0.2000})
    
    musgrave_texture = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': combine_xyz, 'Scale': 9.4000, 'Detail': 5.0000, 'Dimension': 4.0000, 'Lacunarity': 2.5000, 'Offset': 1.0000},
        attrs={'musgrave_type': 'HETERO_TERRAIN'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': musgrave_texture})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Mosaic Rotation"]})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_16, 1: reroute_15, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    cosine = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: 1.0000, 2: 0.0000}, attrs={'operation': 'COSINE'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: modulo, 1: cosine, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: 1.0000, 2: 0.0000}, attrs={'operation': 'SINE'})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_1})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_35})
    
    modulo_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_36, 1: reroute_7, 2: 0.0000}, attrs={'operation': 'MODULO'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: sine, 1: modulo_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: multiply_4, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: modulo, 1: sine, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: cosine, 1: modulo_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply_5, 1: multiply_6, 2: 0.0000})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract_2, 'Y': add})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': round, 'Y': round_1, 'Z': 16.4000})
    
    musgrave_texture_1 = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': combine_xyz_2, 'Scale': 9.4000, 'Detail': 5.0000, 'Dimension': 4.0000, 'Lacunarity': 2.5000, 'Offset': 1.0000},
        attrs={'musgrave_type': 'HETERO_TERRAIN'})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': musgrave_texture_1})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_21, 1: reroute_13, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': round, 'Y': round_1, 'Z': 8.1000})
    
    musgrave_texture_2 = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': combine_xyz_3, 'Scale': 9.4000, 'Detail': 5.0000, 'Dimension': 4.0000, 'Lacunarity': 2.5000, 'Offset': 1.0000},
        attrs={'musgrave_type': 'HETERO_TERRAIN'})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': musgrave_texture_2})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_19, 1: reroute_6, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_7, 'Y': multiply_8})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: combine_xyz_4, 7: reroute_22},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz_1, 1: mix.outputs[2]})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': add_1.outputs["Vector"]})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Translate X"]})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["X"], 1: reroute_32, 2: 0.0000})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Translate Y"]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["Y"], 1: reroute_30, 2: 0.0000})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_2, 'Y': add_3})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': combine_xyz_5})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_2.outputs["X"]})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Global Rotation"]})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_37})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_38})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_40})
    
    multiply_9 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_39, 1: 3.1410, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: multiply_9, 1: 180.0000, 2: 0.0000}, attrs={'operation': 'DIVIDE'})
    
    cosine_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000, 2: 0.0000}, attrs={'operation': 'COSINE'})
    
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_53, 1: cosine_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_2.outputs["Y"]})
    
    sine_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000, 2: 0.0000}, attrs={'operation': 'SINE'})
    
    multiply_11 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_54, 1: sine_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    subtract_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_10, 1: multiply_11, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_12 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_53, 1: sine_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_13 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_54, 1: cosine_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    add_4 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_12, 1: multiply_13, 2: 0.0000})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract_3, 'Y': add_4})
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': combine_xyz_6})
    
    multiply_14 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_3.outputs["Y"], 1: group_input.outputs["Aspect Ratio"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_3.outputs["X"], 'Y': multiply_14, 'Z': separate_xyz_3.outputs["Z"]})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_6})
    
    checker_texture_1 = nw.new_node(Nodes.CheckerTexture,
        input_kwargs={'Vector': reroute_41, 'Color1': (0.0000, 0.0000, 0.0000, 1.0000), 'Color2': (1.0000, 1.0000, 1.0000, 1.0000), 'Scale': 1.0000})
    
    checker_texture_2 = nw.new_node(Nodes.CheckerTexture,
        input_kwargs={'Vector': reroute_41, 'Color1': (0.0100, 0.0100, 0.0100, 1.0000), 'Color2': (0.7874, 0.7874, 0.7874, 1.0000), 'Scale': 4.0000})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: checker_texture_1.outputs["Color"], 7: checker_texture_2.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'DIFFERENCE'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'UV': combine_xyz_7, 'GridView': mix_1.outputs[2]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_scratch_map_001', singleton=False, type='ShaderNodeTree')
def nodegroup_scratch_map_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Location', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Scratches Scale', 30.0000),
            ('NodeSocketFloat', 'Bias', 0.5000),
            ('NodeSocketFloat', 'Randomize', 1.0000),
            ('NodeSocketFloat', 'Randomize Rotation', 9999.0000),
            ('NodeSocketFloatFactor', 'Dots Presence', 1.0000),
            ('NodeSocketFloatFactor', 'Invert', 0.0000)])
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: group_input.outputs["Vector"], 1: group_input.outputs["Location"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add.outputs["Vector"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute, 'Scale': 10.8500, 'Detail': 7.0000, 'Roughness': 0.9133, 'Distortion': -0.1800})
    
    mix_11 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0070, 6: reroute_4, 7: noise_texture_1.outputs["Fac"]},
        attrs={'data_type': 'RGBA'})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_11.outputs[2]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scratches Scale"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Randomize"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Randomize Rotation"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': group_input.outputs["Bias"], 3: 0.8000})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    group_2 = nw.new_node(nodegroup_scatter_001().name,
        input_kwargs={'Vector': reroute_8, 'Scale Individual': (24.2200, 0.4300, 1.0000), 'Scale Grid': reroute_7, 'Scale Uniform': 0.5000, 'W': reroute_31, 'Min': 0.3000, 'Max': 4.3200, 'Randomize Rotation Individual': reroute_2, 'Bias': reroute_1})
    
    gradient_texture_2 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_2.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_2.outputs["Bias Clamp"]})
    
    mix_14 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_2.outputs["Color"], 7: reroute_29},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: 1.0280}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_31, 1: 99.8500}, attrs={'operation': 'MULTIPLY'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.0700})
    
    group_3 = nw.new_node(nodegroup_scatter_001().name,
        input_kwargs={'Vector': reroute_22, 'Scale Individual': (24.2200, -0.5200, 1.0000), 'Scale Grid': multiply, 'Scale Uniform': 0.5000, 'W': multiply_1, 'Min': 0.3000, 'Max': 3.6700, 'Randomize Rotation Individual': reroute_14, 'Rotation All': 78.7000, 'Bias': add_1})
    
    gradient_texture_1 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_3.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_3.outputs["Bias Clamp"]})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_1.outputs["Color"], 7: reroute_28},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    mix_6 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1533, 6: mix_14.outputs[2], 7: mix_4.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: 0.3200}, attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_31, 1: 155.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    group_5 = nw.new_node(nodegroup_scatter_001().name,
        input_kwargs={'Vector': reroute_20, 'Scale Individual': (24.2200, -0.5200, 1.0000), 'Scale Grid': multiply_2, 'Scale Uniform': 0.5000, 'W': multiply_3, 'Min': 0.3000, 'Max': 3.6700, 'Randomize Rotation Individual': reroute_10, 'Rotation All': 78.7000, 'Bias': reroute_9})
    
    gradient_texture_4 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_5.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_5.outputs["Bias Clamp"]})
    
    mix_13 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_4.outputs["Color"], 7: reroute_27},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.3600, 6: mix_6.outputs[2], 7: mix_13.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_19, 1: 1.3000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_32, 1: 155.7000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.0500})
    
    group_4 = nw.new_node(nodegroup_scatter_001().name,
        input_kwargs={'Vector': reroute_18, 'Scale Individual': (24.2200, -0.5200, 1.0000), 'Scale Grid': multiply_4, 'Scale Uniform': 0.5000, 'W': multiply_5, 'Min': 0.3000, 'Max': 3.6700, 'Randomize Rotation Individual': reroute_12, 'Rotation All': 78.7000, 'Bias': add_2})
    
    gradient_texture_3 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_4.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_4.outputs["Bias Clamp"]})
    
    mix_12 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_3.outputs["Color"], 7: reroute_26},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1993, 6: mix_5.outputs[2], 7: mix_12.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: -0.7500}, attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': reroute_5, 'W': reroute_31, 'Scale': multiply_6},
        attrs={'voronoi_dimensions': '4D', 'feature': 'DISTANCE_TO_EDGE'})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Distance"]})
    colorramp_4.color_ramp.elements[0].position = 0.0000
    colorramp_4.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.0026
    colorramp_4.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': multiply_6, 'Detail': 5.0000, 'Roughness': 0.8467, 'Distortion': -0.0900})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_5.color_ramp.elements[0].position = 0.5455
    colorramp_5.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.6982
    colorramp_5.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_10 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_25, 6: colorramp_5.outputs["Color"], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    mix_8 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_4.outputs["Color"], 7: mix_10.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_8.outputs[2]})
    
    mix_9 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_7.outputs[2], 7: reroute_23},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': noise_texture_1.outputs["Fac"]})
    
    mix_16 = nw.new_node(Nodes.Mix, input_kwargs={0: 0.0143, 6: reroute_38, 7: reroute_39}, attrs={'data_type': 'RGBA'})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_44})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_40, 1: 4.0000}, attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture_1 = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mix_16.outputs[2], 'W': reroute_45, 'Scale': multiply_7},
        attrs={'voronoi_dimensions': '4D'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_1.outputs["Distance"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.0463
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_40, 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture_2 = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mix_16.outputs[2], 'W': reroute_43, 'Scale': multiply_8},
        attrs={'voronoi_dimensions': '4D'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_2.outputs["Distance"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.0693
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp.outputs["Color"], 7: colorramp_1.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    mix_17 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["Dots Presence"], 6: mix_9.outputs[2], 7: mix_1.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Fac': group_input.outputs["Invert"], 'Color': mix_17.outputs[2]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Height': invert}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_scatter', singleton=False, type='ShaderNodeTree')
def nodegroup_scatter(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Scale Individual', (1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloat', 'Scale Grid', 5.0000),
            ('NodeSocketFloat', 'Scale Uniform', 1.0000),
            ('NodeSocketFloat', 'W', 0.0000),
            ('NodeSocketFloat', 'Min', 1.0000),
            ('NodeSocketFloat', 'Max', 1.0000),
            ('NodeSocketFloat', 'Randomize Rotation Individual', 0.0000),
            ('NodeSocketFloat', 'Rotation All', 0.0000),
            ('NodeSocketFloat', 'Bias', 0.5000)])
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: group_input.outputs["Vector"], 'Scale': group_input.outputs["Scale Grid"]},
        attrs={'operation': 'SCALE'})
    
    fraction = nw.new_node(Nodes.VectorMath, input_kwargs={0: scale.outputs["Vector"]}, attrs={'operation': 'FRACTION'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': -0.5000, 'Y': -0.5000, 'Z': -0.5000})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: fraction.outputs["Vector"], 1: combine_xyz})
    
    ceil = nw.new_node(Nodes.VectorMath, input_kwargs={0: scale.outputs["Vector"]}, attrs={'operation': 'CEIL'})
    
    white_noise_texture = nw.new_node(Nodes.WhiteNoiseTexture,
        input_kwargs={'Vector': ceil.outputs["Vector"], 'W': group_input.outputs["W"]},
        attrs={'noise_dimensions': '4D'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': white_noise_texture.outputs["Value"], 3: group_input.outputs["Min"], 4: group_input.outputs["Max"]})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add.outputs["Vector"], 'Scale': map_range.outputs["Result"]},
        attrs={'operation': 'SCALE'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: white_noise_texture.outputs["Value"], 1: group_input.outputs["Randomize Rotation Individual"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: group_input.outputs["Rotation All"]})
    
    radians = nw.new_node(Nodes.Math, input_kwargs={0: add_1}, attrs={'operation': 'RADIANS'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate, input_kwargs={'Vector': scale_1.outputs["Vector"], 'Angle': radians})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: vector_rotate, 'Scale': group_input.outputs["Scale Uniform"]},
        attrs={'operation': 'SCALE'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale_2.outputs["Vector"], 1: group_input.outputs["Scale Individual"], 'Scale': 0.5900},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: white_noise_texture.outputs["Value"], 1: group_input.outputs["Bias"]},
        attrs={'operation': 'GREATER_THAN'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Vector': multiply_1.outputs["Vector"], 'Bias Clamp': greater_than, 'Bias ': white_noise_texture.outputs["Value"], 'Color': white_noise_texture.outputs["Color"]},
        attrs={'is_active_output': True})

def shader_clay_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'test'})
    
    group_1 = nw.new_node(nodegroup_uber_mapping__tile_rotation_001().name,
        input_kwargs={'UV': attribute.outputs["Vector"], 'Scale': 1.4300})
    
    group_2 = nw.new_node(nodegroup_scratch_map_001().name,
        input_kwargs={'Vector': group_1.outputs["UV"], 'Scratches Scale': 15.0000})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': attribute.outputs["Vector"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute, 'Scale': 6.5000})
    
    group_3 = nw.new_node(nodegroup_color_ramp_math_001().name,
        input_kwargs={'Fac': noise_texture_1.outputs["Color"], 'Color1': (0.5210, 0.1274, 0.0409, 1.0000), 'Pos 1': 0.5800, 'Color2': (0.1270, 0.0347, 0.0128, 1.0000)})
    
    wave_texture_1 = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': reroute, 'Scale': 2.0000, 'Distortion': 0.2500, 'Detail': 2.9000, 'Phase Offset': 194.0000},
        attrs={'bands_direction': 'Y'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': wave_texture_1.outputs["Color"], 'Scale': 6.5000})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Color"]}, attrs={'operation': 'GREATER_THAN'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1067, 6: group_3, 7: greater_than},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    group = nw.new_node(nodegroup_uber_mapping__tile_rotation_001().name,
        input_kwargs={'UV': attribute.outputs["Vector"], 'Scale': 2.0200, 'Global Rotation': 15.7000, 'Mosaic Rotation': 34.1000})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': group.outputs["UV"]},
        attrs={'image': bpy.data.images['33b2720a9e220549c3eac6bf8ae21c296cdb95d1.jpeg.001']})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.9394, 0.9394, 0.9394, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 1.0000
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_2.outputs[2], 7: colorramp_2.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_2, 6: mix_1.outputs[2], 7: (0.0933, 0.0933, 0.0933, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.8317, 0.8317, 0.8317, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [0.3860, 0.3860, 0.3860, 1.0000]
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.9930, 0.9930, 0.9930, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': attribute.outputs["Vector"], 'Scale': 50.0000, 'Distortion': 6.0000, 'Detail': 2.9000, 'Phase Offset': 194.0000},
        attrs={'bands_direction': 'Y'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0047, 6: colorramp.outputs["Color"], 7: wave_texture.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_2, 6: mix.outputs[2], 7: (0.0320, 0.0320, 0.0320, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.4867, 'Distance': 0.3400, 'Height': mix_3.outputs[2]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_4.outputs[2], 'Roughness': colorramp_1.outputs["Color"], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_to_pipe_001', singleton=False, type='GeometryNodeTree')
def nodegroup_to_pipe_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Curve', None),
            ('NodeSocketFloatDistance', 'Profile Radius', 0.5000),
            ('NodeSocketInt', 'Profile Resolution', 20),
            ('NodeSocketFloatDistance', 'Curve Radius', 1.0000),
            ('NodeSocketBool', 'Fill Caps', False),
            ('NodeSocketBool', 'NURBS', False),
            ('NodeSocketBool', 'Selection', True),
            ('NodeSocketBool', 'Arc', False),
            ('NodeSocketFloatAngle', 'Arc Angle', 6.2832)])
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["NURBS"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Curve"]})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_36})
    
    separate_components = nw.new_node(Nodes.SeparateComponents, input_kwargs={'Geometry': reroute_37})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_components.outputs["Curve"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Selection"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Curve Radius"]})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_1, 'Selection': reroute_6, 'Radius': reroute_33})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_curve_radius})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': set_curve_radius}, attrs={'spline_type': 'NURBS'})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_spline_type})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_41})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_15, 14: reroute_38, 15: reroute_40})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch.outputs[6]})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_43})
    
    spline_parameter_3 = nw.new_node(Nodes.SplineParameter)
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': spline_parameter_3.outputs["Factor"]})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_47})
    
    capture_attribute_3 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': reroute_42, 2: reroute_48})
    
    reroute_60 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_3.outputs["Geometry"]})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_60})
    
    reroute_118 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Arc"]})
    
    reroute_116 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_118})
    
    reroute_122 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_116})
    
    reroute_123 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_122})
    
    reroute_124 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_123})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Profile Resolution"]})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Profile Radius"]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_22, 'Radius': reroute_26})
    
    reroute_102 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute_103 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    reroute_126 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Arc Angle"]})
    
    reroute_117 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_126})
    
    reroute_125 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_117})
    
    arc = nw.new_node('GeometryNodeCurveArc',
        input_kwargs={'Resolution': reroute_102, 'Radius': reroute_103, 'Sweep Angle': reroute_125})
    
    switch_2 = nw.new_node(Nodes.Switch,
        input_kwargs={1: reroute_124, 14: curve_circle.outputs["Curve"], 15: arc.outputs["Curve"]})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': switch_2.outputs[6], 2: spline_parameter.outputs["Factor"]})
    
    reroute_72 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs["Geometry"]})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_72})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Fill Caps"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': reroute_50, 'Profile Curve': reroute_49, 'Fill Caps': reroute_17})
    
    reroute_55 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs[2]})
    
    reroute_86 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_55})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_3.outputs[2]})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_54})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_86, 'Y': reroute_53})
    
    capture_attribute_5 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_to_mesh, 1: combine_xyz_1},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_63 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_5.outputs["Geometry"]})
    
    reroute_64 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_63})
    
    reroute_62 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_53})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_62}, attrs={'operation': 'EQUAL'})
    
    reroute_61 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_62})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_61, 1: 0.9990}, attrs={'operation': 'SUBTRACT'})
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={0: subtract}, attrs={'operation': 'EQUAL'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: equal, 1: equal_1})
    
    separate_geometry_1 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_64, 'Selection': add},
        attrs={'domain': 'FACE'})
    
    reroute_70 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_5.outputs["Attribute"]})
    
    reroute_69 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_70})
    
    reroute_68 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_69})
    
    capture_attribute_8 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': separate_geometry_1.outputs["Inverted"], 1: reroute_68},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_65 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_64})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_65, 'Selection': add},
        attrs={'domain': 'EDGE'})
    
    uv_unwrap = nw.new_node('GeometryNodeUVUnwrap', input_kwargs={'Seam': add})
    
    capture_attribute_6 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': separate_geometry.outputs["Selection"], 1: uv_unwrap},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [capture_attribute_8.outputs["Geometry"], capture_attribute_6.outputs["Geometry"]]})
    
    reroute_71 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_1})
    
    reroute_67 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_6.outputs["Attribute"]})
    
    reroute_66 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_67})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: capture_attribute_8.outputs["Attribute"], 1: reroute_66})
    
    reroute_74 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_1.outputs["Vector"]})
    
    reroute_73 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_74})
    
    capture_attribute_7 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': reroute_71, 1: reroute_73},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_93 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_7.outputs["Geometry"]})
    
    reroute_92 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_93})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': separate_components.outputs["Mesh"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_34})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius,
        input_kwargs={'Curve': mesh_to_curve, 'Selection': reroute_4, 'Radius': reroute_35})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_curve_radius_1})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    set_spline_type_1 = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': set_curve_radius_1}, attrs={'spline_type': 'NURBS'})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_spline_type_1})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_7, 14: reroute_2, 15: reroute_44})
    
    spline_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': spline_parameter_2.outputs["Factor"]})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_46})
    
    capture_attribute_2 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': switch_1.outputs[6], 2: reroute_45})
    
    reroute_114 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_2.outputs["Geometry"]})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_114})
    
    reroute_119 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_118})
    
    reroute_120 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_119})
    
    reroute_121 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_120})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_21, 'Radius': reroute_27})
    
    reroute_106 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute_107 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_127 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_126})
    
    reroute_128 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_127})
    
    reroute_129 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_128})
    
    arc_1 = nw.new_node('GeometryNodeCurveArc',
        input_kwargs={'Resolution': reroute_106, 'Radius': reroute_107, 'Sweep Angle': reroute_129})
    
    switch_3 = nw.new_node(Nodes.Switch,
        input_kwargs={1: reroute_121, 14: curve_circle_1.outputs["Curve"], 15: arc_1.outputs["Curve"]})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': switch_3.outputs[6], 2: spline_parameter_1.outputs["Factor"]})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs["Geometry"]})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_58})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': reroute_52, 'Profile Curve': reroute_51, 'Fill Caps': reroute_16})
    
    reroute_59 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs[2]})
    
    reroute_57 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_59})
    
    reroute_115 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_2.outputs[2]})
    
    reroute_56 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_115})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_57, 'Y': reroute_56})
    
    capture_attribute_4 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_to_mesh_1, 1: combine_xyz},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_90 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_4.outputs["Geometry"]})
    
    reroute_79 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_90})
    
    reroute_80 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_79})
    
    reroute_75 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_56})
    
    reroute_76 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_75})
    
    equal_2 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_76}, attrs={'operation': 'EQUAL'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_75, 1: 0.9990}, attrs={'operation': 'SUBTRACT'})
    
    equal_3 = nw.new_node(Nodes.Compare, input_kwargs={0: subtract_1}, attrs={'operation': 'EQUAL'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: equal_2, 1: equal_3})
    
    separate_geometry_3 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_80, 'Selection': add_2},
        attrs={'domain': 'FACE'})
    
    reroute_89 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_4.outputs["Attribute"]})
    
    reroute_77 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_89})
    
    reroute_84 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_77})
    
    reroute_83 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_84})
    
    capture_attribute_10 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': separate_geometry_3.outputs["Inverted"], 1: reroute_83},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    separate_geometry_2 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_79, 'Selection': add_2},
        attrs={'domain': 'EDGE'})
    
    uv_unwrap_1 = nw.new_node('GeometryNodeUVUnwrap', input_kwargs={'Seam': add_2})
    
    capture_attribute_9 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': separate_geometry_2.outputs["Selection"], 1: uv_unwrap_1},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [capture_attribute_10.outputs["Geometry"], capture_attribute_9.outputs["Geometry"]]})
    
    reroute_85 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_2})
    
    reroute_81 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_9.outputs["Attribute"]})
    
    reroute_82 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_81})
    
    add_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: capture_attribute_10.outputs["Attribute"], 1: reroute_82})
    
    reroute_88 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_3.outputs["Vector"]})
    
    reroute_87 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_88})
    
    capture_attribute_11 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': reroute_85, 1: reroute_87},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_109 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_11.outputs["Geometry"]})
    
    reroute_108 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_109})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_92, reroute_108]})
    
    reroute_111 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_11.outputs["Attribute"]})
    
    reroute_110 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_111})
    
    reroute_113 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_7.outputs["Attribute"]})
    
    reroute_112 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_113})
    
    add_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_110, 1: reroute_112})
    
    reroute_94 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_59})
    
    reroute_95 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_94})
    
    reroute_97 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_54})
    
    reroute_96 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_97})
    
    add_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_95, 1: reroute_96})
    
    reroute_91 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_5})
    
    reroute_78 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_91})
    
    reroute_104 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_86})
    
    reroute_105 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_115})
    
    add_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_104, 1: reroute_105})
    
    reroute_98 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_6})
    
    reroute_99 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_98})
    
    reroute_100 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_99})
    
    reroute_101 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_100})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': join_geometry, 'UV': add_4.outputs["Vector"], 'Factor': reroute_78, 'Profile Factor': reroute_101},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_solidfy_001', singleton=False, type='GeometryNodeTree')
def nodegroup_solidfy_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Mesh', None),
            ('NodeSocketFloatDistance', 'Thickness', 1.0000),
            ('NodeSocketBool', 'Selection', True),
            ('NodeSocketBool', 'Individual', False),
            ('NodeSocketVectorTranslation', 'Offset', (0.0000, 0.0000, 0.0000))])
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Thickness"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={0: reroute}, attrs={'operation': 'LESS_THAN'})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Mesh"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Selection"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Individual"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': reroute_30, 'Selection': reroute_3, 'Offset': group_input.outputs["Offset"], 'Offset Scale': reroute_1, 'Individual': reroute_4})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': reroute_30})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [extrude_mesh.outputs["Mesh"], flip_faces]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry})
    
    flip_faces_1 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': merge_by_distance})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: less_than, 14: merge_by_distance, 15: flip_faces_1})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': extrude_mesh.outputs["Top"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': extrude_mesh.outputs["Side"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: reroute_8})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': extrude_mesh.outputs["Top"]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': extrude_mesh.outputs["Side"]})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': switch.outputs[6], 'Offset': reroute_15, 'Top': reroute_13, 'Side': reroute_14},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_uber_mapping__tile_rotation', singleton=False, type='ShaderNodeTree')
def nodegroup_uber_mapping__tile_rotation(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'UV', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Scale', 1.0000),
            ('NodeSocketFloat', 'Aspect Ratio', 1.0000),
            ('NodeSocketFloat', 'Translate X', 0.0000),
            ('NodeSocketFloat', 'Translate Y', 0.0000),
            ('NodeSocketFloat', 'Global Rotation', 0.0000),
            ('NodeSocketFloat', 'Mosaic Rotation', 0.0000),
            ('NodeSocketFloat', 'Mosaic Noise', 0.0000)])
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["UV"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': reroute})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["X"], 1: reroute_3, 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_44})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: reroute_34, 1: reroute_9, 2: 0.0000}, attrs={'operation': 'MODULO'})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Mosaic Noise"]})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_47})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_48})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_49})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_51})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 0.5000, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_43})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute_42, 'Scale': reroute_44})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': noise_texture.outputs["Fac"]})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_45})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_52})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_50, 6: subtract, 7: reroute_46},
        attrs={'data_type': 'RGBA', 'blend_type': 'DIFFERENCE'})
    
    round = nw.new_node(Nodes.Math, input_kwargs={0: mix_2.outputs[2], 1: 1.3000, 2: 0.0000}, attrs={'operation': 'ROUND'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["Y"], 1: reroute_5, 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: 0.5000, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_51, 6: subtract_1, 7: reroute_52},
        attrs={'data_type': 'RGBA', 'blend_type': 'DIFFERENCE'})
    
    round_1 = nw.new_node(Nodes.Math, input_kwargs={0: mix_3.outputs[2], 1: 1.3000, 2: 0.0000}, attrs={'operation': 'ROUND'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': round, 'Y': round_1, 'Z': 0.2000})
    
    musgrave_texture = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': combine_xyz, 'Scale': 9.4000, 'Detail': 5.0000, 'Dimension': 4.0000, 'Lacunarity': 2.5000, 'Offset': 1.0000},
        attrs={'musgrave_type': 'HETERO_TERRAIN'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': musgrave_texture})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Mosaic Rotation"]})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_16, 1: reroute_15, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    cosine = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: 1.0000, 2: 0.0000}, attrs={'operation': 'COSINE'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: modulo, 1: cosine, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: 1.0000, 2: 0.0000}, attrs={'operation': 'SINE'})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_1})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_35})
    
    modulo_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_36, 1: reroute_7, 2: 0.0000}, attrs={'operation': 'MODULO'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: sine, 1: modulo_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: multiply_4, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: modulo, 1: sine, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: cosine, 1: modulo_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply_5, 1: multiply_6, 2: 0.0000})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract_2, 'Y': add})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': round, 'Y': round_1, 'Z': 16.4000})
    
    musgrave_texture_1 = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': combine_xyz_2, 'Scale': 9.4000, 'Detail': 5.0000, 'Dimension': 4.0000, 'Lacunarity': 2.5000, 'Offset': 1.0000},
        attrs={'musgrave_type': 'HETERO_TERRAIN'})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': musgrave_texture_1})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_21, 1: reroute_13, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': round, 'Y': round_1, 'Z': 8.1000})
    
    musgrave_texture_2 = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': combine_xyz_3, 'Scale': 9.4000, 'Detail': 5.0000, 'Dimension': 4.0000, 'Lacunarity': 2.5000, 'Offset': 1.0000},
        attrs={'musgrave_type': 'HETERO_TERRAIN'})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': musgrave_texture_2})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_19, 1: reroute_6, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_7, 'Y': multiply_8})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: combine_xyz_4, 7: reroute_22},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz_1, 1: mix.outputs[2]})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': add_1.outputs["Vector"]})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Translate X"]})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["X"], 1: reroute_32, 2: 0.0000})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Translate Y"]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["Y"], 1: reroute_30, 2: 0.0000})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_2, 'Y': add_3})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': combine_xyz_5})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_2.outputs["X"]})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Global Rotation"]})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_37})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_38})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_40})
    
    multiply_9 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_39, 1: 3.1410, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: multiply_9, 1: 180.0000, 2: 0.0000}, attrs={'operation': 'DIVIDE'})
    
    cosine_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000, 2: 0.0000}, attrs={'operation': 'COSINE'})
    
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_53, 1: cosine_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_2.outputs["Y"]})
    
    sine_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000, 2: 0.0000}, attrs={'operation': 'SINE'})
    
    multiply_11 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_54, 1: sine_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    subtract_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_10, 1: multiply_11, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_12 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_53, 1: sine_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_13 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_54, 1: cosine_1, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    add_4 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_12, 1: multiply_13, 2: 0.0000})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract_3, 'Y': add_4})
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': combine_xyz_6})
    
    multiply_14 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_3.outputs["Y"], 1: group_input.outputs["Aspect Ratio"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_3.outputs["X"], 'Y': multiply_14, 'Z': separate_xyz_3.outputs["Z"]})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_6})
    
    checker_texture_1 = nw.new_node(Nodes.CheckerTexture,
        input_kwargs={'Vector': reroute_41, 'Color1': (0.0000, 0.0000, 0.0000, 1.0000), 'Color2': (1.0000, 1.0000, 1.0000, 1.0000), 'Scale': 1.0000})
    
    checker_texture_2 = nw.new_node(Nodes.CheckerTexture,
        input_kwargs={'Vector': reroute_41, 'Color1': (0.0100, 0.0100, 0.0100, 1.0000), 'Color2': (0.7874, 0.7874, 0.7874, 1.0000), 'Scale': 4.0000})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: checker_texture_1.outputs["Color"], 7: checker_texture_2.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'DIFFERENCE'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'UV': combine_xyz_7, 'GridView': mix_1.outputs[2]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_color_ramp_math', singleton=False, type='ShaderNodeTree')
def nodegroup_color_ramp_math(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Fac', 0.5000),
            ('NodeSocketColor', 'Color1', (1.0000, 1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloat', 'Pos 1', 1.0000),
            ('NodeSocketColor', 'Color2', (0.0000, 0.0000, 0.0000, 1.0000)),
            ('NodeSocketFloat', 'Pos 2', 0.0000)])
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Pos 2"], 1: group_input.outputs["Pos 1"]},
        attrs={'operation': 'SUBTRACT'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: subtract}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: group_input.outputs["Fac"]}, attrs={'operation': 'MULTIPLY'})
    
    subtract_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Pos 1"], 1: group_input.outputs["Pos 2"]},
        attrs={'operation': 'SUBTRACT'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Pos 1"], 1: subtract_1}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: divide_1})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: add, 6: group_input.outputs["Color1"], 7: group_input.outputs["Color2"]},
        attrs={'data_type': 'RGBA'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Color': mix_2.outputs[2]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_scratch_map', singleton=False, type='ShaderNodeTree')
def nodegroup_scratch_map(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Location', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Scratches Scale', 30.0000),
            ('NodeSocketFloat', 'Bias', 0.5000),
            ('NodeSocketFloat', 'Randomize', 1.0000),
            ('NodeSocketFloat', 'Randomize Rotation', 9999.0000),
            ('NodeSocketFloatFactor', 'Dots Presence', 1.0000),
            ('NodeSocketFloatFactor', 'Invert', 0.0000)])
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: group_input.outputs["Vector"], 1: group_input.outputs["Location"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add.outputs["Vector"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute, 'Scale': 10.8500, 'Detail': 7.0000, 'Roughness': 0.9133, 'Distortion': -0.1800})
    
    mix_11 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0070, 6: reroute_4, 7: noise_texture_1.outputs["Fac"]},
        attrs={'data_type': 'RGBA'})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_11.outputs[2]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scratches Scale"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Randomize"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Randomize Rotation"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': group_input.outputs["Bias"], 3: 0.8000})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    group_2 = nw.new_node(nodegroup_scatter().name,
        input_kwargs={'Vector': reroute_8, 'Scale Individual': (24.2200, 0.4300, 1.0000), 'Scale Grid': reroute_7, 'Scale Uniform': 0.5000, 'W': reroute_31, 'Min': 0.3000, 'Max': 4.3200, 'Randomize Rotation Individual': reroute_2, 'Bias': reroute_1})
    
    gradient_texture_2 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_2.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_2.outputs["Bias Clamp"]})
    
    mix_14 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_2.outputs["Color"], 7: reroute_29},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: 1.0280}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_31, 1: 99.8500}, attrs={'operation': 'MULTIPLY'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.0700})
    
    group_3 = nw.new_node(nodegroup_scatter().name,
        input_kwargs={'Vector': reroute_22, 'Scale Individual': (24.2200, -0.5200, 1.0000), 'Scale Grid': multiply, 'Scale Uniform': 0.5000, 'W': multiply_1, 'Min': 0.3000, 'Max': 3.6700, 'Randomize Rotation Individual': reroute_14, 'Rotation All': 78.7000, 'Bias': add_1})
    
    gradient_texture_1 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_3.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_3.outputs["Bias Clamp"]})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_1.outputs["Color"], 7: reroute_28},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    mix_6 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1533, 6: mix_14.outputs[2], 7: mix_4.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: 0.3200}, attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_31, 1: 155.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    group_5 = nw.new_node(nodegroup_scatter().name,
        input_kwargs={'Vector': reroute_20, 'Scale Individual': (24.2200, -0.5200, 1.0000), 'Scale Grid': multiply_2, 'Scale Uniform': 0.5000, 'W': multiply_3, 'Min': 0.3000, 'Max': 3.6700, 'Randomize Rotation Individual': reroute_10, 'Rotation All': 78.7000, 'Bias': reroute_9})
    
    gradient_texture_4 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_5.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_5.outputs["Bias Clamp"]})
    
    mix_13 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_4.outputs["Color"], 7: reroute_27},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.3600, 6: mix_6.outputs[2], 7: mix_13.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_19, 1: 1.3000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_32, 1: 155.7000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.0500})
    
    group_4 = nw.new_node(nodegroup_scatter().name,
        input_kwargs={'Vector': reroute_18, 'Scale Individual': (24.2200, -0.5200, 1.0000), 'Scale Grid': multiply_4, 'Scale Uniform': 0.5000, 'W': multiply_5, 'Min': 0.3000, 'Max': 3.6700, 'Randomize Rotation Individual': reroute_12, 'Rotation All': 78.7000, 'Bias': add_2})
    
    gradient_texture_3 = nw.new_node(Nodes.GradientTexture,
        input_kwargs={'Vector': group_4.outputs["Vector"]},
        attrs={'gradient_type': 'SPHERICAL'})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_4.outputs["Bias Clamp"]})
    
    mix_12 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: gradient_texture_3.outputs["Color"], 7: reroute_26},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1993, 6: mix_5.outputs[2], 7: mix_12.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: -0.7500}, attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': reroute_5, 'W': reroute_31, 'Scale': multiply_6},
        attrs={'voronoi_dimensions': '4D', 'feature': 'DISTANCE_TO_EDGE'})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Distance"]})
    colorramp_4.color_ramp.elements[0].position = 0.0000
    colorramp_4.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.0026
    colorramp_4.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': multiply_6, 'Detail': 5.0000, 'Roughness': 0.8467, 'Distortion': -0.0900})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_5.color_ramp.elements[0].position = 0.5455
    colorramp_5.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.6982
    colorramp_5.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_10 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_25, 6: colorramp_5.outputs["Color"], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    mix_8 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_4.outputs["Color"], 7: mix_10.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'DARKEN'})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_8.outputs[2]})
    
    mix_9 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix_7.outputs[2], 7: reroute_23},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': noise_texture_1.outputs["Fac"]})
    
    mix_16 = nw.new_node(Nodes.Mix, input_kwargs={0: 0.0143, 6: reroute_38, 7: reroute_39}, attrs={'data_type': 'RGBA'})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_44})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_40, 1: 4.0000}, attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture_1 = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mix_16.outputs[2], 'W': reroute_45, 'Scale': multiply_7},
        attrs={'voronoi_dimensions': '4D'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_1.outputs["Distance"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.0463
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_40, 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture_2 = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mix_16.outputs[2], 'W': reroute_43, 'Scale': multiply_8},
        attrs={'voronoi_dimensions': '4D'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_2.outputs["Distance"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.0693
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp.outputs["Color"], 7: colorramp_1.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    mix_17 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["Dots Presence"], 6: mix_9.outputs[2], 7: mix_1.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Fac': group_input.outputs["Invert"], 'Color': mix_17.outputs[2]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Height': invert}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_pottery_v1_001', singleton=False, type='GeometryNodeTree')
def nodegroup_pottery_v1_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatDistance', 'Profile Radius', 0.2500),
            ('NodeSocketInt', 'Profile Resolution', 32),
            ('NodeSocketInt', 'Curve Resolution', 32),
            ('NodeSocketFloatDistance', 'Height', 0.5000),
            ('NodeSocketFloat', 'Seed', 0.0000),
            ('NodeSocketFloat', 'Noise Scale', 3.0000),
            ('NodeSocketFloatFactor', 'Ridges', 0.0000),
            ('NodeSocketFloatDistance', 'Thickness', -0.0250),
            ('NodeSocketFloat', 'Shape Min', 0.0000),
            ('NodeSocketFloat', 'Shape Max', 1.0000),
            ('NodeSocketMaterial', 'Material', None), #surface.shaderfunc_to_material(shader_clay_001)
            ('NodeSocketString', 'UV Name', 'UV_Pot')])
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Height"]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_29})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Curve Resolution"]})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': reroute_23})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': resample_curve})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_38})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Seed"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Noise Scale"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Ridges"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': reroute, 'Scale': reroute_2, 'Roughness': 0.0000, 'Distortion': reroute_1},
        attrs={'noise_dimensions': '4D'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.3309
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.6182
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve,
        input_kwargs={'Factor': colorramp.outputs["Color"], 'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 1.0000), (1.0000, 1.0000)])
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': float_curve})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shape Min"]})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shape Max"]})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_34})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_8, 3: reroute_36, 4: reroute_35})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    to_pipe_001 = nw.new_node(nodegroup_to_pipe_001().name,
        input_kwargs={'Curve': reroute_37, 'Profile Radius': group_input.outputs["Profile Radius"], 'Profile Resolution': group_input.outputs["Profile Resolution"], 'Curve Radius': reroute_31, 'Fill Caps': True, 'Arc Angle': 6.2795})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["UV Name"]})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': to_pipe_001.outputs["Mesh"], 'Name': reroute_22, 3: to_pipe_001.outputs["UV"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Material"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': store_named_attribute, 'Material': reroute_14})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': to_pipe_001.outputs["Factor"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_6, 1: 0.9990})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': set_material_2, 'Selection': greater_than},
        attrs={'domain': 'FACE'})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Thickness"]})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    solidfy_001 = nw.new_node(nodegroup_solidfy_001().name,
        input_kwargs={'Mesh': delete_geometry, 'Thickness': reroute_10, 'Offset': normal})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': solidfy_001.outputs["Geometry"], 'UV': to_pipe_001.outputs["UV"], 'Factor': to_pipe_001.outputs["Factor"], 'Profile Factor': to_pipe_001.outputs["Profile Factor"]},
        attrs={'is_active_output': True})

def shader_clay(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'UV_Pot'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': attribute.outputs["Vector"]})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'seed'})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': reroute_33, 'W': attribute_1.outputs["Fac"], 'Scale': 18.1000},
        attrs={'voronoi_dimensions': '4D'})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Distance"]})
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.1600
    colorramp_3.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    voronoi_texture_1 = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': reroute_33, 'W': attribute_1.outputs["Fac"], 'Scale': 27.1000},
        attrs={'voronoi_dimensions': '4D'})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_1.outputs["Distance"]})
    colorramp_4.color_ramp.elements[0].position = 0.0000
    colorramp_4.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.1018
    colorramp_4.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_3.outputs["Color"], 7: colorramp_4.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    group_2 = nw.new_node(nodegroup_scratch_map().name,
        input_kwargs={'Vector': reroute_14, 'Scratches Scale': 15.0000, 'Randomize': attribute_1.outputs["Fac"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_2})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_15, 'W': attribute_1.outputs["Fac"], 'Scale': 3.0000, 'Detail': 7.5000, 'Roughness': 0.7188},
        attrs={'noise_dimensions': '4D'})
    
    group_3 = nw.new_node(nodegroup_color_ramp_math().name,
        input_kwargs={'Fac': noise_texture_1.outputs["Color"], 'Color1': (0.6769, 0.1632, 0.0514, 1.0000), 'Pos 1': 0.7000, 'Color2': (0.2517, 0.0648, 0.0220, 1.0000), 'Pos 2': 0.3000})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_3})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    wave_texture_1 = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': reroute, 'Scale': 2.0000, 'Distortion': 5.0000, 'Detail': 2.9000, 'Phase Offset': 194.0000},
        attrs={'bands_direction': 'Y'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': wave_texture_1.outputs["Color"], 'Scale': 10.0000})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': noise_texture.outputs["Fac"], 1: -0.0500, 2: 1.0800, 3: -7.0400, 4: 7.8200})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0500, 6: reroute_29, 7: reroute_31},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_2.outputs[2]})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    group = nw.new_node(nodegroup_uber_mapping__tile_rotation().name,
        input_kwargs={'UV': reroute_13, 'Scale': 2.0200, 'Global Rotation': 15.7000, 'Mosaic Rotation': 34.1000})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': group.outputs["UV"]},
        attrs={'image': bpy.data.images['33b2720a9e220549c3eac6bf8ae21c296cdb95d1.jpeg']})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': image_texture.outputs["Color"]})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_17})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.9394, 0.9394, 0.9394, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 1.0000
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': colorramp_2.outputs["Color"]})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: reroute_20, 7: reroute_21},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_1.outputs[2]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_3, 6: reroute_4, 7: (0.0933, 0.0933, 0.0933, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_6 = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_5.outputs[2], 6: mix_4.outputs[2], 7: (0.1506, 0.1506, 0.1506, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_16})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.8317, 0.8317, 0.8317, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [0.2536, 0.2536, 0.2536, 1.0000]
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': colorramp_1.outputs["Color"]})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_18})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.9930, 0.9930, 0.9930, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': colorramp.outputs["Color"]})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': reroute_1, 'Scale': 70.0000, 'Distortion': 6.0000, 'Detail': 2.9000, 'Phase Offset': 194.0000},
        attrs={'bands_direction': 'Y'})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': wave_texture.outputs["Color"]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    mix = nw.new_node(Nodes.Mix, input_kwargs={0: 0.0047, 6: reroute_27, 7: reroute_9}, attrs={'data_type': 'RGBA'})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix.outputs[2]})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: reroute_8, 6: reroute_23, 7: (0.0320, 0.0320, 0.0320, 1.0000)},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_5.outputs[2], 6: mix_3.outputs[2], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.4867, 'Distance': 0.3400, 'Height': mix_7.outputs[2]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_6.outputs[2], 'Roughness': reroute_25, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatDistance', 'Profile Radius', 0.2500),
            ('NodeSocketInt', 'Profile Resolution', 32),
            ('NodeSocketInt', 'Curve Resolution', 32),
            ('NodeSocketFloatDistance', 'Height', 0.5000),
            ('NodeSocketFloat', 'Seed', 0.0000),
            ('NodeSocketFloat', 'Noise Scale', 3.0000),
            ('NodeSocketFloatFactor', 'Ridges', 0.0000),
            ('NodeSocketFloatDistance', 'Thickness', -0.0250),
            ('NodeSocketFloat', 'Shape Min', 0.0000),
            ('NodeSocketFloat', 'Shape Max', 1.0000),
            ('NodeSocketMaterial', 'Material', None), #surface.shaderfunc_to_material(shader_clay)
            ('NodeSocketString', 'UV Name', 'UV_Pot')])
    
    pottery_v1_001 = nw.new_node(nodegroup_pottery_v1_001().name,
        input_kwargs={'Profile Radius': group_input.outputs["Profile Radius"], 'Profile Resolution': group_input.outputs["Profile Resolution"], 'Curve Resolution': group_input.outputs["Curve Resolution"], 'Height': group_input.outputs["Height"], 'Seed': group_input.outputs["Seed"], 'Noise Scale': group_input.outputs["Noise Scale"], 'Ridges': group_input.outputs["Ridges"], 'Thickness': group_input.outputs["Thickness"], 'Shape Min': group_input.outputs["Shape Min"], 'Shape Max': group_input.outputs["Shape Max"], 'Material': group_input.outputs["Material"], 'UV Name': group_input.outputs["UV Name"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': pottery_v1_001.outputs["Geometry"], 'Seed': group_input.outputs["Seed"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_clay, selection=selection)


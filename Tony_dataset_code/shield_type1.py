import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_shield_handle_gen', singleton=False, type='GeometryNodeTree')
def nodegroup_shield_handle_gen(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    mesh_line = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': 16, 'Start Location': (-1.0000, 0.0000, 0.0000), 'Offset': (1.0000, 0.0000, 0.0000)},
        attrs={'mode': 'END_POINTS'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["X"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["Y"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["Z"]})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"]}, attrs={'operation': 'ABSOLUTE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: absolute})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': add})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0909, 0.0750), (0.5818, 0.2500), (0.9955, 0.9500)])
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_6, 'Y': reroute_5, 'Z': float_curve})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_line, 'Position': combine_xyz})
    
    group_input_2 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Width', 0.0000),
            ('NodeSocketFloat', 'Height', 0.0000),
            ('NodeSocketFloat', 'Thickness', 0.0000),
            ('NodeSocketInt', 'Handle Resolution', 4),
            ('NodeSocketBool', 'Studs', False),
            ('NodeSocketInt', 'Stud Amount', 10),
            ('NodeSocketInt', 'Stud Resolution', 4),
            ('NodeSocketBool', 'Smooth Studs', False)])
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': set_position, 'Scale': group_input_2.outputs["Width"]},
        attrs={'scale_mode': 'SINGLE_AXIS', 'domain': 'EDGE'})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements, 'Scale': group_input_2.outputs["Height"], 'Axis': (0.0000, 0.0000, 1.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS', 'domain': 'EDGE'})
    
    mesh_to_curve_1 = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': scale_elements_1})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_curve_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Thickness"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_2.outputs["Handle Resolution"], 'Radius': reroute_1})
    
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': curve_circle.outputs["Curve"]})
    
    rotate_instances_1 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': geometry_to_instance, 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': rotate_instances_1})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_position_1, 'Profile Curve': realize_instances})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': curve_to_mesh})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry_1, 'Shade Smooth': False})
    
    curve_to_points = nw.new_node(Nodes.CurveToPoints,
        input_kwargs={'Curve': mesh_to_curve_1, 'Count': group_input_2.outputs["Stud Amount"]})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_2.outputs["Stud Resolution"], 1: 1.0000},
        attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.7000}, attrs={'operation': 'MULTIPLY'})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere,
        input_kwargs={'Segments': group_input_2.outputs["Stud Resolution"], 'Rings': subtract, 'Radius': multiply})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: curve_to_points.outputs["Rotation"], 1: (1.5708, 0.0000, 0.0000)})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points.outputs["Points"], 'Instance': uv_sphere.outputs["Mesh"], 'Rotation': add_1.outputs["Vector"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_1.outputs["X"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_8})
    
    absolute_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["Z"]}, attrs={'operation': 'ABSOLUTE'})
    
    clamp = nw.new_node(Nodes.Clamp, input_kwargs={'Value': absolute_1, 'Max': 1.5000})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_2.outputs["Thickness"]}, attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: clamp, 1: multiply_1}, attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: multiply_2})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_1.outputs["Y"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_1.outputs["Z"]})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_2, 'Y': reroute_11, 'Z': reroute_10})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_2.outputs["Thickness"], 1: -1.5000},
        attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': instance_on_points, 'Selection': greater_than, 'Position': combine_xyz_2, 'Offset': combine_xyz_1})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_9}, attrs={'operation': 'LESS_THAN'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: clamp, 1: multiply_3}, attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_4, 1: reroute_7})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_3})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_16, 'Y': reroute_13, 'Z': reroute_12})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_1})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_2, 'Selection': less_than, 'Position': combine_xyz_3, 'Offset': reroute_17})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': set_position_3, 'Shade Smooth': group_input_2.outputs["Smooth Studs"]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_2.outputs["Studs"], 15: set_shade_smooth_1})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_shade_smooth, switch.outputs[6]]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})

def shader_metal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.1415, 0.1278, 0.1174, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.2545})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_shield_wood(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry_2 = nw.new_node(Nodes.NewGeometry)
    
    mapping_1 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': geometry_2.outputs["Position"], 'Scale': (2.4000, -0.3000, 139.3000)})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 5.5000, 'Detail': 2.9000, 'Roughness': 0.6083, 'Distortion': 0.4000})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': noise_texture_1.outputs["Fac"]})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: mapping_1, 1: combine_xyz})
    
    musgrave_texture_2 = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': add.outputs["Vector"], 'Scale': 28.8000, 'Detail': 15.0000, 'Dimension': 2.5000, 'Lacunarity': 2.5000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': musgrave_texture_2})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.9727
    colorramp_2.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    geometry = nw.new_node(Nodes.NewGeometry)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': geometry.outputs["Position"], 'Scale': (0.1000, 0.1500, 1.8500)})
    
    mix_2 = nw.new_node(Nodes.Mix, input_kwargs={0: 0.2333, 6: mapping}, attrs={'data_type': 'RGBA', 'clamp_factor': False})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mix_2.outputs[2], 'Scale': 9.3000, 'Detail': 11.0000, 'Distortion': 1.1000})
    
    musgrave_texture = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': noise_texture.outputs["Fac"], 'Detail': 15.0000, 'Dimension': 0.0000})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.7833, 6: musgrave_texture, 7: noise_texture.outputs["Fac"]},
        attrs={'data_type': 'RGBA', 'clamp_factor': False})
    
    mix_6 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.8000, 6: colorramp_2.outputs["Color"], 7: mix_3.outputs[2]},
        attrs={'data_type': 'RGBA', 'clamp_factor': False, 'blend_type': 'MULTIPLY'})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Scale': 4.0000, 'Detail': 0.0000, 'Detail Scale': -4.7000, 'Detail Roughness': 0.5385},
        attrs={'wave_profile': 'SAW', 'bands_direction': 'Z'})
    
    mix_5 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.5167, 6: mix_6.outputs[2], 7: wave_texture.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'clamp_factor': False, 'blend_type': 'DARKEN'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_5.outputs[2]})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0402, 0.0108, 0.0077, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.2318
    colorramp.color_ramp.elements[1].color = [0.0331, 0.0160, 0.0056, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.5636
    colorramp.color_ramp.elements[2].color = [0.2122, 0.0931, 0.0273, 1.0000]
    colorramp.color_ramp.elements[3].position = 1.0000
    colorramp.color_ramp.elements[3].color = [0.5520, 0.2831, 0.1301, 1.0000]
    
    bump_2 = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.3000, 'Distance': 0.2000, 'Height': colorramp_2.outputs["Color"]})
    
    bump_1 = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.4250, 'Distance': 0.4000, 'Height': wave_texture.outputs["Color"], 'Normal': bump_2})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Specular': 0.3000, 'Roughness': 0.5364, 'Normal': bump_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketBool', 'Side Curve', False),
            ('NodeSocketFloat', 'Crest Z', 1.0000),
            ('NodeSocketVector', 'Crest Handle', (0.0000, 0.0000, 1.0000)),
            ('NodeSocketVector', 'Top Corner Handle', (0.2500, 0.0000, 0.7500)),
            ('NodeSocketFloat', 'Top Corner X', 0.3500),
            ('NodeSocketFloat', 'Top Corner Z', 0.8000),
            ('NodeSocketVector', 'Side Upper Handle', (0.3500, 0.0000, 0.6000)),
            ('NodeSocketVector', 'Side Lower Handle', (0.5000, 0.0000, 0.5000)),
            ('NodeSocketFloat', 'Bottom Corner X', 0.4000),
            ('NodeSocketFloat', 'Bottom Corner Z', 0.4000),
            ('NodeSocketVector', 'Bottom Corner Handle', (0.2500, 0.0000, 0.2500)),
            ('NodeSocketFloat', 'Bottom Z', 0.0000),
            ('NodeSocketVector', 'Bottom Handle', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketMaterial', 'Shield Material', None), #surface.shaderfunc_to_material(shader_shield_wood)),
            ('NodeSocketInt', 'Shield Resolution', 16),
            ('NodeSocketFloat', 'Shield Thickness', 0.1000),
            ('NodeSocketFloat', 'Curve Amount', 0.0000),
            ('NodeSocketFloat', 'Curve X Bias', 1.0000),
            ('NodeSocketFloat', 'Curve Z Bias', 1.0000),
            ('NodeSocketFloat', 'Curve Z Offset', 0.0000),
            ('NodeSocketMaterial', 'Rim Material', None), #surface.shaderfunc_to_material(shader_metal)),
            ('NodeSocketBool', 'Rim', True),
            ('NodeSocketBool', 'Resample Rim', False),
            ('NodeSocketInt', 'Rim Resolution', 64),
            ('NodeSocketInt', 'Rim Profile Resolution', 6),
            ('NodeSocketFloat', 'Rim Thickness', 0.1500),
            ('NodeSocketFloat', 'Rim Depth', 0.7500),
            ('NodeSocketBool', 'Rim Studs', False),
            ('NodeSocketInt', 'Rim Stud Amount', 12),
            ('NodeSocketInt', 'Rim Stud Resolution', 3),
            ('NodeSocketFloat', 'Rim Stud Size', 0.1000),
            ('NodeSocketInt', 'Grip Resolution', 4),
            ('NodeSocketFloat', 'Grip Width', 1.0000),
            ('NodeSocketFloat', 'Grip Height', 1.0000),
            ('NodeSocketFloat', 'Grip Thickness', 0.1500),
            ('NodeSocketFloat', 'Grip Spacing', 0.0000),
            ('NodeSocketFloat', 'Grip Rotation', 0.0000),
            ('NodeSocketFloat', 'Grip Z Offset', 0.0000),
            ('NodeSocketBool', 'Grip Studs', False),
            ('NodeSocketInt', 'Grip Stud Amount', 6),
            ('NodeSocketInt', 'Grip Stud Resolution', 4),
            ('NodeSocketInt', 'Subdivisions', 0),
            ('NodeSocketFloat', 'Edge Crease', 0.0000),
            ('NodeSocketBool', 'Shade Smooth', False)])
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Side Curve"]})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input_1.outputs["Top Corner X"], 'Z': group_input_1.outputs["Top Corner Z"]})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input_1.outputs["Bottom Corner X"], 'Z': group_input_1.outputs["Bottom Corner Z"]})
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={0: reroute_11, 8: combine_xyz_2, 9: combine_xyz_1},
        attrs={'input_type': 'VECTOR'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Bottom Corner Handle"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Bottom Handle"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Bottom Z"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_8})
    
    bezier_segment_2 = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Resolution': 13, 'Start': switch_1.outputs[3], 'Start Handle': reroute, 'End Handle': reroute_6, 'End': combine_xyz})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_1.outputs["Crest Z"]})
    
    bezier_segment_1 = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Resolution': 13, 'Start': combine_xyz_6, 'Start Handle': group_input_1.outputs["Crest Handle"], 'End Handle': group_input_1.outputs["Top Corner Handle"], 'End': combine_xyz_2})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Side Lower Handle"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Side Upper Handle"]})
    
    s_i_d_e = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Resolution': 13, 'Start': combine_xyz_1, 'Start Handle': reroute_10, 'End Handle': reroute_9, 'End': combine_xyz_2},
        label='SIDE')
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_11, 15: s_i_d_e})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [bezier_segment_2, bezier_segment_1, switch.outputs[6]]})
    
    transform_geometry = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry, 'Rotation': (0.0000, 0.0000, 3.1416)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_geometry, join_geometry]})
    
    transform_geometry_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_1, 'Rotation': (1.5708, 0.0000, 0.0000)})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': transform_geometry_1})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': curve_to_mesh})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': merge_by_distance})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': mesh_to_curve, 'Count': group_input_1.outputs["Rim Resolution"]})
    
    switch_2 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_1.outputs["Resample Rim"], 14: mesh_to_curve, 15: resample_curve})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_2.outputs[6]})
    
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': reroute_3}, attrs={'mode': 'NGONS'})
    
    bounding_box_1 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_3})
    
    absolute = nw.new_node(Nodes.VectorMath, input_kwargs={0: bounding_box_1.outputs["Min"]}, attrs={'operation': 'ABSOLUTE'})
    
    separate_xyz_4 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': absolute.outputs["Vector"]})
    
    absolute_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: bounding_box_1.outputs["Max"]}, attrs={'operation': 'ABSOLUTE'})
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': absolute_1.outputs["Vector"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_4.outputs["X"], 1: separate_xyz_3.outputs["X"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: 1.5000}, attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_4.outputs["Y"], 1: separate_xyz_3.outputs["Y"]})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: 1.5000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Shield Resolution"]})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    grid_1 = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': multiply, 'Size Y': multiply_1, 'Vertices X': reroute_14, 'Vertices Y': reroute_14})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_4.outputs["Y"], 1: separate_xyz_3.outputs["Y"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: -0.5000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_2})
    
    transform_geometry_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': grid_1.outputs["Mesh"], 'Translation': combine_xyz_3})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': transform_geometry_3})
    
    intersect = nw.new_node(Nodes.MeshBoolean,
        input_kwargs={'Mesh 2': [fill_curve, extrude_mesh.outputs["Mesh"]]},
        attrs={'operation': 'INTERSECT'})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Shield Thickness"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': intersect.outputs["Mesh"], 'Offset Scale': multiply_3, 'Individual': False})
    
    uv_unwrap = nw.new_node('GeometryNodeUVUnwrap')
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 1: uv_unwrap},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    join_geometry_7 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [intersect.outputs["Mesh"], capture_attribute_1.outputs["Geometry"]]})
    
    merge_by_distance_2 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_7})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: -0.5000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_4})
    
    transform_geometry_11 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': merge_by_distance_2, 'Translation': combine_xyz_9})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': transform_geometry_11, 'Material': group_input_1.outputs["Shield Material"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_2.outputs[6]})
    
    multiply_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Rim Thickness"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_1.outputs["Rim Profile Resolution"], 'Radius': multiply_5})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': reroute_4, 'Profile Curve': curve_circle.outputs["Curve"]})
    
    multiply_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Shield Thickness"], 1: 10.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_7 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_6, 1: group_input_1.outputs["Rim Depth"]},
        attrs={'operation': 'MULTIPLY'})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Scale': multiply_7, 'Axis': (0.0000, 0.0000, 1.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': reroute_4, 'Count': group_input_1.outputs["Rim Stud Amount"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Rim Stud Resolution"]})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_8 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Rim Stud Size"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Segments': reroute_5, 'Rings': subtract_1, 'Radius': multiply_8})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': normal})
    
    add_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: align_euler_to_vector, 1: (0.0000, 0.0000, 0.7854), 2: (0.0000, 0.0000, 0.7854)})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': resample_curve_1, 'Instance': uv_sphere.outputs["Mesh"], 'Rotation': add_2.outputs["Vector"]})
    
    bounding_box_3 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': scale_elements})
    
    separate_xyz_8 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_3.outputs["Max"]})
    
    multiply_9 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_8, 1: 0.2500}, attrs={'operation': 'MULTIPLY'})
    
    subtract_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_8.outputs["Z"], 1: multiply_9},
        attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_13 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': subtract_2})
    
    transform_geometry_12 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': instance_on_points_1, 'Translation': combine_xyz_13})
    
    switch_3 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_1.outputs["Rim Studs"], 15: transform_geometry_12})
    
    join_geometry_6 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [scale_elements, switch_3.outputs[6]]})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_6, 'Material': group_input_1.outputs["Rim Material"]})
    
    switch_5 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_1.outputs["Rim"], 15: set_material_1})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, switch_5.outputs[6]]})
    
    multiply_add = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Curve Z Offset"], 1: -1.0000, 2: -0.5000},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_add})
    
    transform_geometry_2 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': join_geometry_2, 'Translation': combine_xyz_5, 'Rotation': (-1.5708, 0.0000, 0.0000)})
    
    position = nw.new_node(Nodes.InputPosition)
    
    absolute_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position}, attrs={'operation': 'ABSOLUTE'})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': absolute_2.outputs["Vector"]})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': transform_geometry_2})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Min"]})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Max"]})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_2.outputs["X"], 1: separate_xyz_1.outputs["X"], 2: separate_xyz.outputs["X"], 3: -1.0000})
    
    multiply_10 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range.outputs["Result"], 1: group_input_1.outputs["Curve X Bias"]},
        attrs={'operation': 'MULTIPLY'})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_2.outputs["Z"], 1: separate_xyz_1.outputs["Z"], 2: separate_xyz.outputs["Z"], 3: -1.0000})
    
    multiply_11 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_1.outputs["Result"], 1: group_input_1.outputs["Curve Z Bias"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_10, 1: multiply_11})
    
    multiply_12 = nw.new_node(Nodes.Math, input_kwargs={0: add_3}, attrs={'operation': 'MULTIPLY'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': multiply_12})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.6843, 0.6843, 0.6843, 1.0000]
    
    multiply_13 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Curve Amount"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_14 = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp.outputs["Color"], 1: multiply_13},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_14})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': transform_geometry_2, 'Offset': combine_xyz_4})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position})
    
    bezier_segment_3 = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Resolution': 1, 'Start': combine_xyz_6, 'Start Handle': (0.0000, 0.0000, 0.0000), 'End': combine_xyz})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry, bezier_segment_3]})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': join_geometry_3})
    
    merge_by_distance_1 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': curve_to_mesh_2})
    
    mesh_to_curve_1 = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': merge_by_distance_1})
    
    transform_geometry_6 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': mesh_to_curve_1, 'Rotation': (1.5708, 0.0000, 0.0000)})
    
    fill_curve_1 = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': transform_geometry_6}, attrs={'mode': 'NGONS'})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': fill_curve_1}, attrs={'mode': 'FACES'})
    
    multiply_15 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Grip Spacing"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_11 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_15})
    
    transform_geometry_9 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': mesh_to_points, 'Translation': combine_xyz_11})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_geometry_9})
    
    transform_geometry_7 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_1, 'Scale': (-1.0000, 1.0000, 1.0000)})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_1, transform_geometry_7]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_4})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_7 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    bounding_box_4 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': transform_geometry_11})
    
    separate_xyz_6 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_4.outputs["Min"]})
    
    combine_xyz_12 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_7.outputs["X"], 'Y': separate_xyz_7.outputs["Y"], 'Z': separate_xyz_6.outputs["Z"]})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_7, 'Position': combine_xyz_12})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': set_position_2, 1: position_2},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    multiply_16 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_2, 1: (1.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Position': multiply_16.outputs["Vector"]})
    
    combine_xyz_14 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_1.outputs["Grip Rotation"]})
    
    transform_geometry_14 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_3, 'Rotation': combine_xyz_14})
    
    separate_xyz_9 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': capture_attribute.outputs["Attribute"]})
    
    combine_xyz_15 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': separate_xyz_9.outputs["Y"]})
    
    add_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_2, 1: combine_xyz_15})
    
    multiply_17 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Grip Z Offset"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_16 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_17})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': transform_geometry_14, 'Position': add_4.outputs["Vector"], 'Offset': combine_xyz_16})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_5})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    transform_geometry_8 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': set_position_4, 'Translation': reroute_13, 'Rotation': (-1.5708, 0.0000, 0.0000)})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': transform_geometry_8, 'Offset': combine_xyz_4})
    
    shieldhandlegen = nw.new_node(nodegroup_shield_handle_gen().name,
        input_kwargs={'Width': group_input_1.outputs["Grip Width"], 'Height': group_input_1.outputs["Grip Height"], 'Thickness': group_input_1.outputs["Grip Thickness"], 'Handle Resolution': group_input_1.outputs["Grip Resolution"], 'Studs': group_input_1.outputs["Grip Studs"], 'Stud Amount': group_input_1.outputs["Grip Stud Amount"], 'Stud Resolution': group_input_1.outputs["Grip Stud Resolution"], 'Smooth Studs': group_input_1.outputs["Shade Smooth"]})
    
    multiply_add_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Grip Height"], 1: -0.7000, 2: -0.2000},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_add_1})
    
    combine_xyz_17 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_1.outputs["Grip Rotation"]})
    
    transform_geometry_10 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': shieldhandlegen, 'Translation': combine_xyz_10, 'Rotation': combine_xyz_17})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_1, 'Instance': transform_geometry_10, 'Rotation': (0.0000, 1.5708, 1.5708), 'Scale': (0.1000, 0.1000, 0.1000)})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points, 'Material': group_input_1.outputs["Rim Material"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': set_material_2})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': extrude_mesh_1.outputs["Top"]})
    
    set_position_5 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': reroute_2, 'Selection': reroute_17, 'Offset': (0.0000, 0.5000, 0.0000)})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position_5})
    
    difference = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': realize_instances, 'Mesh 2': flip_faces})
    
    transform_geometry_13 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': difference.outputs["Mesh"], 'Translation': (0.0000, 0.0050, 0.0000)})
    
    join_geometry_5 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_2, transform_geometry_13]})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_1.outputs["Curve Z Offset"]})
    
    transform_geometry_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_5, 'Translation': combine_xyz_7})
    
    bounding_box_2 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': transform_geometry_4})
    
    separate_xyz_5 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_2.outputs["Max"]})
    
    multiply_18 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_5.outputs["Y"], 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_18})
    
    transform_geometry_5 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': transform_geometry_4, 'Translation': combine_xyz_8, 'Rotation': (0.0000, 0.0000, 3.1416)})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': transform_geometry_5, 'Level': group_input_1.outputs["Subdivisions"], 'Edge Crease': group_input_1.outputs["Edge Crease"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Shade Smooth"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': subdivision_surface, 'Shade Smooth': reroute_16})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': set_shade_smooth, 'UV': capture_attribute_1.outputs["Attribute"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_shield_wood, selection=selection)
apply(bpy.context.active_object)
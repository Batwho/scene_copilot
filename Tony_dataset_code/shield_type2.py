import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_fittings_wood(nw: NodeWrangler):
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
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_6.outputs[2]})
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
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Specular': 0.3000, 'Roughness': 0.5364, 'Normal': bump_2})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

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

def shader_metal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.1415, 0.1278, 0.1174, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.2545})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_shield_wood_paint_circle_cross(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry_3 = nw.new_node(Nodes.NewGeometry)
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'UV'})
    
    mapping_2 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': attribute.outputs["Vector"], 'Location': (-0.0500, 0.1000, 0.0000), 'Rotation': (0.0000, 0.0000, -0.1222)})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping_2},
        attrs={'image': bpy.data.images['Circle Cross.png']})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.3257, 0.1604, 0.0554, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.1009, 0.0162, 0.0118, 1.0000]
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping_1 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Scale': (2.4000, -0.3000, 139.3000)})
    
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
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Scale': (0.1000, 0.1500, 1.8500)})
    
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
        input_kwargs={0: 0.6833, 6: mix_6.outputs[2], 7: wave_texture.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'clamp_factor': False, 'blend_type': 'DARKEN'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.8167, 6: colorramp.outputs["Color"], 7: mix_5.outputs[2]},
        attrs={'data_type': 'RGBA', 'blend_type': 'MULTIPLY'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_5.outputs[2]})
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0402, 0.0108, 0.0077, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.2318
    colorramp_1.color_ramp.elements[1].color = [0.0331, 0.0160, 0.0056, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 0.5636
    colorramp_1.color_ramp.elements[2].color = [0.2122, 0.0931, 0.0273, 1.0000]
    colorramp_1.color_ramp.elements[3].position = 1.0000
    colorramp_1.color_ramp.elements[3].color = [0.5520, 0.2831, 0.1301, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: geometry_3.outputs["Backfacing"], 6: mix.outputs[2], 7: colorramp_1.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    bump_2 = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.3000, 'Distance': 0.2000, 'Height': colorramp_2.outputs["Color"]})
    
    bump_1 = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.4250, 'Distance': 0.4000, 'Height': wave_texture.outputs["Color"], 'Normal': bump_2})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_1.outputs[2], 'Specular': 0.3000, 'Roughness': 0.5364, 'Normal': bump_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketMaterial', 'Shield Material', None),# surface.shaderfunc_to_material(shader_shield_wood)),
            ('NodeSocketInt', 'Shield Resolution', 8),
            ('NodeSocketFloat', 'Shield Size', 1.0000),
            ('NodeSocketFloat', 'Shield Curve', 0.0000),
            ('NodeSocketFloat', 'Shield Thickness', 0.1000),
            ('NodeSocketMaterial', 'Rim Material', None),#surface.shaderfunc_to_material(shader_metal)),
            ('NodeSocketBool', 'Rim', True),
            ('NodeSocketInt', 'Rim Profile Resolution', 5),
            ('NodeSocketFloat', 'Rim Thickness', 0.3000),
            ('NodeSocketFloat', 'Rim Depth', 1.0000),
            ('NodeSocketBool', 'Rim Studs', False),
            ('NodeSocketFloat', 'Rim Stud Size', 1.0000),
            ('NodeSocketInt', 'Rim Stud Amount', 20),
            ('NodeSocketInt', 'Rim Stud Resolution', 3),
            ('NodeSocketInt', 'Grip Type', 0),
            ('NodeSocketInt', 'Grip Resolution', 6),
            ('NodeSocketFloat', 'Grip Width', 1.0000),
            ('NodeSocketFloat', 'Grip Height', 1.0000),
            ('NodeSocketFloat', 'Grip Thickness', 0.1500),
            ('NodeSocketFloat', 'Grip Spacing', 0.0000),
            ('NodeSocketBool', 'Grip Studs', False),
            ('NodeSocketInt', 'Grip Stud Amount', 12),
            ('NodeSocketInt', 'Grip Stud Resolution', 4),
            ('NodeSocketFloat', 'Grip Stud Size', 0.1500),
            ('NodeSocketBool', 'Central Dome', False),
            ('NodeSocketInt', 'Central Dome Resolution', 2),
            ('NodeSocketFloat', 'Central Dome Size', 0.5000),
            ('NodeSocketFloat', 'Central Dome Y Offset', 0.0000),
            ('NodeSocketFloat', 'Central Dome Depth', 1.0000),
            ('NodeSocketInt', 'Subdivisions', 0),
            ('NodeSocketFloat', 'Edge Crease', 0.0000),
            ('NodeSocketBool', 'Shade Smooth', False)])
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shield Resolution"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_4, 'Radius': 0.0010})
    
    clamp = nw.new_node(Nodes.Clamp, input_kwargs={'Value': reroute_4, 'Max': 8.0000})
    
    reroute_56 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': clamp})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Shield Size"], 1: 0.4000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply, 'Z': 0.0000})
    
    mesh_line = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': reroute_56, 'Resolution': 0.1000, 'Offset': combine_xyz},
        attrs={'mode': 'END_POINTS'})
    
    index = nw.new_node(Nodes.Index)
    
    reroute_57 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_56})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': index, 2: reroute_57})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range.outputs["Result"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.5091, 0.0813), (0.9955, 0.4062)], handles=['VECTOR', 'AUTO', 'AUTO'])
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shield Curve"]})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve, 1: reroute_11}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_1})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_line, 'Offset': combine_xyz_3})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': set_position_2})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_circle.outputs["Curve"], 'Profile Curve': mesh_to_curve})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': curve_to_mesh, 'Distance': 0.0100})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': merge_by_distance})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Shield Thickness"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': reroute, 'Offset Scale': multiply_2, 'Individual': False})
    
    uv_unwrap = nw.new_node('GeometryNodeUVUnwrap')
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 1: uv_unwrap},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute, capture_attribute_1.outputs["Geometry"]]})
    
    merge_by_distance_1 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_2})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: -0.5000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_3})
    
    transform_geometry_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': merge_by_distance_1, 'Translation': combine_xyz_2})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_geometry_2})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_3, 'Material': group_input.outputs["Shield Material"]})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: group_input.outputs["Grip Type"]}, attrs={'data_type': 'INT'})
    
    multiply_add = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Grip Spacing"], 1: 0.1000, 2: 0.1000},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_add, 'Z': -0.5000})
    
    points = nw.new_node('GeometryNodePoints', input_kwargs={'Position': combine_xyz_4, 'Radius': 0.0500})
    
    transform_geometry_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': points, 'Rotation': (0.0000, 0.0000, 3.1416)})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [points, transform_geometry_3]})
    
    transform_geometry_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_3})
    
    position = nw.new_node(Nodes.InputPosition)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': transform_geometry_4, 1: position},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': reroute_2, 'Source Position': capture_attribute.outputs["Attribute"], 'Ray Direction': (0.0000, 0.0000, 1.0000)})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Position': raycast.outputs["Hit Position"]})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_3})
    
    shieldhandlegen = nw.new_node(nodegroup_shield_handle_gen().name,
        input_kwargs={'Width': group_input.outputs["Grip Width"], 'Height': group_input.outputs["Grip Height"], 'Thickness': group_input.outputs["Grip Thickness"], 'Handle Resolution': group_input.outputs["Grip Resolution"], 'Studs': group_input.outputs["Grip Studs"], 'Stud Amount': group_input.outputs["Grip Stud Amount"], 'Stud Resolution': group_input.outputs["Grip Stud Resolution"], 'Smooth Studs': group_input.outputs["Shade Smooth"]})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Grip Height"], 1: -0.8000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_4})
    
    transform_geometry_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': shieldhandlegen, 'Translation': combine_xyz_5})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_51, 'Instance': transform_geometry_5, 'Rotation': (0.0000, 0.0000, 1.5708), 'Scale': (0.1000, 0.1000, 0.1000)})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': extrude_mesh.outputs["Top"]})
    
    set_position_7 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': reroute_2, 'Selection': reroute_36, 'Offset': (0.0000, 0.0000, 0.6000)})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position_7})
    
    difference = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': realize_instances_1, 'Mesh 2': flip_faces})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': difference.outputs["Mesh"], 'Material': group_input.outputs["Rim Material"]})
    
    reroute_55 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_2})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_55})
    
    transform_geometry_6 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_9, 'Rotation': (0.0000, 3.1398, 0.0000)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_9, transform_geometry_6]})
    
    merge_by_distance_2 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry})
    
    transform_geometry_7 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': merge_by_distance_2, 'Rotation': (-1.5708, 0.0000, 0.0000)})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    absolute = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_2}, attrs={'operation': 'ABSOLUTE'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': absolute.outputs["Vector"]})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shield Size"]})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_48, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    less_than = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz.outputs["X"], 1: multiply_5},
        attrs={'operation': 'LESS_THAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': transform_geometry_7, 'Selection': less_than})
    
    mesh_to_curve_1 = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': delete_geometry})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Grip Width"]})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_49, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    quadrilateral = nw.new_node('GeometryNodeCurvePrimitiveQuadrilateral', input_kwargs={'Width': multiply_6, 'Height': 0.0010})
    
    curve_to_mesh_4 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': quadrilateral})
    
    merge_by_distance_3 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': curve_to_mesh_4})
    
    mesh_to_curve_3 = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': merge_by_distance_3})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': mesh_to_curve_1, 'Profile Curve': mesh_to_curve_3, 'Fill Caps': True})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Grip Height"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    absolute_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_1}, attrs={'operation': 'ABSOLUTE'})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': absolute_1.outputs["Vector"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shield Size"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_2.outputs["X"], 2: reroute_8, 3: 1.0000, 4: 0.0000},
        attrs={'clamp': False})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range_1.outputs["Result"]})
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.5455
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.7477
    colorramp_1.color_ramp.elements[1].color = [0.5936, 0.5936, 0.5936, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 0.9045
    colorramp_1.color_ramp.elements[2].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_7 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_12, 1: colorramp_1.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_7, 1: -0.1000}, attrs={'operation': 'MULTIPLY'})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': curve_to_mesh_2, 'Offset Scale': multiply_8, 'Individual': False})
    
    reroute_59 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': extrude_mesh_1.outputs["Mesh"]})
    
    reroute_60 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_59})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_1.outputs["Y"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range_1.outputs["Result"]})
    colorramp.color_ramp.interpolation = "CARDINAL"
    colorramp.color_ramp.elements[0].position = 0.4045
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_9 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_10, 1: colorramp.outputs["Color"]}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_1.outputs["X"], 'Y': multiply_9, 'Z': separate_xyz_1.outputs["Z"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_6})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_60, 'Position': reroute_13})
    
    flip_faces_1 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position_4})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_48})
    
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_47, 1: 0.2000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_10})
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz.outputs["X"], 1: reroute_54})
    
    delete_geometry_1 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': transform_geometry_7, 'Selection': greater_than_1})
    
    mesh_to_curve_2 = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': delete_geometry_1})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Grip Resolution"]})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Grip Thickness"]})
    
    multiply_11 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_45, 1: 0.1500}, attrs={'operation': 'MULTIPLY'})
    
    curve_circle_3 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_46, 'Radius': multiply_11})
    
    curve_to_mesh_3 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': mesh_to_curve_2, 'Profile Curve': curve_circle_3.outputs["Curve"]})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh_3})
    
    multiply_12 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_12, 1: -0.1000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_12})
    
    transform_geometry_8 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_52, 'Translation': combine_xyz_7})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_3})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_54})
    
    reroute_61 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_53})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_2.outputs["X"], 2: reroute_61, 4: 0.9000},
        attrs={'clamp': False})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range_2.outputs["Result"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 1.0000
    colorramp_2.color_ramp.elements[1].color = [0.2501, 0.2501, 0.2501, 1.0000]
    
    multiply_13 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_3.outputs["Z"], 1: colorramp_2.outputs["Color"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_3.outputs["X"], 'Y': separate_xyz_3.outputs["Y"], 'Z': multiply_13})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': transform_geometry_8, 'Position': combine_xyz_8})
    
    join_geometry_5 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces_1, set_position_5]})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_5, 'Material': surface.shaderfunc_to_material(shader_fittings_wood)})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_4})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than, 14: set_material_3, 15: reroute_58})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_1.outputs[6]})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shield Resolution"]})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Central Dome Resolution"]})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_41})
    
    multiply_14 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Central Dome Size"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Segments': reroute_40, 'Rings': reroute_42, 'Radius': multiply_14})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Central Dome Depth"]})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Scale': reroute_43, 'Axis': (0.0000, 0.0000, 1.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_elements})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shield Curve"]})
    
    less_than_1 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_38}, attrs={'operation': 'LESS_THAN'})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': less_than_1})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_1})
    
    switch_5 = nw.new_node(Nodes.Switch,
        input_kwargs={0: reroute_37, 8: bounding_box.outputs["Max"], 9: bounding_box.outputs["Min"]},
        attrs={'input_type': 'VECTOR'})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Central Dome Y Offset"]})
    
    multiply_15 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_44, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_15})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: switch_5.outputs[3], 1: combine_xyz_1})
    
    multiply_16 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add.outputs["Vector"], 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_23, 'Offset': multiply_16.outputs["Vector"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    difference_1 = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': set_position_1, 'Mesh 2': reroute_5})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': difference_1.outputs["Mesh"], 'Material': group_input.outputs["Rim Material"]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Central Dome"], 15: set_material})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch.outputs[6]})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    multiply_17 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Shield Size"], 1: 0.4000},
        attrs={'operation': 'MULTIPLY'})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Shield Resolution"], 'Radius': multiply_17})
    
    less_than_2 = nw.new_node(Nodes.Compare, input_kwargs={0: group_input.outputs["Shield Curve"]}, attrs={'operation': 'LESS_THAN'})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    bounding_box_1 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_22})
    
    switch_2 = nw.new_node(Nodes.Switch,
        input_kwargs={0: less_than_2, 8: bounding_box_1.outputs["Min"], 9: bounding_box_1.outputs["Max"]},
        attrs={'input_type': 'VECTOR'})
    
    multiply_18 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: switch_2.outputs[3], 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_circle_1.outputs["Curve"], 'Offset': multiply_18.outputs["Vector"]})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rim Profile Resolution"]})
    
    multiply_19 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Rim Thickness"], 1: 0.0500},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_20 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Shield Thickness"], 1: 0.0500},
        attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_19, 1: multiply_20})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_34, 'Radius': add_1})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': reroute_27, 'Profile Curve': curve_circle_2.outputs["Curve"]})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rim Depth"]})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Scale': reroute_33, 'Axis': (0.0000, 0.0000, 1.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_elements_1})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rim Studs"]})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rim Stud Amount"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': reroute_28, 'Count': reroute_29})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': resample_curve})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rim Stud Resolution"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_32, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_21 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Rim Stud Size"], 1: 0.0100},
        attrs={'operation': 'MULTIPLY'})
    
    uv_sphere_1 = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Segments': reroute_32, 'Rings': subtract, 'Radius': multiply_21})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': normal}, attrs={'axis': 'Z'})
    
    multiply_add_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: align_euler_to_vector, 1: (0.0000, 0.0000, 1.0000), 2: (0.0000, 0.0000, 0.7854)},
        attrs={'operation': 'MULTIPLY_ADD'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_26, 'Instance': uv_sphere_1.outputs["Mesh"], 'Rotation': multiply_add_1.outputs["Vector"]})
    
    position_4 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_5 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_4})
    
    bounding_box_2 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_35})
    
    separate_xyz_4 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_2.outputs["Max"]})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_5.outputs["X"], 'Y': separate_xyz_5.outputs["Y"], 'Z': separate_xyz_4.outputs["Z"]})
    
    set_position_6 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': instance_on_points, 'Position': combine_xyz_9})
    
    switch_4 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_25, 15: set_position_6})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': switch_4.outputs[6]})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_35, realize_instances]})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rim Material"]})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': join_geometry_1, 'Material': reroute_24})
    
    switch_3 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Rim"], 15: set_material_1})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_3.outputs[6]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_2, reroute_18, reroute_17, reroute_16]})
    
    transform_geometry = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_4, 'Rotation': (1.5708, 0.0000, 0.0000)})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': transform_geometry, 'Level': group_input.outputs["Subdivisions"], 'Edge Crease': group_input.outputs["Edge Crease"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': subdivision_surface, 'Shade Smooth': group_input.outputs["Shade Smooth"]})
    
    reroute_62 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs["Attribute"]})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_62})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': set_shade_smooth, 'UV': reroute_50},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_shield_wood_paint_circle_cross, selection=selection)
    surface.add_material(obj, shader_metal, selection=selection)
apply(bpy.context.active_object)
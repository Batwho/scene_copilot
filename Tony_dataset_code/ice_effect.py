import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_f_r_o_z_e_n', singleton=False, type='ShaderNodeTree')
def nodegroup_f_r_o_z_e_n(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord, attrs={'object': bpy.data.objects['Freeze_control_EMPTY']})
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate_1.outputs["Object"], 'Scale': 11.5700, 'Detail': 6.0000, 'Roughness': 1.0000})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: texture_coordinate.outputs["Object"], 7: noise_texture.outputs["Fac"]},
        attrs={'blend_type': 'OVERLAY', 'data_type': 'RGBA'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate_1.outputs["Object"], 'Scale': 4.6900, 'Detail': 6.0000, 'Roughness': 0.7778})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.2515
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.6515
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix.outputs[2], 7: colorramp.outputs["Color"]},
        attrs={'blend_type': 'LINEAR_LIGHT', 'data_type': 'RGBA'})
    
    length = nw.new_node(Nodes.VectorMath, input_kwargs={0: mix_1.outputs[2]}, attrs={'operation': 'LENGTH'})
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketShader', 'Shader', None),
            ('NodeSocketFloat', 'Ice Shader Distance', 2.3300)])
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': length.outputs["Value"], 2: group_input.outputs["Ice Shader Distance"], 3: 1.0000, 4: 0.0000},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: 0.1800}, attrs={'operation': 'GREATER_THAN'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0300, 'Height': reroute})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.6045, 0.6045, 0.6045, 1.0000), 'Metallic': 0.0939, 'Roughness': 0.2758, 'Emission Strength': 0.2595, 'Normal': bump})
    
    mix_shader = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': greater_than, 1: group_input.outputs["Shader"], 2: principled_bsdf_1})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Shader': mix_shader}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_frost_density', singleton=False, type='GeometryNodeTree')
def nodegroup_frost_density(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    position_3 = nw.new_node(Nodes.InputPosition)
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_3, 1: (0.0000, 0.0000, 3.6500)})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': add.outputs["Vector"], 'Scale': 2.7900, 'Roughness': 0.0000, 'Distortion': 1.0000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp_2.color_ramp.elements[0].position = 0.4212
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5576
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketFloat', 'Value', 2500.0000)])
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_2.outputs["Color"], 1: group_input.outputs["Value"]},
        attrs={'operation': 'MULTIPLY'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': multiply}, attrs={'is_active_output': True})

def shader_ice(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord, attrs={'object': bpy.data.objects['material_coordinater_empty']})
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    noise_texture_4 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 8.4000})
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_4.outputs["Fac"]})
    colorramp_6.color_ramp.elements[0].position = 0.4030
    colorramp_6.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 0.6061
    colorramp_6.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': 5.7900, 'Detail': 8.0000, 'Roughness': 1.0000, 'Distortion': 3.9600})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_2.color_ramp.elements[0].position = 0.3030
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.6212
    colorramp_2.color_ramp.elements[1].color = [0.5387, 0.5387, 0.5387, 1.0000]
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5273
    colorramp.color_ramp.elements[1].color = [0.7323, 0.7323, 0.7323, 1.0000]
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': 0.7100, 'Detail': 8.0000, 'Roughness': 1.0000, 'Distortion': 3.9600})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.4364
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0500, 'Height': colorramp_1.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (1.4366, 1.7620, 2.0000, 1.0000), 'Roughness': colorramp_2.outputs["Color"], 'Clearcoat': 1.0000, 'Transmission': 0.9727, 'Transmission Roughness': colorramp.outputs["Color"], 'Normal': bump})
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 5.7900, 'Detail': 8.0000, 'Roughness': 1.0000, 'Distortion': 3.9600})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_5.color_ramp.elements[0].position = 0.2939
    colorramp_5.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.6758
    colorramp_5.color_ramp.elements[1].color = [0.5370, 0.5370, 0.5370, 1.0000]
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_4.color_ramp.elements[0].position = 0.0000
    colorramp_4.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.5273
    colorramp_4.color_ramp.elements[1].color = [0.2191, 0.2191, 0.2191, 1.0000]
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_1, 'Scale': 0.1600, 'Detail': 8.0000, 'Roughness': 1.0000, 'Distortion': 3.9600})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_3.outputs["Fac"]})
    colorramp_3.color_ramp.elements[0].position = 0.4364
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 1.0000
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump_1 = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0500, 'Height': colorramp_3.outputs["Color"]})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.7234, 0.8121, 0.9055, 1.0000), 'Roughness': colorramp_5.outputs["Color"], 'Transmission': 1.0000, 'Transmission Roughness': colorramp_4.outputs["Color"], 'Normal': bump_1})
    
    mix_shader = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': colorramp_6.outputs["Color"], 1: principled_bsdf, 2: principled_bsdf_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def shader_bake_target(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 81.0000, 'Detail': 3.0000, 'Roughness': 0.7222})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0100, 'Height': noise_texture.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.3656, 0.3656, 0.3656, 1.0000), 'Metallic': 1.0000, 'Specular': 1.0000, 'Roughness': 0.6467, 'Normal': bump})
    
    group = nw.new_node(nodegroup_f_r_o_z_e_n().name, input_kwargs={'Shader': principled_bsdf, 'Ice Shader Distance': 3.2200})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': group}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Ice Grow Distance', 3.5000),
            ('NodeSocketVector', 'Ice Drip Vector', (0.0000, 0.0000, -1.2600)),
            ('NodeSocketFloat', 'Ice Resolution', 128.0000),
            ('NodeSocketFloat', 'Frost Grow Distance', 6.0000),
            ('NodeSocketFloat', 'Frost Particles Density', 2500.0000),
            ('NodeSocketFloat', 'Frost Particles Scale', 1.0000),
            ('NodeSocketFloat', 'Icicle Grow Distance', 8.0000),
            ('NodeSocketFloat', 'Icicle Radius Grow Distance', 8.0000),
            ('NodeSocketFloat', 'Icicles Density', 20.0000),
            ('NodeSocketFloat', 'Icicle Length', 1.0000),
            ('NodeSocketFloatDistance', 'Icicle Radius', 0.0050),
            ('NodeSocketVectorEuler', 'Icicle Grow Direction Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketObject', 'Object To Freeze', None)])# bpy.data.objects['parts_main.o.001'])])
    
    object_info_4 = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': group_input.outputs["Object To Freeze"]},
        attrs={'transform_space': 'RELATIVE'})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': object_info_4.outputs["Geometry"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    normal_1 = nw.new_node(Nodes.InputNormal)
    
    dot_product = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normal_1, 1: (0.0000, 0.0000, -1.0000)},
        attrs={'operation': 'DOT_PRODUCT'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: dot_product.outputs["Value"], 1: group_input.outputs["Icicles Density"]},
        attrs={'operation': 'MULTIPLY'})
    
    distribute_points_on_faces_2 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_11, 'Density': multiply, 'Seed': 17},
        attrs={'use_legacy_normal': True})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Icicle Length"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_1})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.0900, -0.0900, -0.1300), 1: (0.0800, 0.0800, 0.3300)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    rotate_euler_1 = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': random_value_1.outputs["Value"], 'Rotate By': group_input.outputs["Icicle Grow Direction Vector"]})
    
    position_4 = nw.new_node(Nodes.InputPosition)
    
    object_info_2 = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Freeze_control_EMPTY']},
        attrs={'transform_space': 'RELATIVE'})
    
    distance = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_4, 1: object_info_2.outputs["Location"]},
        attrs={'operation': 'DISTANCE'})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': distance.outputs["Value"], 2: group_input.outputs["Icicle Grow Distance"], 3: 1.0000, 4: 0.0000},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.2000, 3: 1.5000})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_2.outputs["Result"], 1: random_value.outputs[1]},
        attrs={'operation': 'MULTIPLY'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_2.outputs["Points"], 'Instance': curve_line, 'Rotation': rotate_euler_1, 'Scale': multiply_2})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points}, attrs={'legacy_behavior': True})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': realize_instances_1, 'Count': 6})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    map_range_5 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': distance.outputs["Value"], 2: group_input.outputs["Icicle Radius Grow Distance"], 3: 25.0000, 4: 0.0000},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_5.outputs["Result"]})
    
    map_range_4 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': curve_parameter.outputs["Factor"], 2: 1.1000, 3: reroute_8, 4: 0.1000})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve, 'Radius': map_range_4.outputs["Result"]})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': set_curve_radius}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type}, attrs={'handle_type': 'ALIGN'})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    position_8 = nw.new_node(Nodes.InputPosition)
    
    normal_5 = nw.new_node(Nodes.InputNormal)
    
    sample_nearest_2 = nw.new_node(Nodes.SampleNearest,
        input_kwargs={'Geometry': group_input.outputs["Geometry"]},
        attrs={'domain': 'FACE'})
    
    sample_index_2 = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 3: normal_5, 'Index': sample_nearest_2},
        attrs={'domain': 'FACE', 'data_type': 'FLOAT_VECTOR'})
    
    multiply_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: sample_index_2.outputs[2], 1: (0.0500, 0.0500, 0.0500)},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_8, 1: multiply_3.outputs["Vector"]})
    
    set_handle_positions = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_handle_type, 'Selection': endpoint_selection, 'Position': add.outputs["Vector"]},
        attrs={'mode': 'RIGHT'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 10, 'Radius': group_input.outputs["Icicle Radius"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_handle_positions, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    position_7 = nw.new_node(Nodes.InputPosition)
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 11.7500})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture_3.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: (2.0000, 2.0000, 2.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_5 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_4.outputs["Vector"], 1: (0.0300, 0.0300, 0.0300)},
        attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_7, 1: multiply_5.outputs["Vector"]})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': curve_to_mesh, 'Position': add_1.outputs["Vector"]})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_3, 'Material': surface.shaderfunc_to_material(shader_ice)})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Addition Object']},
        attrs={'transform_space': 'RELATIVE'})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_12, object_info_1.outputs["Geometry"]]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_1})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute, 'Density': 512.0000},
        attrs={'use_legacy_normal': True})
    
    position = nw.new_node(Nodes.InputPosition)
    
    object_info = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Freeze_control_EMPTY']},
        attrs={'transform_space': 'RELATIVE'})
    
    distance_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position, 1: object_info.outputs["Location"]},
        attrs={'operation': 'DISTANCE'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': distance_1.outputs["Value"], 2: group_input.outputs["Ice Grow Distance"], 3: 0.2000, 4: 0.0000},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    points_to_volume = nw.new_node(Nodes.PointsToVolume,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Density': 2.0000, 'Voxel Amount': group_input.outputs["Ice Resolution"], 'Radius': reroute_1})
    
    volume_to_mesh = nw.new_node(Nodes.VolumeToMesh,
        input_kwargs={'Volume': points_to_volume, 'Voxel Size': 0.0100, 'Voxel Amount': 128.0000, 'Threshold': 0.8800})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': volume_to_mesh, 'Level': 2})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    normal = nw.new_node(Nodes.InputNormal)
    
    multiply_6 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normal, 1: (-0.0800, -0.0800, -0.0800)},
        attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Scale': 6.8600}, attrs={'distance': 'CHEBYCHEV'})
    
    multiply_7 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: voronoi_texture.outputs["Distance"], 1: (1.0300, 1.0300, 1.0300)},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_8 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_6.outputs["Vector"], 1: multiply_7.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Detail': 4.0000})
    
    subtract_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_9 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract_1.outputs["Vector"], 1: (2.0000, 2.0000, 2.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_10 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_9.outputs["Vector"], 1: (3.6100, 3.6100, 3.6100)},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_11 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_8.outputs["Vector"], 1: multiply_10.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_1, 1: multiply_11.outputs["Vector"]})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_2.outputs["Vector"]})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': subdivision_surface, 'Position': reroute_18})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    normal_3 = nw.new_node(Nodes.InputNormal)
    
    sample_nearest = nw.new_node(Nodes.SampleNearest, input_kwargs={'Geometry': reroute_17})
    
    sample_index = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': reroute_17, 3: normal_3, 'Index': sample_nearest},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    dot_product_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: sample_index.outputs[2], 1: (0.0000, 0.0000, -1.0000)},
        attrs={'operation': 'DOT_PRODUCT'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': dot_product_1.outputs["Value"]})
    colorramp.color_ramp.interpolation = "B_SPLINE"
    colorramp.color_ramp.elements[0].position = 0.3773
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 3.0400, 'Detail': 1.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.3121
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.7000
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp.outputs["Color"], 7: colorramp_1.outputs["Color"]},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    position_5 = nw.new_node(Nodes.InputPosition)
    
    object_info_3 = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Freeze_control_EMPTY']},
        attrs={'transform_space': 'RELATIVE'})
    
    distance_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_5, 1: object_info_3.outputs["Location"]},
        attrs={'operation': 'DISTANCE'})
    
    map_range_3 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': distance_2.outputs["Value"], 2: 5.0000, 3: 1.0000, 4: 0.0000},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_3.outputs["Result"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.5000, 1.0000), (1.0000, 0.8217)])
    
    multiply_12 = nw.new_node(Nodes.VectorMath, input_kwargs={0: mix.outputs[2], 1: float_curve}, attrs={'operation': 'MULTIPLY'})
    
    multiply_13 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_12.outputs["Vector"], 1: group_input.outputs["Ice Drip Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_2, 1: multiply_13.outputs["Vector"]})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_20, 'Position': add_3.outputs["Vector"]})
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': set_position_1})
    
    position_6 = nw.new_node(Nodes.InputPosition)
    
    normal_2 = nw.new_node(Nodes.InputNormal)
    
    wave_texture = nw.new_node(Nodes.WaveTexture, attrs={'bands_direction': 'Z'})
    
    multiply_14 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normal_2, 1: wave_texture.outputs["Fac"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    normal_4 = nw.new_node(Nodes.InputNormal)
    
    dot_product_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normal_4, 1: (0.0000, 0.0000, -1.0000)},
        attrs={'operation': 'DOT_PRODUCT'})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': dot_product_2.outputs["Value"]})
    colorramp_3.color_ramp.interpolation = "B_SPLINE"
    colorramp_3.color_ramp.elements[0].position = 0.7742
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 1.0000
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_15 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: float_curve, 1: colorramp_3.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    sample_nearest_1 = nw.new_node(Nodes.SampleNearest, input_kwargs={'Geometry': reroute_21})
    
    sample_index_1 = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': reroute_21, 3: multiply_15.outputs["Vector"], 'Index': sample_nearest_1},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': sample_index_1.outputs[2]})
    
    multiply_16 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_14.outputs["Vector"], 1: reroute_15},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_17 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_16.outputs["Vector"], 1: (-0.0500, -0.0500, -0.0500)},
        attrs={'operation': 'MULTIPLY'})
    
    add_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_6, 1: multiply_17.outputs["Vector"]})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': subdivision_surface_1, 'Position': add_4.outputs["Vector"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_2, 'Material': surface.shaderfunc_to_material(shader_ice)})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_shade_smooth})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    frost_density = nw.new_node(nodegroup_frost_density().name, input_kwargs={'Value': group_input.outputs["Frost Particles Density"]})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_6, 'Density': frost_density},
        attrs={'use_legacy_normal': True})
    
    collection_info = nw.new_node(Nodes.CollectionInfo, input_kwargs={'Collection': bpy.data.collections['Frost_Particles']})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.8600, -0.8600, -0.8600), 1: (0.5800, 0.5800, 0.5800)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    rotate_euler = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': distribute_points_on_faces_1.outputs["Rotation"], 'Rotate By': random_value_2.outputs["Value"]})
    
    random_value_3 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.5000, 3: 2.0000})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': distance_1.outputs["Value"], 2: group_input.outputs["Frost Grow Distance"], 3: 1.0000, 4: 0.0000},
        attrs={'interpolation_type': 'SMOOTHERSTEP'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_1.outputs["Result"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    multiply_18 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_3.outputs[1], 1: reroute_2}, attrs={'operation': 'MULTIPLY'})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Frost Particles Scale"]})
    
    multiply_19 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_18, 1: reroute_22}, attrs={'operation': 'MULTIPLY'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Instance': collection_info, 'Rotation': rotate_euler, 'Scale': multiply_19})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_1})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_1, reroute_7, reroute_9]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_bake_target, selection=selection)
apply(bpy.context.active_object)
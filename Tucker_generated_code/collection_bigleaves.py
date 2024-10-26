import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_cracked_ground_by_abhay_siddhartha', singleton=False, type='ShaderNodeTree')
def nodegroup_cracked_ground_by_abhay_siddhartha(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000))])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Vector"]})
    
    base_color = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Base Color',
        attrs={'image': bpy.data.images['cracked_ground_Diffuse.jpg']})
    
    roughness = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Roughness',
        attrs={'image': bpy.data.images['cracked_ground_Roughness.jpg']})
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Color': roughness.outputs["Color"]})
    
    normal = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Normal',
        attrs={'image': bpy.data.images['cracked_ground_Normal.jpg']})
    
    normal_map = nw.new_node(Nodes.ShaderNodeNormalMap, input_kwargs={'Strength': 3.0000, 'Color': normal.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': base_color.outputs["Color"], 'Metallic': 0.0500, 'Specular': invert, 'Roughness': roughness.outputs["Color"], 'Normal': normal_map})
    
    displacement = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        label='Displacement',
        attrs={'image': bpy.data.images['cracked_ground_Displacement.jpg']})
    
    displacement_1 = nw.new_node(Nodes.Displacement, input_kwargs={'Height': displacement.outputs["Color"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'BSDF': principled_bsdf, 'Displacement': displacement_1},
        attrs={'is_active_output': True})

def shader_livistona_branch(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'B_UV'})
    
    mapping_1 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': attribute.outputs["Vector"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mapping_1})
    
    gradient_texture = nw.new_node(Nodes.GradientTexture, input_kwargs={'Vector': reroute})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': gradient_texture.outputs["Color"]})
    colorramp_2.color_ramp.interpolation = "EASE"
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.8500
    colorramp_2.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.4560
    colorramp_1.color_ramp.elements[0].color = [0.1366, 0.6038, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.5233
    colorramp_1.color_ramp.elements[1].color = [0.9728, 1.0000, 0.0181, 1.0000]
    
    translucent_bsdf = nw.new_node(Nodes.TranslucentBSDF, input_kwargs={'Color': colorramp_1.outputs["Color"]})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': reroute, 'Scale': 3.0000, 'Distortion': 10.0000},
        attrs={'wave_type': 'RINGS'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': wave_texture.outputs["Color"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0020, 0.0331, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.0569, 0.1706, 0.0514, 1.0000]
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Color': wave_texture.outputs["Color"]})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.2000, 'Height': wave_texture.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Specular': invert, 'Roughness': wave_texture.outputs["Color"], 'Normal': bump})
    
    mix_shader = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': colorramp_2.outputs["Color"], 1: translucent_bsdf, 2: principled_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_flat_stem', singleton=False, type='GeometryNodeTree')
def nodegroup_flat_stem(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketIntUnsigned', 'Resolution', 16),
            ('NodeSocketInt', 'Perimeter Resolution', 12),
            ('NodeSocketVectorTranslation', 'Middle', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Length', 1.0000),
            ('NodeSocketFloat', 'Radius', 1.0000),
            ('NodeSocketFloat', 'Thickness', 0.0000),
            ('NodeSocketFloat', 'EndPoint Radius', 0.5000),
            ('NodeSocketFloat', 'W', -1.8900),
            ('NodeSocketFloat', 'Detail', 2.0000),
            ('NodeSocketFloat', 'Distortion', 0.0000),
            ('NodeSocketMaterial', 'Material', None)])
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Resolution"]})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Middle"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Length"]})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_9})
    
    quadratic_bezier = nw.new_node(Nodes.QuadraticBezier,
        input_kwargs={'Resolution': reroute_13, 'Start': (0.0000, 0.0000, 0.0000), 'Middle': reroute_12, 'End': combine_xyz_1})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input.outputs["W"], 'Scale': 0.2500, 'Detail': group_input.outputs["Detail"], 'Roughness': 1.0000, 'Distortion': group_input.outputs["Distortion"]},
        attrs={'noise_dimensions': '4D'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': spline_parameter.outputs["Factor"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: reroute_7},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': quadratic_bezier, 'Offset': multiply.outputs["Vector"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': spline_parameter.outputs["Length"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': set_position_1, 2: reroute_5})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["EndPoint Radius"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_7, 3: 1.0000, 4: reroute})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range.outputs["Result"], 1: reroute_17},
        attrs={'operation': 'MULTIPLY'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: 30.0000}, attrs={'operation': 'DIVIDE'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius,
        input_kwargs={'Curve': capture_attribute_1.outputs["Geometry"], 'Radius': divide})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Perimeter Resolution"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_10})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute_6})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.1200, 0.9500), (0.2500, 0.7500), (0.5130, 0.0000), (0.7500, 0.7500), (0.8808, 0.9500)])
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Thickness"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_19, 1: 1.5000}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract_1})
    
    multiply_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: float_curve, 1: combine_xyz_2}, attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Offset': multiply_2.outputs["Vector"]})
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': set_position, 2: reroute_3})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': capture_attribute.outputs["Geometry"], 'Fill Caps': True})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Material"]})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    set_material = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': curve_to_mesh, 'Material': reroute_20})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs[2]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_15, 'Y': capture_attribute.outputs[2]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': set_material, 'Curve': set_curve_radius, 'UV': combine_xyz, 'Length': reroute_14},
        attrs={'is_active_output': True})

def shader_mars_soil_texture(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': texture_coordinate.outputs["Object"]})
    
    noname = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    _1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': noname, 'Scale': 8.0000, 'Detail': 15.0000, 'Roughness': 0.5500})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute, 'Scale': 10.0000, 'Roughness': 0.4500})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.1500, 6: reroute, 7: noise_texture.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'LINEAR_LIGHT'})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': mix.outputs[2], 'Scale': 3.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Distance"]})
    colorramp.color_ramp.elements[0].position = 0.2598
    colorramp.color_ramp.elements[0].color = [0.7454, 0.7454, 0.7454, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.4079
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    mix_legacy = nw.new_node(Nodes.MixRGB,
        input_kwargs={'Fac': 0.1743, 'Color1': _1.outputs["Fac"], 'Color2': colorramp.outputs["Color"]},
        attrs={'blend_type': 'DARKEN'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0500, 6: reroute, 7: noise_texture.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'LINEAR_LIGHT'})
    
    voronoi_texture_2 = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': mix_2.outputs[2], 'Scale': 30.0000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_2.outputs["Distance"]})
    colorramp_2.color_ramp.elements[0].position = 0.1057
    colorramp_2.color_ramp.elements[0].color = [0.4125, 0.4125, 0.4125, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.3988
    colorramp_2.color_ramp.elements[1].color = [0.4125, 0.4125, 0.4125, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0500, 6: reroute, 7: noise_texture.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'LINEAR_LIGHT'})
    
    voronoi_texture_1 = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': mix_1.outputs[2], 'Scale': 15.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture_1.outputs["Distance"]})
    colorramp_1.color_ramp.elements[0].position = 0.1057
    colorramp_1.color_ramp.elements[0].color = [0.5711, 0.5711, 0.5711, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.4079
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    mix_legacy_2 = nw.new_node(Nodes.MixRGB,
        input_kwargs={'Fac': 1.0000, 'Color1': colorramp_2.outputs["Color"], 'Color2': colorramp_1.outputs["Color"]},
        attrs={'blend_type': 'LIGHTEN'})
    
    mix_legacy_1 = nw.new_node(Nodes.MixRGB,
        input_kwargs={'Fac': 0.4271, 'Color1': mix_legacy, 'Color2': mix_legacy_2},
        attrs={'blend_type': 'LIGHTEN'})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_legacy_1})
    colorramp_3.color_ramp.elements[0].position = 0.4182
    colorramp_3.color_ramp.elements[0].color = [0.0704, 0.0369, 0.0194, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.6955
    colorramp_3.color_ramp.elements[1].color = [0.0331, 0.0075, 0.0010, 1.0000]
    
    bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp_3.outputs["Color"], 'Subsurface Color': (0.0704, 0.0369, 0.0194, 1.0000)})
    
    _2 = nw.new_node(Nodes.Displacement, input_kwargs={'Height': mix_legacy_1, 'Scale': 0.1400})
    
    _3 = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': bsdf, 'Displacement': _2},
        attrs={'is_active_output': True})

def shader_livistona_base(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'uv_map'})
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': attribute.outputs["Vector"]})
    
    group_1 = nw.new_node(nodegroup_cracked_ground_by_abhay_siddhartha().name, input_kwargs={'Vector': mapping})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': group_1.outputs["BSDF"]},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Density', 200.0000),
            ('NodeSocketFloat', 'Exponent', 2.7183),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketBool', 'Shade Smooth', True),
            ('NodeSocketString', 'Branches', ''),
            ('NodeSocketFloat', 'Rotation', -4.2000),
            ('NodeSocketIntUnsigned', 'Resolution', 16),
            ('NodeSocketInt', 'Perimeter Resolution', 12),
            ('NodeSocketFloat', 'Length', 1.0000),
            ('NodeSocketFloat', 'Radius', 0.6800),
            ('NodeSocketFloat', 'Thickness', 0.0000),
            ('NodeSocketFloat', 'EndPoint Radius', 0.2000),
            ('NodeSocketFloat', 'W', -2.3150),
            ('NodeSocketFloat', 'Detail', 2.0000),
            ('NodeSocketFloat', 'Distortion', 0.0000),
            ('NodeSocketString', 'Leaves', ''),
            ('NodeSocketInt', 'Select leaf', 0),
            ('NodeSocketFloat', 'Scale', 1.0000),
            ('NodeSocketFloat', 'Leaves Rotaion', 0.5000),
            ('NodeSocketString', 'Base', ''),
            ('NodeSocketInt', 'Resolution_1', 8),
            ('NodeSocketFloatDistance', 'Radius_1', 0.1000)])
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Resolution_1"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius_1"]})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Segments': reroute_1, 'Rings': reroute_1, 'Radius': reroute_17})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: -0.0100}, attrs={'operation': 'LESS_THAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': store_named_attribute, 'Selection': less_than})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Density"]})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Seed"]})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': delete_geometry, 'Density Max': 250.0000, 'Density': reroute_24, 'Density Factor': 0.5000, 'Seed': reroute},
        attrs={'use_legacy_normal': True})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Resolution"]})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Perimeter Resolution"]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Length"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Thickness"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["EndPoint Radius"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["W"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Detail"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Distortion"]})
    
    flat_stem = nw.new_node(nodegroup_flat_stem().name,
        input_kwargs={'Resolution': reroute_13, 'Perimeter Resolution': reroute_12, 'Length': reroute_11, 'Radius': reroute_10, 'Thickness': reroute_9, 'EndPoint Radius': reroute_8, 'W': reroute_7, 'Detail': reroute_6, 'Distortion': reroute_5, 'Material': surface.shaderfunc_to_material(shader_livistona_branch)})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['Livistona(Chinese_Fan_Palm)'], 'Separate Children': True, 'Reset Children': True})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Select leaf"]})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent}, attrs={'axis': 'Z', 'pivot_axis': 'Z'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': flat_stem.outputs["Curve"], 'Selection': endpoint_selection, 'Instance': collection_info, 'Pick Instance': True, 'Instance Index': reroute_16, 'Rotation': align_euler_to_vector, 'Scale': reroute_15})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Leaves Rotaion"]})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute_28, 1: 57.2958}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances, input_kwargs={'Instances': instance_on_points, 'Rotation': combine_xyz_1})
    
    translate_instances = nw.new_node(Nodes.TranslateInstances,
        input_kwargs={'Instances': rotate_instances, 'Translation': (0.0000, -0.0030, -0.0010)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flat_stem.outputs["Mesh"], translate_instances]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Shade Smooth"]})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry, 'Shade Smooth': reroute_29})
    
    align_euler_to_vector_1 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Vector': distribute_points_on_faces.outputs["Normal"]},
        attrs={'axis': 'Y', 'pivot_axis': 'Z'})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.8000, 3: 1.2000, 'Seed': reroute})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Exponent"]})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: random_value.outputs[1], 1: reroute_27}, attrs={'operation': 'POWER'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': set_shade_smooth_1, 'Rotation': align_euler_to_vector_1, 'Scale': power})
    
    index = nw.new_node(Nodes.Index)
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rotation"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_30})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: reroute_31}, attrs={'operation': 'MULTIPLY'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 57.2958}, attrs={'operation': 'DIVIDE'})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 10.0000, 3: -10.0000, 'Seed': reroute})
    
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_1.outputs[1], 1: 57.2958}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide_1, 'Y': divide_2, 'Z': divide_2})
    
    rotate_instances_1 = nw.new_node(Nodes.RotateInstances, input_kwargs={'Instances': instance_on_points_1, 'Rotation': combine_xyz})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': delete_geometry, 'Offset Scale': 0.0200})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': extrude_mesh.outputs["Mesh"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': subdivision_surface, 'Shade Smooth': reroute_29})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_mars_soil_texture)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [rotate_instances_1, set_material]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_1})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': merge_by_distance})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': realize_instances})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': flat_stem.outputs["UV"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': reroute_20, 'branch_uv': reroute_19},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_livistona_base, selection=selection)
    surface.add_material(obj, shader_mars_soil_texture, selection=selection)
apply(bpy.context.active_object)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_band_color', singleton=False, type='ShaderNodeTree')
def nodegroup_band_color(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    rgb = nw.new_node(Nodes.RGB)
    rgb.outputs[0].default_value = (0.1789, 0.1325, 0.0310, 1.0000)
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Color': rgb}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_noise_scratches', singleton=False, type='ShaderNodeTree')
def nodegroup_noise_scratches(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Scale', 5.0000),
            ('NodeSocketFloat', 'Ratio', 0.5000),
            ('NodeSocketFloat', 'Spread', 1.0000),
            ('NodeSocketFloat', 'Detail', 2.0000)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Vector"]})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: reroute}, attrs={'operation': 'ABSOLUTE'})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: absolute, 1: 0.0000}, attrs={'operation': 'GREATER_THAN'})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mix_6 = nw.new_node(Nodes.Mix,
        input_kwargs={0: greater_than, 6: texture_coordinate.outputs["Generated"], 7: reroute},
        attrs={'data_type': 'RGBA'})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_6.outputs[2]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    voronoi_texture_3 = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': reroute_14, 'Scale': reroute_15})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 10.0000, 1: reroute_15}, attrs={'operation': 'DIVIDE'})
    
    mix_14 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: voronoi_texture_3.outputs["Color"], 7: divide},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    mix_8 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: reroute_14, 7: mix_14.outputs[2]},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_15, 1: group_input.outputs["Ratio"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Detail"]})
    
    noise_texture_4 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mix_8.outputs[2], 'Scale': multiply, 'Detail': reroute_17})
    
    separate_rgb_3 = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': noise_texture_4.outputs["Color"]})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: separate_rgb_3.outputs["Red"]}, attrs={'operation': 'SUBTRACT'})
    
    absolute_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract}, attrs={'operation': 'ABSOLUTE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Spread"], 1: 1.0000})
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: 10.0000, 1: add}, attrs={'operation': 'POWER'})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': power})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: absolute_1, 1: reroute_16},
        attrs={'operation': 'MULTIPLY', 'use_clamp': True})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_rgb_3.outputs["Green"]}, attrs={'operation': 'SUBTRACT'})
    
    absolute_2 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_1}, attrs={'operation': 'ABSOLUTE'})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: absolute_2, 1: reroute_16},
        attrs={'operation': 'MULTIPLY', 'use_clamp': True})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_1, 1: multiply_2},
        attrs={'operation': 'MULTIPLY', 'use_clamp': True})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_rgb_3.outputs["Blue"]}, attrs={'operation': 'SUBTRACT'})
    
    absolute_3 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_2}, attrs={'operation': 'ABSOLUTE'})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: absolute_3, 1: reroute_16},
        attrs={'operation': 'MULTIPLY', 'use_clamp': True})
    
    multiply_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_3, 1: multiply_4},
        attrs={'operation': 'MULTIPLY', 'use_clamp': True})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': reroute_14, 'Scale': reroute_15}, attrs={'feature': 'F2'})
    
    multiply_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: voronoi_texture.outputs["Distance"], 1: voronoi_texture.outputs["Distance"]},
        attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture_7 = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': reroute_14, 'Scale': reroute_15})
    
    multiply_7 = nw.new_node(Nodes.Math,
        input_kwargs={0: voronoi_texture_7.outputs["Distance"], 1: voronoi_texture_7.outputs["Distance"]},
        attrs={'operation': 'MULTIPLY'})
    
    subtract_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_6, 1: multiply_7}, attrs={'operation': 'SUBTRACT'})
    
    power_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_3, 1: 0.5000}, attrs={'operation': 'POWER', 'use_clamp': True})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': power_1})
    
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_5, 1: reroute_13},
        attrs={'operation': 'DIVIDE', 'use_clamp': True})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Value': divide_1, 'Cells': voronoi_texture_3.outputs["Color"], 'Falloff': reroute_13},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_noise_streaks', singleton=False, type='ShaderNodeTree')
def nodegroup_noise_streaks(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Input', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Scale', 5.0000),
            ('NodeSocketFloat', 'Ratio', 10.0000),
            ('NodeSocketFloat', 'Count', 1.0000),
            ('NodeSocketFloat', 'Variation', 0.0000)])
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Input"]})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7}, attrs={'operation': 'ABSOLUTE'})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: absolute, 1: 0.0000}, attrs={'operation': 'GREATER_THAN'})
    
    texture_coordinate_9 = nw.new_node(Nodes.TextureCoord)
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': texture_coordinate_9.outputs["Generated"], 'Axis': (0.0000, 1.0000, 0.0000), 'Angle': 1.5708})
    
    mix_15 = nw.new_node(Nodes.Mix, input_kwargs={0: greater_than, 6: vector_rotate, 7: reroute_7}, attrs={'data_type': 'RGBA'})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': mix_15.outputs[2]})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Ratio"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_2.outputs["X"], 1: reroute_21},
        attrs={'operation': 'MULTIPLY'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Y"], 1: reroute_21}, attrs={'operation': 'DIVIDE'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Z"], 1: reroute_21}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply, 'Y': divide, 'Z': divide_1})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    voronoi_texture_1 = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': combine_xyz_2, 'Scale': reroute_22},
        attrs={'feature': 'F2'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: voronoi_texture_1.outputs["Distance"], 1: voronoi_texture_1.outputs["Distance"]},
        attrs={'operation': 'MULTIPLY'})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': combine_xyz_2, 'Scale': reroute_22})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: voronoi_texture.outputs["Distance"], 1: voronoi_texture.outputs["Distance"]},
        attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: multiply_2}, attrs={'operation': 'SUBTRACT'})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Variation"]})
    
    voronoi_texture_2 = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': combine_xyz_2, 'Scale': reroute_22})
    
    separate_rgb_3 = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': voronoi_texture_2.outputs["Color"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Count"]})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: reroute_15}, attrs={'operation': 'SUBTRACT', 'use_clamp': True})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_1})
    
    greater_than_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_rgb_3.outputs["Red"], 1: reroute_11},
        attrs={'operation': 'GREATER_THAN'})
    
    subtract_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_rgb_3.outputs["Green"], 1: reroute_11},
        attrs={'operation': 'SUBTRACT'})
    
    subtract_3 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: reroute_11}, attrs={'operation': 'SUBTRACT'})
    
    divide_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: subtract_2, 1: subtract_3},
        attrs={'operation': 'DIVIDE', 'use_clamp': True})
    
    mix_4 = nw.new_node(Nodes.Mix, input_kwargs={0: reroute_16, 6: greater_than_1, 7: divide_2}, attrs={'data_type': 'RGBA'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: mix_4.outputs[2]}, attrs={'operation': 'MULTIPLY'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Value': multiply_3, 'Color': voronoi_texture_2.outputs["Color"]},
        attrs={'is_active_output': True})

def shader_treasure_base(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 25.5000, 'Detail': 9.9000, 'Roughness': 0.3083, 'Distortion': 0.1000})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.6441, 0.3755, 0.0770, 1.0000), 'Metallic': 0.7227, 'Specular': 0.6955, 'Roughness': 0.4364})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.1245, 0.0457, 0.0000, 1.0000), 'Metallic': 0.7227, 'Specular': 0.6955, 'Roughness': 0.4364})
    
    mix_shader = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': noise_texture.outputs["Color"], 1: principled_bsdf, 2: principled_bsdf_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def shader_handles(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 5.5000, 'Detail': 1.9000, 'Roughness': 0.2833})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Color"], 1: 0.0600}, attrs={'operation': 'MULTIPLY'})
    
    bevel = nw.new_node('ShaderNodeBevel', input_kwargs={'Radius': multiply})
    
    geometry_1 = nw.new_node(Nodes.NewGeometry)
    
    dot_product = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bevel, 1: geometry_1.outputs["Normal"]},
        attrs={'operation': 'DOT_PRODUCT'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': dot_product.outputs["Value"], 3: 1.0000, 4: 0.0000})
    
    group = nw.new_node(nodegroup_band_color().name)
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.4583, 6: map_range.outputs["Result"], 7: group},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.1000, 'Height': map_range.outputs["Result"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Metallic': 1.0000, 'Specular': 1.0000, 'Roughness': 0.5091, 'Sheen': 0.3182, 'Normal': bump})
    
    glossy_bsdf = nw.new_node(Nodes.GlossyBSDF, input_kwargs={'Color': mix.outputs[2]})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': 0.6750, 1: principled_bsdf, 2: glossy_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_handle_gen', singleton=False, type='GeometryNodeTree')
def nodegroup_handle_gen(nw: NodeWrangler):
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
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.1455, 0.1188), (0.6591, 0.2563), (0.9955, 0.9500)])
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_6, 'Y': reroute_5, 'Z': float_curve})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_line, 'Position': combine_xyz})
    
    group_input_2 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Width', 0.0000),
            ('NodeSocketFloat', 'Height', 0.0000),
            ('NodeSocketFloat', 'Thickness', 0.0000),
            ('NodeSocketInt', 'Fitting Resolution', 4),
            ('NodeSocketFloat', 'Fitting Size', 1.0000),
            ('NodeSocketInt', 'Handle Resolution', 4),
            ('NodeSocketBool', 'Studs', False),
            ('NodeSocketInt', 'Stud Amount', 10),
            ('NodeSocketInt', 'Stud Resolution', 4),
            ('NodeSocketBool', 'Smooth Studs', False)])
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': set_position, 'Scale': group_input_2.outputs["Width"]},
        attrs={'domain': 'EDGE', 'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements, 'Scale': group_input_2.outputs["Height"], 'Axis': (0.0000, 0.0000, 1.0000)},
        attrs={'domain': 'EDGE', 'scale_mode': 'SINGLE_AXIS'})
    
    mesh_to_curve_1 = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': scale_elements_1})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_curve_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_2.outputs["Thickness"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_2.outputs["Handle Resolution"], 'Radius': reroute_1})
    
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': curve_circle.outputs["Curve"]})
    
    rotate_instances_1 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': geometry_to_instance, 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': rotate_instances_1})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_position_1, 'Profile Curve': realize_instances})
    
    curve_to_points_1 = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': mesh_to_curve_1, 'Count': 2})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_2.outputs["Fitting Resolution"], 1: 2.0000},
        attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_2.outputs["Fitting Size"], 1: 2.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_2.outputs["Thickness"], 1: multiply},
        attrs={'operation': 'MULTIPLY'})
    
    uv_sphere_1 = nw.new_node(Nodes.MeshUVSphere,
        input_kwargs={'Segments': group_input_2.outputs["Fitting Resolution"], 'Rings': subtract, 'Radius': multiply_1})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere_1.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points_1.outputs["Points"], 'Instance': store_named_attribute})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_to_mesh, instance_on_points_1]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry_1, 'Shade Smooth': False})
    
    curve_to_points = nw.new_node(Nodes.CurveToPoints,
        input_kwargs={'Curve': mesh_to_curve_1, 'Count': group_input_2.outputs["Stud Amount"]})
    
    subtract_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_2.outputs["Stud Resolution"], 1: 2.0000},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.7000}, attrs={'operation': 'MULTIPLY'})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere,
        input_kwargs={'Segments': group_input_2.outputs["Stud Resolution"], 'Rings': subtract_1, 'Radius': multiply_2})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points.outputs["Points"], 'Instance': store_named_attribute_1, 'Rotation': curve_to_points.outputs["Rotation"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_1.outputs["X"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_8})
    
    absolute_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["Z"]}, attrs={'operation': 'ABSOLUTE'})
    
    clamp = nw.new_node(Nodes.Clamp, input_kwargs={'Value': absolute_1, 'Max': 1.5000})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_2.outputs["Thickness"]}, attrs={'operation': 'MULTIPLY'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: clamp, 1: multiply_3}, attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: multiply_4})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_1.outputs["Y"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_1.outputs["Z"]})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_1, 'Y': reroute_11, 'Z': reroute_10})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: -1.5000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': instance_on_points, 'Selection': greater_than, 'Position': combine_xyz_2, 'Offset': combine_xyz_1})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_9}, attrs={'operation': 'LESS_THAN'})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: clamp, 1: multiply_5}, attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_6, 1: reroute_7})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_2})
    
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

def shader_fittings(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 5.5000, 'Detail': 1.9000, 'Roughness': 0.2833})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Color"], 1: 0.0250}, attrs={'operation': 'MULTIPLY'})
    
    bevel = nw.new_node('ShaderNodeBevel', input_kwargs={'Radius': multiply})
    
    geometry_1 = nw.new_node(Nodes.NewGeometry)
    
    dot_product = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bevel, 1: geometry_1.outputs["Normal"]},
        attrs={'operation': 'DOT_PRODUCT'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': dot_product.outputs["Value"], 3: 1.0000, 4: 0.0000})
    
    group = nw.new_node(nodegroup_band_color().name)
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.4583, 6: map_range.outputs["Result"], 7: group},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.1000, 'Height': map_range.outputs["Result"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Metallic': 1.0000, 'Specular': 1.0000, 'Roughness': 0.5091, 'Sheen': 0.3182, 'Normal': bump})
    
    glossy_bsdf = nw.new_node(Nodes.GlossyBSDF, input_kwargs={'Color': mix.outputs[2]})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={1: principled_bsdf, 2: glossy_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def shader_bands(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group = nw.new_node(nodegroup_band_color().name)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 5.5000, 'Detail': 4.4000, 'Roughness': 0.4417, 'Distortion': 0.1000})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Color"], 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    bevel = nw.new_node('ShaderNodeBevel', input_kwargs={'Radius': multiply})
    
    geometry_1 = nw.new_node(Nodes.NewGeometry)
    
    dot_product = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bevel, 1: geometry_1.outputs["Normal"]},
        attrs={'operation': 'DOT_PRODUCT'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': dot_product.outputs["Value"], 3: 1.0000, 4: 0.0000})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.4583, 6: group, 7: map_range.outputs["Result"]},
        attrs={'blend_type': 'ADD', 'data_type': 'RGBA'})
    
    glossy_bsdf = nw.new_node(Nodes.GlossyBSDF, input_kwargs={'Color': mix.outputs[2], 'Roughness': 0.4308})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Height': map_range.outputs["Result"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Metallic': 1.0000, 'Specular': 1.0000, 'Roughness': 0.5091, 'Sheen': 0.3182, 'Normal': bump})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': 0.4667, 1: glossy_bsdf, 2: principled_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def shader_chest_base(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry = nw.new_node(Nodes.NewGeometry)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': geometry.outputs["Position"], 'Rotation': (0.0000, 1.5708, 0.0000)})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mapping})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_3, 'Scale': 4.7000, 'Detail': 0.0000, 'Roughness': 0.5167, 'Distortion': 0.4000})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Color"], 1: 0.0500}, attrs={'operation': 'MULTIPLY'})
    
    bevel = nw.new_node('ShaderNodeBevel', input_kwargs={'Radius': multiply})
    
    geometry_1 = nw.new_node(Nodes.NewGeometry)
    
    dot_product = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bevel, 1: geometry_1.outputs["Normal"]},
        attrs={'operation': 'DOT_PRODUCT'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': dot_product.outputs["Value"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range.outputs["Result"]})
    colorramp.color_ramp.elements[0].position = 0.9318
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.1713, 0.0436, 0.0187, 1.0000]
    
    group = nw.new_node(nodegroup_noise_streaks().name, input_kwargs={'Input': reroute_3, 'Scale': 0.6000, 'Ratio': 25.0000})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: group.outputs["Color"], 6: (0.0549, 0.0317, 0.0080, 1.0000), 7: (0.0205, 0.0049, 0.0022, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp.outputs["Color"], 7: mix_2.outputs[2]},
        attrs={'blend_type': 'DARKEN', 'data_type': 'RGBA'})
    
    principled_bsdf_2 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_3.outputs[2], 'Subsurface Color': (0.7383, 0.8000, 0.0004, 1.0000)})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group.outputs["Color"]})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: (1.0000, 1.0000, 1.0000, 1.0000), 7: reroute},
        attrs={'blend_type': 'SUBTRACT', 'data_type': 'RGBA'})
    
    mix = nw.new_node(Nodes.Mix, input_kwargs={0: 0.0000, 6: reroute, 7: mix_1.outputs[2]}, attrs={'data_type': 'RGBA'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix.outputs[2]})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Height': reroute_1})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_2.outputs[2], 'Roughness': reroute_1, 'Normal': bump})
    
    group_1 = nw.new_node(nodegroup_noise_scratches().name,
        input_kwargs={'Vector': reroute_3, 'Scale': 7.5000, 'Ratio': 0.3000, 'Spread': 1.1000, 'Detail': 0.5000})
    
    bump_1 = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.8500, 'Distance': 1.0000, 'Height': group_1.outputs["Value"]})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_2.outputs[2], 'Roughness': group_1.outputs["Value"], 'Normal': bump_1})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={1: principled_bsdf, 2: principled_bsdf_1})
    
    mix_shader_1 = nw.new_node(Nodes.MixShader, input_kwargs={1: principled_bsdf_2, 2: mix_shader})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': mix_shader_1, 'Displacement': reroute_2},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Seed', 0),
            ('NodeSocketInt', 'X Resolution', 2),
            ('NodeSocketInt', 'Y Resolution', 2),
            ('NodeSocketInt', 'Z Resolution', 2),
            ('NodeSocketFloat', 'Chest Depth', 1.5000),
            ('NodeSocketFloat', 'Chest Width', 3.0000),
            ('NodeSocketFloat', 'Chest Height', 1.5000),
            ('NodeSocketFloat', 'Chest Base Size', 1.0000),
            ('NodeSocketBool', 'Square Lid', False),
            ('NodeSocketFloat', 'Lid Rotation', 0.0000),
            ('NodeSocketInt', 'Lid Resolution', 3),
            ('NodeSocketInt', 'Lid Side Bands', 1),
            ('NodeSocketFloat', 'Lid Height', 0.6000),
            ('NodeSocketFloat', 'Lid Slope', 0.0000),
            ('NodeSocketFloat', 'Lid Size', 1.0000),
            ('NodeSocketBool', 'Pillowed Corners', False),
            ('NodeSocketFloat', 'Corner Size', 0.0000),
            ('NodeSocketInt', 'Corner Subdivisions', 0),
            ('NodeSocketFloat', 'Corner Edge Crease', 0.0000),
            ('NodeSocketFloat', 'Corner Vertex Crease', 0.0000),
            ('NodeSocketFloat', 'Band Size', 0.5000),
            ('NodeSocketInt', 'Band Resolution', 4),
            ('NodeSocketInt', 'Band Subdivisions', 1),
            ('NodeSocketFloat', 'Band Edge Crease', 0.0000),
            ('NodeSocketFloat', 'Band Vert Crease', 0.3000),
            ('NodeSocketBool', 'Studs', False),
            ('NodeSocketInt', 'Stud Amount', 2),
            ('NodeSocketInt', 'Stud Resolution', 2),
            ('NodeSocketFloat', 'Stud Size', 1.0000),
            ('NodeSocketFloat', 'Stud Spikiness', 0.0000),
            ('NodeSocketBool', 'Smooth Studs', False),
            ('NodeSocketBool', 'Hinges', True),
            ('NodeSocketInt', 'Hinge Amount', 0),
            ('NodeSocketBool', 'Clasps', True),
            ('NodeSocketInt', 'Clasps Per Edge', 0),
            ('NodeSocketInt', 'Clasp Number', 0),
            ('NodeSocketFloat', 'Clasp Rotation', -1.5708),
            ('NodeSocketBool', 'Locks', True),
            ('NodeSocketFloat', 'Lock Size', 1.0000),
            ('NodeSocketBool', 'Handles', True),
            ('NodeSocketFloat', 'Handle Width', 1.0000),
            ('NodeSocketFloat', 'Handle Length', 1.0000),
            ('NodeSocketFloat', 'Handle Height', 0.0000),
            ('NodeSocketFloat', 'Handle Thickness', 0.2000),
            ('NodeSocketFloat', 'Handle Rotation', 1.0000),
            ('NodeSocketInt', 'Handle Fitting Resolution', 4),
            ('NodeSocketFloat', 'Handle Fitting Size', 1.0000),
            ('NodeSocketInt', 'Handle Resolution', 4),
            ('NodeSocketBool', 'Treasure', True),
            ('NodeSocketFloat', 'Treasure Amount', 5.0000),
            ('NodeSocketBool', 'Gems', True),
            ('NodeSocketFloat', 'Gem Amount', 1.0000)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Chest Depth"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Chest Width"]})
    
    reroute_129 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Chest Height"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute, 'Y': reroute_9, 'Z': reroute_129})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_4})
    
    reroute_128 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["X Resolution"]})
    
    reroute_127 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Y Resolution"]})
    
    reroute_126 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Z Resolution"]})
    
    cube = nw.new_node(Nodes.MeshCube,
        input_kwargs={'Size': reroute_10, 'Vertices X': reroute_128, 'Vertices Y': reroute_127, 'Vertices Z': reroute_126})
    
    store_named_attribute_7 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    position_15 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_16 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_15})
    
    reroute_270 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Chest Height"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_270, 1: 0.4950}, attrs={'operation': 'MULTIPLY'})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_16.outputs["Z"], 1: multiply})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': store_named_attribute_7, 'Selection': greater_than},
        attrs={'domain': 'FACE'})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': delete_geometry})
    
    reroute_66 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    position_7 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_8 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_7})
    
    reroute_113 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_8.outputs["X"]})
    
    reroute_115 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_270})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_115}, attrs={'operation': 'MULTIPLY'})
    
    reroute_271 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Chest Base Size"]})
    
    reroute_114 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_271})
    
    reroute_67 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_114})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz_8.outputs["Z"], 2: multiply_1, 3: reroute_67})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range.outputs["Result"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0000), (0.5636, 0.4687), (1.0000, 1.0000)])
    
    reroute_201 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': float_curve_1})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_113, 1: reroute_201}, attrs={'operation': 'MULTIPLY'})
    
    reroute_68 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_8.outputs["Y"]})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_201, 1: reroute_68}, attrs={'operation': 'MULTIPLY'})
    
    reroute_111 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_8.outputs["Z"]})
    
    reroute_112 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_111})
    
    combine_xyz_17 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_2, 'Y': multiply_3, 'Z': reroute_112})
    
    set_position_11 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_66, 'Position': combine_xyz_17})
    
    reroute_175 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_11})
    
    reroute_88 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_175})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_88, 'Material': surface.shaderfunc_to_material(shader_chest_base)})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_175})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    mesh_to_curve_1 = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': reroute_7})
    
    reroute_82 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mesh_to_curve_1})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_82})
    
    reroute_63 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_35})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_63})
    
    geometry_to_instance_3 = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': reroute_28})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': geometry_to_instance_3})
    
    reroute_83 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Stud Amount"]})
    
    reroute_85 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_83})
    
    reroute_86 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_85})
    
    reroute_84 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_86})
    
    curve_to_points = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': reroute_21, 'Count': reroute_84})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_3.outputs["X"]}, attrs={'operation': 'ABSOLUTE'})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Depth"], 1: 0.4000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_4, 1: group_input_1.outputs["Chest Base Size"]},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute, 1: multiply_5})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Stud Resolution"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_38, 1: 2.0000})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_38})
    
    multiply_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: 0.1000, 1: group_input_1.outputs["Band Size"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_87 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Stud Size"]})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_6, 1: reroute_87}, attrs={'operation': 'MULTIPLY'})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Segments': add, 'Rings': reroute_46, 'Radius': multiply_7})
    
    store_named_attribute_5 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_65 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Studs"]})
    
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: reroute_65}, attrs={'operation': 'NOT'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_1.outputs["Stud Spikiness"], 1: 1.0000})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_1, 'Y': 1.0000, 'Z': 1.0000})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points.outputs["Points"], 'Selection': greater_than_1, 'Instance': store_named_attribute_5, 'Pick Instance': op_not, 'Scale': combine_xyz_7})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1})
    
    position_5 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_5})
    
    less_equal = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_1.outputs["X"], 1: -0.0000, 'Epsilon': 0.5010},
        attrs={'operation': 'LESS_EQUAL'})
    
    reroute_231 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_231, 1: -0.1400}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_33 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_8})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances_2, 'Selection': less_equal, 'Offset': combine_xyz_33})
    
    greater_than_2 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_1.outputs["X"]})
    
    multiply_9 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_231, 1: 0.1400}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_34 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_9})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': greater_than_2, 'Offset': combine_xyz_34})
    
    absolute_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_3.outputs["Y"]}, attrs={'operation': 'ABSOLUTE'})
    
    multiply_10 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Width"], 1: 0.4000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_11 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_10, 1: group_input_1.outputs["Chest Base Size"]},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_3 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute_1, 1: multiply_11})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': add_1, 'Z': 1.0000})
    
    instance_on_points_6 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points.outputs["Points"], 'Selection': greater_than_3, 'Instance': store_named_attribute_5, 'Pick Instance': op_not, 'Scale': combine_xyz_8})
    
    realize_instances_9 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_6})
    
    position_6 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_6 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_6})
    
    less_equal_1 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_6.outputs["Y"], 1: -0.0000, 'Epsilon': 0.5010},
        attrs={'operation': 'LESS_EQUAL'})
    
    combine_xyz_35 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_8})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances_9, 'Selection': less_equal_1, 'Offset': combine_xyz_35})
    
    greater_than_4 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_6.outputs["Y"]})
    
    combine_xyz_36 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_9})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_2, 'Selection': greater_than_4, 'Offset': combine_xyz_36})
    
    join_geometry_9 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_1, set_position_3]})
    
    set_shade_smooth_3 = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': join_geometry_9, 'Shade Smooth': group_input_1.outputs["Smooth Studs"]})
    
    reroute_73 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_shade_smooth_3})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Band Size"], 1: 5.0000},
        attrs={'operation': 'DIVIDE'})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_1.outputs["Band Resolution"], 'Radius': divide})
    
    geometry_to_instance_1 = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': curve_circle_1.outputs["Curve"]})
    
    add_2 = nw.new_node(Nodes.VectorMath, input_kwargs={1: (0.0000, 0.0000, 0.7854)})
    
    rotate_instances_2 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': geometry_to_instance_1, 'Rotation': add_2.outputs["Vector"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': rotate_instances_2})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': reroute_82, 'Profile Curve': realize_instances})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh_1, 'Shade Smooth': False})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_shade_smooth_1})
    
    reroute_91 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_91})
    
    reroute_70 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_48})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': reroute_70, 'Level': group_input_1.outputs["Band Subdivisions"], 'Edge Crease': group_input_1.outputs["Band Edge Crease"], 'Vertex Crease': group_input_1.outputs["Band Vert Crease"]})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': reroute_5})
    
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Corner Size"], 1: 3.5000},
        attrs={'operation': 'DIVIDE'})
    
    divide_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Band Size"], 1: 5.0000},
        attrs={'operation': 'DIVIDE'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: divide_1, 1: divide_2})
    
    add_4 = nw.new_node(Nodes.Math, input_kwargs={0: add_3, 1: 0.0390})
    
    reroute_76 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_4})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_76, 'Y': reroute_76, 'Z': reroute_76})
    
    cube_1 = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz_3})
    
    store_named_attribute_6 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_1.outputs["Mesh"], 'Name': 'uv_map', 3: cube_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_to_points, 'Instance': store_named_attribute_6})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': instance_on_points, 'Offset Scale': 0.0100})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': 0.5000},
        label='Scale Elements')
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [instance_on_points, scale_elements]})
    
    switch_4 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_1.outputs["Pillowed Corners"], 14: instance_on_points, 15: join_geometry_1})
    
    subdivision_surface_3 = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': switch_4.outputs[6], 'Level': group_input_1.outputs["Corner Subdivisions"], 'Edge Crease': group_input_1.outputs["Corner Edge Crease"], 'Vertex Crease': group_input_1.outputs["Corner Vertex Crease"]})
    
    reroute_55 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subdivision_surface_3})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_55})
    
    reroute_69 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_41})
    
    join_geometry_5 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_73, subdivision_surface, reroute_69]})
    
    realize_instances_6 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': join_geometry_5})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': realize_instances_6, 'Material': surface.shaderfunc_to_material(shader_bands)})
    
    reroute_80 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_3, reroute_80]})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_4})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_53})
    
    reroute_124 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Square Lid"]})
    
    reroute_123 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_124})
    
    multiply_12 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Lid Resolution"], 1: 2.0000},
        attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Y Resolution"], 1: 1.0000},
        attrs={'operation': 'SUBTRACT'})
    
    reroute_119 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Lid Side Bands"]})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': reroute_10})
    
    multiply_13 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"]}, attrs={'operation': 'MULTIPLY'})
    
    cylinder_1 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': multiply_12, 'Side Segments': subtract, 'Fill Segments': reroute_119, 'Radius': multiply_13, 'Depth': separate_xyz.outputs["Y"]},
        attrs={'fill_type': 'TRIANGLE_FAN'})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder_1.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    position_8 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_9 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_8})
    
    greater_than_5 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_9.outputs["Y"]})
    
    reroute_207 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Lid Slope"]})
    
    add_5 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_207, 1: 3.0000})
    
    absolute_2 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_9.outputs["Z"]}, attrs={'operation': 'ABSOLUTE'})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': absolute_2, 2: 1.0000, 3: reroute_207, 4: 0.0000})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_1.outputs["Result"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.1227, 0.2062), (0.5136, 0.5062), (0.9500, 0.6688)])
    
    multiply_14 = nw.new_node(Nodes.Math, input_kwargs={0: add_5, 1: float_curve}, attrs={'operation': 'MULTIPLY'})
    
    add_6 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_9.outputs["Y"], 1: multiply_14})
    
    combine_xyz_20 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_9.outputs["X"], 'Y': add_6, 'Z': separate_xyz_9.outputs["Z"]})
    
    set_position_13 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute_2, 'Selection': greater_than_5, 'Position': combine_xyz_20})
    
    reroute_192 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["X"]})
    
    reroute_193 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["Z"]})
    
    reroute_191 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["Y"]})
    
    combine_xyz_18 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_192, 'Y': reroute_193, 'Z': reroute_191})
    
    reroute_195 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["X Resolution"]})
    
    reroute_194 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Y Resolution"]})
    
    cube_4 = nw.new_node(Nodes.MeshCube,
        input_kwargs={'Size': combine_xyz_18, 'Vertices X': reroute_195, 'Vertices Y': 3, 'Vertices Z': reroute_194})
    
    store_named_attribute_3 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_4.outputs["Mesh"], 'Name': 'uv_map', 3: cube_4.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    switch_5 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_123, 14: set_position_13, 15: store_named_attribute_3})
    
    divide_3 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_122 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide_3})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_122})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': group_input_1.outputs["Lid Height"], 'Z': 1.0000})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': switch_5.outputs[6], 'Translation': combine_xyz, 'Rotation': (1.5708, 0.0000, 0.0000), 'Scale': combine_xyz_9})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': transform, 'Distance': 0.0500})
    
    reroute_282 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': merge_by_distance})
    
    position_16 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_17 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_16})
    
    multiply_15 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Height"], 1: 0.5010},
        attrs={'operation': 'MULTIPLY'})
    
    less_equal_2 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_17.outputs["Z"], 1: multiply_15},
        attrs={'operation': 'LESS_EQUAL'})
    
    delete_geometry_1 = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': reroute_282, 'Selection': less_equal_2},
        attrs={'domain': 'FACE'})
    
    reroute_205 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': delete_geometry_1})
    
    position_17 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_18 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_17})
    
    multiply_16 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Height"], 1: 0.5100},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_6 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_18.outputs["Z"], 1: multiply_16})
    
    multiply_17 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Lid Height"], 1: 6.9000},
        attrs={'operation': 'MULTIPLY'})
    
    map_range_5 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_18.outputs["Z"], 2: multiply_17, 3: group_input_1.outputs["Lid Size"]})
    
    float_curve_3 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_5.outputs["Result"]})
    node_utils.assign_curve(float_curve_3.mapping.curves[0], [(0.0227, 0.0375), (0.4955, 0.5000), (0.9909, 1.0000)])
    
    reroute_299 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': float_curve_3})
    
    multiply_18 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_299, 1: separate_xyz_18.outputs["X"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_19 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_18.outputs["Y"], 1: reroute_299},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_45 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_18, 'Y': multiply_19, 'Z': separate_xyz_18.outputs["Z"]})
    
    set_position_19 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': reroute_205, 'Selection': greater_than_6, 'Position': combine_xyz_45})
    
    reroute_75 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_19})
    
    reroute_116 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_75})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': reroute_116})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mesh_to_curve})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_34})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_36})
    
    reroute_101 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_43})
    
    reroute_104 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_101})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_104})
    
    curve_to_points_1 = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': reroute_44, 'Count': group_input_1.outputs["Stud Amount"]})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_points_1.outputs["Points"]})
    
    reroute_94 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_45})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    reroute_106 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_2.outputs["X"]})
    
    absolute_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_106}, attrs={'operation': 'ABSOLUTE'})
    
    divide_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Depth"], 1: 5.0000},
        attrs={'operation': 'DIVIDE'})
    
    greater_than_7 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute_3, 1: divide_4})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Stud Resolution"]})
    
    add_7 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_54, 1: 2.0000})
    
    reroute_100 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_7})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_54})
    
    reroute_103 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Stud Size"]})
    
    reroute_102 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_103})
    
    reroute_105 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    multiply_20 = nw.new_node(Nodes.Math, input_kwargs={0: 0.1000, 1: reroute_105}, attrs={'operation': 'MULTIPLY'})
    
    multiply_21 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_102, 1: multiply_20}, attrs={'operation': 'MULTIPLY'})
    
    uv_sphere_1 = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Segments': reroute_100, 'Rings': reroute_42, 'Radius': multiply_21})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere_1.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_96 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': store_named_attribute})
    
    reroute_99 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Studs"]})
    
    reroute_93 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_99})
    
    op_not_1 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: reroute_93}, attrs={'operation': 'NOT'})
    
    reroute_95 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': op_not_1})
    
    add_8 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_1.outputs["Stud Spikiness"], 1: 1.0000})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_8})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    reroute_133 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_50})
    
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_133, 'Y': 1.0000, 'Z': 1.0000})
    
    f_r_o_n_t_b_a_c_k = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_94, 'Selection': greater_than_7, 'Instance': reroute_96, 'Pick Instance': reroute_95, 'Scale': combine_xyz_10},
        label='FRONT/BACK')
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_4 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    reroute_107 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_4.outputs["X"]})
    
    greater_than_8 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_107})
    
    reroute_232 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    multiply_22 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_232, 1: 0.1400}, attrs={'operation': 'MULTIPLY'})
    
    reroute_238 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_22})
    
    combine_xyz_40 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_238})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': f_r_o_n_t_b_a_c_k, 'Selection': greater_than_8, 'Offset': combine_xyz_40})
    
    reroute_108 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_107})
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_108}, attrs={'operation': 'LESS_THAN'})
    
    multiply_23 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_232, 1: -0.1400}, attrs={'operation': 'MULTIPLY'})
    
    reroute_233 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_23})
    
    combine_xyz_37 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_233})
    
    set_position_5 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_4, 'Selection': less_than, 'Offset': combine_xyz_37})
    
    reroute_74 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_94})
    
    absolute_4 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Y"]}, attrs={'operation': 'ABSOLUTE'})
    
    multiply_24 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Width"], 1: 0.4000},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_9 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute_4, 1: multiply_24})
    
    reroute_97 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_96})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_95})
    
    combine_xyz_11 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': reroute_50, 'Z': 1.0000})
    
    s_i_d_e_s = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_74, 'Selection': greater_than_9, 'Instance': reroute_97, 'Pick Instance': reroute_47, 'Scale': combine_xyz_11},
        label='SIDES')
    
    reroute_109 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_4.outputs["Y"]})
    
    greater_than_10 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_109})
    
    reroute_239 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_238})
    
    combine_xyz_41 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute_239})
    
    set_position_6 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': s_i_d_e_s, 'Selection': greater_than_10, 'Offset': combine_xyz_41})
    
    less_than_1 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_109}, attrs={'operation': 'LESS_THAN'})
    
    reroute_237 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_233})
    
    combine_xyz_38 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute_237})
    
    set_position_7 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_6, 'Selection': less_than_1, 'Offset': combine_xyz_38})
    
    reroute_79 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_74})
    
    reroute_110 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_2.outputs["Z"]})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_110})
    
    reroute_135 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Chest Height"]})
    
    multiply_25 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_135}, attrs={'operation': 'MULTIPLY'})
    
    reroute_134 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Lid Height"]})
    
    add_9 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_25, 1: reroute_134})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: add_9, 1: 0.4000}, attrs={'operation': 'SUBTRACT'})
    
    greater_than_11 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_20, 1: subtract_1})
    
    reroute_98 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_97})
    
    reroute_64 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_47})
    
    combine_xyz_12 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 1.0000, 'Z': reroute_29})
    
    t_o_p = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_79, 'Selection': greater_than_11, 'Instance': reroute_98, 'Pick Instance': reroute_64, 'Scale': combine_xyz_12},
        label='TOP')
    
    reroute_241 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_239})
    
    combine_xyz_39 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_241})
    
    set_position_8 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': t_o_p, 'Offset': combine_xyz_39})
    
    join_geometry_10 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_5, set_position_7, set_position_8]})
    
    set_shade_smooth_2 = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': join_geometry_10, 'Shade Smooth': group_input_1.outputs["Smooth Studs"]})
    
    reroute_78 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_shade_smooth_2})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_78})
    
    divide_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Band Size"], 1: 5.0000},
        attrs={'operation': 'DIVIDE'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_1.outputs["Band Resolution"], 'Radius': divide_5})
    
    geometry_to_instance_2 = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': curve_circle.outputs["Curve"]})
    
    rotate_instances_3 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': geometry_to_instance_2, 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    realize_instances_4 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': rotate_instances_3})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': reroute_34, 'Profile Curve': realize_instances_4})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh, 'Shade Smooth': False})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_shade_smooth})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': reroute_51, 'Level': group_input_1.outputs["Band Subdivisions"], 'Edge Crease': group_input_1.outputs["Band Edge Crease"], 'Vertex Crease': group_input_1.outputs["Band Vert Crease"]})
    
    reroute_72 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subdivision_surface_1})
    
    reroute_202 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_75})
    
    mesh_to_points_1 = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': reroute_202}, attrs={'mode': 'CORNERS'})
    
    divide_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Corner Size"], 1: 3.5000},
        attrs={'operation': 'DIVIDE'})
    
    divide_7 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Band Size"], 1: 5.0000},
        attrs={'operation': 'DIVIDE'})
    
    add_10 = nw.new_node(Nodes.Math, input_kwargs={0: divide_6, 1: divide_7})
    
    add_11 = nw.new_node(Nodes.Math, input_kwargs={0: add_10, 1: 0.0390})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_11, 'Y': add_11, 'Z': add_11})
    
    cube_3 = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz_1})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_3.outputs["Mesh"], 'Name': 'uv_map', 3: cube_3.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_to_points_1, 'Instance': store_named_attribute_1})
    
    reroute_136 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_2})
    
    reroute_137 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_136})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': instance_on_points_2, 'Offset Scale': 0.0100})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Selection': extrude_mesh_1.outputs["Top"], 'Scale': 0.5000})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_136, scale_elements_1]})
    
    switch_2 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_1.outputs["Pillowed Corners"], 14: reroute_137, 15: join_geometry_2})
    
    subdivision_surface_2 = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': switch_2.outputs[6], 'Level': group_input_1.outputs["Corner Subdivisions"], 'Edge Crease': group_input_1.outputs["Corner Edge Crease"], 'Vertex Crease': group_input_1.outputs["Corner Vertex Crease"]})
    
    scale_elements_2 = nw.new_node(Nodes.ScaleElements, input_kwargs={'Geometry': subdivision_surface_2, 'Scale': 1.0010})
    
    reroute_77 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_elements_2})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_77})
    
    reroute_277 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_276 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_277})
    
    join_geometry_6 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_37, reroute_72, reroute_276]})
    
    realize_instances_8 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': join_geometry_6})
    
    merge_by_distance_3 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': realize_instances_8})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': merge_by_distance_3, 'Material': surface.shaderfunc_to_material(shader_bands)})
    
    reroute_177 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_1})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_116})
    
    reroute_143 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_143, 'Material': surface.shaderfunc_to_material(shader_chest_base)})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_2})
    
    greater_than_12 = nw.new_node(Nodes.Compare,
        input_kwargs={2: group_input_1.outputs["Lid Resolution"], 3: 5},
        attrs={'data_type': 'INT'})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_205})
    
    reroute_223 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_218 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_223})
    
    reroute_217 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Clasps Per Edge"]})
    
    reroute_222 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_217})
    
    subdivide_mesh_4 = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': reroute_218, 'Level': reroute_222})
    
    position_11 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_12 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_11})
    
    multiply_26 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Depth"], 1: -0.4950},
        attrs={'operation': 'MULTIPLY'})
    
    less_than_2 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_12.outputs["X"], 1: multiply_26},
        attrs={'operation': 'LESS_THAN'})
    
    multiply_27 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Height"], 1: 0.6000},
        attrs={'operation': 'MULTIPLY'})
    
    add_12 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_27, 1: 0.0100})
    
    less_than_3 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_12.outputs["Z"], 1: add_12},
        attrs={'operation': 'LESS_THAN'})
    
    op_and = nw.new_node(Nodes.BooleanMath, input_kwargs={0: less_than_2, 1: less_than_3})
    
    mesh_to_points_6 = nw.new_node(Nodes.MeshToPoints,
        input_kwargs={'Mesh': subdivide_mesh_4, 'Selection': op_and},
        attrs={'mode': 'EDGES'})
    
    reroute_219 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    reroute_216 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_219})
    
    multiply_28 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_216, 1: -0.1500}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_25 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_28})
    
    set_position_16 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points_6, 'Offset': combine_xyz_25})
    
    combine_xyz_43 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_28, 'Z': -0.0250})
    
    set_position_23 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points_6, 'Offset': combine_xyz_43})
    
    switch_14 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than_12, 14: set_position_16, 15: set_position_23})
    
    index_2 = nw.new_node(Nodes.Index)
    
    modulo = nw.new_node(Nodes.Math,
        input_kwargs={0: index_2, 1: group_input_1.outputs["Clasp Number"]},
        attrs={'operation': 'MODULO'})
    
    op_not_2 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: modulo}, attrs={'operation': 'NOT'})
    
    object_info_9 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Clasp Flap']})
    
    op_not_3 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: group_input_1.outputs["Clasps"]}, attrs={'operation': 'NOT'})
    
    instance_on_points_16 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': switch_14.outputs[6], 'Selection': op_not_2, 'Instance': object_info_9.outputs["Geometry"], 'Pick Instance': op_not_3, 'Scale': (1.0000, 1.0000, 0.9000)})
    
    reroute_220 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_216})
    
    combine_xyz_26 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_220, 'Y': reroute_220, 'Z': reroute_220})
    
    reroute_221 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_26})
    
    scale_instances_4 = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': instance_on_points_16, 'Scale': reroute_221})
    
    reroute_227 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Clasp Rotation"]})
    
    reroute_226 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_227})
    
    combine_xyz_27 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute_226})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': scale_instances_4, 'Rotation': combine_xyz_27, 'Pivot Point': (-0.0360, 0.0000, 0.0000)})
    
    reroute_257 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': rotate_instances})
    
    greater_than_13 = nw.new_node(Nodes.Compare,
        input_kwargs={2: group_input_1.outputs["Lid Resolution"], 3: 5},
        attrs={'data_type': 'INT'})
    
    reroute_212 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_214 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Clasps Per Edge"]})
    
    reroute_211 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_214})
    
    subdivide_mesh_2 = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': reroute_212, 'Level': reroute_211})
    
    position_9 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_10 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_9})
    
    multiply_29 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Depth"], 1: -0.4900},
        attrs={'operation': 'MULTIPLY'})
    
    less_than_4 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_10.outputs["X"], 1: multiply_29},
        attrs={'operation': 'LESS_THAN'})
    
    multiply_30 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Height"], 1: 0.6000},
        attrs={'operation': 'MULTIPLY'})
    
    less_than_5 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_10.outputs["Z"], 1: multiply_30},
        attrs={'operation': 'LESS_THAN'})
    
    op_and_1 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: less_than_4, 1: less_than_5})
    
    mesh_to_points_4 = nw.new_node(Nodes.MeshToPoints,
        input_kwargs={'Mesh': subdivide_mesh_2, 'Selection': op_and_1},
        attrs={'mode': 'EDGES'})
    
    reroute_215 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_215})
    
    multiply_31 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_49, 1: -0.1500}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_22 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_31})
    
    set_position_14 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points_4, 'Offset': combine_xyz_22})
    
    combine_xyz_44 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_31, 'Z': -0.0250})
    
    set_position_24 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points_4, 'Offset': combine_xyz_44})
    
    switch_15 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than_13, 14: set_position_14, 15: set_position_24})
    
    index_3 = nw.new_node(Nodes.Index)
    
    modulo_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: index_3, 1: group_input_1.outputs["Clasp Number"]},
        attrs={'operation': 'MODULO'})
    
    op_not_4 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: modulo_1}, attrs={'operation': 'NOT'})
    
    object_info_7 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Lid Clasp']})
    
    op_not_5 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: group_input_1.outputs["Clasps"]}, attrs={'operation': 'NOT'})
    
    instance_on_points_14 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': switch_15.outputs[6], 'Selection': op_not_4, 'Instance': object_info_7.outputs["Geometry"], 'Pick Instance': op_not_5, 'Scale': (1.0000, 1.0000, 0.9000)})
    
    reroute_92 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_49})
    
    combine_xyz_21 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_92, 'Y': reroute_92, 'Z': reroute_92})
    
    reroute_213 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_21})
    
    scale_instances_2 = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': instance_on_points_14, 'Scale': reroute_213})
    
    reroute_173 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_instances_2})
    
    reroute_258 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_173})
    
    reroute_56 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_205})
    
    reroute_203 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_56})
    
    reroute_144 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_203})
    
    reroute_172 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_144})
    
    reroute_141 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_172})
    
    reroute_139 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Hinge Amount"]})
    
    reroute_140 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_139})
    
    subdivide_mesh_1 = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': reroute_141, 'Level': reroute_140})
    
    position_4 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_7 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_4})
    
    multiply_32 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Depth"], 1: 0.4900},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_14 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_7.outputs["X"], 1: multiply_32})
    
    multiply_33 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_1.outputs["Chest Height"]}, attrs={'operation': 'MULTIPLY'})
    
    add_13 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_33, 1: 0.0100})
    
    less_than_6 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_7.outputs["Z"], 1: add_13},
        attrs={'operation': 'LESS_THAN'})
    
    op_and_2 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: greater_than_14, 1: less_than_6})
    
    mesh_to_points_3 = nw.new_node(Nodes.MeshToPoints,
        input_kwargs={'Mesh': subdivide_mesh_1, 'Selection': op_and_2},
        attrs={'mode': 'EDGES'})
    
    reroute_59 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    divide_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_59, 1: 7.3000}, attrs={'operation': 'DIVIDE'})
    
    multiply_34 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_59, 1: 0.0075}, attrs={'operation': 'MULTIPLY'})
    
    multiply_35 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_34, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_15 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide_8, 'Z': multiply_35})
    
    set_position_10 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points_3, 'Offset': combine_xyz_15})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Hinge']})
    
    op_not_6 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: group_input_1.outputs["Hinges"]}, attrs={'operation': 'NOT'})
    
    instance_on_points_5 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_10, 'Instance': object_info_1.outputs["Geometry"], 'Pick Instance': op_not_6, 'Rotation': (3.1416, 4.7124, 0.0000), 'Scale': (1.0000, 1.5000, 1.5000)})
    
    reroute_57 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_59})
    
    combine_xyz_13 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_57, 'Y': reroute_57, 'Z': reroute_57})
    
    reroute_138 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_13})
    
    scale_instances = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': instance_on_points_5, 'Scale': reroute_138})
    
    reroute_259 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_instances})
    
    join_geometry_13 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_257, reroute_258, reroute_259]})
    
    set_material_6 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_13, 'Material': surface.shaderfunc_to_material(shader_fittings)})
    
    reroute_225 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_6})
    
    reroute_224 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_225})
    
    join_geometry_7 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_177, reroute_25, reroute_224]})
    
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': join_geometry_7})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Lid Rotation"]})
    
    reroute_131 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_40})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute_131})
    
    multiply_36 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_1.outputs["Chest Depth"]}, attrs={'operation': 'MULTIPLY'})
    
    reroute_61 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    divide_9 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_61, 1: 6.6500}, attrs={'operation': 'DIVIDE'})
    
    add_14 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_36, 1: divide_9})
    
    divide_10 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Width"], 1: 0.0000},
        attrs={'operation': 'DIVIDE'})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Chest Height"]})
    
    divide_11 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_30, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_62 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_61})
    
    divide_12 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_62, 1: 7.9000}, attrs={'operation': 'DIVIDE'})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: divide_11, 1: divide_12}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_14, 'Y': divide_10, 'Z': subtract_2})
    
    rotate_instances_1 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': geometry_to_instance, 'Rotation': combine_xyz_5, 'Pivot Point': combine_xyz_2})
    
    reroute_132 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_62})
    
    divide_13 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_132, 1: 3.5000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide_13})
    
    transform_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': rotate_instances_1, 'Translation': combine_xyz_6})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_3})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_130 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    reroute_210 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Clasps Per Edge"]})
    
    subdivide_mesh_3 = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': reroute_130, 'Level': reroute_210})
    
    position_10 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_11 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_10})
    
    multiply_37 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Depth"], 1: -0.4900},
        attrs={'operation': 'MULTIPLY'})
    
    less_than_7 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_11.outputs["X"], 1: multiply_37},
        attrs={'operation': 'LESS_THAN'})
    
    multiply_38 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Height"], 1: 0.4950},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_15 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_11.outputs["Z"], 1: multiply_38})
    
    op_and_3 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: less_than_7, 1: greater_than_15})
    
    mesh_to_points_5 = nw.new_node(Nodes.MeshToPoints,
        input_kwargs={'Mesh': subdivide_mesh_3, 'Selection': op_and_3},
        attrs={'mode': 'EDGES'})
    
    reroute_199 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    multiply_39 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_199, 1: -0.1500}, attrs={'operation': 'MULTIPLY'})
    
    add_15 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_39, 1: 0.0020})
    
    combine_xyz_23 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_15})
    
    set_position_15 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points_5, 'Offset': combine_xyz_23})
    
    index = nw.new_node(Nodes.Index)
    
    reroute_285 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Clasp Number"]})
    
    modulo_2 = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: reroute_285}, attrs={'operation': 'MODULO'})
    
    op_not_7 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: modulo_2}, attrs={'operation': 'NOT'})
    
    object_info_8 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Chest Clasp']})
    
    op_not_8 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: group_input_1.outputs["Clasps"]}, attrs={'operation': 'NOT'})
    
    instance_on_points_15 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_15, 'Selection': op_not_7, 'Instance': object_info_8.outputs["Geometry"], 'Pick Instance': op_not_8})
    
    reroute_198 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_199})
    
    combine_xyz_24 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_198, 'Y': reroute_198, 'Z': reroute_198})
    
    scale_instances_3 = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': instance_on_points_15, 'Scale': combine_xyz_24})
    
    reroute_208 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_instances_3})
    
    reroute_200 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_208})
    
    reroute_256 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_200})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_130})
    
    reroute_254 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_230 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Clasps Per Edge"]})
    
    subdivide_mesh_5 = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': reroute_254, 'Level': reroute_230})
    
    position_12 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_13 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_12})
    
    multiply_40 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Depth"], 1: -0.4900},
        attrs={'operation': 'MULTIPLY'})
    
    less_than_8 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_13.outputs["X"], 1: multiply_40},
        attrs={'operation': 'LESS_THAN'})
    
    multiply_41 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Height"], 1: 0.4950},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_16 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_13.outputs["Z"], 1: multiply_41})
    
    op_and_4 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: less_than_8, 1: greater_than_16})
    
    mesh_to_points_7 = nw.new_node(Nodes.MeshToPoints,
        input_kwargs={'Mesh': subdivide_mesh_5, 'Selection': op_and_4},
        attrs={'mode': 'EDGES'})
    
    reroute_229 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    multiply_42 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_229, 1: -0.2000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_229})
    
    reroute_244 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Lock Size"]})
    
    divide_14 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_244, 1: -2.7500}, attrs={'operation': 'DIVIDE'})
    
    multiply_43 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_15, 1: divide_14}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_29 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_42, 'Z': multiply_43})
    
    set_position_17 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points_7, 'Offset': combine_xyz_29})
    
    index_1 = nw.new_node(Nodes.Index)
    
    modulo_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: index_1, 1: group_input_1.outputs["Clasp Number"]},
        attrs={'operation': 'MODULO'})
    
    op_not_9 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: modulo_3}, attrs={'operation': 'NOT'})
    
    object_info_10 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Lock']})
    
    op_not_10 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: group_input_1.outputs["Locks"]}, attrs={'operation': 'NOT'})
    
    random_value_10 = nw.new_node(Nodes.RandomValue, input_kwargs={2: -0.1000, 3: 0.1000, 'Seed': group_input_1.outputs["Seed"]})
    
    random_value_11 = nw.new_node(Nodes.RandomValue, input_kwargs={2: -0.2000, 3: 0.2000, 'Seed': group_input_1.outputs["Seed"]})
    
    combine_xyz_30 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': random_value_10.outputs[1], 'Z': random_value_11.outputs[1]})
    
    reroute_286 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_244})
    
    combine_xyz_46 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_286, 'Y': reroute_286, 'Z': reroute_286})
    
    instance_on_points_17 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_17, 'Selection': op_not_9, 'Instance': object_info_10.outputs["Geometry"], 'Pick Instance': op_not_10, 'Rotation': combine_xyz_30, 'Scale': combine_xyz_46})
    
    reroute_228 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    combine_xyz_28 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_228, 'Y': reroute_228, 'Z': reroute_228})
    
    scale_instances_5 = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': instance_on_points_17, 'Scale': combine_xyz_28})
    
    rotate_instances_4 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': scale_instances_5, 'Rotation': (0.0000, 0.4677, 0.0000), 'Pivot Point': (0.0000, 0.0000, 0.3750)})
    
    switch_6 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_1.outputs["Clasps"], 15: rotate_instances_4})
    
    reroute_234 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_6.outputs[6]})
    
    reroute_283 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_234})
    
    reroute_255 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_283})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_254})
    
    subdivide_mesh = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': reroute_52, 'Level': group_input_1.outputs["Hinge Amount"]})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_5 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_3})
    
    multiply_44 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Depth"], 1: 0.4950},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_17 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_5.outputs["X"], 1: multiply_44})
    
    multiply_45 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Height"], 1: 0.4950},
        attrs={'operation': 'MULTIPLY', 'use_clamp': True})
    
    greater_than_18 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_5.outputs["Z"], 1: multiply_45})
    
    op_and_5 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: greater_than_17, 1: greater_than_18})
    
    mesh_to_points_2 = nw.new_node(Nodes.MeshToPoints,
        input_kwargs={'Mesh': subdivide_mesh, 'Selection': op_and_5},
        attrs={'mode': 'EDGES'})
    
    reroute_60 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Band Size"]})
    
    divide_15 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_60, 1: 7.3000}, attrs={'operation': 'DIVIDE'})
    
    divide_16 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_60, 1: 25.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_16 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide_15, 'Z': divide_16})
    
    set_position_9 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points_2, 'Offset': combine_xyz_16})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Hinge']})
    
    op_not_11 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: group_input_1.outputs["Hinges"]}, attrs={'operation': 'NOT'})
    
    instance_on_points_4 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_9, 'Instance': object_info.outputs["Geometry"], 'Pick Instance': op_not_11, 'Rotation': (0.0000, 1.5708, 0.0000), 'Scale': (1.0000, 1.5000, 1.5000)})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_60})
    
    combine_xyz_14 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_58, 'Y': reroute_58, 'Z': reroute_58})
    
    scale_instances_1 = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': instance_on_points_4, 'Scale': combine_xyz_14})
    
    reroute_179 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_instances_1})
    
    reroute_235 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_179})
    
    join_geometry_12 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_256, reroute_255, reroute_235]})
    
    set_material_5 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_12, 'Material': surface.shaderfunc_to_material(shader_fittings)})
    
    reroute_264 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["X Resolution"]})
    
    greater_than_19 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_264, 3: 2}, attrs={'data_type': 'INT'})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Z Resolution"]})
    
    greater_than_20 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_24, 3: 2}, attrs={'data_type': 'INT'})
    
    reroute_176 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_272 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_176})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_272})
    
    reroute_89 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    reroute_242 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_89})
    
    reroute_209 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_242})
    
    reroute_263 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_209})
    
    position_13 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_14 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_13})
    
    absolute_5 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_14.outputs["Y"]}, attrs={'operation': 'ABSOLUTE'})
    
    multiply_46 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Width"], 1: 0.4900},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_21 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute_5, 1: multiply_46})
    
    mesh_to_points_8 = nw.new_node(Nodes.MeshToPoints,
        input_kwargs={'Mesh': reroute_263, 'Selection': greater_than_21},
        attrs={'mode': 'FACES'})
    
    map_range_3 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': group_input_1.outputs["Z Resolution"], 1: 3.0000, 2: 7.0000, 4: 0.4000})
    
    multiply_47 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Height"], 1: map_range_3.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_22 = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_14.outputs["Z"], 1: multiply_47})
    
    op_and_6 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: greater_than_21, 1: greater_than_22})
    
    mesh_to_points_13 = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': reroute_209, 'Selection': op_and_6}, attrs={'mode': 'FACES'})
    
    switch_13 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than_20, 14: mesh_to_points_8, 15: mesh_to_points_13})
    
    multiply_48 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Width"], 1: 0.4000},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_23 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute_5, 1: multiply_48})
    
    reroute_281 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_14.outputs["Z"]})
    
    multiply_49 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Height"], 1: 0.4900},
        attrs={'operation': 'MULTIPLY'})
    
    greater_than_24 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_281, 1: multiply_49})
    
    op_and_7 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: greater_than_23, 1: greater_than_24})
    
    reroute_246 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_14.outputs["X"]})
    
    reroute_250 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_246})
    
    reroute_251 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_250})
    
    reroute_245 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Chest Depth"]})
    
    reroute_288 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_245})
    
    multiply_50 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_288, 1: -0.4900}, attrs={'operation': 'MULTIPLY'})
    
    greater_than_25 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_251, 1: multiply_50})
    
    multiply_51 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_245, 1: 0.4900}, attrs={'operation': 'MULTIPLY'})
    
    less_than_9 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_250, 1: multiply_51}, attrs={'operation': 'LESS_THAN'})
    
    op_and_8 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: greater_than_25, 1: less_than_9})
    
    op_and_9 = nw.new_node(Nodes.BooleanMath, input_kwargs={0: op_and_7, 1: op_and_8})
    
    mesh_to_points_9 = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': reroute_242, 'Selection': op_and_9})
    
    switch_7 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than_19, 14: switch_13.outputs[6], 15: mesh_to_points_9})
    
    add_16 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_1.outputs["Stud Amount"], 1: 4.0000})
    
    add_17 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_1.outputs["Stud Resolution"], 1: 2.0000})
    
    handlegen = nw.new_node(nodegroup_handle_gen().name,
        input_kwargs={'Width': group_input_1.outputs["Handle Width"], 'Height': group_input_1.outputs["Handle Length"], 'Thickness': group_input_1.outputs["Handle Thickness"], 'Fitting Resolution': group_input_1.outputs["Handle Fitting Resolution"], 'Fitting Size': group_input_1.outputs["Handle Fitting Size"], 'Handle Resolution': group_input_1.outputs["Handle Resolution"], 'Studs': group_input_1.outputs["Studs"], 'Stud Amount': add_16, 'Stud Resolution': add_17, 'Smooth Studs': group_input_1.outputs["Smooth Studs"]})
    
    instance_on_points_19 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': switch_7.outputs[6], 'Instance': handlegen, 'Scale': (0.2500, 0.2500, 0.2500)})
    
    reroute_279 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_14.outputs["Y"]})
    
    reroute_280 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_279})
    
    reroute_252 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_280})
    
    greater_than_26 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_252})
    
    combine_xyz_48 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input_1.outputs["Handle Rotation"]})
    
    multiply_52 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Handle Length"], 1: 0.7000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_52 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_52})
    
    rotate_instances_6 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': instance_on_points_19, 'Selection': greater_than_26, 'Rotation': combine_xyz_48, 'Pivot Point': combine_xyz_52})
    
    reroute_278 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_252})
    
    less_than_10 = nw.new_node(Nodes.Compare, input_kwargs={0: reroute_278}, attrs={'operation': 'LESS_THAN'})
    
    multiply_53 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Handle Rotation"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_47 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_53})
    
    rotate_instances_7 = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': rotate_instances_6, 'Selection': less_than_10, 'Rotation': combine_xyz_47, 'Pivot Point': combine_xyz_52})
    
    multiply_54 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Handle Length"], 1: -0.1780},
        attrs={'operation': 'MULTIPLY'})
    
    add_18 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_54, 1: group_input_1.outputs["Handle Height"]})
    
    combine_xyz_31 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_18})
    
    set_position_18 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': rotate_instances_7, 'Offset': combine_xyz_31})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': set_position_18, 'Selection': less_than_10},
        attrs={'domain': 'INSTANCE'})
    
    map_range_2 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': group_input_1.outputs["Chest Base Size"], 3: 1.0000, 4: 0.0000})
    
    multiply_55 = nw.new_node(Nodes.Math, input_kwargs={0: map_range_2.outputs["Result"]}, attrs={'operation': 'MULTIPLY'})
    
    add_19 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_55, 1: -0.0500})
    
    combine_xyz_32 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': add_19})
    
    set_position_20 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': separate_geometry.outputs["Selection"], 'Offset': combine_xyz_32})
    
    multiply_56 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_55, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    add_20 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_56, 1: 0.0500})
    
    combine_xyz_49 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': add_20})
    
    set_position_21 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': separate_geometry.outputs["Inverted"], 'Offset': combine_xyz_49})
    
    join_geometry_11 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_20, set_position_21]})
    
    switch_9 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_1.outputs["Handles"], 15: join_geometry_11})
    
    set_material_7 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': switch_9.outputs[6], 'Material': surface.shaderfunc_to_material(shader_handles)})
    
    join_geometry_14 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_5, set_material_7]})
    
    reroute_261 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_14})
    
    reroute_206 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_261})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_206})
    
    reroute_180 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Treasure"]})
    
    reroute_182 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_180})
    
    multiply_57 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Depth"], 1: 1.1000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_58 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Chest Width"], 1: 1.1000},
        attrs={'operation': 'MULTIPLY'})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': multiply_57, 'Size Y': multiply_58, 'Vertices X': 6, 'Vertices Y': 12})
    
    store_named_attribute_4 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Chest Height"]})
    
    multiply_59 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_14, 1: 0.5000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Seed"]})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={'Seed': reroute_2})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': random_value.outputs[1], 'Scale': 0.9000, 'Detail': 1.2000, 'Roughness': 0.4083},
        attrs={'noise_dimensions': '4D'})
    
    multiply_60 = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Color"], 1: 1.1000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_61 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_59, 1: multiply_60}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_19 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_61})
    
    set_position_12 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': store_named_attribute_4, 'Offset': combine_xyz_19})
    
    reroute_71 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': store_named_attribute_7})
    
    reroute_81 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_71})
    
    scale_elements_5 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': reroute_81, 'Scale': 1.2000},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_8 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements_5, 'Scale': 1.2000, 'Axis': (0.0000, 1.0000, 0.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_9 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements_8, 'Scale': 0.9000, 'Axis': (0.0000, 0.0000, 1.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    position_14 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_15 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_14})
    
    reroute_265 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_15.outputs["X"]})
    
    reroute_273 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_270})
    
    multiply_62 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_273}, attrs={'operation': 'MULTIPLY'})
    
    reroute_274 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_271})
    
    reroute_268 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_274})
    
    map_range_4 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz_15.outputs["Z"], 2: multiply_62, 3: reroute_268})
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_4.outputs["Result"]})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.0000, 0.0000), (0.5673, 0.4125), (1.0000, 1.0000)])
    
    reroute_267 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': float_curve_2})
    
    multiply_63 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_265, 1: reroute_267}, attrs={'operation': 'MULTIPLY'})
    
    reroute_266 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_15.outputs["Y"]})
    
    multiply_64 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_267, 1: reroute_266}, attrs={'operation': 'MULTIPLY'})
    
    reroute_269 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_15.outputs["Z"]})
    
    reroute_240 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_269})
    
    reroute_284 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_240})
    
    combine_xyz_42 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_63, 'Y': multiply_64, 'Z': reroute_284})
    
    set_position_22 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_81, 'Position': combine_xyz_42})
    
    scale_elements_6 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': set_position_22, 'Scale': 0.9950},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_7 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements_6, 'Scale': 0.9950, 'Axis': (0.0000, 1.0000, 0.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    difference = nw.new_node(Nodes.MeshBoolean,
        input_kwargs={'Mesh 1': scale_elements_9, 'Mesh 2': scale_elements_7, 'Self Intersection': True})
    
    difference_1 = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': set_position_12, 'Mesh 2': difference.outputs["Mesh"]})
    
    reroute_275 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': difference_1.outputs["Mesh"]})
    
    set_shade_smooth_4 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': reroute_275})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth_4, 'Material': surface.shaderfunc_to_material(shader_treasure_base)})
    
    reroute_260 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_4})
    
    scale_elements_3 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': reroute_275, 'Scale': 0.9000},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_4 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements_3, 'Scale': 0.9000, 'Axis': (0.0000, 1.0000, 0.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    reroute_125 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_elements_4})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Treasure Amount"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    multiply_65 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_16, 1: 10.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_65})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_125, 'Density Max': reroute_19, 'Density': 87.5000, 'Seed': reroute_1},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info_2 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['GoldCoin']})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={'Seed': reroute_1}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': random_value_1.outputs["Value"]})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    instance_on_points_9 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': object_info_2.outputs["Geometry"], 'Rotation': reroute_22, 'Scale': (0.5000, 0.5000, 0.5000)})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_260, instance_on_points_9]})
    
    reroute_184 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_3})
    
    reroute_183 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_184})
    
    reroute_186 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_183})
    
    reroute_145 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_125})
    
    reroute_164 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_1.outputs["Gem Amount"]})
    
    reroute_166 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_164})
    
    multiply_66 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_166, 1: 5.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_167 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_66})
    
    reroute_163 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_167})
    
    reroute_162 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_163})
    
    reroute_161 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_162})
    
    reroute_165 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_161})
    
    reroute_156 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_155 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_156})
    
    reroute_157 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_155})
    
    add_21 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_157, 1: 1.0000})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_145, 'Density Max': reroute_165, 'Seed': add_21},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info_3 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Diamond']})
    
    reroute_147 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': object_info_3.outputs["Geometry"]})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={1: (3.1400, 3.1400, 3.1400), 'Seed': 4},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_146 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': random_value_2.outputs["Value"]})
    
    random_value_3 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.6000, 0.6000, 0.6000), 'Seed': 6},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points_10 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Instance': reroute_147, 'Rotation': reroute_146, 'Scale': random_value_3.outputs["Value"]})
    
    reroute_187 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_10})
    
    reroute_185 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_187})
    
    reroute_148 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_145})
    
    reroute_168 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_165})
    
    reroute_158 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_157})
    
    add_22 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_158, 1: 2.0000})
    
    distribute_points_on_faces_2 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_148, 'Density Max': reroute_168, 'Seed': add_22},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info_4 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Emerald']})
    
    reroute_150 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': object_info_4.outputs["Geometry"]})
    
    random_value_4 = nw.new_node(Nodes.RandomValue,
        input_kwargs={1: (3.1400, 3.1400, 3.1400), 'Seed': 4},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_149 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': random_value_4.outputs["Value"]})
    
    random_value_5 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.6000, 0.6000, 0.6000), 'Seed': 6},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points_11 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_2.outputs["Points"], 'Instance': reroute_150, 'Rotation': reroute_149, 'Scale': random_value_5.outputs["Value"]})
    
    reroute_188 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_11})
    
    reroute_151 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_148})
    
    reroute_169 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_168})
    
    reroute_159 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_158})
    
    add_23 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_159, 1: 3.0000})
    
    distribute_points_on_faces_3 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_151, 'Density Max': reroute_169, 'Seed': add_23},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info_5 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Ruby']})
    
    random_value_6 = nw.new_node(Nodes.RandomValue,
        input_kwargs={1: (3.1400, 3.1400, 3.1400), 'Seed': 4},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_152 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': random_value_6.outputs["Value"]})
    
    random_value_7 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.6000, 0.6000, 0.6000), 'Seed': 6},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points_12 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_3.outputs["Points"], 'Instance': object_info_5.outputs["Geometry"], 'Rotation': reroute_152, 'Scale': random_value_7.outputs["Value"]})
    
    reroute_190 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_12})
    
    reroute_153 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_151})
    
    reroute_170 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_169})
    
    reroute_160 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_159})
    
    add_24 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_160, 1: 4.0000})
    
    distribute_points_on_faces_4 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_153, 'Density Max': reroute_170, 'Seed': add_24},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info_6 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Sapphire']})
    
    random_value_9 = nw.new_node(Nodes.RandomValue,
        input_kwargs={1: (3.1400, 3.1400, 3.1400), 'Seed': 4},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_154 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': random_value_9.outputs["Value"]})
    
    random_value_8 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.6000, 0.6000, 0.6000), 'Seed': 6},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points_13 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_4.outputs["Points"], 'Instance': object_info_6.outputs["Geometry"], 'Rotation': reroute_154, 'Scale': random_value_8.outputs["Value"]})
    
    reroute_189 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_13})
    
    join_geometry_8 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [reroute_186, reroute_185, reroute_188, reroute_190, reroute_189]})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_1.outputs["Gems"], 14: reroute_184, 15: join_geometry_8})
    
    reroute_181 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_1.outputs[6]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_182, 15: reroute_181})
    
    reroute_262 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch.outputs[6]})
    
    reroute_174 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_262})
    
    reroute_171 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_174})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_6, reroute_23, reroute_17, reroute_171]})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': join_geometry})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': realize_instances_1}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_chest_base, selection=selection)
apply(bpy.context.active_object)
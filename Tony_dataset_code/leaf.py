import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_leaf(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry_1 = nw.new_node(Nodes.NewGeometry)
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': geometry_1.outputs["Pointiness"]})
    colorramp_1.color_ramp.elements[0].position = 0.4318
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.4818
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 3.0000, 'Detail': 0.0000, 'Roughness': 0.5000, 'Distortion': 0.1000})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_1.outputs["Color"], 1: noise_texture.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    geometry = nw.new_node(Nodes.NewGeometry)
    
    rgb = nw.new_node(Nodes.RGB)
    rgb.outputs[0].default_value = (0.5000, 0.5000, 0.5000, 1.0000)
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': rgb, 'Specular': 0.3091, 'Roughness': 0.5136})
    
    rgb_1 = nw.new_node(Nodes.RGB)
    rgb_1.outputs[0].default_value = (0.1303, 0.1473, 0.0005, 1.0000)
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Hue': 0.4000, 'Saturation': 0.6000, 'Value': 1.3000, 'Color': rgb_1})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': hue_saturation_value, 'Specular': 0.4864, 'Roughness': 0.7864})
    
    mix_shader = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': geometry.outputs["Backfacing"], 1: principled_bsdf, 2: principled_bsdf_1})
    
    principled_bsdf_2 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.2513, 0.1119, 0.0402, 1.0000), 'Roughness': 0.4682})
    
    mix_shader_1 = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': multiply, 1: mix_shader, 2: principled_bsdf_2})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': rgb})
    colorramp.color_ramp.elements[0].position = 0.0227
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.7273
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={6: (0.0537, 0.1032, 0.0020, 1.0000), 7: colorramp.outputs["Color"]},
        attrs={'blend_type': 'SOFT_LIGHT', 'data_type': 'RGBA'})
    
    translucent_bsdf = nw.new_node(Nodes.TranslucentBSDF, input_kwargs={'Color': mix.outputs[2]})
    
    add_shader = nw.new_node('ShaderNodeAddShader', input_kwargs={0: mix_shader_1, 1: translucent_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': add_shader}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Seed', 0),
            ('NodeSocketFloat', 'Noise Amount', 0.0000),
            ('NodeSocketInt', 'Leaf Resolution', 2),
            ('NodeSocketFloat', 'Leaf Length', 2.0000),
            ('NodeSocketFloat', 'Leaf Bend', 1.0000),
            ('NodeSocketFloat', 'Leaf Width', 1.0000),
            ('NodeSocketFloat', 'Leaf Waviness', 0.0000),
            ('NodeSocketFloat', 'Leaf Wave Position', 0.0000),
            ('NodeSocketFloat', 'Leaf Thickness', 0.0000),
            ('NodeSocketFloat', 'Central Branch Thickness', 0.2000),
            ('NodeSocketInt', 'Central Branch Resolution', 4)])
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Leaf Resolution"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Leaf Length"]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_11}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_12})
    
    quadratic_bezier = nw.new_node(Nodes.QuadraticBezier,
        input_kwargs={'Resolution': reroute_7, 'Start': (0.0000, 0.0000, 0.0000), 'Middle': combine_xyz_3, 'End': combine_xyz_2})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': quadratic_bezier})
    
    position = nw.new_node(Nodes.InputPosition)
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': curve_to_mesh})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box.outputs["Max"], 1: (0.0000, 0.0000, 0.5000)},
        attrs={'operation': 'MULTIPLY'})
    
    index = nw.new_node(Nodes.Index)
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': index})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_2, 2: reroute_8})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range.outputs["Result"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.1864, 0.0687), (0.5591, 0.2375), (1.0000, 0.4000)])
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: float_curve, 1: group_input.outputs["Leaf Bend"]},
        attrs={'operation': 'MULTIPLY'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': position, 'Center': multiply_1.outputs["Vector"], 'Angle': multiply_2},
        attrs={'rotation_type': 'Y_AXIS'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': curve_to_mesh, 'Position': vector_rotate})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': set_position})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    map_range_3 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': reroute_1, 2: reroute, 3: 1.0000, 4: 0.0000},
        attrs={'clamp': False})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: map_range_3.outputs["Result"], 1: 0.2000}, attrs={'operation': 'MULTIPLY'})
    
    clamp = nw.new_node(Nodes.Clamp, input_kwargs={'Value': multiply_3, 'Min': 0.0100, 'Max': 1.7000})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': mesh_to_curve, 'Radius': clamp})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Central Branch Thickness"], 1: 0.2000},
        attrs={'operation': 'MULTIPLY'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input.outputs["Central Branch Resolution"], 'Radius': multiply_4})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    is_shade_smooth = nw.new_node('GeometryNodeInputShadeSmooth')
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': set_position, 4: is_shade_smooth},
        attrs={'data_type': 'BOOLEAN', 'domain': 'FACE'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_4, 2: reroute_9})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_1.outputs["Result"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.1364, 0.0313), (0.3800, 0.1875), (0.6818, 0.1750), (0.8818, 0.0500)])
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Leaf Width"], 1: 5.0000},
        attrs={'operation': 'DIVIDE'})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: divide}, attrs={'operation': 'MULTIPLY'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: group_input.outputs["Leaf Wave Position"]})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: group_input.outputs["Seed"]})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: add_1}, attrs={'operation': 'SINE'})
    
    multiply_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: sine, 1: group_input.outputs["Leaf Waviness"]},
        attrs={'operation': 'MULTIPLY'})
    
    smooth_min = nw.new_node(Nodes.Math, input_kwargs={0: multiply_6, 1: -2.5000, 2: 10.0000}, attrs={'operation': 'SMOOTH_MIN'})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: smooth_min}, attrs={'operation': 'ABSOLUTE'})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_5, 1: absolute}, attrs={'operation': 'MULTIPLY'})
    
    random_value_3 = nw.new_node(Nodes.RandomValue,
        input_kwargs={3: group_input.outputs["Noise Amount"], 'Seed': group_input.outputs["Seed"]})
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': random_value_3.outputs[1], 'Detail': 0.6000, 'Roughness': 0.4583})
    
    multiply_8 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_7, 1: noise_texture_3.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_8})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': capture_attribute.outputs["Geometry"], 'Offset': combine_xyz, 'Offset Scale': 4.0000},
        attrs={'mode': 'EDGES'})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Shade Smooth': capture_attribute.outputs[4]})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_shade_smooth_1, 'Scale': (1.0000, -1.0000, 1.0000)})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_shade_smooth_1})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform, flip_faces]})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 0.1000})
    
    multiply_9 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Leaf Thickness"], 1: 1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    map_range_2 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': position_1, 3: 1.0000, 4: 0.0000})
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_2.outputs["Result"]})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.2273, 0.0187), (0.5591, 0.1500), (1.0000, 0.0000)])
    
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_9, 1: float_curve_2}, attrs={'operation': 'MULTIPLY'})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': join_geometry_1, 'Offset': combine_xyz_1, 'Offset Scale': multiply_10, 'Individual': False})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_1})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [curve_to_mesh_1, extrude_mesh_1.outputs["Mesh"], reroute_13]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': merge_by_distance, 'Material': surface.shaderfunc_to_material(shader_leaf)})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': set_material})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_shade_smooth}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_leaf, selection=selection)
apply(bpy.context.active_object)
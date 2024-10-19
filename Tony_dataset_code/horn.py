import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_tip(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 3.6000, 'Detail': 1.3000, 'Roughness': 0.3667, 'Distortion': 0.2000})
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.1583, 'Distance': 0.1000, 'Height': noise_texture.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.6008, 0.3854, 0.0786, 1.0000), 'Metallic': 0.8545, 'Specular': 0.7727, 'Roughness': 0.2455, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_horn_base(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 3.1000}, attrs={'noise_dimensions': '4D'})
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Factor'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.4864
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.8091
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture_2.outputs["Fac"], 1: colorramp_1.outputs["Color"]})
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 1.6000}, attrs={'noise_dimensions': '4D'})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute.outputs["Fac"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.2318
    colorramp_2.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture_3.outputs["Fac"], 1: colorramp_2.outputs["Color"]})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: add_1, 6: (1.0000, 0.2076, 0.3083, 1.0000), 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_2 = nw.new_node(Nodes.Mix, input_kwargs={0: add, 7: mix_3.outputs[2]}, attrs={'data_type': 'RGBA'})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': attribute.outputs["Vector"], 'Scale': 16.1000, 'Distortion': 3.5000, 'Detail': 4.8000, 'Detail Scale': 0.6000, 'Detail Roughness': 0.9462, 'Phase Offset': 4.1000},
        attrs={'rings_direction': 'Z'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 175.8000, 'Detail': 2.7000, 'Roughness': 0.7833})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: wave_texture.outputs["Fac"], 1: noise_texture_1.outputs["Fac"]},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 381.4000, 'Detail': 8.0000, 'Roughness': 0.9833, 'Distortion': 0.1000})
    
    bump_1 = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.6000, 'Distance': 0.2000, 'Height': noise_texture.outputs["Fac"]})
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.5167, 'Distance': 0.1000, 'Height': multiply, 'Normal': bump_1})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_2.outputs[2], 'Roughness': 0.6591, 'Emission Strength': 0.0000, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_horn_alt(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Factor'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute.outputs["Fac"]})
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0299, 0.0000, 0.0004, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.6227
    colorramp_1.color_ramp.elements[1].color = [0.3313, 0.2171, 0.1170, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 0.8909
    colorramp_1.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': attribute.outputs["Vector"], 'Scale': 16.1000, 'Distortion': 3.5000, 'Detail': 4.8000, 'Detail Scale': 0.6000, 'Detail Roughness': 0.9462, 'Phase Offset': 4.1000},
        attrs={'rings_direction': 'Z'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 175.8000, 'Detail': 2.7000, 'Roughness': 0.7833})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: wave_texture.outputs["Fac"], 1: noise_texture_1.outputs["Fac"]},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 381.4000, 'Detail': 8.0000, 'Roughness': 0.9833, 'Distortion': 0.1000})
    
    bump_1 = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.6000, 'Distance': 0.2000, 'Height': noise_texture.outputs["Fac"]})
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.5167, 'Distance': 0.1000, 'Height': multiply, 'Normal': bump_1})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp_1.outputs["Color"], 'Specular': 0.3091, 'Roughness': 0.6364, 'Emission Strength': 0.0000, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Horn Length', 0.2000),
            ('NodeSocketInt', 'Horn Res', 50),
            ('NodeSocketInt', 'Horn Curve Res', 8),
            ('NodeSocketFloat', 'Horn Thickness', 1.0000),
            ('NodeSocketFloat', 'Horn Curve', 0.0000),
            ('NodeSocketFloat', 'Horn Twist', 1.0000),
            ('NodeSocketInt', 'Tip Size', 0),
            ('NodeSocketFloat', 'Horn Spacing', 0.0500),
            ('NodeSocketVector', 'Horn Rotation', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketMaterial', 'Horn', None)]) #surface.shaderfunc_to_material(shader_horn_base))])
    
    curve_line = nw.new_node(Nodes.CurveLine,
        input_kwargs={'End': (0.0000, 0.0000, 0.3000), 'Length': group_input.outputs["Horn Length"]},
        attrs={'mode': 'DIRECTION'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Horn Res"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': reroute_1})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': resample_curve})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    index = nw.new_node(Nodes.Index)
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': index, 2: reroute_10})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_1.outputs["Result"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0000), (0.5136, 0.0188), (1.0000, 0.0000)])
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Horn Curve"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: reroute_7}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_1, 1: combine_xyz})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_6, 'Position': add.outputs["Vector"]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_6})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: bounding_box.outputs["Max"], 1: (0.0000, 1.0000, 0.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': index})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    map_range_4 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_16, 2: reroute_17, 3: 1.0000, 4: 0.0000})
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_4.outputs["Result"]})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.0045, 0.0313), (0.3636, 0.3250), (1.0000, 0.9437)])
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Horn Twist"]})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_2, 1: reroute_11}, attrs={'operation': 'MULTIPLY'})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_2})
    
    vector_rotate_1 = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': position, 'Center': multiply_1.outputs["Vector"], 'Angle': reroute_18},
        attrs={'rotation_type': 'Z_AXIS'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_3, 'Position': vector_rotate_1})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': position})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_16, 2: reroute_17, 3: 0.1000, 4: 0.4000})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range.outputs["Result"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 1.0000), (0.5227, 0.1938), (1.0000, 0.1437)])
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': float_curve})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': reroute_21, 'Center': multiply_1.outputs["Vector"], 'Angle': reroute_19},
        attrs={'rotation_type': 'X_AXIS'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_2, 'Position': vector_rotate})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute, input_kwargs={'Geometry': set_position, 2: spline_parameter.outputs["Factor"]})
    
    index_3 = nw.new_node(Nodes.Index)
    
    map_range_3 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': index_3, 2: reroute_1, 3: 1.0000, 4: 0.0000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range_3.outputs["Result"]})
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.1455
    colorramp_2.color_ramp.elements[1].color = [0.2357, 0.2357, 0.2357, 1.0000]
    colorramp_2.color_ramp.elements[2].position = 0.3000
    colorramp_2.color_ramp.elements[2].color = [0.3720, 0.3720, 0.3720, 1.0000]
    colorramp_2.color_ramp.elements[3].position = 0.7182
    colorramp_2.color_ramp.elements[3].color = [0.7366, 0.7366, 0.7366, 1.0000]
    colorramp_2.color_ramp.elements[4].position = 1.0000
    colorramp_2.color_ramp.elements[4].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Horn Thickness"]})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_2.outputs["Color"], 1: reroute_12},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_3})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius,
        input_kwargs={'Curve': capture_attribute.outputs["Geometry"], 'Radius': reroute_5})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Horn Curve Res"]})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_14, 'Radius': 0.0100})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': curve_circle_1.outputs["Curve"], 'Fill Caps': True})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_3})
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz.outputs["Z"], 1: 0.0010}, attrs={'operation': 'LESS_THAN'})
    
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: less_than}, attrs={'operation': 'NOT'})
    
    index_2 = nw.new_node(Nodes.Index)
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Horn Res"], 1: group_input.outputs["Tip Size"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_add = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: reroute_14, 2: -1.0000}, attrs={'operation': 'MULTIPLY_ADD'})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: index_2, 3: multiply_add}, attrs={'data_type': 'INT'})
    
    op_and = nw.new_node(Nodes.BooleanMath, input_kwargs={0: op_not, 1: greater_than})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': curve_to_mesh_1, 'Selection': op_and, 'Offset Scale': 0.0010, 'Individual': False})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': 0.7500})
    
    set_material = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': scale_elements, 'Material': group_input.outputs["Horn"]})
    
    op_or = nw.new_node(Nodes.BooleanMath,
        input_kwargs={0: extrude_mesh.outputs["Top"], 1: extrude_mesh.outputs["Side"]},
        attrs={'operation': 'OR'})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_material, 'Selection': op_or, 'Material': surface.shaderfunc_to_material(shader_tip)})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Horn Spacing"]})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_9})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Horn Rotation"]})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': set_material_1, 'Translation': combine_xyz_2, 'Rotation': reroute_8})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform, 'Scale': (-1.0000, 1.0000, 1.0000)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform, transform_1]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs[2]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': set_shade_smooth, 'Factor': reroute_2},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_horn_alt, selection=selection)
apply(bpy.context.active_object)
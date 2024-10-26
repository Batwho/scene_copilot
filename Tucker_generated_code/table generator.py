import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Generated"]})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping},
        attrs={'image': bpy.data.images['20210727_163525.jpg']})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Value': 0.4000, 'Color': image_texture.outputs["Color"]})
    
    bright_contrast = nw.new_node('ShaderNodeBrightContrast', input_kwargs={'Color': hue_saturation_value, 'Contrast': 0.1000})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': bright_contrast, 'Specular': 0.4591})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_t_a_b_l_e_g_e_n_e_r_a_t_o_r(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'surface anglecount', 4),
            ('NodeSocketFloatDistance', 'corner bevel', 0.3000),
            ('NodeSocketInt', 'corner segment', 13),
            ('NodeSocketFloat', 'thickness', 0.4000),
            ('NodeSocketFloat', 'Height', 2.7000),
            ('NodeSocketFloat', 'width', 1.2000),
            ('NodeSocketFloat', 'length', 0.7000),
            ('NodeSocketFloatDistance', 'Radius', 2.9000),
            ('NodeSocketInt', 'subdivde', 30),
            ('NodeSocketInt', 'leg radial count', 6),
            ('NodeSocketFloatDistance', 'leg thickness', 4.3000),
            ('NodeSocketFloatDistance', 'leg bevel', 0.3000),
            ('NodeSocketFloat', 'leg joint offset', 0.0000),
            ('NodeSocketInt', 'leg count', 4)])
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["thickness"]})
    
    reroute_73 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute_72 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_73})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_72})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_3})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["subdivde"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': reroute_5})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_parameter.outputs["Factor"]})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    reroute_66 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_44})
    
    reroute_67 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_66})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_67})
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute_45})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.0109, 0.5687), (0.0679, 0.6062), (0.1495, 0.5187), (0.2364, 0.5500), (0.6677, 0.4375), (0.8282, 0.5812), (0.8913, 0.7000), (0.9429, 0.6250), (1.0000, 0.8125)])
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_2, 1: -0.1000, 2: 2.0000}, attrs={'operation': 'POWER'})
    
    reroute_70 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': power})
    
    reroute_71 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_70})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve, 'Radius': reroute_71})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_curve_radius})
    
    reroute_87 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["surface anglecount"]})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius"]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_27, 'Radius': reroute_29})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_circle.outputs["Curve"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_49})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_9, 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["width"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["length"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_16, 'Y': reroute_15})
    
    reroute_68 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_2})
    
    reroute_69 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_68})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform, 'Scale': reroute_69})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_2})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["corner segment"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["corner bevel"]})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    fillet_curve = nw.new_node(Nodes.FilletCurve,
        input_kwargs={'Curve': reroute_14, 'Count': reroute_10, 'Radius': reroute_11, 'Limit Radius': True},
        attrs={'mode': 'POLY'})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': reroute_87, 'Profile Curve': fillet_curve, 'Fill Caps': True})
    
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_to_mesh, 'Scale': (1.2000, 1.2000, 1.0000)})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_5})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Height"]})
    
    reroute_65 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_65})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_1, 'Translation': reroute_2})
    
    reroute_74 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_4})
    
    reroute_75 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_74})
    
    reroute_91 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["leg count"]})
    
    reroute_92 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_91})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_92, 'Radius': reroute_20})
    
    normal_1 = nw.new_node(Nodes.InputNormal)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_circle_2.outputs["Curve"], 1: normal_1},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': capture_attribute_1.outputs["Geometry"], 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    reroute_64 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_68})
    
    transform_6 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_1, 'Scale': reroute_64})
    
    reroute_77 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_6})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_77})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Height"]})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_30})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_1})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["subdivde"]})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_1, 'Count': reroute_31})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute_42})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.2125), (0.0486, 0.1063), (0.2070, 0.0000), (0.3735, 0.0937), (0.6209, 0.2875), (0.9023, 0.0062), (1.0000, 0.0000)])
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: float_curve, 1: 0.4000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_63 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_63})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': resample_curve_1, 'Offset': reroute_51})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_41})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute_43})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0875), (0.0272, 0.2875), (0.1119, 0.3313), (0.1647, 0.4437), (0.2242, 0.3063), (0.4512, 0.2813), (0.8529, 0.7500), (1.0000, 0.5000)])
    
    reroute_62 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': float_curve_1})
    
    reroute_61 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_62})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_61, 1: -0.5000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_1})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_47})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_position, 'Radius': reroute_46})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_curve_radius_1})
    
    reroute_60 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_52})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["leg radial count"]})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_34})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_36})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_38})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["leg thickness"]})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_35})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_37})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_40, 'Radius': reroute_39})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle_1.outputs["Curve"], 'Rotation': (0.0000, 0.0000, 0.7854), 'Scale': (0.3000, 0.3000, 0.3000)})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["leg bevel"]})
    
    reroute_55 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_32})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_55})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_54})
    
    fillet_curve_1 = nw.new_node(Nodes.FilletCurve,
        input_kwargs={'Curve': transform_3, 'Count': 5, 'Radius': reroute_53, 'Limit Radius': True},
        attrs={'mode': 'POLY'})
    
    reroute_59 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': fillet_curve_1})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_59})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': reroute_60, 'Profile Curve': reroute_58, 'Fill Caps': True})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs["Attribute"]})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: reroute_48, 1: (55.1000, 17.0000, 9.2000), 'Scale': 1.3000},
        attrs={'operation': 'SCALE'})
    
    reroute_57 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale.outputs["Vector"]})
    
    reroute_56 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_57})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': reroute_56}, attrs={'pivot_axis': 'Z'})
    
    reroute_78 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': align_euler_to_vector})
    
    reroute_79 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_78})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_50, 'Instance': curve_to_mesh_1, 'Rotation': reroute_79})
    
    reroute_81 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["leg joint offset"]})
    
    reroute_82 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_81})
    
    reroute_83 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_82})
    
    reroute_84 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_83})
    
    reroute_86 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_84})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_86, 'Y': reroute_84})
    
    reroute_85 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_4})
    
    reroute_80 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_85})
    
    translate_instances = nw.new_node(Nodes.TranslateInstances, input_kwargs={'Instances': instance_on_points, 'Translation': reroute_80})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': translate_instances})
    
    reroute_76 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_75, reroute_76]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': surface.shaderfunc_to_material(shader_material)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_t_a_b_l_e_g_e_n_e_r_a_t_o_r, selection=selection, attributes=[])
    surface.add_material(obj, shader_material, selection=selection)
apply(bpy.context.active_object)
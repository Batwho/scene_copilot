import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_material_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Location': (0.4000, 0.4000, -0.3000), 'Rotation': (0.0000, 1.5708, 0.0000), 'Scale': (2.3100, 2.6000, 2.1000)})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping},
        attrs={'image': bpy.data.images['20210727_190627.jpg']})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': image_texture.outputs["Color"], 'Specular': 0.0000, 'Roughness': 0.4864})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_c_u_r_t_a_i_n_g_e_n_e_r_a_t_o_r(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatDistance', 'height', 1.0000),
            ('NodeSocketFloat', 'drapery', 0.1000),
            ('NodeSocketFloat', 'wrincle', 1.0000),
            ('NodeSocketFloat', 'open/close', 10.4000),
            ('NodeSocketFloat', 'folds thickness', -2.6000),
            ('NodeSocketFloat', 'folds starting', 0.4000),
            ('NodeSocketFloat', 'open wider', 0.0000),
            ('NodeSocketInt', 'subdivideX', 30),
            ('NodeSocketInt', 'subdivideY', 30),
            ('NodeSocketString', 'drape', ''),
            ('NodeSocketBool', 'on/off', False),
            ('NodeSocketFloat', 'drop', 1.4000),
            ('NodeSocketFloat', 'gravity', -79.8000),
            ('NodeSocketFloat', 'thickness', -1.7000)])
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["on/off"]})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_41})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_42})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_43})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["open wider"], 1: 1.0000},
        attrs={'operation': 'DIVIDE'})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_5})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_line, 'Translation': (0.0000, 0.0000, 0.0000), 'Rotation': (-1.5708, 0.0000, 0.0000), 'Scale': (1.0000, 1.0000, 1.3000)})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': transform_3, 'Count': 3})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': resample_curve}, attrs={'spline_type': 'BEZIER'})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 3})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection)
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: endpoint_selection, 1: endpoint_selection_1},
        attrs={'operation': 'GREATER_THAN'})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': greater_than})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_34})
    
    set_handle_type = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type, 'Selection': reroute_35})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': greater_than})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: -0.0400, 1: group_input.outputs["gravity"]},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_6})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_handle_type, 'Selection': reroute_32, 'Offset': reroute_36})
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position_4, 'Count': 30})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_parameter.outputs["Factor"]})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_38})
    
    float_curve_4 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': reroute_37})
    node_utils.assign_curve(float_curve_4.mapping.curves[0], [(0.0000, 0.0000), (0.5273, 0.2438), (1.0000, 0.0000)])
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: float_curve_4, 1: group_input.outputs["drop"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve_2, 'Radius': multiply_1})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_curve_radius})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 2.4000)})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_line_1, 'Rotation': (-1.5708, 0.0000, 0.0000)})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': transform_2, 'Count': 44})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0000), (0.0636, 0.2000), (0.0955, 0.0312), (0.1636, 0.1750), (0.2273, 0.0187), (0.2955, 0.1937), (0.3545, 0.0187), (0.4091, 0.1688), (0.4818, 0.0250), (0.5727, 0.1875), (0.6409, 0.0062), (0.7273, 0.1938), (0.8136, 0.0063), (0.9091, 0.1938), (1.0000, 0.0000)])
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: float_curve_1, 1: group_input.outputs["thickness"]},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_2})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': resample_curve_1, 'Offset': combine_xyz_4})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_3})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': reroute_30, 'Profile Curve': reroute_29})
    
    transform_5 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_to_mesh, 'Translation': (-0.0900, 0.0000, 3.9600)})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_40, 15: transform_5})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["height"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["subdivideX"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["subdivideY"]})
    
    grid = nw.new_node(Nodes.MeshGrid, input_kwargs={'Size X': reroute_8, 'Vertices X': reroute_9, 'Vertices Y': reroute_10})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute, 'Translation': (0.0000, 0.0000, 0.0000), 'Rotation': (0.0000, 1.5708, 0.0000)})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    position = nw.new_node(Nodes.InputPosition)
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': position})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    map_range_4 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': reroute_11, 2: -0.1000, 3: -0.0000, 4: 0.2000})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_4.outputs["Result"]})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_12, 1: 0.0000})
    
    multiply_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_14, 1: add}, attrs={'operation': 'MULTIPLY'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["drapery"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_3.outputs["Vector"], 'Scale': reroute_15},
        attrs={'operation': 'SCALE'})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale.outputs["Vector"]})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': reroute_24, 'Selection': reroute_25, 'Offset': reroute_26})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_2})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': reroute_18})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz.outputs["Y"], 1: -0.5000, 2: 0.5000, 3: 0.0000, 4: group_input.outputs["wrincle"]})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"], 1: 24.3000}, attrs={'operation': 'SINE'})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': sine})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.0448, 0.2125), (0.0792, 0.0437), (0.1636, 0.2000), (0.1939, 0.0562), (0.2680, 0.1813), (0.3208, 0.0250), (0.3887, 0.1812), (0.4528, 0.1000), (0.5088, 0.1812), (0.5548, 0.0662), (0.6261, 0.2188), (0.6650, 0.0562), (0.7508, 0.1938), (0.8066, 0.0687), (0.8837, 0.2062), (0.9488, 0.0437), (0.9867, 0.1875), (1.0000, 0.0000)])
    
    clamp = nw.new_node(Nodes.Clamp, input_kwargs={'Value': group_input.outputs["folds starting"], 'Min': 0.2000})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz.outputs["Z"], 1: clamp, 2: 0.5000, 3: 0.0000, 4: 0.3000})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: float_curve, 1: map_range_2.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_4, 'Y': 0.0000})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_4, 1: combine_xyz})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': reroute_7, 'Position': add_1.outputs["Vector"], 'Offset': (-0.0000, 0.0000, 0.0000)})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input.outputs["folds thickness"], 'Y': 1.5000, 'Z': 3.0000})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position, 'Scale': combine_xyz_1})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': reroute_1})
    
    map_range_3 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_1.outputs["Y"], 1: -1.8000, 2: 33.6000, 3: 0.4000, 4: -4.8000})
    
    float_curve_3 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_3.outputs["Result"]})
    node_utils.assign_curve(float_curve_3.mapping.curves[0], [(0.0000, 0.0000), (0.5151, 0.9937), (0.9962, 0.0000)])
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_3, 1: 1.6000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["open/close"]})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_1.outputs["Z"], 1: reroute_19, 2: -14.1000, 3: 0.0000})
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_1.outputs["Result"]})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.0000, 0.0063), (0.4528, 0.2500), (0.5057, 0.8250), (0.5057, 1.0000), (1.0000, 0.0000)])
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_5, 1: float_curve_2}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_6})
    
    add_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_2, 1: combine_xyz_2})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': transform_4, 'Position': add_2.outputs["Vector"], 'Offset': (-0.5000, -0.5000, -0.5000)})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["open wider"]})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 0.6000, 'Y': reroute, 'Z': 2.4000})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_3})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_22, 'Translation': reroute_21})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [switch.outputs[6], transform_1]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_material_001)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_c_u_r_t_a_i_n_g_e_n_e_r_a_t_o_r, selection=selection, attributes=[])
    surface.add_material(obj, shader_material_001, selection=selection)
apply(bpy.context.active_object)
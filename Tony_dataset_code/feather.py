import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_feather', singleton=False, type='GeometryNodeTree')
def nodegroup_feather(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_17 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Length', 1.0000),
            ('NodeSocketInt', 'Resolution', 14),
            ('NodeSocketMaterial', 'Base', None),
            ('NodeSocketFloat', 'Start', 0.4000),
            ('NodeSocketFloat', 'Thickness', 0.8000),
            ('NodeSocketFloat', 'Bias', 0.0000),
            ('NodeSocketFloat', 'Width', 1.0000),
            ('NodeSocketFloat', 'Plucking', 0.0000),
            ('NodeSocketFloat', 'Spread color', 0.0000),
            ('NodeSocketFloat', 'Count', 100.0000),
            ('NodeSocketInt', 'Subdivision', 2),
            ('NodeSocketFloat', 'Bending point', 0.0000),
            ('NodeSocketFloat', 'Bending scale', 1.0000),
            ('NodeSocketFloat', 'Bending spread', 1.5000),
            ('NodeSocketMaterial', 'Feather', None),#surface.shaderfunc_to_material(shader_feather)),
            ('NodeSocketFloat', 'Noise', 0.0000),
            ('NodeSocketFloat', 'Noise offset', 0.0000),
            ('NodeSocketFloat', 'Noise base', 0.0000),
            ('NodeSocketGeometry', 'Instance points', None),
            ('NodeSocketVectorEuler', 'Rotation', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVectorXYZ', 'Scale', (1.0000, 1.0000, 1.0000))])
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_17.outputs["Length"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_line})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_17.outputs["Resolution"], 1: 2.0000},
        attrs={'operation': 'MULTIPLY'})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': reroute, 'Count': multiply})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.2500, 0.4937), (1.0000, 0.0000)])
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve, 'Radius': float_curve})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': set_curve_radius, 2: spline_parameter_1.outputs["Factor"]})
    
    arc = nw.new_node('GeometryNodeCurveArc',
        input_kwargs={'Resolution': 11, 'Radius': 0.0100, 'Sweep Angle': 6.2832, 'Connect Center': True})
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': arc.outputs["Curve"], 2: spline_parameter_1.outputs["Factor"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': capture_attribute.outputs["Geometry"], 'Profile Curve': capture_attribute_1.outputs["Geometry"], 'Fill Caps': True})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': capture_attribute.outputs[2], 'Y': capture_attribute_1.outputs[2]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': curve_to_mesh, 'Name': 'feather_base_uv', 3: combine_xyz_1},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': store_named_attribute}, attrs={'mode': 'CONNECTED'})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': merge_by_distance, 'Material': group_input_17.outputs["Base"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_line})
    
    spline_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': spline_parameter_2.outputs["Factor"], 3: group_input_17.outputs["Start"]})
    
    sample_curve = nw.new_node(Nodes.SampleCurve,
        input_kwargs={'Curves': reroute_2, 'Factor': map_range.outputs["Result"]},
        attrs={'use_all_curves': True})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_2, 'Position': sample_curve.outputs["Position"]})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': set_position, 'Count': group_input_17.outputs["Resolution"]})
    
    spline_parameter_3 = nw.new_node(Nodes.SplineParameter)
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': resample_curve_1, 'Name': 'Z', 4: spline_parameter_3.outputs["Length"]})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': store_named_attribute_1, 'Name': 'thickness', 4: group_input_17.outputs["Thickness"]})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (1.0000, 0.0000, 0.0000)})
    
    spline_parameter_4 = nw.new_node(Nodes.SplineParameter)
    
    store_named_attribute_3 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': curve_line_1, 'Name': 'X', 4: spline_parameter_4.outputs["Factor"]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': store_named_attribute_2, 'Profile Curve': store_named_attribute_3, 'Fill Caps': True})
    
    index = nw.new_node(Nodes.Index)
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: 1.0000})
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: modulo}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    store_named_attribute_4 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Name': 'boundary', 6: equal},
        attrs={'data_type': 'BOOLEAN'})
    
    named_attribute = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'boundary'}, attrs={'data_type': 'BOOLEAN'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_17.outputs["Bias"]})
    
    multiply_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position, 1: combine_xyz_2}, attrs={'operation': 'MULTIPLY'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute_4, 'Selection': named_attribute.outputs[3], 'Offset': multiply_1.outputs["Vector"]})
    
    named_attribute_1 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'boundary'}, attrs={'data_type': 'BOOLEAN'})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_17.outputs["Width"], 1: group_input_17.outputs["Thickness"]},
        attrs={'operation': 'DIVIDE'})
    
    index_1 = nw.new_node(Nodes.Index)
    
    named_attribute_2 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'boundary'}, attrs={'data_type': 'BOOLEAN'})
    
    attribute_statistic = nw.new_node(Nodes.AttributeStatistic,
        input_kwargs={'Geometry': set_position_1, 'Selection': named_attribute_2.outputs[3], 2: index_1})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': index_1, 1: attribute_statistic.outputs["Min"], 2: attribute_statistic.outputs["Max"]})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_1.outputs["Result"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0000), (0.2227, 0.4500), (0.6091, 0.3438), (0.9136, 0.1250), (1.0000, 0.0000)])
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: float_curve_1}, attrs={'operation': 'MULTIPLY'})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': multiply_2, 'Y': separate_xyz.outputs["Y"], 'Z': separate_xyz.outputs["Z"]})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_1, 'Selection': named_attribute_1.outputs[3], 'Position': combine_xyz_3})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_2, 'Scale': (-1.0000, 1.0000, 1.0000)})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': transform})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces, set_position_2]})
    
    store_named_attribute_5 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': join_geometry, 'Name': 'plucking', 4: group_input_17.outputs["Plucking"]})
    
    store_named_attribute_6 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': store_named_attribute_5, 'Name': 'spread_color', 4: group_input_17.outputs["Spread color"]})
    
    store_named_attribute_7 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': store_named_attribute_6, 'Name': 'count', 4: group_input_17.outputs["Count"]})
    
    subdivide_mesh = nw.new_node(Nodes.SubdivideMesh,
        input_kwargs={'Mesh': store_named_attribute_7, 'Level': group_input_17.outputs["Subdivision"]})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    capture_attribute_2 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': subdivide_mesh, 1: position_2},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    named_attribute_3 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'X'})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: named_attribute_3.outputs[1], 1: group_input_17.outputs["Bending scale"]},
        attrs={'operation': 'MULTIPLY'})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': group_input_17.outputs["Bending spread"], 3: 1.0000, 4: 2.0000},
        attrs={'clamp': False})
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: map_range_2.outputs["Result"]}, attrs={'operation': 'POWER'})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': capture_attribute_2.outputs["Attribute"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': store_named_attribute_2})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    sample_curve_1 = nw.new_node(Nodes.SampleCurve,
        input_kwargs={'Curves': reroute_3, 'Factor': group_input_17.outputs["Bending point"]},
        attrs={'use_all_curves': True})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': sample_curve_1.outputs["Position"]})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_1.outputs["Z"], 1: separate_xyz_2.outputs["Z"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: power, 1: subtract}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_4})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': capture_attribute_2.outputs["Geometry"], 'Offset': combine_xyz_4})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_3})
    
    less_equal = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz_3.outputs["X"]}, attrs={'operation': 'LESS_EQUAL'})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={0: less_equal, 2: 1.0000}, attrs={'input_type': 'FLOAT'})
    
    store_named_attribute_8 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': set_position_3, 'Name': 'side', 4: switch.outputs["Output"]})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': store_named_attribute_8, 'Material': group_input_17.outputs["Feather"]})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_6, set_material_1]})
    
    position_4 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_4 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_4})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_4.outputs["Z"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    position_5 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_5 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_5})
    
    attribute_statistic_2 = nw.new_node(Nodes.AttributeStatistic, input_kwargs={'Geometry': reroute_7, 2: separate_xyz_5.outputs["Z"]})
    
    attribute_statistic_1 = nw.new_node(Nodes.AttributeStatistic, input_kwargs={'Geometry': join_geometry_1, 2: separate_xyz_4.outputs["Z"]})
    
    map_range_3 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': reroute_8, 1: attribute_statistic_2.outputs["Min"], 2: attribute_statistic_1.outputs["Max"]})
    
    store_named_attribute_9 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': join_geometry_1, 'Name': 'absolute_z', 4: map_range_3.outputs["Result"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': group_input_17.outputs["Instance points"], 'Instance': store_named_attribute_9, 'Rotation': group_input_17.outputs["Rotation"], 'Scale': group_input_17.outputs["Scale"]})
    
    random_value = nw.new_node(Nodes.RandomValue)
    
    store_named_attribute_10 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': instance_on_points, 'Name': 'random', 4: random_value.outputs[1]},
        attrs={'domain': 'INSTANCE'})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': store_named_attribute_10})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input_17.outputs["Noise offset"], 'Scale': group_input_17.outputs["Noise"], 'Detail': 0.0000, 'Roughness': 0.0000},
        attrs={'noise_dimensions': '4D'})
    
    subtract_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_5 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normal, 1: subtract_1.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    named_attribute_4 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'X'})
    
    named_attribute_5 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'Z'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_17.outputs["Bending point"]})
    
    pingpong = nw.new_node(Nodes.Math,
        input_kwargs={0: named_attribute_5.outputs[1], 1: reroute_5},
        attrs={'operation': 'PINGPONG'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: pingpong, 1: reroute_5}, attrs={'operation': 'DIVIDE'})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: named_attribute_4.outputs[1], 1: divide_1}, attrs={'operation': 'MULTIPLY'})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_5.outputs["Vector"], 'Scale': multiply_6},
        attrs={'operation': 'SCALE'})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': realize_instances, 'Offset': scale.outputs["Vector"]})
    
    named_attribute_7 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'random'})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: named_attribute_7.outputs[1], 1: 100.0000}, attrs={'operation': 'MULTIPLY'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': multiply_7, 'Scale': group_input_17.outputs["Noise base"], 'Detail': 0.0000, 'Roughness': 0.0000},
        attrs={'noise_dimensions': '4D'})
    
    subtract_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture_1.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    named_attribute_6 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'absolute_z'})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract_2.outputs["Vector"], 'Scale': named_attribute_6.outputs[1]},
        attrs={'operation': 'SCALE'})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_4, 'Offset': scale_1.outputs["Vector"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_position_5}, attrs={'is_active_output': True})

def shader_feather(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'X'})
    
    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Z'})
    
    attribute_6 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'side'})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: attribute_6.outputs["Fac"], 1: 0.0000}, attrs={'operation': 'GREATER_THAN'})
    
    attribute_7 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'random'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: attribute_7.outputs["Fac"], 1: 1000.0000}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: greater_than, 1: multiply})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: attribute.outputs["Fac"], 1: add})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': add_1})
    
    attribute_3 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'spread_color'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_2, 'Scale': attribute_3.outputs["Fac"], 'Detail': 1.0000, 'Roughness': 1.0000})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: attribute_1.outputs["Fac"], 7: noise_texture.outputs["Fac"]},
        attrs={'blend_type': 'LINEAR_LIGHT', 'data_type': 'RGBA'})
    
    attribute_5 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'thickness'})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': mix.outputs[2], 2: attribute_5.outputs["Fac"]})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range_1.outputs["Result"]})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0478, 0.0195, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.4818
    colorramp.color_ramp.elements[1].color = [0.1954, 0.0546, 0.0134, 1.0000]
    colorramp.color_ramp.elements[2].position = 1.0000
    colorramp.color_ramp.elements[2].color = [0.5239, 0.2237, 0.0413, 1.0000]
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Color': attribute_1.outputs["Fac"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    attribute_2 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'count'})
    
    wave_texture = nw.new_node(Nodes.WaveTexture, input_kwargs={'Vector': reroute_1, 'Scale': attribute_2.outputs["Fac"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    attribute_4 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'plucking'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute, 'Scale': attribute_4.outputs["Fac"], 'Detail': 0.0000, 'Roughness': 0.0000})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: wave_texture.outputs["Color"], 7: noise_texture_1.outputs["Fac"]},
        attrs={'blend_type': 'LINEAR_LIGHT', 'data_type': 'RGBA'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: invert, 1: mix_1.outputs[2]}, attrs={'operation': 'MULTIPLY'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': attribute_5.outputs["Fac"], 3: 1.0000, 4: 0.0000})
    
    greater_than_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_1, 1: map_range.outputs["Result"]},
        attrs={'operation': 'GREATER_THAN'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Roughness': 1.0000, 'Alpha': greater_than_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_feather_base(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    material_output = nw.new_node(Nodes.MaterialOutput, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    arc = nw.new_node('GeometryNodeCurveArc', input_kwargs={'Resolution': 9, 'Radius': 0.1000, 'Sweep Angle': 6.2832})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': arc.outputs["Curve"], 'Rotation': (1.5708, -1.5708, 0.0000)})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent}, attrs={'axis': 'Z'})
    
    rotate_euler = nw.new_node(Nodes.RotateEuler,
        input_kwargs={'Rotation': align_euler_to_vector, 'Rotate By': (0.0000, 1.5708, 0.0000)})
    
    feather = nw.new_node(nodegroup_feather().name,
        input_kwargs={'Base': surface.shaderfunc_to_material(shader_feather_base), 'Start': 0.5000, 'Thickness': 0.8200, 'Bias': 0.2500, 'Width': 0.9063, 'Plucking': 100.0000, 'Spread color': 10.0000, 'Count': 200.0000, 'Subdivision': 4, 'Bending point': 0.4000, 'Noise': 1.0000, 'Noise offset': 7.2000, 'Noise base': 1.0000, 'Instance points': transform, 'Rotation': rotate_euler})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': feather}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_feather_base, selection=selection)
    surface.add_material(obj, shader_feather, selection=selection)
apply(bpy.context.active_object)
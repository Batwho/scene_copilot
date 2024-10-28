import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_branch_base_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Object"]})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mapping, 'W': 2.1100, 'Scale': 100.0000, 'Smoothness': 0.0000},
        attrs={'feature': 'SMOOTH_F1', 'voronoi_dimensions': '4D', 'distance': 'CHEBYCHEV'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Distance"]})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.4955
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5000
    colorramp.color_ramp.elements[1].color = [0.9053, 1.0000, 0.3267, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.5000
    colorramp.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 30.0000, 'Distortion': 3.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.2136
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.4591
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp.outputs["Color"], 1: colorramp_1.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 20.0000, 'Detail': 0.2000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.2909
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5591
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.2083, 'Distance': 0.1000, 'Height': colorramp_2.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0034, 0.0018, 0.0054, 1.0000), 'Subsurface': 0.2409, 'Subsurface Color': (0.0019, 0.0026, 0.0040, 1.0000), 'Specular': 0.5727, 'Roughness': 0.1136, 'Emission': multiply, 'Emission Strength': 2.0000, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_branch_base(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Object"]})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': mapping, 'Scale': 100.0000, 'Smoothness': 0.0000},
        attrs={'feature': 'SMOOTH_F1', 'distance': 'CHEBYCHEV'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Distance"]})
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.4955
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5000
    colorramp.color_ramp.elements[1].color = [0.9053, 1.0000, 0.3267, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.5000
    colorramp.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 30.0000, 'Distortion': 3.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.2136
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.4591
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp.outputs["Color"], 1: colorramp_1.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 20.0000, 'Detail': 0.2000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.2909
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5591
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.2083, 'Distance': 0.1000, 'Height': colorramp_2.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0034, 0.0018, 0.0054, 1.0000), 'Subsurface': 0.2409, 'Subsurface Color': (0.0019, 0.0026, 0.0040, 1.0000), 'Specular': 0.5727, 'Roughness': 0.1136, 'Emission': multiply, 'Emission Strength': 1.1800, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_bulb_stem(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0010, 0.0007, 0.0042, 1.0000), 'Subsurface': 0.5864, 'Subsurface Radius': (1.0000, 0.8000, 1.4000), 'Subsurface Color': (0.0010, 0.0007, 0.0042, 1.0000), 'Metallic': 0.1864, 'Specular': 0.7545, 'Roughness': 0.1909})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    main_branch_thickness = nw.new_node(Nodes.GroupInput,
        label='Main Branch Thickness',
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatFactor', 'Grow [M] ', 1.0000),
            ('NodeSocketInt', 'Curve Resolution [M] ', 100),
            ('NodeSocketInt', 'Profile Resolution [M] ', 32),
            ('NodeSocketFloat', 'Thickness [M] ', 1.0000),
            ('NodeSocketFloatFactor', 'Grow [S] ', 1.0000),
            ('NodeSocketFloat', 'Growth Threshold [S]', 1.0000),
            ('NodeSocketFloat', 'Growth Limiter [S] ', 1.0000),
            ('NodeSocketInt', 'Curve Resolution [S] ', 10),
            ('NodeSocketInt', 'Profile Resolution [S] ', 16),
            ('NodeSocketFloatDistance', 'Thickness [S] ', 1.0000),
            ('NodeSocketFloat', 'Height [S] ', 0.2000),
            ('NodeSocketFloat', 'Scale Factor [S] ', 1.0000),
            ('NodeSocketFloat', 'Randomize Scale Factor [S] ', 0.5000),
            ('NodeSocketInt', 'Random Scale Seed [S] ', 0),
            ('NodeSocketFloat', 'Crookedness [S] ', 0.0000),
            ('NodeSocketIntUnsigned', 'Crookedness Smooth [S] ', 1),
            ('NodeSocketInt', 'Random Crookedness Seed [S] ', 0),
            ('NodeSocketFloat', 'Z Offset [S] ', 0.0000),
            ('NodeSocketFloat', 'Z End Handle [S] ', 0.0000),
            ('NodeSocketFloat', 'Z Start Handle [S] ', 0.0000),
            ('NodeSocketFloatDistance', 'Distribution Min. Distance [S] ', 0.1000),
            ('NodeSocketFloat', 'Density Max [S] ', 150.0000),
            ('NodeSocketFloatFactor', 'Density Factor [S] ', 1.0000),
            ('NodeSocketInt', 'Distribution Seed [S] ', 1),
            ('NodeSocketFloat', 'Scale Object', 0.0000),
            ('NodeSocketObject', 'Object', None)])
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': main_branch_thickness.outputs["Geometry"], 'Count': main_branch_thickness.outputs["Curve Resolution [M] "]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branch_thickness.outputs["Grow [M] "]})
    
    trim_curve = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': resample_curve_1, 3: reroute_29})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: main_branch_thickness.outputs["Thickness [M] "], 1: 0.0400},
        attrs={'operation': 'MULTIPLY'})
    
    spline_parameter_3 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_3 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter_3.outputs["Factor"]})
    node_utils.assign_curve(float_curve_3.mapping.curves[0], [(0.0000, 1.0000), (0.0955, 0.8250), (0.9259, 0.5187), (1.0000, 0.0000)])
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: float_curve_3}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius_2 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': trim_curve, 'Radius': multiply_1})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branch_thickness.outputs["Profile Resolution [M] "]})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_13})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_2, 'Profile Curve': curve_circle_2.outputs["Curve"], 'Fill Caps': True})
    
    subdivide_curve_2 = nw.new_node(Nodes.SubdivideCurve, input_kwargs={'Curve': trim_curve, 'Cuts': 2})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: reroute_30, 1: 0.1250}, attrs={'operation': 'POWER'})
    
    trim_curve_2 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': subdivide_curve_2, 3: power})
    
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Vertices X': 1, 'Vertices Y': 1, 'Vertices Z': 1})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': store_named_attribute})
    
    curve_to_mesh_3 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': trim_curve_2, 'Profile Curve': mesh_to_curve, 'Fill Caps': True})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_to_mesh_2, curve_to_mesh_3]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': main_branch_thickness.outputs["Geometry"], 'Count': main_branch_thickness.outputs["Curve Resolution [M] "]})
    
    spline_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter_1.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 1.0000), (0.0955, 0.8250), (0.9259, 0.5187), (0.9931, 0.0000)])
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: main_branch_thickness.outputs["Thickness [M] "], 1: 0.0400},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve, 1: multiply_2}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': resample_curve, 'Radius': multiply_3})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branch_thickness.outputs["Profile Resolution [M] "]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_4})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_circle.outputs["Curve"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_curve_radius, 'Profile Curve': reroute_14})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_3, 'Distance Min': main_branch_thickness.outputs["Distribution Min. Distance [S] "], 'Density Max': main_branch_thickness.outputs["Density Max [S] "], 'Density Factor': main_branch_thickness.outputs["Density Factor [S] "], 'Seed': main_branch_thickness.outputs["Distribution Seed [S] "]},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: main_branch_thickness.outputs["Height [S] "], 1: 0.0300},
        attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': subtract})
    
    bezier_segment = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Resolution': main_branch_thickness.outputs["Crookedness Smooth [S] "], 'Start': (0.0000, 0.0000, -0.0400), 'Start Handle': (0.0000, 0.0000, 0.0000), 'End Handle': (0.0000, 0.0000, 0.0200), 'End': combine_xyz_1},
        attrs={'mode': 'OFFSET'})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    sample_nearest_surface = nw.new_node(Nodes.SampleNearestSurface,
        input_kwargs={'Mesh': reroute_3, 3: normal},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Vector': sample_nearest_surface.outputs[2]},
        attrs={'axis': 'Z'})
    
    subtract_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: main_branch_thickness.outputs["Randomize Scale Factor [S] "]},
        attrs={'operation': 'SUBTRACT'})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: subtract_1, 'Seed': main_branch_thickness.outputs["Random Scale Seed [S] "]})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: main_branch_thickness.outputs["Scale Factor [S] "], 1: random_value.outputs[1]},
        attrs={'operation': 'MULTIPLY'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': bezier_segment, 'Rotation': align_euler_to_vector, 'Scale': multiply_4})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branch_thickness.outputs["Growth Limiter [S] "]})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute_26, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh_3})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    index_1 = nw.new_node(Nodes.Index)
    
    sample_nearest = nw.new_node(Nodes.SampleNearest, input_kwargs={'Geometry': reroute_7})
    
    sample_index = nw.new_node(Nodes.SampleIndex, input_kwargs={'Geometry': reroute_7, 1: index_1, 'Index': sample_nearest})
    
    attribute_statistic = nw.new_node(Nodes.AttributeStatistic, input_kwargs={'Geometry': reroute_7, 2: index_1})
    
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: sample_index.outputs["Value"], 1: attribute_statistic.outputs["Max"]},
        attrs={'operation': 'DIVIDE'})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: divide_1}, attrs={'operation': 'SUBTRACT'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: subtract_2})
    
    float_curve_4 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': add})
    node_utils.assign_curve(float_curve_4.mapping.curves[0], [(0.0000, 1.0000), (0.2000, 1.0000), (0.8318, 0.9062), (0.9273, 0.6813), (0.9727, 0.0938), (1.0000, 0.0000)], handles=['AUTO', 'VECTOR', 'AUTO', 'AUTO', 'AUTO', 'AUTO'])
    
    scale_instances = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': reroute_27, 'Scale': float_curve_4})
    
    position = nw.new_node(Nodes.InputPosition)
    
    length = nw.new_node(Nodes.VectorMath, input_kwargs={0: position}, attrs={'operation': 'LENGTH'})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branch_thickness.outputs["Growth Threshold [S]"]})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: length.outputs["Value"], 1: reroute_10}, attrs={'operation': 'LESS_THAN'})
    
    delete_geometry_2 = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': scale_instances, 'Selection': less_than},
        attrs={'domain': 'INSTANCE'})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': delete_geometry_2})
    
    set_handle_type = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': realize_instances_1})
    
    endpoint_selection_2 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': main_branch_thickness.outputs["Z End Handle [S] "]})
    
    set_handle_positions = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_handle_type, 'Selection': endpoint_selection_2, 'Offset': combine_xyz_2})
    
    endpoint_selection_3 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branch_thickness.outputs["Z Start Handle [S] "]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_9})
    
    set_handle_positions_1 = nw.new_node(Nodes.SetHandlePositions,
        input_kwargs={'Curve': set_handle_positions, 'Selection': endpoint_selection_3, 'Offset': combine_xyz_3})
    
    subdivide_curve = nw.new_node(Nodes.SubdivideCurve,
        input_kwargs={'Curve': set_handle_positions_1, 'Cuts': main_branch_thickness.outputs["Curve Resolution [S] "]})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': main_branch_thickness.outputs["Curve Resolution [S] "]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0, 'End Size': reroute_19})
    
    divide_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: main_branch_thickness.outputs["Z Offset [S] "], 1: 50.0000},
        attrs={'operation': 'DIVIDE'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': divide_2})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve_2 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve_2.mapping.curves[0], [(0.0000, 0.0000), (0.4545, 0.1563), (1.0000, 1.0000)])
    
    multiply_5 = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz, 1: float_curve_2}, attrs={'operation': 'MULTIPLY'})
    
    spline_parameter_4 = nw.new_node(Nodes.SplineParameter)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': spline_parameter_4.outputs["Factor"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': 52.9605, 'Scale': 5.9900, 'Roughness': 0.0000},
        attrs={'noise_dimensions': '4D'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Vector': noise_texture.outputs["Color"], 9: (-1.0000, -1.0000, -1.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    multiply_6 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: colorramp.outputs["Color"], 1: map_range.outputs["Vector"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_7 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_6.outputs["Vector"], 1: (0.0100, 0.0100, 0.0100)},
        attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: multiply_5.outputs["Vector"], 1: multiply_7.outputs["Vector"]})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': subdivide_curve, 'Selection': endpoint_selection_1, 'Offset': add_1.outputs["Vector"]})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': float_curve_4})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    multiply_8 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_37, 1: main_branch_thickness.outputs["Grow [S] "]},
        attrs={'operation': 'MULTIPLY'})
    
    trim_curve_1 = nw.new_node(Nodes.TrimCurve, input_kwargs={'Curve': reroute_38, 3: multiply_8, 5: 0.0000})
    
    spline_parameter_2 = nw.new_node(Nodes.SplineParameter)
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': spline_parameter_2.outputs["Factor"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 1.2750), (0.0636, 1.1813), (0.2591, 0.6813), (0.5227, 0.5375), (0.8909, 0.4375), (0.9773, 0.2000)], handles=['AUTO', 'VECTOR', 'AUTO', 'AUTO', 'AUTO', 'AUTO'])
    
    multiply_9 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: 0.0100}, attrs={'operation': 'MULTIPLY'})
    
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_37, 1: multiply_9}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': trim_curve_1, 'Radius': multiply_10})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': main_branch_thickness.outputs["Profile Resolution [S] "], 'Radius': main_branch_thickness.outputs["Thickness [S] "]})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': curve_circle_1.outputs["Curve"], 'Fill Caps': True})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_34, curve_to_mesh_1]})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': surface.shaderfunc_to_material(shader_branch_base_001)})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': trim_curve_1})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': main_branch_thickness.outputs["Object"]})
    
    curve_tangent_2 = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector_2 = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent_2}, attrs={'axis': 'Z'})
    
    multiply_11 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: reroute_37, 1: main_branch_thickness.outputs["Scale Object"]},
        attrs={'operation': 'MULTIPLY'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': realize_instances_2, 'Selection': endpoint_selection, 'Instance': object_info.outputs["Geometry"], 'Rotation': align_euler_to_vector_2, 'Scale': multiply_11.outputs["Vector"]})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_1, instance_on_points_1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_2}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_bulb_stem, selection=selection)
    surface.add_material(obj, shader_branch_base, selection=selection)
apply(bpy.context.active_object)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_web(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    glass_bsdf = nw.new_node(Nodes.GlassBSDF, input_kwargs={'Roughness': 0.5231})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': glass_bsdf}, attrs={'is_active_output': True})

def shader_web_droplets(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    glass_bsdf = nw.new_node(Nodes.GlassBSDF, input_kwargs={'Roughness': 0.2974, 'IOR': 1.4000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': glass_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_3 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Num Rays', 5),
            ('NodeSocketInt', 'Num Circles', 10),
            ('NodeSocketFloatDistance', 'Size', 1.0000),
            ('NodeSocketFloat', 'Max Circle Dist', 1.0000),
            ('NodeSocketFloat', 'Noise Strength', 0.6000),
            ('NodeSocketFloat', 'Noise Scale', 0.6100),
            ('NodeSocketVector', 'Center', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Droplets Density', 40.0000),
            ('NodeSocketFloat', 'Droplets Max Size', 1.0000),
            ('NodeSocketFloat', 'Missing Points Chance', 0.0000),
            ('NodeSocketVector', 'Gravity Force Vector', (0.0000, 0.0000, 0.0000))])
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_3.outputs["Num Rays"], 'Radius': group_input_3.outputs["Size"]})
    
    curve_to_points = nw.new_node(Nodes.CurveToPoints,
        input_kwargs={'Curve': curve_circle.outputs["Curve"], 'Count': group_input_3.outputs["Num Rays"]})
    
    mesh_line = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': 2, 'Offset': (0.0000, 0.0000, 0.0000)},
        attrs={'mode': 'END_POINTS'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points.outputs["Points"], 'Instance': mesh_line})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points})
    
    id = nw.new_node(Nodes.InputID)
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: id, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={0: modulo}, attrs={'operation': 'EQUAL'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances, 'Selection': equal, 'Position': group_input_3.outputs["Center"]})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine,
        input_kwargs={'End': group_input_3.outputs["Center"], 'Direction': (0.0000, 0.0000, 0.0000), 'Length': 2.4000})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_3.outputs["Num Circles"]})
    
    curve_to_points_1 = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': curve_line_1, 'Count': reroute})
    
    integer_1 = nw.new_node(Nodes.Integer)
    integer_1.integer = 10
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Num Rays"], 1: integer_1},
        attrs={'operation': 'MULTIPLY'})
    
    mesh_circle = nw.new_node(Nodes.MeshCircle, input_kwargs={'Vertices': multiply, 'Radius': group_input_3.outputs["Size"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    normalize = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_1, 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'NORMALIZE'})
    
    distance = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_1}, attrs={'operation': 'DISTANCE'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normalize.outputs["Vector"], 1: distance.outputs["Value"]},
        attrs={'operation': 'MULTIPLY'})
    
    id_3 = nw.new_node(Nodes.InputID)
    
    modulo_1 = nw.new_node(Nodes.Math, input_kwargs={0: id_3, 1: integer_1}, attrs={'operation': 'MODULO'})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': modulo_1, 2: integer_1})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range_1.outputs["Result"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.2667), (0.3424, 0.1333), (0.4818, 0.1250), (0.6667, 0.1500), (1.0000, 0.2708)])
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve, 1: 0.3200}, attrs={'operation': 'MULTIPLY'})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_1.outputs["Vector"], 1: (0.5000, 0.5000, 0.5000), 'Scale': multiply_2},
        attrs={'operation': 'SCALE'})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_circle, 'Offset': scale.outputs["Vector"]})
    
    id_1 = nw.new_node(Nodes.InputID)
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.2200, 3: group_input_3.outputs["Max Circle Dist"], 'Seed': 3})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: group_input_3.outputs["Max Circle Dist"], 1: random_value_2.outputs[1]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': id_1, 2: reroute, 3: add, 4: 0.1000})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': curve_to_points_1.outputs["Points"], 'Instance': set_position_4, 'Scale': map_range.outputs["Result"]})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position, realize_instances_1]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry})
    
    random_value_3 = nw.new_node(Nodes.RandomValue)
    
    less_than = nw.new_node(Nodes.Compare,
        input_kwargs={0: random_value_3.outputs[1], 1: group_input_3.outputs["Missing Points Chance"]},
        attrs={'operation': 'LESS_THAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': reroute_2, 'Selection': less_than},
        attrs={'mode': 'EDGE_FACE'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': delete_geometry})
    
    mesh_to_curve_1 = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': reroute_3})
    
    subdivide_curve = nw.new_node(Nodes.SubdivideCurve, input_kwargs={'Curve': mesh_to_curve_1, 'Cuts': 4})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': group_input_3.outputs["Noise Scale"]})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: (0.5000, 0.5000, 0.5000), 'Scale': group_input_3.outputs["Noise Strength"]},
        attrs={'operation': 'SCALE'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': subdivide_curve, 'Offset': scale_1.outputs["Vector"]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    distance_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position, 1: group_input_3.outputs["Center"]},
        attrs={'operation': 'DISTANCE'})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: distance_1.outputs["Value"], 1: group_input_3.outputs["Size"]},
        attrs={'operation': 'DIVIDE'})
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': divide})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 1.0000), (0.6394, 0.7208), (1.0000, 0.0000)])
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: 1.6600}, attrs={'operation': 'POWER'})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: group_input_3.outputs["Gravity Force Vector"], 'Scale': power},
        attrs={'operation': 'SCALE'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_2, 'Offset': scale_2.outputs["Vector"]})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0400, 1: 100.0000}, attrs={'operation': 'DIVIDE'})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 12, 'Radius': divide_1})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_position_3, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_1, 'Material': surface.shaderfunc_to_material(shader_web)})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Droplets Density"], 1: 100.0000},
        attrs={'operation': 'MULTIPLY'})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_1, 'Density': multiply_3},
        attrs={'use_legacy_normal': True})
    
    ico_sphere = nw.new_node(Nodes.MeshIcoSphere, input_kwargs={'Subdivisions': 2})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': ico_sphere.outputs["Mesh"], 'Name': 'UVMap', 3: ico_sphere.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': store_named_attribute})
    
    divide_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Droplets Max Size"], 1: 100.0000},
        attrs={'operation': 'DIVIDE'})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.0010, 3: divide_2})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': set_shade_smooth, 'Scale': random_value.outputs[1]})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points_2, 'Material': surface.shaderfunc_to_material(shader_web_droplets)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_2, set_material_1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_1}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_web_droplets, selection=selection)
    surface.add_material(obj, shader_web, selection=selection)
apply(bpy.context.active_object)
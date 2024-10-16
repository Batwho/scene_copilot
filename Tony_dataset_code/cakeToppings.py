import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    object_info_2 = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Cakifier']},
        attrs={'transform_space': 'RELATIVE'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': object_info_2.outputs["Geometry"]})
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketBool', 'Selection', True)])
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Selection"]})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_2, 'Selection': reroute_1, 'Distance Min': 0.0200, 'Density Max': 300.0000, 'Density': 50.0000, 'Seed': 5},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['Raspberries'], 'Separate Children': True, 'Reset Children': True})
    
    random_value_4 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (89.1600, -0.6600, 0.0000), 1: (89.4100, 0.7600, 360.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    random_value_5 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.0090, 3: 0.0150})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Instance': collection_info, 'Pick Instance': True, 'Rotation': random_value_4.outputs["Value"], 'Scale': random_value_5.outputs[1]})
    
    translate_instances_2 = nw.new_node(Nodes.TranslateInstances,
        input_kwargs={'Instances': instance_on_points_2, 'Translation': (0.0000, 0.7300, 0.0000)})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_2, 'Selection': reroute_1, 'Distance Min': 0.0200, 'Density Max': 400.0000, 'Density': 50.0000, 'Seed': 7},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Cherry']})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.2500, 0.3800, 0.0000), 1: (0.3600, 0.2900, 360.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.0075, 3: 0.0095})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': object_info.outputs["Geometry"], 'Rotation': random_value_1.outputs["Value"], 'Scale': random_value.outputs[1]})
    
    translate_instances = nw.new_node(Nodes.TranslateInstances,
        input_kwargs={'Instances': instance_on_points, 'Translation': (0.0000, 0.0000, -0.1100)})
    
    distribute_points_on_faces_2 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_2, 'Selection': reroute_1, 'Distance Min': 0.0200, 'Density Max': 400.0000, 'Density': 50.0000, 'Seed': 3},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Blueberry']})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.2500, 0.3800, 0.0000), 1: (0.3600, 0.2900, 360.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    random_value_3 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.0050, 3: 0.0070})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_2.outputs["Points"], 'Instance': object_info_1.outputs["Geometry"], 'Rotation': random_value_2.outputs["Value"], 'Scale': random_value_3.outputs[1]})
    
    translate_instances_1 = nw.new_node(Nodes.TranslateInstances,
        input_kwargs={'Instances': instance_on_points_1, 'Translation': (0.0000, 0.0000, -0.1800)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [translate_instances_2, translate_instances, translate_instances_1]})
    
    scale_instances = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': join_geometry, 'Scale': (1.1000, 1.1000, 1.1000)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': scale_instances}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
apply(bpy.context.active_object)
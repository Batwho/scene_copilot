import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_ground(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.1687, 0.1093, 0.0993, 1.0000), 'Roughness': 0.8000},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_pebbles(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatFactor', 'Large Pebbles Mask', 1.0000),
            ('NodeSocketFloat', 'Factor', 5.0000),
            ('NodeSocketFloat', 'Medium Pebbles Mask', 10.0000),
            ('NodeSocketFloat', 'Factor_1', 8.0000),
            ('NodeSocketFloat', 'Small Pebbles Mask', 10.0000),
            ('NodeSocketFloat', 'Factor_2', 10.0000)])
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Factor"], 1: 100.0000, 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': group_input_1.outputs["Geometry"], 'Distance Min': 0.0200, 'Density Max': multiply, 'Density Factor': group_input_1.outputs["Large Pebbles Mask"]},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['GEO-pebble'], 'As Instance': True})
    
    random_rotation = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-3.1416, -3.1416, -3.1416), 1: (3.1416, 3.1416, 3.1416), 2: 0.2500, 3: 0.6000},
        label='Random Rotation',
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.2500, 3: 0.6000})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': object_info.outputs["Geometry"], 'Rotation': random_rotation.outputs["Value"], 'Scale': random_value.outputs[1]})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Medium Pebbles Mask"], 1: 100.0000, 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_1, 1: group_input_1.outputs["Factor_1"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': group_input_1.outputs["Geometry"], 'Distance Min': 0.0200, 'Density': multiply_2},
        attrs={'use_legacy_normal': True})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['GEO-pebble.004'], 'As Instance': True})
    
    random_rotation_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-3.1416, -3.1416, -3.1416), 1: (3.1416, 3.1416, 3.1416), 2: 0.2500, 3: 0.6000},
        label='Random Rotation',
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.2500, 3: 0.4500})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Instance': object_info_1.outputs["Geometry"], 'Rotation': random_rotation_1.outputs["Value"], 'Scale': random_value_2.outputs[1]})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Factor_2"], 1: 100.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_1.outputs["Small Pebbles Mask"], 1: multiply_3},
        attrs={'operation': 'MULTIPLY'})
    
    distribute_points_on_faces_2 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': group_input_1.outputs["Geometry"], 'Distance Min': 0.0200, 'Density': multiply_4},
        attrs={'use_legacy_normal': True})
    
    object_info_2 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['GEO-pebble.002'], 'As Instance': True})
    
    random_rotation_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-3.1416, -3.1416, -3.1416), 1: (3.1416, 3.1416, 3.1416), 2: 0.2500, 3: 0.6000},
        label='Random Rotation',
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    random_value_3 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.1000, 3: 0.3500, 'Seed': 2})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_2.outputs["Points"], 'Instance': object_info_2.outputs["Geometry"], 'Rotation': random_rotation_2.outputs["Value"], 'Scale': random_value_3.outputs[1]})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [instance_on_points, instance_on_points_1, instance_on_points_2, group_input_1.outputs["Geometry"]]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_3}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_pebbles, selection=selection, attributes=[])
    surface.add_material(obj, shader_ground, selection=selection)
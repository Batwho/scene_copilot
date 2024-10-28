import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_pine_cone_pedal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0607, 0.0158, 0.0000, 1.0000), 'Roughness': 0.8373})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_black(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0174, 0.0094, 0.0060, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0805, 0.0180, 0.0009, 1.0000), 'Specular': 0.3409, 'Roughness': 0.7217})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': group_input_1.outputs["Geometry"], 'Density Max': 615.4000, 'Density': 130.0000, 'Seed': 32},
        attrs={'use_legacy_normal': True})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['Pedal'], 'Separate Children': True, 'Reset Children': True},
        attrs={'transform_space': 'RELATIVE'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': collection_info, 'Offset': (-1.7000, 0.3000, -0.2000)})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (1.0000, 0.5000, 1.0000), 1: (1.0000, 0.8000, 1.0000), 2: 0.6000, 3: 1.5000})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: random_value.outputs[1], 1: 0.8000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: random_value.outputs[1], 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply, 'Y': random_value.outputs[1], 'Z': multiply_1})
    
    scale_instances = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': set_position, 'Scale': combine_xyz})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': scale_instances, 'Rotation': (0.4032, 0.1257, 0.8657), 'Scale': (1.0000, 0.6000, 1.0000)})
    
    add = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: distribute_points_on_faces.outputs["Rotation"], 1: (0.5000, 6.3000, -0.5000)})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': transform, 'Rotation': add.outputs["Vector"], 'Scale': (0.5000, 0.5000, 0.5000)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [group_input_1.outputs["Geometry"], instance_on_points]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': surface.shaderfunc_to_material(shader_pine_cone_pedal)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material, selection=selection)
    surface.add_material(obj, shader_black, selection=selection)
apply(bpy.context.active_object)
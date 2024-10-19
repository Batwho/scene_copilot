import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_droplets(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    glass_bsdf = nw.new_node(Nodes.GlassBSDF, input_kwargs={'Roughness': 0.0500, 'IOR': 1.3330})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': glass_bsdf}, attrs={'is_active_output': True})

def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF)
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Size', 0.1000),
            ('NodeSocketInt', 'Density', 100),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketInt', 'Subdivisions', 2)])
    
    face_area = nw.new_node(Nodes.InputMeshFaceArea)
    
    attribute_statistic = nw.new_node(Nodes.AttributeStatistic,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 2: face_area},
        attrs={'domain': 'FACE'})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Density"], 1: attribute_statistic.outputs["Sum"]},
        attrs={'operation': 'DIVIDE'})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': group_input.outputs["Geometry"], 'Distance Min': group_input.outputs["Size"], 'Density Max': divide, 'Seed': group_input.outputs["Seed"]},
        attrs={'use_legacy_normal': True, 'distribute_method': 'POISSON'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Size"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    ico_sphere = nw.new_node(Nodes.MeshIcoSphere,
        input_kwargs={'Radius': divide_1, 'Subdivisions': group_input.outputs["Subdivisions"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': ico_sphere.outputs["Mesh"], 'Name': 'UVMap', 3: ico_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.6000, 3: 1.2000, 'Seed': group_input.outputs["Seed"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': store_named_attribute, 'Rotation': distribute_points_on_faces.outputs["Rotation"], 'Scale': random_value.outputs[1]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': instance_on_points})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_droplets)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, group_input.outputs["Geometry"]]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material, selection=selection)
apply(bpy.context.active_object)
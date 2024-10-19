import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_quartz(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'cracks'})
    
    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': object_info.outputs["Color"]})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Saturation': 0.4400, 'Color': reroute})
    
    attribute_3 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'cracks'})
    
    mix_1 = nw.new_node(Nodes.Mix, input_kwargs={0: attribute_3.outputs["Fac"], 2: 0.0500, 3: 0.2000})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 2.3000, 'Detail': 15.0000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': mix_1.outputs["Result"], 'Height': noise_texture.outputs["Fac"]})
    
    glass_bsdf_3 = nw.new_node(Nodes.GlassBSDF,
        input_kwargs={'Color': hue_saturation_value, 'Roughness': 0.1481, 'IOR': 1.4800, 'Normal': bump})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': glass_bsdf_3})
    
    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'cracks edges'})
    
    color_ramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute_1.outputs["Fac"]})
    color_ramp.color_ramp.elements[0].position = 0.1673
    color_ramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp.color_ramp.elements[1].position = 0.9855
    color_ramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    transparent_bsdf = nw.new_node(Nodes.TransparentBSDF)
    
    mix_shader_1 = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': color_ramp.outputs["Color"], 1: reroute_1, 2: transparent_bsdf})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': attribute.outputs["Fac"], 1: reroute_1, 2: mix_shader_1})
    
    principled_volume_1 = nw.new_node(Nodes.PrincipledVolume, input_kwargs={'Color': reroute})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': mix_shader, 'Volume': principled_volume_1},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_7 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Cracks Resolutions', 3),
            ('NodeSocketFloat', 'Cracks Thickness', 1.0000),
            ('NodeSocketInt', 'Cracks Number', 0),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketMaterial', 'Material', None)])
    
    mesh_line = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': group_input_7.outputs["Cracks Number"], 'Offset': (0.0000, 0.0000, 0.0000)})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': group_input_7.outputs["Geometry"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': bounding_box.outputs["Min"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': bounding_box.outputs["Max"]})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: reroute_6, 1: reroute_7, 'Seed': group_input_7.outputs["Seed"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_line, 'Position': random_value_1.outputs["Value"]})
    
    distance = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_6, 1: reroute_7}, attrs={'operation': 'DISTANCE'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: distance.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Cracks Resolutions"]})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': reroute_5, 'Size Y': reroute_5, 'Vertices X': reroute_4, 'Vertices Y': reroute_4})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    store_named_attribute_4 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'cracks UV', 3: position_3},
        attrs={'data_type': 'FLOAT2'})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-3.1416, -3.1416, -3.1416), 1: (3.1416, 3.1416, 3.1416), 'Seed': group_input_7.outputs["Seed"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_2, 'Instance': store_named_attribute_4, 'Rotation': random_value.outputs["Value"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Geometry"]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    sample_nearest_surface_1 = nw.new_node(Nodes.SampleNearestSurface,
        input_kwargs={'Mesh': reroute_3, 3: position},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_1, 1: sample_nearest_surface_1.outputs[2]},
        attrs={'operation': 'SUBTRACT'})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    sample_nearest_surface = nw.new_node(Nodes.SampleNearestSurface,
        input_kwargs={'Mesh': reroute_3, 3: normal},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    dot_product = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: sample_nearest_surface.outputs[2]},
        attrs={'operation': 'DOT_PRODUCT'})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: dot_product.outputs["Value"]})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': realize_instances, 'Selection': greater_than})
    
    vertex_neighbors = nw.new_node(Nodes.VertexNeighbors)
    
    less_than = nw.new_node(Nodes.Compare,
        input_kwargs={2: vertex_neighbors.outputs["Face Count"], 3: 4},
        attrs={'operation': 'LESS_THAN', 'data_type': 'INT'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': less_than})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': delete_geometry, 'Name': 'cracks edges', 6: reroute_2},
        attrs={'data_type': 'BOOLEAN'})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    sample_nearest_surface_2 = nw.new_node(Nodes.SampleNearestSurface,
        input_kwargs={'Mesh': group_input_7.outputs["Geometry"], 3: position_2},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute, 'Selection': reroute_2, 'Position': sample_nearest_surface_2.outputs[2]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': reroute})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Cracks Thickness"]})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': reroute, 'Offset Scale': reroute_1, 'Individual': False})
    
    store_named_attribute_3 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Name': 'cracks edges', 6: extrude_mesh.outputs["Side"]},
        attrs={'data_type': 'BOOLEAN'})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces, store_named_attribute_3]})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_1, 'Distance': divide_1})
    
    flip_faces_1 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': merge_by_distance})
    
    named_attribute = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'cracks edges'}, attrs={'data_type': 'BOOLEAN'})
    
    blur_attribute = nw.new_node(Nodes.BlurAttribute, input_kwargs={0: named_attribute.outputs[3], 'Iterations': 6})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': flip_faces_1, 'Name': 'cracks edges', 4: blur_attribute.outputs["Value"], 6: True})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': store_named_attribute_2, 'Name': 'cracks', 6: True},
        attrs={'data_type': 'BOOLEAN'})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': store_named_attribute_1})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_shade_smooth, group_input_7.outputs["Geometry"]]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry, 'Material': group_input_7.outputs["Material"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_quartz, selection=selection)
apply(bpy.context.active_object)
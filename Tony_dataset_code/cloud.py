import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_cloud_base_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    distance = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: texture_coordinate.outputs["Generated"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'DISTANCE'})
    
    do_not_adjust = nw.new_node(Nodes.Value, label='do not adjust')
    do_not_adjust.outputs[0].default_value = 0.5000
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: distance.outputs["Value"], 1: do_not_adjust},
        attrs={'operation': 'MULTIPLY'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': multiply})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.5273
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: colorramp_1.outputs["Color"], 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: distance.outputs["Value"], 1: multiply_1})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: do_not_adjust}, attrs={'operation': 'LESS_THAN'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': less_than, 4: 0.5400})
    
    cloud_pore_scale = nw.new_node(Nodes.Value, label='cloud pore scale')
    cloud_pore_scale.outputs[0].default_value = 5.0000
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Scale': cloud_pore_scale, 'Detail': 0.5000})
    
    cloud_porousness = nw.new_node(Nodes.Value, label='cloud porousness')
    cloud_porousness.outputs[0].default_value = 0.4000
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: noise_texture.outputs["Color"], 1: cloud_porousness},
        attrs={'operation': 'GREATER_THAN'})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: do_not_adjust, 1: distance.outputs["Value"]},
        attrs={'operation': 'SUBTRACT'})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': subtract})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: map_range.outputs["Result"], 6: greater_than, 7: map_range_1.outputs["Result"]},
        attrs={'blend_type': 'LINEAR_LIGHT', 'data_type': 'RGBA'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix.outputs[2]})
    colorramp.color_ramp.elements[0].position = 0.4531
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.6061
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"], 1: 10.0000}, attrs={'operation': 'MULTIPLY'})
    
    principled_volume = nw.new_node(Nodes.PrincipledVolume,
        input_kwargs={'Color': (1.0000, 1.0000, 1.0000, 1.0000), 'Density': multiply_2})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Volume': principled_volume}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'X Resolution', 10),
            ('NodeSocketInt', 'Y Resolution', 10),
            ('NodeSocketInt', 'Z Resolution', 10),
            ('NodeSocketVectorTranslation', 'X Offset', (5.0000, 0.0000, 0.0000)),
            ('NodeSocketVectorTranslation', 'Y Offset', (0.0000, 5.0000, 0.0000)),
            ('NodeSocketVectorTranslation', 'Z Offset', (0.0000, 0.0000, 5.0000)),
            ('NodeSocketFloat', 'Min Cloud Size', 0.0000),
            ('NodeSocketFloat', 'Max Cloud Size', 1.0000),
            ('NodeSocketInt', 'Cloud Size Seed', 0),
            ('NodeSocketFloat', 'Cloud Deletion Lower Threshold', 0.0000),
            ('NodeSocketFloat', 'Cloud Deletion Upper Threshold', 1.0000),
            ('NodeSocketInt', 'Cloud Deletion Threshold Seed', 1),
            ('NodeSocketFloat', 'Cloud Min Rotation', 0.0000),
            ('NodeSocketFloat', 'Cloud Max Rotation', 360.0000),
            ('NodeSocketInt', 'Cloud Rotation Seed', 2),
            ('NodeSocketFloat', 'Upper Height Distribution', 1.0000),
            ('NodeSocketFloat', 'Cloud Noise Scale', 10.0000),
            ('NodeSocketFloat', 'Cloud Noise Threshold', 0.5000),
            ('NodeSocketInt', 'Cloud Subdivision Level Viewport', 2),
            ('NodeSocketInt', 'Cloud Subdivision Level Render', 3)])
    
    mesh_line = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': group_input.outputs["X Resolution"], 'Offset': group_input.outputs["X Offset"]})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': mesh_line})
    
    mesh_line_1 = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': group_input.outputs["Y Resolution"], 'Offset': group_input.outputs["Y Offset"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_to_points, 'Instance': mesh_line_1})
    
    mesh_line_2 = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': group_input.outputs["Z Resolution"], 'Offset': group_input.outputs["Z Offset"]})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': instance_on_points, 'Instance': mesh_line_2})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1}, attrs={'legacy_behavior': True})
    
    mesh_to_points_1 = nw.new_node(Nodes.MeshToPoints, input_kwargs={'Mesh': realize_instances})
    
    is_viewport = nw.new_node(Nodes.IsViewport)
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: is_viewport, 6: group_input.outputs["Cloud Subdivision Level Render"], 7: group_input.outputs["Cloud Subdivision Level Viewport"]},
        attrs={'data_type': 'RGBA'})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': group_input.outputs["Geometry"], 'Level': mix.outputs[2]})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': mesh_to_points_1, 'Instance': subdivision_surface})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input.outputs["Min Cloud Size"], 3: group_input.outputs["Max Cloud Size"], 'Seed': group_input.outputs["Cloud Size Seed"]})
    
    scale_instances = nw.new_node(Nodes.ScaleInstances,
        input_kwargs={'Instances': instance_on_points_2, 'Scale': random_value.outputs[1]})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input.outputs["Cloud Deletion Lower Threshold"], 3: group_input.outputs["Cloud Deletion Upper Threshold"], 5: 1, 'Seed': group_input.outputs["Cloud Deletion Threshold Seed"]})
    
    round = nw.new_node(Nodes.Math, input_kwargs={0: random_value_1.outputs[1]}, attrs={'operation': 'ROUND'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Z Offset"], 1: group_input.outputs["Z Resolution"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply, 1: group_input.outputs["Upper Height Distribution"]},
        attrs={'operation': 'MULTIPLY'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz.outputs["Z"], 2: multiply_1, 3: 1.0000, 4: 0.0000})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"]}, attrs={'operation': 'LESS_THAN'})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': less_than, 1: 1.0000, 2: 0.0000})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_1.outputs["Result"], 1: map_range.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: round, 1: multiply_2}, attrs={'operation': 'MULTIPLY'})
    
    scale_instances_1 = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': scale_instances, 'Scale': multiply_3})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': group_input.outputs["Cloud Noise Scale"]})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': group_input.outputs["Cloud Noise Threshold"], 3: 1.0000, 4: 0.0000})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: noise_texture.outputs["Color"], 1: map_range_2.outputs["Result"]},
        attrs={'operation': 'GREATER_THAN'})
    
    scale_instances_2 = nw.new_node(Nodes.ScaleInstances, input_kwargs={'Instances': scale_instances_1, 'Scale': greater_than})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input.outputs["Cloud Min Rotation"], 3: group_input.outputs["Cloud Max Rotation"], 5: 1, 'Seed': group_input.outputs["Cloud Rotation Seed"]})
    
    multiply_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: random_value_2.outputs[1], 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': scale_instances_2, 'Rotation': multiply_4.outputs["Vector"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': rotate_instances, 'Material': surface.shaderfunc_to_material(shader_cloud_base_material)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_cloud_base_material, selection=selection)
apply(bpy.context.active_object)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_node_group', singleton=False, type='ShaderNodeTree')
def nodegroup_node_group(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    geometry = nw.new_node(Nodes.NewGeometry)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': geometry.outputs["Random Per Island"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketColor', 'Color 1', (0.1022, 0.0319, 0.0185, 1.0000)),
            ('NodeSocketColor', 'Color 2', (0.1559, 0.0762, 0.0545, 1.0000)),
            ('NodeSocketFloat', 'Scale', 1.0000)])
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp.outputs["Color"], 6: group_input.outputs["Color 1"], 7: group_input.outputs["Color 2"]},
        attrs={'data_type': 'RGBA'})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': group_input.outputs["Scale"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 1.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0200, 0.0200, 0.0200, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.5000
    colorramp_1.color_ramp.elements[1].color = [0.9500, 0.9500, 0.9500, 1.0000]
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': 30.0000, 'Detail': 15.0000, 'Roughness': 0.7000})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.5000
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Height': colorramp_2.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Roughness': colorramp_1.outputs["Color"], 'Normal': bump})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'BSDF': principled_bsdf}, attrs={'is_active_output': True})

def shader_brick_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group = nw.new_node(nodegroup_node_group().name)
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': group}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_3 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Horizontal Count', 20),
            ('NodeSocketInt', 'Vertical Count', 30),
            ('NodeSocketFloat', 'Brick Width', 0.2400),
            ('NodeSocketFloat', 'Brick Depth', 0.1200),
            ('NodeSocketFloat', 'Brick Height', 0.0600),
            ('NodeSocketFloat', 'Gap Size', 0.0150),
            ('NodeSocketFloat', 'Displacement', 1.0000),
            ('NodeSocketFloat', 'Seed', 0.0000),
            ('NodeSocketMaterial', 'Material', None)])
    
    add = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Brick Width"], 1: group_input_3.outputs["Gap Size"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: add, 1: group_input_3.outputs["Horizontal Count"]},
        attrs={'operation': 'MULTIPLY'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: 4.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: divide}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract})
    
    add_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Brick Height"], 1: group_input_3.outputs["Gap Size"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_1})
    
    mesh_line_2 = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': group_input_3.outputs["Vertical Count"], 'Start Location': combine_xyz_5, 'Offset': combine_xyz_4})
    
    index_1 = nw.new_node(Nodes.Index)
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: index_1, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_1})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': mesh_line_2, 'Selection': modulo, 'Offset': combine_xyz_6})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'W': group_input_3.outputs["Seed"]}, attrs={'noise_dimensions': '4D'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Fac"]}, attrs={'operation': 'SUBTRACT'})
    
    minimum = nw.new_node(Nodes.Math, input_kwargs={0: subtract_1, 1: 0.0000}, attrs={'operation': 'MINIMUM'})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Displacement"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: minimum, 1: multiply_2}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_3})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_1, 'Offset': combine_xyz_8})
    
    subtract_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Brick Width"], 1: group_input_3.outputs["Gap Size"]},
        attrs={'operation': 'SUBTRACT'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_2, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': divide_1, 'Y': group_input_3.outputs["Brick Depth"], 'Z': group_input_3.outputs["Brick Height"]})
    
    cube_1 = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz_7})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_1.outputs["Mesh"], 'Name': 'uv_map', 3: cube_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': set_position_3, 'Instance': store_named_attribute})
    
    add_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Brick Height"], 1: group_input_3.outputs["Gap Size"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_2})
    
    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': group_input_3.outputs["Vertical Count"], 'Offset': combine_xyz})
    
    index = nw.new_node(Nodes.Index)
    
    modulo_1 = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    add_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Brick Width"], 1: group_input_3.outputs["Gap Size"]})
    
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: add_3, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide_2})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': mesh_line, 'Selection': modulo_1, 'Offset': combine_xyz_1})
    
    add_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Brick Width"], 1: group_input_3.outputs["Gap Size"]})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_4})
    
    mesh_line_1 = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': group_input_3.outputs["Horizontal Count"], 'Offset': combine_xyz_2})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': set_position, 'Instance': mesh_line_1})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': realize_instances, 'Offset': combine_xyz_8})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input_3.outputs["Brick Width"], 'Y': group_input_3.outputs["Brick Depth"], 'Z': group_input_3.outputs["Brick Height"]})
    
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz_3})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': set_position_2, 'Instance': store_named_attribute_1})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [instance_on_points_2, instance_on_points_1]})
    
    add_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Brick Width"], 1: group_input_3.outputs["Gap Size"]})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: add_5, 1: group_input_3.outputs["Horizontal Count"]},
        attrs={'operation': 'MULTIPLY'})
    
    divide_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_4, 1: -2.0000}, attrs={'operation': 'DIVIDE'})
    
    divide_4 = nw.new_node(Nodes.Math, input_kwargs={0: add_5, 1: 4.0000}, attrs={'operation': 'DIVIDE'})
    
    add_6 = nw.new_node(Nodes.Math, input_kwargs={0: divide_3, 1: divide_4})
    
    divide_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Brick Height"], 1: 2.0000},
        attrs={'operation': 'DIVIDE'})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_6, 'Z': divide_5})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': join_geometry, 'Offset': combine_xyz_9})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': set_position_4})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': realize_instances_1, 'Material': group_input_3.outputs["Material"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_brick_material, selection=selection)
apply(bpy.context.active_object)
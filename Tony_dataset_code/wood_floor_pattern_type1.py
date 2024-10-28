import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_square_basket_parquet', singleton=False, type='GeometryNodeTree')
def nodegroup_square_basket_parquet(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Tile Size', 0.4000),
            ('NodeSocketInt', 'Count Per Tile', 4),
            ('NodeSocketFloat', 'Board Depth', 0.0100),
            ('NodeSocketFloat', 'Bevel Depth', 0.0100),
            ('NodeSocketFloat', 'Bevel Length', 0.9700),
            ('NodeSocketFloat', 'Bevel Width', 0.8800),
            ('NodeSocketInt', 'Tiles X', 5),
            ('NodeSocketInt', 'Tiles Y', 5)])
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tile Size"]})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tiles X"]})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_20, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_24, 1: subtract}, attrs={'operation': 'MULTIPLY'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tiles Y"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_19, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_24, 1: subtract_1}, attrs={'operation': 'MULTIPLY'})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': multiply, 'Size Y': multiply_1, 'Vertices X': reroute_29, 'Vertices Y': reroute_28})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tile Size"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Count Per Tile"]})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: reroute_16}, attrs={'operation': 'DIVIDE'})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_16, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: subtract_2}, attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: -0.5000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_3})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute_1})
    
    curve_line = nw.new_node(Nodes.CurveLine,
        input_kwargs={'Start': combine_xyz_1, 'Direction': (0.0000, 1.0000, 0.0000), 'Length': multiply_2},
        attrs={'mode': 'DIRECTION'})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Count Per Tile"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': reroute_14})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Tile Size"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Count Per Tile"]})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_15, 1: reroute_3}, attrs={'operation': 'DIVIDE'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Board Depth"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_5, 'Y': divide_1, 'Z': reroute_2})
    
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    index = nw.new_node(Nodes.Index)
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: index, 3: 2}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bevel Depth"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': store_named_attribute, 'Selection': equal, 'Offset Scale': reroute_6, 'Individual': False})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bevel Length"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': reroute_11},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bevel Width"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements, 'Selection': extrude_mesh.outputs["Top"], 'Scale': reroute_10, 'Axis': (0.0000, 1.0000, 0.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': resample_curve, 'Instance': scale_elements_1})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points})
    
    index_1 = nw.new_node(Nodes.Index)
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: index_1, 1: reroute_19}, attrs={'operation': 'MODULO'})
    
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: index_1, 1: reroute_19}, attrs={'operation': 'DIVIDE'})
    
    float_to_integer = nw.new_node(Nodes.FloatToInt, input_kwargs={'Float': divide_2}, attrs={'rounding_mode': 'TRUNCATE'})
    
    modulo_1 = nw.new_node(Nodes.Math, input_kwargs={0: float_to_integer, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: modulo, 1: modulo_1})
    
    modulo_2 = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={0: modulo_2, 'Epsilon': 0.0000}, attrs={'operation': 'EQUAL'})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={0: equal_1, 9: (0.0000, 0.0000, 1.5708)}, attrs={'input_type': 'VECTOR'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': store_named_attribute_1, 'Instance': reroute_25, 'Rotation': switch.outputs[3]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Mesh': instance_on_points_1}, attrs={'is_active_output': True})

def shader_material_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': object_info.outputs["Random"], 3: 0.3400})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"], 1: 8.8000}, attrs={'operation': 'MULTIPLY'})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Scale': multiply, 'Distortion': 3.6000},
        attrs={'wave_profile': 'SAW', 'wave_type': 'RINGS'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': wave_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.1730, 0.0281, 0.0110, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.5022, 0.1560, 0.0911, 1.0000]
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Value': object_info.outputs["Random"], 'Color': colorramp.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': hue_saturation_value})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    squarebasket_parquet = nw.new_node(nodegroup_square_basket_parquet().name, input_kwargs={'Tiles X': 7, 'Tiles Y': 7})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': squarebasket_parquet, 'Material': surface.shaderfunc_to_material(shader_material_001)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material_001, selection=selection)
apply(bpy.context.active_object)
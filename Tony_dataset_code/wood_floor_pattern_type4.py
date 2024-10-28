import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_horizontal_strip_flooring', singleton=False, type='GeometryNodeTree')
def nodegroup_horizontal_strip_flooring(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatDistance', 'Plank Width', 0.1000),
            ('NodeSocketFloatDistance', 'Plank Length', 1.2192),
            ('NodeSocketFloat', 'Plank Depth', 0.0100),
            ('NodeSocketInt', 'Columns', 5),
            ('NodeSocketInt', 'Rows', 3),
            ('NodeSocketFloat', 'Bevel Depth', 0.0050),
            ('NodeSocketFloat', 'Bevel on Length', 0.9800),
            ('NodeSocketFloat', 'Bevel on Width', 0.9800),
            ('NodeSocketFloat', 'Major Offset', 0.5000),
            ('NodeSocketFloat', 'Offset Random Factor', 0.0000),
            ('NodeSocketInt', 'Offset Seed', 0)])
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Plank Width"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Columns"], 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_4, 1: subtract}, attrs={'operation': 'MULTIPLY'})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Plank Length"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Rows"], 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: subtract_1}, attrs={'operation': 'MULTIPLY'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Columns"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rows"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': multiply, 'Size Y': multiply_1, 'Vertices X': reroute_1, 'Vertices Y': reroute})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    index_1 = nw.new_node(Nodes.Index)
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: index_1, 1: reroute}, attrs={'operation': 'DIVIDE'})
    
    float_to_integer = nw.new_node(Nodes.FloatToInt, input_kwargs={'Float': divide}, attrs={'rounding_mode': 'FLOOR'})
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: float_to_integer, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Offset Random Factor"]})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Offset Seed"]})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: reroute_22, 3: 0.0000, 'ID': float_to_integer, 'Seed': reroute_14})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: random_value.outputs[1], 1: reroute_25}, attrs={'operation': 'MULTIPLY'})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Major Offset"]})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_23, 1: reroute_25}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: multiply_3})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': add})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute, 'Selection': modulo, 'Offset': combine_xyz_1})
    
    index_2 = nw.new_node(Nodes.Index)
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: index_2, 1: reroute}, attrs={'operation': 'DIVIDE'})
    
    float_to_integer_1 = nw.new_node(Nodes.FloatToInt, input_kwargs={'Float': divide_1}, attrs={'rounding_mode': 'FLOOR'})
    
    modulo_1 = nw.new_node(Nodes.Math, input_kwargs={0: float_to_integer_1, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    op_not = nw.new_node(Nodes.BooleanMath, input_kwargs={0: modulo_1}, attrs={'operation': 'NOT'})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: reroute_24, 3: 0.0000, 'ID': float_to_integer_1, 'Seed': reroute_14})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_29})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: random_value_1.outputs[1], 1: reroute_27}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_4})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position, 'Selection': op_not, 'Offset': combine_xyz_2})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Plank Width"], 'Y': group_input.outputs["Plank Length"], 'Z': group_input.outputs["Plank Depth"]})
    
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    index = nw.new_node(Nodes.Index)
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: index, 3: 2}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bevel Depth"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': store_named_attribute_1, 'Selection': equal, 'Offset Scale': reroute_15, 'Individual': False})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bevel on Length"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': reroute_13},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': extrude_mesh.outputs["Top"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bevel on Width"]})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements, 'Selection': reroute_6, 'Scale': reroute_12, 'Axis': (0.0000, 1.0000, 0.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': set_position_2, 'Instance': scale_elements_1})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Mesh': instance_on_points}, attrs={'is_active_output': True})

def shader_material_003(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Rotation': (0.0000, 0.0000, -0.9425)},
        attrs={'vector_type': 'TEXTURE'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': object_info.outputs["Random"], 3: 0.3400})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"], 1: 8.8000}, attrs={'operation': 'MULTIPLY'})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': mapping, 'Scale': multiply, 'Distortion': 3.6000},
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

    horizontal_strip_flooring = nw.new_node(nodegroup_horizontal_strip_flooring().name, input_kwargs={'Columns': 46})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': horizontal_strip_flooring, 'Material': surface.shaderfunc_to_material(shader_material_003)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material_003, selection=selection)
apply(bpy.context.active_object)
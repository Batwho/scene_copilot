import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_node_group', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Plank Width', 0.0000),
            ('NodeSocketFloat', 'Plank Length', 0.0000),
            ('NodeSocketFloat', 'Plank Height', 0.0700),
            ('NodeSocketFloat', 'Bevel Width', 0.9000),
            ('NodeSocketFloat', 'Bevel Length', 0.9800),
            ('NodeSocketFloat', 'Bevel Height', 0.0600)])
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Plank Width"], 'Y': group_input.outputs["Plank Length"], 'Z': group_input.outputs["Plank Height"]})
    
    cube_1 = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': combine_xyz_1})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_1.outputs["Mesh"], 'Name': 'uv_map', 3: cube_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    index = nw.new_node(Nodes.Index)
    
    equal = nw.new_node(Nodes.Compare, input_kwargs={2: index, 3: 2}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': store_named_attribute, 'Selection': equal, 'Offset Scale': group_input.outputs["Bevel Height"]})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': group_input.outputs["Bevel Width"]},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements, 'Selection': extrude_mesh.outputs["Top"], 'Scale': group_input.outputs["Bevel Length"], 'Axis': (0.0000, 1.0000, 0.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Plank Length"], 1: -2.0000},
        attrs={'operation': 'DIVIDE'})
    
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Plank Width"], 1: 2.0000},
        attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: divide_1})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': add})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': scale_elements_1, 'Translation': combine_xyz_2})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_herringbone_parquet', singleton=False, type='GeometryNodeTree')
def nodegroup_herringbone_parquet(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Columns (Pairs)', 2),
            ('NodeSocketInt', 'Rows', 20),
            ('NodeSocketFloat', 'Plank Width', 0.0750),
            ('NodeSocketFloat', 'Plank Length', 1.3200),
            ('NodeSocketFloat', 'Plank Depth', 0.0100),
            ('NodeSocketFloat', 'Bevel on Width', 0.9950),
            ('NodeSocketFloat', 'Bevel on Length', 0.9800),
            ('NodeSocketFloat', 'Bevel Depth', 0.0100)])
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Columns (Pairs)"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Plank Length"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_13, 1: 1.4140}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: multiply}, attrs={'operation': 'MULTIPLY'})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rows"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_17, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Plank Width"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_1, 1: reroute_19}, attrs={'operation': 'MULTIPLY'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: 1.4140}, attrs={'operation': 'MULTIPLY'})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    grid_2 = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': multiply_1, 'Size Y': multiply_3, 'Vertices X': reroute_1, 'Vertices Y': reroute_18})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid_2.outputs["Mesh"], 'Name': 'uv_map', 3: grid_2.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: reroute_6}, attrs={'operation': 'MULTIPLY'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: multiply_4, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    sqrt = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000}, attrs={'operation': 'SQRT'})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: sqrt, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_5, 'Y': multiply_5})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Translation': combine_xyz})
    
    nodegroup = nw.new_node(nodegroup_node_group().name,
        input_kwargs={'Plank Width': reroute_15, 'Plank Length': reroute_13, 'Plank Height': group_input.outputs["Plank Depth"], 'Bevel Width': group_input.outputs["Bevel on Width"], 'Bevel Length': group_input.outputs["Bevel on Length"], 'Bevel Height': group_input.outputs["Bevel Depth"]})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': transform, 'Instance': nodegroup, 'Rotation': (0.0000, 0.0000, -0.7854)})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_14, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_11, 1: 1.4140}, attrs={'operation': 'MULTIPLY'})
    
    multiply_7 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_2, 1: multiply_6}, attrs={'operation': 'MULTIPLY'})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    subtract_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_12, 1: subtract_3}, attrs={'operation': 'MULTIPLY'})
    
    multiply_9 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_8, 1: 1.4140}, attrs={'operation': 'MULTIPLY'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_14})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    grid_1 = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': multiply_7, 'Size Y': multiply_9, 'Vertices X': reroute_5, 'Vertices Y': reroute_4})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid_1.outputs["Mesh"], 'Name': 'uv_map', 3: grid_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_1})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': transform_1, 'Instance': nodegroup, 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [instance_on_points_2, instance_on_points_1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})

def shader_material_004(nw: NodeWrangler):
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

    herringbone_parquet = nw.new_node(nodegroup_herringbone_parquet().name,
        input_kwargs={'Columns (Pairs)': 3, 'Rows': 39, 'Plank Width': 0.1350, 'Plank Length': 2.0400})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': herringbone_parquet, 'Material': surface.shaderfunc_to_material(shader_material_004)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material_004, selection=selection)
apply(bpy.context.active_object)
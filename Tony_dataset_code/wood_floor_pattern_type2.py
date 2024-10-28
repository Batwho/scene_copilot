import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_chevron_parquet', singleton=False, type='GeometryNodeTree')
def nodegroup_chevron_parquet(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Columns', 3),
            ('NodeSocketInt', 'Rows', 3),
            ('NodeSocketFloatDistance', 'Point Offset', 0.5000),
            ('NodeSocketFloatDistance', 'Width', 0.2000),
            ('NodeSocketFloatDistance', 'Height', 0.8000),
            ('NodeSocketFloat', 'Bevel Depth', 0.0500),
            ('NodeSocketFloat', 'Bevel X', 0.9300),
            ('NodeSocketFloat', 'Bevel Y', 0.9300)])
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Columns"]})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_4, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Height"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_3, 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: multiply}, attrs={'operation': 'MULTIPLY'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rows"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_7, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Width"], 1: subtract_1},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': multiply_1, 'Size Y': multiply_2, 'Vertices X': reroute_6, 'Vertices Y': reroute_7})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Width"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Height"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Point Offset"]})
    
    quadrilateral_1 = nw.new_node('GeometryNodeCurvePrimitiveQuadrilateral',
        input_kwargs={'Width': reroute_1, 'Height': reroute_2, 'Offset': reroute},
        attrs={'mode': 'PARALLELOGRAM'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: -2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': quadrilateral_1, 'Translation': combine_xyz_1, 'Rotation': (0.0000, 0.0000, 1.5708), 'Scale': (-1.0000, 1.0000, 1.0000)})
    
    fill_curve_1 = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': transform_1}, attrs={'mode': 'NGONS'})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': fill_curve_1})
    
    quadrilateral = nw.new_node('GeometryNodeCurvePrimitiveQuadrilateral',
        input_kwargs={'Width': reroute_1, 'Height': reroute_2, 'Offset': reroute},
        attrs={'mode': 'PARALLELOGRAM'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide_1})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': quadrilateral, 'Translation': combine_xyz, 'Rotation': (0.0000, 0.0000, 1.5708)})
    
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': transform}, attrs={'mode': 'NGONS'})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': fill_curve})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_15, reroute_14]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': store_named_attribute, 'Instance': join_geometry})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bevel Depth"]})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': instance_on_points, 'Offset Scale': reroute_9, 'Individual': False})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bevel X"]})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': reroute_13},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bevel Y"]})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements, 'Selection': extrude_mesh.outputs["Top"], 'Scale': reroute_12, 'Axis': (0.0000, 1.0000, 0.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': scale_elements_1}, attrs={'is_active_output': True})

def shader_material_002(nw: NodeWrangler):
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

    chevron_parquet = nw.new_node(nodegroup_chevron_parquet().name,
        input_kwargs={'Rows': 28, 'Point Offset': 0.3000, 'Width': 0.1262, 'Height': 0.9000, 'Bevel Depth': 0.0100, 'Bevel X': 0.9900})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': chevron_parquet, 'Material': surface.shaderfunc_to_material(shader_material_002)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material_002, selection=selection)
apply(bpy.context.active_object)
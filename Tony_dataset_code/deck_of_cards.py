import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_card(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: 13.0000}, attrs={'operation': 'DIVIDE'})
    
    snap = nw.new_node(Nodes.Math, input_kwargs={0: object_info.outputs["Random"], 1: divide}, attrs={'operation': 'SNAP'})
    
    white_noise_texture = nw.new_node(Nodes.WhiteNoiseTexture,
        input_kwargs={'W': object_info.outputs["Random"]},
        attrs={'noise_dimensions': '1D'})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: 5.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: divide_1}, attrs={'operation': 'SUBTRACT'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': white_noise_texture.outputs["Value"], 4: subtract})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide_1})
    
    snap_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: reroute_2}, attrs={'operation': 'SNAP'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: snap_1, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': snap, 'Y': multiply})
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["UV"], 'Location': combine_xyz})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping},
        attrs={'image': bpy.data.images['cards.png']})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': image_texture.outputs["Color"]})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Density Max', 5.4000),
            ('NodeSocketFloatDistance', 'Distance Min', 0.0000),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketFloat', 'Length deck', 0.0000),
            ('NodeSocketInt', 'Cards x deck', 10),
            ('NodeSocketFloat', 'Curvature', 0.1300),
            ('NodeSocketFloat', 'Rot. decks', 1.0000),
            ('NodeSocketFloat', 'Rot. cards', 1.0000)])
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': group_input.outputs["Geometry"], 'Distance Min': group_input.outputs["Distance Min"], 'Density Max': group_input.outputs["Density Max"], 'Seed': group_input.outputs["Seed"]},
        attrs={'use_legacy_normal': True, 'distribute_method': 'POISSON'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input.outputs["Length deck"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_1})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cards x deck"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': reroute_2})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Length deck"]})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: -2.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Curvature"]})
    
    spline_parameter = nw.new_node(Nodes.SplineParameter)
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': spline_parameter.outputs["Factor"], 4: 3.1416})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: map_range.outputs["Result"]}, attrs={'operation': 'SINE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: sine}, attrs={'operation': 'MULTIPLY'})
    
    index = nw.new_node(Nodes.Index)
    
    thickness_card = nw.new_node(Nodes.Value, label='Thickness card')
    thickness_card.outputs[0].default_value = 0.0003
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: thickness_card}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': divide, 'Y': multiply, 'Z': multiply_1})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': resample_curve, 'Offset': combine_xyz})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': group_input.outputs["Rot. decks"], 4: 6.2832})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': map_range_1.outputs["Result"]})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={1: combine_xyz_2}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': set_position, 'Rotation': random_value.outputs["Value"]})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points})
    
    object_info = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Card']},
        attrs={'transform_space': 'RELATIVE'})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': align_euler_to_vector})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': separate_xyz.outputs["Z"]})
    
    map_range_2 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': group_input.outputs["Rot. cards"], 4: 6.2832})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': map_range_2.outputs["Result"]})
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={1: combine_xyz_4}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz_3, 1: random_value_2.outputs["Value"]})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': realize_instances, 'Instance': object_info.outputs["Geometry"], 'Rotation': add.outputs["Vector"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points_1, 'Material': surface.shaderfunc_to_material(shader_card)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_card, selection=selection)
apply(bpy.context.active_object)
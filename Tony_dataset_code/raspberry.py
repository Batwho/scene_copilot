import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_raspberry(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    layer_weight_2 = nw.new_node(Nodes.LayerWeight, input_kwargs={'Blend': 0.5200})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': layer_weight_2.outputs["Fresnel"]})
    colorramp_4.color_ramp.interpolation = "B_SPLINE"
    colorramp_4.color_ramp.elements[0].position = 0.7182
    colorramp_4.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 1.0000
    colorramp_4.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    layer_weight_1 = nw.new_node(Nodes.LayerWeight, input_kwargs={'Blend': 0.4000})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': layer_weight_1.outputs["Fresnel"]})
    colorramp_5.color_ramp.elements[0].position = 0.0636
    colorramp_5.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.2227
    colorramp_5.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord, attrs={'object': bpy.data.objects['Raspberry red 1']})
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["Object"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': 150.0000, 'Detail': 6.3000, 'Roughness': 0.7083})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5727
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': colorramp.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.2455
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.9682
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_5.outputs["Color"], 7: colorramp_1.outputs["Color"]},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_4.outputs["Color"], 7: mix_1.outputs[2]},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_1.outputs[2], 6: (0.5210, 0.0018, 0.0212, 1.0000), 7: (0.6939, 0.0908, 0.1529, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_2.outputs[2], 6: mix.outputs[2], 7: (0.7326, 0.4995, 0.4780, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': object_info.outputs["Random"]})
    colorramp_3.color_ramp.elements[0].position = 0.5545
    colorramp_3.color_ramp.elements[0].color = [0.5210, 0.0018, 0.0212, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.9591
    colorramp_3.color_ramp.elements[1].color = [0.1187, 0.0009, 0.0071, 1.0000]
    
    mix_4 = nw.new_node(Nodes.Mix,
        input_kwargs={6: mix_3.outputs[2], 7: colorramp_3.outputs["Color"]},
        attrs={'blend_type': 'HUE', 'data_type': 'RGBA'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_4.outputs[2]})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': colorramp.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.4773
    colorramp_2.color_ramp.elements[0].color = [0.1786, 0.1786, 0.1786, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.9955
    colorramp_2.color_ramp.elements[1].color = [0.3370, 0.3370, 0.3370, 1.0000]
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.1000, 'Height': colorramp.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': reroute_1, 'Subsurface': 0.8455, 'Subsurface Color': reroute_1, 'Roughness': colorramp_2.outputs["Color"], 'Transmission': 0.5545, 'Normal': bump},
        attrs={'subsurface_method': 'BURLEY'})
    
    layer_weight = nw.new_node(Nodes.LayerWeight, input_kwargs={'Blend': 0.8700})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Value': layer_weight.outputs["Facing"], 'Color': reroute_1})
    
    translucent_bsdf = nw.new_node(Nodes.TranslucentBSDF, input_kwargs={'Color': hue_saturation_value})
    
    add_shader = nw.new_node('ShaderNodeAddShader', input_kwargs={0: principled_bsdf, 1: translucent_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': add_shader}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Raspberry length', 1.3000),
            ('NodeSocketMaterial', 'Material', None)])#surface.shaderfunc_to_material(shader_raspberry))])
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': group_input.outputs["Geometry"], 'Level': 3})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_2.outputs["Z"], 1: group_input.outputs["Raspberry length"]},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_2.outputs["X"], 'Y': separate_xyz_2.outputs["Y"], 'Z': multiply})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': subdivision_surface, 'Position': combine_xyz_1, 'Offset': (0.0000, 0.0000, -0.1200)})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz.outputs["Z"], 1: 0.5000}, attrs={'operation': 'LESS_THAN'})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': set_position_1, 'Selection': less_than, 'Distance Min': 0.2000, 'Density Max': 231.6000, 'Density': 63.1000},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': (1.0000, 1.0000, 1.0500)})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': store_named_attribute, 'Level': 2})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.3600, 3: 0.4600})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': subdivision_surface_1, 'Scale': random_value.outputs[1]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points, 'Material': group_input.outputs["Material"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    less_than_1 = nw.new_node(Nodes.Compare,
        input_kwargs={0: separate_xyz_1.outputs["Z"], 1: 0.5000},
        attrs={'operation': 'LESS_THAN'})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': set_position_1, 'Selection': less_than_1, 'Distance Min': 0.1500, 'Density Max': 9.9000, 'Density': 63.1000, 'Seed': 2},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['hairs'], 'Separate Children': True, 'Reset Children': True})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 0.7000, 3: 1.4000})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Instance': collection_info, 'Pick Instance': True, 'Rotation': distribute_points_on_faces_1.outputs["Rotation"], 'Scale': random_value_1.outputs[1]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, instance_on_points_1]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_shade_smooth}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_raspberry, selection=selection)
apply(bpy.context.active_object)
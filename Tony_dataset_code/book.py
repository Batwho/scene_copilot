import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_book_mat(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    gradient_texture = nw.new_node(Nodes.GradientTexture)
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': gradient_texture.outputs["Color"]})
    colorramp_1.color_ramp.interpolation = "CONSTANT"
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.0050
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    texture_coordinate_2 = nw.new_node(Nodes.TextureCoord)
    
    mapping_2 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_2.outputs["Object"]})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': mapping_2})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 2.2400
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: value, 1: 0.4000, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["Y"], 1: subtract, 2: 0.0000})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: -0.2000, 2: 0.0000}, attrs={'operation': 'GREATER_THAN'})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: 0.2000, 2: 0.0000}, attrs={'operation': 'LESS_THAN'})
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: greater_than, 7: less_than},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: colorramp_1.outputs["Color"], 7: mix_3.outputs[2]},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_2.outputs[2]})
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    z = nw.new_node(Nodes.Value, label='Z')
    z.outputs[0].default_value = 0.2600
    
    cover = nw.new_node(Nodes.Value, label='Cover')
    cover.outputs[0].default_value = 0.0500
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: cover, 1: 0.0010, 2: 0.0000})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: z, 1: add_1, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    less_than_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["Z"], 1: subtract_1, 2: 0.0000},
        attrs={'operation': 'LESS_THAN'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: cover, 1: 0.0010, 2: 0.0000})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: z, 1: add_2, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: subtract_2, 1: -1.0000, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    greater_than_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["Z"], 1: multiply, 2: 0.0000},
        attrs={'operation': 'GREATER_THAN'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: less_than_1, 7: greater_than_1},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: cover, 1: 0.0010, 2: 0.0000})
    
    greater_than_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["X"], 1: add_3, 2: 0.0000},
        attrs={'operation': 'GREATER_THAN'})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: mix.outputs[2], 7: greater_than_2},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix_1.outputs[2]})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Distortion': 0.3000})
    
    colorramp_8 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_2.outputs["Fac"]})
    colorramp_8.color_ramp.elements[0].position = 0.0000
    colorramp_8.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_8.color_ramp.elements[1].position = 0.3136
    colorramp_8.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    texture_coordinate_5 = nw.new_node(Nodes.TextureCoord)
    
    mapping_9 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_5.outputs["Object"]})
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': mapping_9})
    
    subtract_3 = nw.new_node(Nodes.Math, input_kwargs={0: z, 1: 0.0010, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    greater_than_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_3.outputs["Z"], 1: subtract_3, 2: 0.0000},
        attrs={'operation': 'GREATER_THAN'})
    
    texture_coordinate_4 = nw.new_node(Nodes.TextureCoord)
    
    mapping_7 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_4.outputs["Object"]})
    
    absolute = nw.new_node(Nodes.VectorMath, input_kwargs={0: mapping_7}, attrs={'operation': 'ABSOLUTE'})
    
    x = nw.new_node(Nodes.Value, label='X')
    x.outputs[0].default_value = 1.4500
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: x, 1: -1.0000, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_1})
    
    mapping_8 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': absolute.outputs["Vector"], 'Location': combine_xyz, 'Rotation': (0.0000, 0.0000, 1.5708)})
    
    absolute_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: mapping_8}, attrs={'operation': 'ABSOLUTE'})
    
    musgrave_texture = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': absolute_1.outputs["Vector"], 'Scale': 0.9200},
        attrs={'musgrave_type': 'HYBRID_MULTIFRACTAL'})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': musgrave_texture})
    colorramp_3.color_ramp.interpolation = "CONSTANT"
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.0182
    colorramp_3.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_7 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_8.outputs["Color"], 6: greater_than_3, 7: colorramp_3.outputs["Color"]},
        attrs={'blend_type': 'MULTIPLY', 'data_type': 'RGBA'})
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_7.outputs[2]})
    colorramp_6.color_ramp.elements[0].position = 0.0000
    colorramp_6.color_ramp.elements[0].color = [0.0142, 0.0065, 0.0038, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 1.0000
    colorramp_6.color_ramp.elements[1].color = [0.0159, 0.0029, 0.0290, 1.0000]
    
    mapping_10 = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_4.outputs["Object"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping_10, 'Scale': 150.0000, 'Detail': 16.0000, 'Roughness': 0.8333, 'Distortion': 0.1000})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp_4.color_ramp.elements[0].position = 0.3500
    colorramp_4.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 1.0000
    colorramp_4.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_8 = nw.new_node(Nodes.Mix,
        input_kwargs={0: mix_7.outputs[2], 6: colorramp_4.outputs["Color"], 7: (1.0000, 1.0000, 1.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': mix_8.outputs[2]})
    colorramp_5.color_ramp.elements[0].position = 0.0000
    colorramp_5.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.2727
    colorramp_5.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump_1 = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.2000, 'Height': colorramp_4.outputs["Color"]})
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp_6.outputs["Color"], 'Roughness': colorramp_5.outputs["Color"], 'Normal': bump_1},
        attrs={'subsurface_method': 'BURLEY'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': principled_bsdf_1})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Scale': (-0.1600, 0.1500, 100.0000)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': -10.7100})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.3773
    colorramp.color_ramp.elements[0].color = [0.1193, 0.1193, 0.1193, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.9169, 1.0000, 0.7254, 1.0000]
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': colorramp.outputs["Color"]})
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.1136
    colorramp_2.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.5000, 'Height': colorramp.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Subsurface Color': (1.0000, 1.0000, 1.0000, 1.0000), 'Roughness': colorramp_2.outputs["Color"], 'Normal': bump},
        attrs={'subsurface_method': 'BURLEY'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': principled_bsdf})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': reroute, 1: reroute_4, 2: reroute_3})
    
    principled_bsdf_2 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.6064, 0.8000, 0.4597, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.2000},
        attrs={'subsurface_method': 'BURLEY'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': principled_bsdf_2})
    
    mix_shader_1 = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': reroute_2, 1: mix_shader, 2: reroute_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader_1}, attrs={'is_active_output': True})

def geometry_realize_instances_2_93_legacy(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': group_input.outputs["Geometry"]})
    
    separate_components = nw.new_node(Nodes.SeparateComponents, input_kwargs={'Geometry': realize_instances})
    
    points_to_vertices = nw.new_node(Nodes.PointsToVertices, input_kwargs={'Points': separate_components.outputs["Curve"]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [points_to_vertices, separate_components.outputs["Volume"], separate_components.outputs["Point Cloud"], separate_components.outputs["Mesh"]]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'X', 1.0000),
            ('NodeSocketFloat', 'Y', 1.0000),
            ('NodeSocketFloat', 'Z', 1.0000),
            ('NodeSocketFloat', 'Cover', 0.1000),
            ('NodeSocketFloat', 'Pages X', 0.0500),
            ('NodeSocketFloat', 'Pages Y', 0.1000)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["X"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Y"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Z"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_2, 'Y': reroute_3, 'Z': reroute_4})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute, 'Scale': combine_xyz})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': transform_2})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cover"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_1})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute_4, 1: reroute_1, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_2, 'Y': reroute_3, 'Z': subtract})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': reroute, 'Translation': combine_xyz_4, 'Scale': combine_xyz_1})
    
    difference = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': realize_instances, 'Mesh 2': transform})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_1})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 2.0000, 2: 0.0000}, attrs={'operation': 'DIVIDE'})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Pages X"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: reroute_11, 2: 0.0000})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_8, 1: add, 2: 0.0000}, attrs={'operation': 'SUBTRACT'})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    subtract_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: reroute_9, 1: group_input.outputs["Pages Y"], 2: 0.0000},
        attrs={'operation': 'SUBTRACT'})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract_1, 'Y': subtract_2, 'Z': reroute_6})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': reroute_10, 'Translation': combine_xyz_5, 'Scale': combine_xyz_2})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [difference.outputs["Mesh"], transform_1]})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': join_geometry})
    
    triangulate = nw.new_node('GeometryNodeTriangulate', input_kwargs={'Mesh': realize_instances_1, 'Minimum Vertices': 5})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': triangulate}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_geomod(obj, geometry_realize_instances_2_93_legacy, selection=selection, attributes=[])
    surface.add_material(obj, shader_book_mat, selection=selection)
apply(bpy.context.active_object)
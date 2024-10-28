import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_sprinkles(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': object_info.outputs["Random"]})
    colorramp.color_ramp.interpolation = "CONSTANT"
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [1.0000, 1.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.2500
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.5000
    colorramp.color_ramp.elements[2].color = [0.0000, 1.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[3].position = 0.7500
    colorramp.color_ramp.elements[3].color = [1.0000, 0.0000, 0.0000, 1.0000]
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Hue': 0.0800, 'Saturation': 0.9000, 'Value': 0.8000, 'Color': colorramp.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': hue_saturation_value, 'Roughness': 0.4000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_icing(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    rgb = nw.new_node(Nodes.RGB)
    rgb.outputs[0].default_value = (0.2086, 0.0762, 0.0000, 1.0000)
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue, input_kwargs={'Saturation': 0.8000, 'Color': rgb})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': rgb, 'Subsurface': 0.2000, 'Subsurface Radius': (0.1000, 0.1000, 0.1000), 'Subsurface Color': hue_saturation_value, 'Roughness': 0.4000, 'Clearcoat Roughness': 0.0100},
        attrs={'distribution': 'MULTI_GGX'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_donut(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Location': (0.0000, 0.0000, 0.5000)})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': mapping})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': separate_xyz.outputs["Z"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements.new(0)
    colorramp.color_ramp.elements[0].position = 0.2000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp.color_ramp.elements[2].position = 0.8000
    colorramp.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    invert = nw.new_node(Nodes.Invert, input_kwargs={'Color': colorramp.outputs["Color"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 20.0000, 'Detail': 6.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.1520
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.7040
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix_3 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_1.outputs["Color"], 6: (0.8388, 0.4910, 0.0976, 1.0000), 7: (0.6418, 0.3306, 0.0299, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_1.outputs["Color"], 6: (1.0000, 0.3284, 0.0000, 1.0000), 7: (0.6418, 0.0829, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    mix_1 = nw.new_node(Nodes.Mix, input_kwargs={0: invert, 6: mix_3.outputs[2], 7: mix.outputs[2]}, attrs={'data_type': 'RGBA'})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp.outputs["Color"], 6: colorramp_1.outputs["Color"], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.1000, 'Height': mix_2.outputs[2]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_1.outputs[2], 'Normal': bump},
        attrs={'distribution': 'MULTI_GGX'})
    
    displacement = nw.new_node(Nodes.Displacement, input_kwargs={'Height': mix_2.outputs[2], 'Scale': 0.0500})
    
    material_output = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': principled_bsdf, 'Displacement': displacement},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    curve_circle = nw.new_node(Nodes.CurveCircle)
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 16, 'Radius': 0.7500})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_circle.outputs["Curve"], 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Donut subsurf', 1),
            ('NodeSocketFloat', 'Donut Noise scale', 2.5000),
            ('NodeSocketInt', 'Donut disp subsurf', 1),
            ('NodeSocketFloat', 'Icing size', 0.4500),
            ('NodeSocketInt', 'Icing subsurf', 1),
            ('NodeSocketFloat', 'Sprinkle density', 40.0000),
            ('NodeSocketFloat', 'Size of sprinlkles', 0.1000),
            ('NodeSocketInt', 'Sprinkles seed', 1)])
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': curve_to_mesh, 'Level': group_input.outputs["Donut subsurf"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    map_range_2 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz_2.outputs["Z"], 1: -1.4643, 2: 1.4643})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range_2.outputs["Result"]})
    colorramp_5.color_ramp.interpolation = "EASE"
    colorramp_5.color_ramp.elements.new(0)
    colorramp_5.color_ramp.elements[0].position = 0.1880
    colorramp_5.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.5000
    colorramp_5.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_5.color_ramp.elements[2].position = 0.7880
    colorramp_5.color_ramp.elements[2].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: colorramp_5.outputs["Color"], 1: 0.3000}, attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: 0.3600}, attrs={'operation': 'MULTIPLY'})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': subdivision_surface_1, 'Offset Scale': multiply, 'Individual': False})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': group_input.outputs["Donut Noise scale"], 'Detail': 6.0000})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Vector': noise_texture.outputs["Fac"], 9: (-1.0000, -1.0000, -1.0000)},
        attrs={'data_type': 'FLOAT_VECTOR', 'clamp': False})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: map_range.outputs["Vector"], 'Scale': 0.1250},
        attrs={'operation': 'SCALE'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Offset': scale.outputs["Vector"]})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position, 'Scale': (1.0000, 1.0000, 0.7500)})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_4})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: group_input.outputs["Icing size"]},
        attrs={'operation': 'DIVIDE'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: divide}, attrs={'operation': 'SUBTRACT'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': subtract_1})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': reroute_11, 'Selection': colorramp.outputs["Color"]},
        attrs={'domain': 'FACE'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': separate_geometry.outputs["Selection"], 'Offset Scale': 0.0250, 'Individual': False})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': separate_geometry.outputs["Selection"]})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [extrude_mesh.outputs["Mesh"], flip_faces]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_1})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': merge_by_distance, 'Level': group_input.outputs["Icing subsurf"]})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    scale_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal, 'Scale': 0.1000}, attrs={'operation': 'SCALE'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 1.8100, 'Detail': 6.0000, 'Roughness': 0.4118, 'Distortion': 3.5000},
        attrs={'noise_dimensions': '4D'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale_1.outputs["Vector"], 1: noise_texture_1.outputs["Color"], 'Scale': 0.0100},
        attrs={'operation': 'MULTIPLY'})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_1.outputs["Vector"], 'Scale': 0.8100},
        attrs={'operation': 'SCALE'})
    
    set_position_5 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': subdivision_surface, 'Selection': extrude_mesh.outputs["Top"], 'Offset': scale_2.outputs["Vector"]})
    
    icing = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_5}, label='Icing')
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': icing, 'Material': surface.shaderfunc_to_material(shader_icing)})
    
    subdivision_surface_2 = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': transform_4, 'Level': group_input.outputs["Donut disp subsurf"]})
    
    base_donut = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subdivision_surface_2}, label='Base donut')
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': base_donut, 'Material': surface.shaderfunc_to_material(shader_donut)})
    
    goes_to_sprinkles = nw.new_node(Nodes.Reroute, input_kwargs={'Input': icing}, label='Goes to sprinkles')
    
    density = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Sprinkle density"]}, label='Density')
    
    seed_icing = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Sprinkles seed"]}, label='Seed Icing')
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: seed_icing, 1: 3.0000})
    
    distribute_points_on_faces_3 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': goes_to_sprinkles, 'Distance Min': 0.0500, 'Density Max': density, 'Density': 27.8000, 'Seed': add},
        attrs={'use_legacy_normal': True, 'distribute_method': 'POISSON'})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': extrude_mesh.outputs["Top"]})
    
    selects_top_of_icing = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_4}, label='Selects top of icing')
    
    base_height_of_spriknles = nw.new_node(Nodes.Reroute,
        input_kwargs={'Input': group_input.outputs["Size of sprinlkles"]},
        label='Base height of spriknles')
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': 12, 'Side Segments': 5, 'Fill Segments': 3, 'Radius': 0.0100, 'Depth': base_height_of_spriknles},
        attrs={'fill_type': 'TRIANGLE_FAN'})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: base_height_of_spriknles, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_1.outputs["Z"], 1: multiply_2, 2: base_height_of_spriknles},
        attrs={'interpolation_type': 'SMOOTHSTEP'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_1.outputs["Result"]})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_2})
    colorramp_4.color_ramp.interpolation = "EASE"
    colorramp_4.color_ramp.elements.new(0)
    colorramp_4.color_ramp.elements[0].position = 0.0000
    colorramp_4.color_ramp.elements[0].color = [0.2139, 0.2139, 0.2139, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.6360
    colorramp_4.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[2].position = 1.0000
    colorramp_4.color_ramp.elements[2].color = [0.1328, 0.1328, 0.1328, 1.0000]
    
    bummer = nw.new_node(Nodes.Value, label='Bummer')
    bummer.outputs[0].default_value = 0.1000
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': bummer})
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_4.outputs["Color"], 1: reroute_3},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_3})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': store_named_attribute, 'Offset': combine_xyz_3})
    
    value_3 = nw.new_node(Nodes.Value)
    value_3.outputs[0].default_value = 0.0090
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': value_3})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_4})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': set_position_4, 'Translation': reroute_9, 'Scale': (1.0000, 1.0000, 1.2500)})
    
    random_value_6 = nw.new_node(Nodes.RandomValue, input_kwargs={1: (6.2832, 6.2832, 6.2832)}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    add_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: distribute_points_on_faces_3.outputs["Rotation"], 1: random_value_6.outputs["Value"]})
    
    align_euler_to_vector_3 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': add_1.outputs["Vector"], 'Vector': distribute_points_on_faces_3.outputs["Normal"]},
        attrs={'axis': 'Y'})
    
    random_value_7 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.8500, 0.8500, 0.8500), 1: (1.2000, 1.0000, 1.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points_3 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_3.outputs["Points"], 'Selection': selects_top_of_icing, 'Instance': transform_3, 'Rotation': align_euler_to_vector_3, 'Scale': random_value_7.outputs["Value"]})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: seed_icing, 1: 2.0000})
    
    distribute_points_on_faces_2 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': goes_to_sprinkles, 'Distance Min': 0.0500, 'Density Max': density, 'Density': 27.8000, 'Seed': add_2},
        attrs={'use_legacy_normal': True, 'distribute_method': 'POISSON'})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_2})
    colorramp_3.color_ramp.interpolation = "EASE"
    colorramp_3.color_ramp.elements.new(0)
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.1328, 0.1328, 0.1328, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.3680
    colorramp_3.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_3.color_ramp.elements[2].position = 1.0000
    colorramp_3.color_ramp.elements[2].color = [0.1328, 0.1328, 0.1328, 1.0000]
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_3.outputs["Color"], 1: reroute_3},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_4})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': store_named_attribute, 'Offset': combine_xyz_2})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_3, 'Translation': reroute_9})
    
    random_value_4 = nw.new_node(Nodes.RandomValue, input_kwargs={1: (6.2832, 6.2832, 6.2832)}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    add_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: distribute_points_on_faces_2.outputs["Rotation"], 1: random_value_4.outputs["Value"]})
    
    align_euler_to_vector_2 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': add_3.outputs["Vector"], 'Vector': distribute_points_on_faces_2.outputs["Normal"]},
        attrs={'axis': 'Y'})
    
    random_value_5 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.8500, 0.8500, 0.8500), 1: (1.2000, 1.0000, 1.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_2.outputs["Points"], 'Selection': selects_top_of_icing, 'Instance': transform_2, 'Rotation': align_euler_to_vector_2, 'Scale': random_value_5.outputs["Value"]})
    
    add_4 = nw.new_node(Nodes.Math, input_kwargs={0: seed_icing, 1: 1.0000})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': goes_to_sprinkles, 'Distance Min': 0.0500, 'Density Max': density, 'Density': 27.8000, 'Seed': add_4},
        attrs={'use_legacy_normal': True, 'distribute_method': 'POISSON'})
    
    colorramp_2 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_2})
    colorramp_2.color_ramp.interpolation = "EASE"
    colorramp_2.color_ramp.elements.new(0)
    colorramp_2.color_ramp.elements[0].position = 0.0000
    colorramp_2.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_2.color_ramp.elements[1].position = 0.7120
    colorramp_2.color_ramp.elements[1].color = [0.1328, 0.1328, 0.1328, 1.0000]
    colorramp_2.color_ramp.elements[2].position = 1.0000
    colorramp_2.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    multiply_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_2.outputs["Color"], 1: reroute_3},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_5})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': store_named_attribute, 'Offset': combine_xyz_1})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_2, 'Translation': reroute_9})
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={1: (6.2832, 6.2832, 6.2832)}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    add_5 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: distribute_points_on_faces_1.outputs["Rotation"], 1: random_value_2.outputs["Value"]})
    
    align_euler_to_vector_1 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': add_5.outputs["Vector"], 'Vector': distribute_points_on_faces_1.outputs["Normal"]},
        attrs={'axis': 'Y'})
    
    random_value_3 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.8500, 0.8500, 0.8500), 1: (1.2000, 1.0000, 1.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Selection': selects_top_of_icing, 'Instance': transform_1, 'Rotation': align_euler_to_vector_1, 'Scale': random_value_3.outputs["Value"]})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': goes_to_sprinkles, 'Distance Min': 0.0500, 'Density Max': density, 'Density': 27.8000, 'Seed': seed_icing},
        attrs={'use_legacy_normal': True, 'distribute_method': 'POISSON'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_2})
    colorramp_1.color_ramp.interpolation = "EASE"
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [0.2632, 0.2632, 0.2632, 1.0000]
    
    multiply_6 = nw.new_node(Nodes.Math,
        input_kwargs={0: colorramp_1.outputs["Color"], 1: reroute_3},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply_6})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute, 'Position': position_2, 'Offset': combine_xyz})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_1, 'Translation': reroute_9})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={1: (6.2832, 6.2832, 6.2832)}, attrs={'data_type': 'FLOAT_VECTOR'})
    
    add_6 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: distribute_points_on_faces.outputs["Rotation"], 1: random_value.outputs["Value"]})
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': add_6.outputs["Vector"], 'Vector': distribute_points_on_faces.outputs["Normal"]},
        attrs={'axis': 'Y'})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.8500, 0.8500, 0.8500), 1: (1.2000, 1.0000, 1.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Selection': selects_top_of_icing, 'Instance': transform, 'Rotation': align_euler_to_vector, 'Scale': random_value_1.outputs["Value"]})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [instance_on_points_3, instance_on_points_2, instance_on_points_1, instance_on_points]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_2, 'Material': surface.shaderfunc_to_material(shader_sprinkles)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_1, set_material_2, set_material]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_shade_smooth}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_donut, selection=selection)
    surface.add_material(obj, shader_icing, selection=selection)
    surface.add_material(obj, shader_sprinkles, selection=selection)
apply(bpy.context.active_object)
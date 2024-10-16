import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_crystal_volume(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Detail': 1.0000, 'Roughness': 0.6444})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.4811
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5220
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"], 1: 1.0000}, attrs={'operation': 'POWER'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Color"], 1: 5.0000}, attrs={'operation': 'MULTIPLY'})
    
    principled_volume = nw.new_node(Nodes.PrincipledVolume,
        input_kwargs={'Color': (1.0000, 1.0000, 1.0000, 1.0000), 'Density': power, 'Emission Strength': multiply, 'Emission Color': (0.8388, 0.8388, 0.8388, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Volume': principled_volume}, attrs={'is_active_output': True})

def shader_crystal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'imperfection_fac'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': attribute.outputs["Fac"]})
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_2})
    colorramp_6.color_ramp.elements[0].position = 0.0000
    colorramp_6.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 0.4091
    colorramp_6.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    noise_texture_4 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 3.9600, 'Detail': 0.0000})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_4.outputs["Fac"]})
    colorramp_5.color_ramp.elements[0].position = 0.3121
    colorramp_5.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.6606
    colorramp_5.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    geometry = nw.new_node(Nodes.NewGeometry)
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': geometry.outputs["Pointiness"]})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_1})
    colorramp_3.color_ramp.elements[0].position = 0.4333
    colorramp_3.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.4818
    colorramp_3.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate_1.outputs["Generated"], 'Rotation': (0.0000, 0.0820, 0.0000)})
    
    wave_texture_1 = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': mapping, 'Scale': 4.5800, 'Distortion': 0.8000, 'Detail Scale': 1.1300, 'Detail Roughness': 0.5590},
        attrs={'bands_direction': 'Z'})
    
    wave_texture_2 = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': texture_coordinate_1.outputs["Generated"], 'Scale': wave_texture_1.outputs["Fac"], 'Distortion': 2.3900, 'Detail': 1.0000, 'Detail Roughness': 1.0000},
        attrs={'bands_direction': 'Z'})
    
    colorramp_10 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': wave_texture_2.outputs["Fac"]})
    colorramp_10.color_ramp.elements[0].position = 0.0000
    colorramp_10.color_ramp.elements[0].color = [0.7855, 0.7855, 0.7855, 1.0000]
    colorramp_10.color_ramp.elements[1].position = 0.0152
    colorramp_10.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': colorramp_10.outputs["Color"]})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_5.outputs["Color"], 6: colorramp_3.outputs["Color"], 7: reroute},
        attrs={'data_type': 'RGBA', 'blend_type': 'LIGHTEN'})
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_1})
    colorramp_4.color_ramp.elements[0].position = 0.4212
    colorramp_4.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.4727
    colorramp_4.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': colorramp_4.outputs["Color"], 3: 1.4300, 4: 0.0000})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': texture_coordinate.outputs["Object"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_3, 'Scale': 6.0000, 'Detail': 10.0000, 'Roughness': 0.1000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.3091
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.4955
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute_3, 'Scale': 6.0000, 'Detail': 10.0000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.1000, 'Height': noise_texture.outputs["Fac"]})
    
    bump_1 = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.0600, 'Height': colorramp_1.outputs["Color"], 'Normal': bump},
        attrs={'invert': True})
    
    glass_bsdf = nw.new_node(Nodes.GlassBSDF,
        input_kwargs={'Roughness': mix_1.outputs[2], 'IOR': map_range.outputs["Result"], 'Normal': bump_1})
    
    multiply_add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: 20.0000, 2: 20.0000}, attrs={'operation': 'MULTIPLY_ADD'})
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': reroute_3, 'Scale': multiply_add, 'Detail': 0.0000, 'Roughness': 0.0000})
    
    colorramp_9 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_3.outputs["Fac"]})
    colorramp_9.color_ramp.elements[0].position = 0.3909
    colorramp_9.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_9.color_ramp.elements[1].position = 0.6500
    colorramp_9.color_ramp.elements[1].color = [0.5186, 0.5186, 0.5186, 1.0000]
    
    principled_bsdf_1 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.7046, 0.8915, 1.0000, 1.0000), 'Roughness': colorramp_9.outputs["Color"], 'Transmission': 0.7000, 'Emission Strength': 0.0000, 'Normal': bump_1})
    
    mix_shader = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': colorramp_6.outputs["Color"], 1: glass_bsdf, 2: principled_bsdf_1})
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Vector': reroute_3, 'Scale': 1.8600})
    
    displacement = nw.new_node(Nodes.Displacement, input_kwargs={'Height': voronoi_texture.outputs["Distance"], 'Scale': 0.0800})
    
    material_output_1 = nw.new_node(Nodes.MaterialOutput,
        input_kwargs={'Surface': mix_shader, 'Displacement': displacement},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_3 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Nb Sides', 5),
            ('NodeSocketFloat', 'Base Shape Noise Strength', 1.0000),
            ('NodeSocketBool', 'Apply Damage', False),
            ('NodeSocketFloat', 'Imperfection Area Size', 1.0000),
            ('NodeSocketFloat', 'Imperfection Area Strength', 0.5000),
            ('NodeSocketFloat', 'Edges Damage Factor', 1.0000),
            ('NodeSocketFloat', 'Edges Damage Randomness', 0.5000),
            ('NodeSocketFloat', 'Edges Damage Details Factor', 0.3000),
            ('NodeSocketFloat', 'Edges Damage Radius', 1.0000),
            ('NodeSocketBool', 'Add Internal Volume', False),
            ('NodeSocketBool', 'Subdivision Surface', False),
            ('NodeSocketMaterial', 'Material', None), #surface.shaderfunc_to_material(shader_crystal)
            ('NodeSocketMaterial', 'Volume Material',None)]) # surface.shaderfunc_to_material(shader_crystal_volume))]
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_3.outputs["Nb Sides"]})
    
    mesh_circle = nw.new_node(Nodes.MeshCircle, input_kwargs={'Vertices': reroute_1}, attrs={'fill_type': 'NGON'})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': mesh_circle, 'Offset Scale': 0.8000})
    
    extrude_mesh_2 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': extrude_mesh_1.outputs["Mesh"], 'Selection': extrude_mesh_1.outputs["Top"], 'Offset Scale': 0.9000})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh_2.outputs["Mesh"], 'Selection': extrude_mesh_2.outputs["Top"], 'Scale': 0.2000})
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 3.1416, 1: reroute_1}, attrs={'operation': 'DIVIDE'})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={0: modulo, 3: divide}, attrs={'input_type': 'FLOAT'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': 3.1416, 'Z': switch.outputs["Output"]})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': scale_elements_1, 'Rotation': combine_xyz})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform, scale_elements_1]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': merge_by_distance})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'W': 3.4000, 'Scale': 2.0000}, attrs={'noise_dimensions': '4D'})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 'Scale': group_input_3.outputs["Base Shape Noise Strength"]},
        attrs={'operation': 'SCALE'})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    multiply = nw.new_node(Nodes.VectorMath, input_kwargs={0: scale.outputs["Vector"], 1: normal}, attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_2, 'Offset': multiply.outputs["Vector"]})
    
    switch_3 = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input_3.outputs["Subdivision Surface"], 4: 1, 5: 3},
        attrs={'input_type': 'INT'})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': set_position, 'Level': switch_3.outputs[1]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subdivision_surface})
    
    noise_texture_6 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'W': 8.5100, 'Scale': 0.5000, 'Detail': 0.0000, 'Roughness': 0.1556})
    
    position = nw.new_node(Nodes.InputPosition)
    
    object_info = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['crystal_empty']},
        attrs={'transform_space': 'RELATIVE'})
    
    distance = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position, 1: object_info.outputs["Location"]},
        attrs={'operation': 'DISTANCE'})
    
    noise_texture_4 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 2.9200, 'Detail': 2.0800, 'Roughness': 0.7556})
    
    noise_texture_5 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 1.4300, 'Detail': 0.4000, 'Roughness': 0.0000})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={6: noise_texture_4.outputs["Fac"], 7: noise_texture_5.outputs["Fac"]},
        attrs={'data_type': 'RGBA'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: mix.outputs[2], 1: group_input_3.outputs["Imperfection Area Size"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': distance.outputs["Value"], 2: add, 3: 1.0000, 4: 0.0000})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': map_range.outputs["Result"], 1: 1.0000, 2: 0.0000, 3: 3.0000, 4: 1.1400})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': 8.5100, 'Scale': 3.0000, 'Detail': map_range_1.outputs["Result"], 'Roughness': 0.5889})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.5056, 6: noise_texture_6.outputs["Color"], 7: noise_texture_2.outputs["Color"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    subtract_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: mix_1.outputs[2], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract_1.outputs["Vector"], 'Scale': group_input_3.outputs["Imperfection Area Strength"]},
        attrs={'operation': 'SCALE'})
    
    normal_1 = nw.new_node(Nodes.InputNormal)
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale_1.outputs["Vector"], 1: normal_1},
        attrs={'operation': 'MULTIPLY'})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_1.outputs["Vector"], 'Scale': map_range.outputs["Result"]},
        attrs={'operation': 'SCALE'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_4, 'Offset': scale_2.outputs["Vector"]})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: 0.1000})
    
    map_range_3 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': distance.outputs["Value"], 2: add_1, 3: 1.0000, 4: 0.0000})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints,
        input_kwargs={'Mesh': set_position_2, 'Selection': map_range_3.outputs["Result"], 'Radius': 0.0100})
    
    points_to_volume_1 = nw.new_node(Nodes.PointsToVolume,
        input_kwargs={'Points': mesh_to_points, 'Voxel Amount': 600.0000, 'Radius': 0.2000})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': points_to_volume_1, 'Scale': (0.5000, 0.5000, 0.5000)})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': transform_2, 'Material': group_input_3.outputs["Volume Material"]})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_3.outputs["Add Internal Volume"], 15: set_material_1})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_2})
    
    id = nw.new_node(Nodes.InputID)
    
    subtract_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Nb Sides"], 1: 1.0000},
        attrs={'operation': 'SUBTRACT'})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: id, 3: subtract_2}, attrs={'data_type': 'INT'})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': set_position, 'Selection': greater_than})
    
    curve_to_points = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': mesh_to_curve, 'Count': 50})
    
    random_value = nw.new_node(Nodes.RandomValue)
    
    greater_than_1 = nw.new_node(Nodes.Compare,
        input_kwargs={0: random_value.outputs[1], 1: group_input_3.outputs["Edges Damage Factor"]})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': curve_to_points.outputs["Points"], 'Selection': greater_than_1})
    
    delete_geometry_1 = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': delete_geometry, 'Selection': map_range.outputs["Result"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 3.0000})
    
    subtract_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture_1.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    scale_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract_3.outputs["Vector"], 'Scale': group_input_3.outputs["Edges Damage Randomness"]},
        attrs={'operation': 'SCALE'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': delete_geometry_1, 'Offset': scale_3.outputs["Vector"]})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': group_input_3.outputs["Edges Damage Details Factor"], 3: 0.5000, 4: 10.0000})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range_2.outputs["Result"], 1: 100.0000},
        attrs={'operation': 'MULTIPLY'})
    
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_3.outputs["Edges Damage Radius"], 1: 10.0000},
        attrs={'operation': 'DIVIDE'})
    
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: divide_1, 1: 10.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: divide_2, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    random_value_1 = nw.new_node(Nodes.RandomValue, input_kwargs={2: multiply_3, 3: divide_2})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: divide_1, 1: random_value_1.outputs[1]})
    
    points_to_volume = nw.new_node(Nodes.PointsToVolume,
        input_kwargs={'Points': set_position_1, 'Voxel Amount': multiply_2, 'Radius': add_2})
    
    volume_to_mesh = nw.new_node(Nodes.VolumeToMesh,
        input_kwargs={'Volume': points_to_volume, 'Threshold': 0.1100, 'Adaptivity': 1.0000})
    
    difference = nw.new_node(Nodes.MeshBoolean,
        input_kwargs={'Mesh 1': reroute, 'Mesh 2': volume_to_mesh, 'Self Intersection': True})
    
    switch_1 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_3.outputs["Apply Damage"], 14: reroute, 15: difference.outputs["Mesh"]})
    
    switch_4 = nw.new_node(Nodes.Switch,
        input_kwargs={0: group_input_3.outputs["Subdivision Surface"], 5: 1},
        attrs={'input_type': 'INT'})
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': switch_1.outputs[6], 'Level': switch_4.outputs[1]})
    
    edge_angle = nw.new_node(Nodes.InputEdgeAngle)
    
    less_than = nw.new_node(Nodes.Compare,
        input_kwargs={0: edge_angle.outputs["Unsigned Angle"], 1: 0.4516},
        attrs={'operation': 'LESS_THAN'})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': subdivision_surface_1, 'Selection': less_than})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': group_input_3.outputs["Material"]})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [switch_2.outputs[6], set_material]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range.outputs["Result"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry_1, 'Imperfection Factor': reroute_3},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_crystal, selection=selection)
apply(bpy.context.active_object)
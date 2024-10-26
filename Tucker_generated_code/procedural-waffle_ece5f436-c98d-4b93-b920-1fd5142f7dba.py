import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_sugar(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    fresnel = nw.new_node(Nodes.Fresnel)
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Specular': 0.7955, 'Roughness': 0.0000, 'Transmission': 0.6045, 'Transmission Roughness': 0.9045, 'Emission': (0.7354, 0.7354, 0.7354, 1.0000), 'Emission Strength': fresnel})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_syrup(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.6648, 0.4202, 0.2523, 1.0000), 'Roughness': 0.0952, 'Transmission': 1.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_waffle(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate_1 = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate_1.outputs["Object"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 38.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]})
    colorramp_1.color_ramp.elements[0].position = 0.5864
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.9500
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    ambient_occlusion = nw.new_node(Nodes.AmbientOcclusion)
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': ambient_occlusion.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.2409
    colorramp.color_ramp.elements[0].color = [0.4980, 0.1440, 0.0860, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 0.4772, 0.1933, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp_1.outputs["Color"], 6: colorramp.outputs["Color"]},
        attrs={'data_type': 'RGBA'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mix.outputs[2]})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': 55.0000, 'Detail': 4.0000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.3833, 'Height': noise_texture.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': reroute, 'Subsurface': 0.1000, 'Subsurface Radius': (0.2000, 0.0400, 0.0200), 'Subsurface Color': reroute, 'Roughness': 0.5773, 'Normal': bump},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatFactor', 'Syrup Probability', 0.5750),
            ('NodeSocketInt', 'Syrup Seed', 7),
            ('NodeSocketVectorTranslation', 'syrup height', (0.0000, 0.0000, 0.0500)),
            ('NodeSocketFloatDistance', 'Waffle Rectangle Size', 1.0000),
            ('NodeSocketInt', 'Waffle Number of rectangles', 12),
            ('NodeSocketInt', 'Waffle number of sides', 60),
            ('NodeSocketFloatDistance', 'Waffle Radius', 0.5000),
            ('NodeSocketVectorTranslation', 'Waffle Cross size', (1.0000, 0.1000, 1.0000)),
            ('NodeSocketFloat', 'Waffle Height', 0.0600),
            ('NodeSocketFloat', 'Waffle distortion ammount', 0.0600),
            ('NodeSocketFloat', 'Waffle distortion Scale', 5.0000),
            ('NodeSocketFloat', 'Waffle distortion Detail', 1.0000),
            ('NodeSocketFloat', 'Waffle Density', 6000.0000),
            ('NodeSocketInt', 'Waffle Density Seed', 6),
            ('NodeSocketFloat', 'Volume Voxel Amount', 100.0000),
            ('NodeSocketFloatDistance', 'Volume points Radius', 0.0200),
            ('NodeSocketFloat', 'Volume to Mesh Threshold', 0.1000),
            ('NodeSocketFloat', 'Sugar Density', 3000.0000),
            ('NodeSocketFloatFactor', 'Sugar Density Factor', 1.0000),
            ('NodeSocketInt', 'Sugar Seed', 0),
            ('NodeSocketFloat', 'Sugar Rotation Min', 0.0000),
            ('NodeSocketFloat', 'Sugar Rotation Max', 1.0000),
            ('NodeSocketInt', 'Sugar Rotation Seed', 0),
            ('NodeSocketFloat', 'Sugar Size Min', 0.0000),
            ('NodeSocketFloat', 'Sugar Size Max', 0.0250),
            ('NodeSocketInt', 'Sugar Size Seed', 3),
            ('NodeSocketFloat', 'Sugar dispersion Multiplier', -1.2300),
            ('NodeSocketFloat', 'Sugar dispersion  Addend', 1.0000)])
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': group_input.outputs["Waffle number of sides"], 'Radius': group_input.outputs["Waffle Radius"]})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': group_input.outputs["Waffle Rectangle Size"], 'Size Y': group_input.outputs["Waffle Rectangle Size"], 'Vertices X': group_input.outputs["Waffle Number of rectangles"], 'Vertices Y': group_input.outputs["Waffle Number of rectangles"]})
    
    store_named_attribute_4 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    intersect = nw.new_node(Nodes.MeshBoolean,
        input_kwargs={'Mesh 2': [store_named_attribute_1, store_named_attribute_4]},
        attrs={'operation': 'INTERSECT'})
    
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': group_input.outputs["Waffle Cross size"]})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute_2, 'Rotation': (0.0000, 0.0000, 1.5708)})
    
    difference = nw.new_node(Nodes.MeshBoolean,
        input_kwargs={'Mesh 1': intersect.outputs["Mesh"], 'Mesh 2': [store_named_attribute_2, transform]})
    
    is_shade_smooth = nw.new_node('GeometryNodeInputShadeSmooth')
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': difference.outputs["Mesh"], 4: is_shade_smooth},
        attrs={'domain': 'FACE', 'data_type': 'BOOLEAN'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': capture_attribute.outputs["Geometry"], 'Offset Scale': group_input.outputs["Waffle Height"]},
        attrs={'mode': 'EDGES'})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Shade Smooth': capture_attribute.outputs[4]})
    
    mesh_circle = nw.new_node(Nodes.MeshCircle, input_kwargs={'Vertices': 60, 'Radius': 0.5100}, attrs={'fill_type': 'NGON'})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': mesh_circle, 'Translation': (0.0000, 0.0000, 0.0100)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_shade_smooth_1, transform_1]})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': join_geometry, 'Density': group_input.outputs["Waffle Density"], 'Seed': group_input.outputs["Waffle Density Seed"]},
        attrs={'use_legacy_normal': True})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': group_input.outputs["Waffle distortion Scale"], 'Detail': group_input.outputs["Waffle distortion Detail"]})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: (0.5000, 0.5000, 0.5000), 'Scale': group_input.outputs["Waffle distortion ammount"]},
        attrs={'operation': 'SCALE'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': distribute_points_on_faces.outputs["Points"], 'Offset': scale.outputs["Vector"]})
    
    points_to_volume = nw.new_node(Nodes.PointsToVolume,
        input_kwargs={'Points': set_position, 'Voxel Amount': group_input.outputs["Volume Voxel Amount"], 'Radius': group_input.outputs["Volume points Radius"]})
    
    volume_to_mesh = nw.new_node(Nodes.VolumeToMesh,
        input_kwargs={'Volume': points_to_volume, 'Threshold': group_input.outputs["Volume to Mesh Threshold"]})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': volume_to_mesh})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': subdivision_surface})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_waffle)})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={'Probability': group_input.outputs["Syrup Probability"], 'Seed': group_input.outputs["Syrup Seed"]},
        attrs={'data_type': 'BOOLEAN'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': difference.outputs["Mesh"], 'Selection': random_value.outputs[3]},
        attrs={'domain': 'FACE'})
    
    transform_2 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': delete_geometry, 'Translation': group_input.outputs["syrup height"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': transform_2, 'Material': surface.shaderfunc_to_material(shader_syrup)})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': subdivision_surface, 'Density Max': group_input.outputs["Sugar Density"], 'Density': 598.2000, 'Density Factor': group_input.outputs["Sugar Density Factor"], 'Seed': group_input.outputs["Sugar Seed"]},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    cube_1 = nw.new_node(Nodes.MeshCube)
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube_1.outputs["Mesh"], 'Name': 'uv_map', 3: cube_1.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input.outputs["Sugar Rotation Min"], 3: group_input.outputs["Sugar Rotation Max"], 'Seed': group_input.outputs["Sugar Rotation Seed"]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Radius': 0.0200})
    
    store_named_attribute_3 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute_3, 'Translation': (0.0000, 0.0000, 0.6900)})
    
    geometry_proximity = nw.new_node(Nodes.Proximity, input_kwargs={'Target': transform_3})
    
    distance = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position, 1: geometry_proximity.outputs["Position"]},
        attrs={'operation': 'DISTANCE'})
    
    multiply_add = nw.new_node(Nodes.Math,
        input_kwargs={0: distance.outputs["Value"], 1: group_input.outputs["Sugar dispersion Multiplier"], 2: group_input.outputs["Sugar dispersion  Addend"]},
        attrs={'use_clamp': True, 'operation': 'MULTIPLY_ADD'})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input.outputs["Sugar Size Min"], 3: group_input.outputs["Sugar Size Max"], 'Seed': group_input.outputs["Sugar Size Seed"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_add, 1: random_value_2.outputs[1]},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply, 'Y': multiply, 'Z': multiply})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Instance': store_named_attribute, 'Rotation': random_value_1.outputs[1], 'Scale': combine_xyz})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points, 'Material': surface.shaderfunc_to_material(shader_sugar)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_1, set_material, set_material_2]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_1}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_waffle, selection=selection)
    surface.add_material(obj, shader_syrup, selection=selection)
    surface.add_material(obj, shader_sugar, selection=selection)


import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_churros_sugar(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Specular Tint': 0.5000, 'Roughness': 0.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_churros_main(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': 30.0000, 'Detail': 0.0000, 'Roughness': 0.3722})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: noise_texture.outputs["Fac"], 7: (0.7529, 0.1714, 0.0060, 1.0000)},
        attrs={'blend_type': 'COLOR', 'data_type': 'RGBA'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.3611, 'Height': noise_texture.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Specular Tint': 0.5000, 'Roughness': 0.8970, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Sugar Density', 90.0000),
            ('NodeSocketFloat', 'Sugar Grain Scale', 0.0000),
            ('NodeSocketInt', 'Length Subdiv', 6),
            ('NodeSocketInt', 'Curve Profile Nb Spikes', 7),
            ('NodeSocketFloatDistance', 'Radius', 1.0000),
            ('NodeSocketFloatAngle', 'Twist Degrees', 0.6981),
            ('NodeSocketFloat', 'Imperfections Density', 20.0000),
            ('NodeSocketFloatDistance', 'Imperfections Strength', 0.1700)])
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'End Size': 0})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt,
        input_kwargs={'Curve': group_input.outputs["Geometry"], 'Selection': endpoint_selection_1, 'Tilt': group_input.outputs["Twist Degrees"]})
    
    subdivide_curve_1 = nw.new_node(Nodes.SubdivideCurve,
        input_kwargs={'Curve': set_curve_tilt, 'Cuts': group_input.outputs["Length Subdiv"]})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection)
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius,
        input_kwargs={'Curve': subdivide_curve_1, 'Selection': endpoint_selection, 'Radius': 0.0700})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 0.1400, 'Detail': 0.0000, 'Roughness': 0.0000})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: (0.5000, 0.5000, 0.5000), 'Scale': 1.3000},
        attrs={'operation': 'SCALE'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_curve_radius, 'Offset': scale.outputs["Vector"]})
    
    integer = nw.new_node(Nodes.Integer)
    integer.integer = 10
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: integer, 1: group_input.outputs["Curve Profile Nb Spikes"]},
        attrs={'operation': 'MULTIPLY'})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': multiply, 'Radius': group_input.outputs["Radius"]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    normalize = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position, 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'NORMALIZE'})
    
    curve_profile = nw.new_node(Nodes.VectorMath, input_kwargs={0: position}, label='Curve Profile', attrs={'operation': 'DISTANCE'})
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normalize.outputs["Vector"], 1: curve_profile.outputs["Value"]},
        attrs={'operation': 'MULTIPLY'})
    
    id_2 = nw.new_node(Nodes.InputID)
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: id_2, 1: integer}, attrs={'operation': 'MODULO'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': modulo, 2: integer})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': map_range.outputs["Result"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.4121, 0.3500), (0.5152, 0.5000), (0.6394, 0.3542), (1.0000, 0.0000)])
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_1.outputs["Vector"], 1: (0.5000, 0.5000, 0.5000), 'Scale': float_curve},
        attrs={'operation': 'SCALE'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_circle_1.outputs["Curve"], 'Offset': scale_1.outputs["Vector"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_position, 'Profile Curve': set_position_3, 'Fill Caps': True})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_churros_main)})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    value_2 = nw.new_node(Nodes.Value)
    value_2.outputs[0].default_value = -0.1000
    
    multiply_2 = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal, 1: value_2}, attrs={'operation': 'MULTIPLY'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_shade_smooth, 'Offset': multiply_2.outputs["Vector"]})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': set_position_1, 'Density': group_input.outputs["Imperfections Density"]},
        attrs={'use_legacy_normal': True})
    
    points_to_volume = nw.new_node(Nodes.PointsToVolume,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Voxel Amount': 200.0000, 'Radius': group_input.outputs["Imperfections Strength"]})
    
    volume_to_mesh = nw.new_node(Nodes.VolumeToMesh,
        input_kwargs={'Volume': points_to_volume, 'Threshold': 0.0700, 'Adaptivity': 1.0000})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': volume_to_mesh})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth_1, 'Material': surface.shaderfunc_to_material(shader_churros_main)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, set_material_2]})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': join_geometry, 'Density': group_input.outputs["Sugar Density"]},
        attrs={'use_legacy_normal': True})
    
    ico_sphere = nw.new_node(Nodes.MeshIcoSphere)
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': ico_sphere.outputs["Mesh"], 'Name': 'UVMap', 3: ico_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Sugar Grain Scale"], 1: 10.0000},
        attrs={'operation': 'DIVIDE'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': divide})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute, 'Y': reroute, 'Z': reroute})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': store_named_attribute, 'Scale': combine_xyz})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': instance_on_points, 'Material': surface.shaderfunc_to_material(shader_churros_sugar)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry, set_material_1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_1}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_churros_main, selection=selection)
    surface.add_material(obj, shader_churros_sugar, selection=selection)
apply(bpy.context.active_object)
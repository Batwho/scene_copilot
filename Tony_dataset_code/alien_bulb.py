import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_orb_infect(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    layer_weight = nw.new_node(Nodes.LayerWeight)
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': layer_weight.outputs["Fresnel"]})
    colorramp_6.color_ramp.elements[0].position = 0.1864
    colorramp_6.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 0.7545
    colorramp_6.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': layer_weight.outputs["Facing"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0126, 0.0082, 0.0203, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.5500
    colorramp_1.color_ramp.elements[1].color = [0.0038, 0.0706, 0.0954, 1.0000]
    
    geometry = nw.new_node(Nodes.NewGeometry)
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Location': (-0.0309, 0.0000, 0.0309)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': -1.5600, 'Detail': 15.0000, 'Distortion': 0.3000})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Fac"], 1: 2.2900})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': add, 'Scale': 35.4200, 'Detail': 15.0000, 'Distortion': 2.1000},
        attrs={'noise_dimensions': '1D'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements[0].position = 0.1500
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.9864
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={6: geometry.outputs["Normal"], 7: colorramp.outputs["Color"]},
        attrs={'blend_type': 'LINEAR_LIGHT', 'data_type': 'RGBA'})
    
    glossy_bsdf = nw.new_node(Nodes.GlossyBSDF,
        input_kwargs={'Color': colorramp_1.outputs["Color"], 'Roughness': 0.2615, 'Normal': mix.outputs[2]})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': layer_weight.outputs["Facing"]})
    colorramp_5.color_ramp.elements[0].position = 0.0000
    colorramp_5.color_ramp.elements[0].color = [0.0318, 0.0286, 0.0553, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.6045
    colorramp_5.color_ramp.elements[1].color = [0.0213, 0.4310, 1.0000, 1.0000]
    
    emission = nw.new_node(Nodes.Emission, input_kwargs={'Color': colorramp_5.outputs["Color"], 'Strength': 5.0000})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': colorramp_6.outputs["Color"], 1: glossy_bsdf, 2: emission})
    
    light_path = nw.new_node(Nodes.LightPath)
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp)
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.1089, 0.2113, 1.0000, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 0.9955
    colorramp_3.color_ramp.elements[1].color = [0.3064, 0.0008, 1.0000, 1.0000]
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: light_path.outputs["Is Camera Ray"], 6: colorramp_3.outputs["Color"], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    emission_1 = nw.new_node(Nodes.Emission, input_kwargs={'Color': mix_2.outputs[2], 'Strength': 10.0000})
    
    add_shader_1 = nw.new_node('ShaderNodeAddShader', input_kwargs={0: mix_shader, 1: emission_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': add_shader_1}, attrs={'is_active_output': True})

def shader_orb_infect_stem(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    layer_weight = nw.new_node(Nodes.LayerWeight)
    
    colorramp_6 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': layer_weight.outputs["Fresnel"]})
    colorramp_6.color_ramp.elements[0].position = 0.1864
    colorramp_6.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_6.color_ramp.elements[1].position = 0.7545
    colorramp_6.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': layer_weight.outputs["Facing"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0169, 0.0112, 0.0203, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.5500
    colorramp_1.color_ramp.elements[1].color = [0.0015, 0.0836, 0.0954, 1.0000]
    
    geometry = nw.new_node(Nodes.NewGeometry)
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Generated"], 'Location': (-0.0309, 0.0000, 0.0309)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': -1.5600, 'Detail': 15.0000, 'Distortion': 0.3000})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Fac"], 1: 2.2900})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': add, 'Scale': 35.4200, 'Detail': 15.0000, 'Distortion': 2.1000},
        attrs={'noise_dimensions': '1D'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements[0].position = 0.1500
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.9864
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={6: geometry.outputs["Normal"], 7: colorramp.outputs["Color"]},
        attrs={'blend_type': 'LINEAR_LIGHT', 'data_type': 'RGBA'})
    
    glossy_bsdf = nw.new_node(Nodes.GlossyBSDF,
        input_kwargs={'Color': colorramp_1.outputs["Color"], 'Roughness': 0.8358, 'Normal': mix.outputs[2]})
    
    colorramp_5 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': layer_weight.outputs["Facing"]})
    colorramp_5.color_ramp.elements[0].position = 0.6364
    colorramp_5.color_ramp.elements[0].color = [0.0318, 0.0286, 0.0553, 1.0000]
    colorramp_5.color_ramp.elements[1].position = 0.7773
    colorramp_5.color_ramp.elements[1].color = [0.0213, 0.4310, 1.0000, 1.0000]
    
    emission = nw.new_node(Nodes.Emission, input_kwargs={'Color': colorramp_5.outputs["Color"], 'Strength': 3.4000})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': colorramp_6.outputs["Color"], 1: glossy_bsdf, 2: emission})
    
    light_path = nw.new_node(Nodes.LightPath)
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp)
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.1053, 0.1172, 0.2104, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 1.0000
    colorramp_3.color_ramp.elements[1].color = [0.0236, 0.8079, 1.0000, 1.0000]
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: light_path.outputs["Is Camera Ray"], 6: colorramp_3.outputs["Color"], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    emission_1 = nw.new_node(Nodes.Emission, input_kwargs={'Color': mix_2.outputs[2], 'Strength': 1.8000})
    
    add_shader_1 = nw.new_node('ShaderNodeAddShader', input_kwargs={0: mix_shader, 1: emission_1})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': add_shader_1}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    ico_sphere = nw.new_node(Nodes.MeshIcoSphere, input_kwargs={'Radius': 0.1420, 'Subdivisions': 2})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': ico_sphere.outputs["Mesh"], 'Name': 'UVMap', 3: ico_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    dual_mesh = nw.new_node(Nodes.DualMesh, input_kwargs={'Mesh': store_named_attribute, 'Keep Boundaries': True})
    
    normal_1 = nw.new_node(Nodes.InputNormal)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': normal_1})
    
    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Extrude', 0.5000),
            ('NodeSocketInt', 'Bulb Subdivisions', 2),
            ('NodeSocketFloatFactor', 'Bulb Crease', 0.3154),
            ('NodeSocketFloatDistance', 'Knob Radius', 0.0300),
            ('NodeSocketFloat', 'Knob Scale', 3.0000),
            ('NodeSocketInt', 'Knob Subdivisions', 2),
            ('NodeSocketFloatFactor', 'Knob Crease', 0.6615),
            ('NodeSocketFloat', 'Adjust Instance Height', 0.8600),
            ('NodeSocketFloat', 'Z Cutoff', -0.6000),
            ('NodeSocketObject', 'Instance Object',None),# bpy.data.objects['Icosphere.002']),
            ('NodeSocketFloat', 'Instance Scale', 1.0000),
            ('NodeSocketFloat', 'Leaves Scale (experimental', 0.5000),
            ('NodeSocketMaterial', 'Material', None)])#surface.shaderfunc_to_material(shader_orb_infect))])
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: separate_xyz.outputs["Z"], 1: group_input_1.outputs["Z Cutoff"]})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': dual_mesh, 'Selection': greater_than, 'Offset Scale': group_input_1.outputs["Extrude"]})
    
    mesh_to_points = nw.new_node(Nodes.MeshToPoints,
        input_kwargs={'Mesh': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Radius': 0.0100},
        attrs={'mode': 'FACES'})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_1, 1: (0.2767, 0.2722, -0.3270)},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': multiply.outputs["Vector"], 'W': 2.7000, 'Scale': 7.6600, 'Detail': 4.0000, 'Roughness': 0.1854},
        attrs={'noise_dimensions': '4D'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements[0].position = 0.4636
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.6364
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    normal = nw.new_node(Nodes.InputNormal)
    
    multiply_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: colorramp.outputs["Color"], 1: normal},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_1.outputs["Vector"], 1: (0.0100, 0.0100, 0.0100)},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': 61.7366, 'Scale': 0.2000, 'Detail': 4.0000, 'Roughness': 0.6271},
        attrs={'noise_dimensions': '4D'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Vector': noise_texture_1.outputs["Color"], 9: (-1.0000, -1.0000, -1.0000)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo,
        input_kwargs={'Object': bpy.data.objects['Bulb']},
        attrs={'transform_space': 'RELATIVE'})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    distance = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: object_info_1.outputs["Location"], 1: position_2},
        attrs={'operation': 'DISTANCE'})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': distance.outputs["Value"]})
    colorramp_1.color_ramp.interpolation = "B_SPLINE"
    colorramp_1.color_ramp.elements[0].position = 0.4591
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.7136
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    multiply_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: map_range.outputs["Vector"], 1: colorramp_1.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: multiply_3.outputs["Vector"], 1: (0.3000, 0.3000, 0.3000)},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: multiply_2.outputs["Vector"], 1: multiply_4.outputs["Vector"]})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_to_points, 'Offset': add.outputs["Vector"]})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': group_input_1.outputs["Instance Object"]})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': object_info.outputs["Geometry"], 'Translation': (-0.0170, -0.0170, -0.0013)})
    
    position = nw.new_node(Nodes.InputPosition)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': position}, attrs={'axis': 'Z'})
    
    add_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: align_euler_to_vector, 1: (3.1416, 0.0000, 0.0000)})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_1, 'Instance': transform, 'Rotation': add_1.outputs["Vector"], 'Scale': group_input_1.outputs["Knob Scale"]})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': extrude_mesh.outputs["Mesh"], 'Level': group_input_1.outputs["Bulb Subdivisions"], 'Edge Crease': group_input_1.outputs["Bulb Crease"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': subdivision_surface, 'Material': group_input_1.outputs["Material"]})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_material, 'Offset': add.outputs["Vector"]})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [instance_on_points_2, set_position]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry_2})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_shade_smooth}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_orb_infect_stem, selection=selection)
apply(bpy.context.active_object)
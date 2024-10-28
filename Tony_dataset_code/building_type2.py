import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_scalar_multiple', singleton=False, type='ShaderNodeTree')
def nodegroup_scalar_multiple(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    input1 =nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketColor', 'Vector', (0.8000, 0.8000, 0.8000, 1.0000)),
            ('NodeSocketFloat', 'Scalar', 0.0000)])
    
    rgb_2 = nw.new_node(Nodes.SeparateColor, input_kwargs={'Color': input1.outputs["Vector"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: rgb_2.outputs["Red"], 1: input1.outputs["Scalar"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: rgb_2.outputs["Green"], 1: input1.outputs["Scalar"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: rgb_2.outputs["Blue"], 1: input1.outputs["Scalar"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    _1 = nw.new_node(Nodes.CombineColor, input_kwargs={'Red': multiply, 'Green': multiply_1, 'Blue': multiply_2})
    
    _2 = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': _1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_hit', singleton=False, type='ShaderNodeTree')
def nodegroup_hit(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    input2 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketColor', 'incoming', (0.8000, 0.8000, 0.8000, 1.0000)),
            ('NodeSocketVector', 'p', (0.5000, 0.5000, 0.5000)),
            ('NodeSocketFloat', 'p_s', 0.5000),
            ('NodeSocketFloat', 'incoming_s', 0.5000),
            ('NodeSocketFloat', 'Coordinate', -1.0000)])
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: input2.outputs["Coordinate"], 1: input2.outputs["p_s"], 2: 0.0000},
        attrs={'operation': 'SUBTRACT'})
    
    divide = nw.new_node(Nodes.Math,
        input_kwargs={0: subtract, 1: input2.outputs["incoming_s"], 2: 0.0000},
        attrs={'operation': 'DIVIDE'})
    
    node1 = nw.new_node(nodegroup_scalar_multiple().name, input_kwargs={'Vector': input2.outputs["incoming"], 'Scalar': divide})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: node1, 1: input2.outputs["p"]})
    
    _1 = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': add.outputs["Vector"]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_calc_r', singleton=False, type='ShaderNodeTree')
def nodegroup_calc_r(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    input3 = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000))])
    
    xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': input3.outputs["Vector"]})
    
    power = nw.new_node(Nodes.Math, input_kwargs={0: xyz_3.outputs["X"], 1: 2.0000, 2: 0.0000}, attrs={'operation': 'POWER'})
    
    power_1 = nw.new_node(Nodes.Math, input_kwargs={0: xyz_3.outputs["Y"], 1: 2.0000, 2: 0.0000}, attrs={'operation': 'POWER'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: power, 1: power_1, 2: 0.0000})
    
    power_2 = nw.new_node(Nodes.Math, input_kwargs={0: xyz_3.outputs["Z"], 1: 2.0000, 2: 0.0000}, attrs={'operation': 'POWER'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: power_2, 2: 0.0000})
    
    power_3 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 2: 0.0000}, attrs={'operation': 'POWER'})
    
    _1 = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': power_3}, attrs={'is_active_output': True})

def shader_balcony(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0000, 0.0000, 0.0000, 1.0000), 'Specular': 0.6901, 'Roughness': 0.8678})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_006', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_006(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    cylinder = nw.new_node('GeometryNodeMeshCylinder', input_kwargs={'Vertices': 128, 'Radius': 0.0600, 'Depth': 0.3500})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': store_named_attribute, 'Selection': cylinder.outputs["Top"], 'Offset Scale': -0.0100})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': 2.5000})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': scale_elements, 'Selection': extrude_mesh.outputs["Top"], 'Offset Scale': 0.1000})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Selection': extrude_mesh_1.outputs["Top"], 'Scale': 0.0000})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': scale_elements_1, 'Material': surface.shaderfunc_to_material(shader_degradable_metal)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_chimney', singleton=False, type='GeometryNodeTree')
def nodegroup_chimney(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatDistance', 'Depth', 1.2000),
            ('NodeSocketFloatDistance', 'Radius', 0.2000)])
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': 64, 'Radius': group_input.outputs["Radius"], 'Depth': group_input.outputs["Depth"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': store_named_attribute, 'Selection': cylinder.outputs["Top"], 'Offset Scale': 0.0000})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Selection': extrude_mesh_1.outputs["Top"], 'Scale': 0.6900})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Depth"], 1: -1.4200}, attrs={'operation': 'DIVIDE'})
    
    extrude_mesh_2 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': scale_elements_1, 'Selection': extrude_mesh_1.outputs["Top"], 'Offset Scale': divide})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: extrude_mesh_2.outputs["Side"], 1: cylinder.outputs["Side"]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': extrude_mesh_2.outputs["Mesh"], 'Selection': add, 'Shade Smooth': False})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_chimney)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_random_picker_chimney', singleton=False, type='GeometryNodeTree')
def nodegroup_random_picker_chimney(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'W', 0.0000),
            ('NodeSocketFloat', 'Value', 30.5000),
            ('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000))])
    
    white_noise_texture = nw.new_node(Nodes.WhiteNoiseTexture, input_kwargs={'W': group_input.outputs["W"]}, attrs={'noise_dimensions': '4D'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 50.0000}, attrs={'operation': 'DIVIDE'})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: white_noise_texture.outputs["Color"], 1: divide},
        attrs={'operation': 'GREATER_THAN'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': greater_than}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_paralax', singleton=False, type='ShaderNodeTree')
def nodegroup_paralax(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    node1 = nw.new_node(Nodes.NewGeometry)
    
    node3 = nw.new_node('ShaderNodeVectorTransform', input_kwargs={'Vector': node1.outputs["Incoming"]})
    
    node44 = nw.new_node(nodegroup_scalar_multiple().name, input_kwargs={'Vector': node3, 'Scalar': -1.0000})
    
    node2 = nw.new_node('ShaderNodeVectorTransform',
        input_kwargs={'Vector': node1.outputs["Position"]},
        attrs={'vector_type': 'POINT'})
    
    node6 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': node2, 'Location': (-0.5300, 0.0000, -0.5200), 'Scale': (1.1000, 1.1000, 1.1000)})
    
    xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': node6})
    
    xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': node44})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: xyz_3.outputs["Z"], 1: 0.0000, 2: 0.0000},
        attrs={'operation': 'GREATER_THAN'})
    
    node7 = nw.new_node(Nodes.Value)
    node7.outputs[0].default_value = -0.5000
    
    node10 = nw.new_node(Nodes.Value)
    node10.outputs[0].default_value = 0.5000
    
    node5 = nw.new_node(Nodes.Mix, input_kwargs={0: greater_than, 6: node7, 7: node10}, attrs={'data_type': 'RGBA'})
    
    node28 = nw.new_node(nodegroup_hit().name,
        input_kwargs={'incoming': node44, 'p': node6, 'p_s': xyz_2.outputs["Z"], 'incoming_s': xyz_3.outputs["Z"], 'Coordinate': node5.outputs[2]})
    
    node25 = nw.new_node(nodegroup_calc_r().name, input_kwargs={'Vector': node28})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': node25})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    greater_than_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: xyz_3.outputs["X"], 1: 0.0000, 2: 0.0000},
        attrs={'operation': 'GREATER_THAN'})
    
    node8 = nw.new_node(Nodes.Value)
    node8.outputs[0].default_value = -0.5000
    
    node9 = nw.new_node(Nodes.Value)
    node9.outputs[0].default_value = 0.5000
    
    node9_1 = nw.new_node(Nodes.Mix, input_kwargs={0: greater_than_1, 6: node8, 7: node9}, attrs={'data_type': 'RGBA'})
    
    node26 = nw.new_node(nodegroup_hit().name,
        input_kwargs={'incoming': node44, 'p': node6, 'p_s': xyz_2.outputs["X"], 'incoming_s': xyz_3.outputs["X"], 'Coordinate': node9_1.outputs[2]})
    
    node23 = nw.new_node(nodegroup_calc_r().name, input_kwargs={'Vector': node26})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': node23})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: reroute_25, 1: reroute_22, 2: 0.0000}, attrs={'operation': 'LESS_THAN'})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': node23})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    node8_1 = nw.new_node(Nodes.Mix, input_kwargs={0: less_than, 6: reroute_27, 7: reroute_24}, attrs={'data_type': 'RGBA'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': node8_1.outputs[2]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    node11 = nw.new_node(Nodes.Value)
    node11.outputs[0].default_value = 0.9400
    
    node27 = nw.new_node(nodegroup_hit().name,
        input_kwargs={'incoming': node44, 'p': node6, 'p_s': xyz_2.outputs["Y"], 'incoming_s': xyz_3.outputs["Y"], 'Coordinate': node11})
    
    node24 = nw.new_node(nodegroup_calc_r().name, input_kwargs={'Vector': node27})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': node24})
    
    less_than_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_15, 1: reroute_2, 2: 0.0000}, attrs={'operation': 'LESS_THAN'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': less_than_1})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    node7_1 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': node27, 'Location': (0.5000, 0.0000, 0.5000), 'Rotation': (1.5708, 0.0000, 0.0000), 'Scale': (1.9900, 2.0000, 5.0000)},
        attrs={'vector_type': 'TEXTURE'})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': node7_1})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    node5_1 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': node26, 'Location': (0.0000, 3.8000, 0.4900), 'Rotation': (-1.5708, 1.5708, -1.5708), 'Scale': (1.9800, 1.9000, 5.0000)},
        attrs={'vector_type': 'TEXTURE'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': node5_1})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    node1_1 = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': node28, 'Location': (-0.5500, 0.9300, 0.0000), 'Scale': (2.0900, 1.8700, 5.0000)},
        attrs={'vector_type': 'TEXTURE'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': node1_1})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    node4 = nw.new_node(Nodes.Mix, input_kwargs={0: less_than, 6: reroute_4, 7: reroute_5}, attrs={'data_type': 'RGBA'})
    
    node10_1 = nw.new_node(Nodes.Mix, input_kwargs={0: reroute_14, 6: reroute_9, 7: node4.outputs[2]}, attrs={'data_type': 'RGBA'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Color': node10_1.outputs[2]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_008', singleton=False, type='ShaderNodeTree')
def nodegroup_node_group_008(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketFloatFactor', 'Strength', 0.0917)])
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 0.0700, 'Detail': 15.1000, 'Roughness': 0.8250})
    
    musgrave_texture = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': noise_texture.outputs["Color"], 'Scale': 0.0700, 'Detail': 16.0000, 'Dimension': 152.9000, 'Lacunarity': 12.6000})
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': group_input.outputs["Strength"], 'Distance': 0.5000, 'Height': musgrave_texture})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Normal': bump}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_015', singleton=False, type='ShaderNodeTree')
def nodegroup_node_group_015(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 7.1000, 'Detail': 15.4000, 'Roughness': 0.8167})
    
    musgrave_texture_1 = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': noise_texture_2.outputs["Color"], 'Scale': 1.0000, 'Detail': 4.6000, 'Dimension': 0.0000, 'Lacunarity': 7.0000})
    
    dustamt = nw.new_node(Nodes.GroupInput, label='Dustamt', expose_input=[('NodeSocketFloatFactor', 'Wear', 0.0000)])
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: musgrave_texture_1, 1: dustamt.outputs["Wear"], 2: 0.0000})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': add})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.8955
    colorramp_1.color_ramp.elements[1].color = [0.8770, 0.0763, 0.1826, 1.0000]
    
    vector_curves = nw.new_node(Nodes.VectorCurve, input_kwargs={'Fac': 0.0000, 'Vector': colorramp_1.outputs["Color"]})
    node_utils.assign_curve(vector_curves.mapping.curves[0], [(-1.0000, -1.0000), (-0.4273, 0.0375), (0.2273, 0.2500), (0.6000, 0.7000), (1.0000, 1.0000)])
    node_utils.assign_curve(vector_curves.mapping.curves[1], [(-1.0000, -1.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(vector_curves.mapping.curves[2], [(-1.0000, -1.0000), (1.0000, 1.0000)])
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': vector_curves}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_016', singleton=False, type='ShaderNodeTree')
def nodegroup_node_group_016(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': 28.6000, 'Detail': 11.5000, 'Roughness': 0.9750, 'Distortion': -0.8000})
    
    color_ramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]}, label='color ramp')
    color_ramp.color_ramp.elements[0].position = 0.0000
    color_ramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    color_ramp.color_ramp.elements[1].position = 0.6591
    color_ramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Color': color_ramp.outputs["Color"]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_017', singleton=False, type='ShaderNodeTree')
def nodegroup_node_group_017(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping, input_kwargs={'Vector': texture_coordinate.outputs["UV"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': mapping, 'Scale': 1.9000, 'Detail': 16.0000, 'Roughness': 1.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.0145, 0.0095, 0.0059, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [1.0000, 0.8057, 0.6350, 1.0000]
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Color': colorramp.outputs["Color"]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_ground', singleton=False, type='GeometryNodeTree')
def nodegroup_ground(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Value length1', 0.5000),
            ('NodeSocketFloat', 'Value width1', 0.5000),
            ('NodeSocketFloat', 'Value width', 0.5000),
            ('NodeSocketFloat', 'Value length', 0.5000),
            ('NodeSocketFloat', 'Value ground', 45.0000),
            ('NodeSocketFloat', 'Value curb extrusion', 1.0000),
            ('NodeSocketFloat', 'Value curb size', 985.0000)])
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value width1"], 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value ground"], 1: 15.0000}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: divide})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value length1"], 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_1, 1: divide})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value width"], 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value length"], 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    grid_2 = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': add, 'Size Y': add_1, 'Vertices X': multiply, 'Vertices Y': multiply_1})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid_2.outputs["Mesh"], 'Name': 'uv_map', 3: grid_2.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 0.0100
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: value, 1: -1.0000}, attrs={'operation': 'DIVIDE'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': divide_1})
    
    transform_7 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute, 'Translation': separate_xyz.outputs["Z"]})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': transform_7, 'Offset Scale': 0.0000})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': 0.9900})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': scale_elements_1, 'Selection': extrude_mesh.outputs["Top"], 'Offset Scale': value})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_ground)})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: add, 1: 0.1000})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: 0.1000})
    
    grid_3 = nw.new_node(Nodes.MeshGrid, input_kwargs={'Size X': add_2, 'Size Y': add_3, 'Vertices X': 2, 'Vertices Y': 2})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid_3.outputs["Mesh"], 'Name': 'uv_map', 3: grid_3.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    transform_8 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_1})
    
    divide_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value curb extrusion"], 1: 50.0000}, attrs={'operation': 'DIVIDE'})
    
    extrude_mesh_2 = nw.new_node(Nodes.ExtrudeMesh, input_kwargs={'Mesh': transform_8, 'Offset Scale': divide_2})
    
    extrude_mesh_3 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': extrude_mesh_2.outputs["Mesh"], 'Selection': extrude_mesh_2.outputs["Top"], 'Offset Scale': 0.0000})
    
    divide_3 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value curb size"], 1: 1000.0000}, attrs={'operation': 'DIVIDE'})
    
    scale_elements_2 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh_3.outputs["Mesh"], 'Selection': extrude_mesh_3.outputs["Top"], 'Scale': divide_3})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: divide_2, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: 0.0010}, attrs={'operation': 'SUBTRACT'})
    
    extrude_mesh_4 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': scale_elements_2, 'Selection': extrude_mesh_3.outputs["Top"], 'Offset Scale': subtract_2})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': extrude_mesh_4.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_ground_2)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={"Geometry1": set_material, "Geometry2": set_material_1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_rooftop', singleton=False, type='GeometryNodeTree')
def nodegroup_rooftop(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Vertices X', 3),
            ('NodeSocketInt', 'Vertices Y', 3),
            ('NodeSocketFloat', 'Value sub1', 0.5000),
            ('NodeSocketFloat', 'Value sub2', 0.5000),
            ('NodeSocketFloat', 'Value div', 0.5000),
            ('NodeSocketMaterial', 'Material', None),#surface.shaderfunc_to_material(shader_roof)),
            ('NodeSocketFloat', 'W', 0.8000),
            ('NodeSocketFloat', 'Value ran', 44.0000),
            ('NodeSocketBool', 'Switch', False)])
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value sub1"], 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value sub2"], 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    grid_2 = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': subtract, 'Size Y': subtract_1, 'Vertices X': group_input.outputs["Vertices X"], 'Vertices Y': group_input.outputs["Vertices Y"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid_2.outputs["Mesh"], 'Name': 'uv_map', 3: grid_2.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value div"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: -0.1000})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': 5.5000, 'Z': add})
    
    transform_7 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute, 'Translation': combine_xyz_5})
    
    set_material = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': transform_7, 'Material': group_input.outputs["Material"]})
    
    scale_elements = nw.new_node(Nodes.ScaleElements, input_kwargs={'Geometry': transform_7, 'Scale': 0.8000})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_elements})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["W"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Value ran"]})
    
    random_picker_chimney = nw.new_node(nodegroup_random_picker_chimney().name, input_kwargs={'W': reroute_2, 'Value': reroute_1})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 0.3000
    
    value_1 = nw.new_node(Nodes.Value)
    value_1.outputs[0].default_value = 0.0500
    
    chimney = nw.new_node(nodegroup_chimney().name, input_kwargs={'Depth': value, 'Radius': value_1})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: value, 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': divide_1})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': chimney, 'Translation': separate_xyz.outputs["Z"]})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute, 'Selection': random_picker_chimney, 'Instance': transform})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: 0.0100})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: 0.0100})
    
    random_picker_chimney_1 = nw.new_node(nodegroup_random_picker_chimney().name, input_kwargs={'W': add_1, 'Value': add_2})
    
    nodegroup_006 = nw.new_node(nodegroup_node_group_006().name)
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': nodegroup_006, 'Translation': (0.0000, 0.0000, 0.1000)})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute, 'Selection': random_picker_chimney_1, 'Instance': transform_1})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [instance_on_points, instance_on_points_1]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Switch"], 15: join_geometry_1})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Cube'], 'As Instance': True})
    
    transform_8 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': object_info.outputs["Geometry"], 'Translation': combine_xyz_5})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_1})
    
    multiply_add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: reroute_5, 2: 100.0000}, attrs={'operation': 'MULTIPLY_ADD'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': multiply_add})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': combine_xyz_5})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_1.outputs["Z"], 1: 0.0200})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_1.outputs["X"], 'Y': separate_xyz_1.outputs["Y"], 'Z': add_3})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: subtract_2}, attrs={'operation': 'MULTIPLY'})
    
    subtract_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_3}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply, 'Y': multiply_1, 'Z': 1.0000})
    
    transform_2 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Translation': combine_xyz_1, 'Scale': combine_xyz})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 0.8000, 'Detail': 0.0000, 'Roughness': 0.0000})
    
    subtract_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Fac"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract_4.outputs["Vector"], 1: (0.5000, 0.5000, 0.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    scale = nw.new_node(Nodes.VectorMath, input_kwargs={0: multiply_2.outputs["Vector"]}, attrs={'operation': 'SCALE'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': transform_2, 'Offset': scale.outputs["Vector"]})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 16, 'Radius': 0.0035})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_position, 'Profile Curve': curve_circle_1.outputs["Curve"]})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_degradable_metal)})
    
    multiply_add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: reroute_5, 2: -3.0000}, attrs={'operation': 'MULTIPLY_ADD'})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position, 'Count': multiply_add_1})
    
    value_2 = nw.new_node(Nodes.Value)
    value_2.outputs[0].default_value = 0.0400
    
    cube = nw.new_node(Nodes.MeshCube, input_kwargs={'Size': value_2})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': resample_curve, 'Instance': store_named_attribute_1})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': instance_on_points_2, 'Translation': (0.0000, 0.0000, -0.0100)})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': transform_3, 'Material': surface.shaderfunc_to_material(shader_balcony)})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_2, set_material_1]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_2})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: True, 15: reroute_4})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [set_material, switch.outputs[6], transform_8, switch_1.outputs[6]]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_003', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_003(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Value', 0.5000)])
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_3})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_3.outputs["X"], 1: subtract}, attrs={'operation': 'LESS_THAN'})
    
    separate_geometry_3 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': less_than})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Selection': separate_geometry_3.outputs["Selection"], 'Inverted': separate_geometry_3.outputs["Inverted"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_002', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_002(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Value', 0.5000)])
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: subtract}, attrs={'operation': 'LESS_THAN'})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': less_than})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Selection': separate_geometry.outputs["Selection"], 'Inverted': separate_geometry.outputs["Inverted"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_001', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Value', 0.5000)])
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_2.outputs["X"], 1: subtract}, attrs={'operation': 'LESS_THAN'})
    
    separate_geometry_2 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': less_than})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': separate_geometry_2.outputs["Inverted"], 'Translation': (0.0000, 0.0000, 1.0000)})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Selection': separate_geometry_2.outputs["Selection"], 'Inverted': transform},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Value', 0.5000)])
    
    position_8 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_8 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_8})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: -1.2000}, attrs={'operation': 'SUBTRACT'})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_8.outputs["Z"], 1: subtract},
        attrs={'operation': 'GREATER_THAN'})
    
    separate_geometry_1 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': greater_than})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Inverted': separate_geometry_1.outputs["Inverted"], 'Selection': separate_geometry_1.outputs["Selection"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_004', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_004(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Value1', 0.5000),
            ('NodeSocketFloat', 'Value2', 0.5000),
            ('NodeSocketGeometry', 'Geometry', None)])
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value1"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 5.0000})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': add})
    
    transform_2 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Translation': combine_xyz, 'Rotation': (0.0000, 0.0000, 3.1416)})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value2"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: divide_1, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 6.0000})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': add_1})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Translation': combine_xyz_1})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_2, transform_1]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_1}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_random_picker', singleton=False, type='GeometryNodeTree')
def nodegroup_random_picker(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'W', 0.0000),
            ('NodeSocketFloat', 'Value', 30.5000),
            ('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000))])
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={3: 3.0000, 'Seed': group_input.outputs["W"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': random_value.outputs[1]}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_random_picker_1st', singleton=False, type='GeometryNodeTree')
def nodegroup_random_picker_1st(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'W', 0.0000),
            ('NodeSocketFloat', 'Value', 30.5000),
            ('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000))])
    
    white_noise_texture = nw.new_node(Nodes.WhiteNoiseTexture,
        input_kwargs={'Vector': group_input.outputs["Vector"], 'W': group_input.outputs["W"]},
        attrs={'noise_dimensions': '4D'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 50.0000}, attrs={'operation': 'DIVIDE'})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: white_noise_texture.outputs["Color"], 1: divide},
        attrs={'operation': 'GREATER_THAN'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': greater_than}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_010', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_010(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Value', 0.5000)])
    
    position_9 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_10 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_9})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    less_than = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_10.outputs["X"], 1: subtract},
        attrs={'operation': 'LESS_THAN'})
    
    separate_geometry_10 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': less_than})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': separate_geometry_10.outputs["Inverted"], 'Translation': (0.0000, 0.0000, 1.0000)})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Selection': separate_geometry_10.outputs["Selection"], 'Inverted': transform},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_009', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_009(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Value', 0.5000),
            ('NodeSocketGeometry', 'Geometry', None)])
    
    position_11 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_9 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_11})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: -1.2000}, attrs={'operation': 'SUBTRACT'})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_9.outputs["Z"], 1: subtract},
        attrs={'operation': 'GREATER_THAN'})
    
    separate_geometry_8 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': greater_than})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Inverted': separate_geometry_8.outputs["Inverted"], 'Selection': separate_geometry_8.outputs["Selection"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_011', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_011(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Value', 0.5000),
            ('NodeSocketGeometry', 'Geometry', None)])
    
    position_8 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_11 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_8})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    less_than = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_11.outputs["Z"], 1: subtract},
        attrs={'operation': 'LESS_THAN'})
    
    separate_geometry_11 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': less_than})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Selection': separate_geometry_11.outputs["Selection"], 'Inverted': separate_geometry_11.outputs["Inverted"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_012', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_012(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Value', 0.5000)])
    
    position_10 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_8 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_10})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_8.outputs["X"], 1: subtract}, attrs={'operation': 'LESS_THAN'})
    
    separate_geometry_9 = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Selection': less_than})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Selection': separate_geometry_9.outputs["Selection"], 'Inverted': separate_geometry_9.outputs["Inverted"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_005', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_005(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Value1', 0.5000),
            ('NodeSocketFloat', 'Value2', 0.5000),
            ('NodeSocketGeometry', 'Geometry', None)])
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value1"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: -0.5000})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add, 'Y': 5.5000})
    
    transform_4 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Translation': combine_xyz_2, 'Rotation': (0.0000, 0.0000, 1.5708)})
    
    divide_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value2"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: divide_1, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add_1, 'Y': 5.5000})
    
    transform_5 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Translation': combine_xyz_3, 'Rotation': (0.0000, 0.0000, -1.5708)})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_4, transform_5]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_3}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_node_group_007', singleton=False, type='GeometryNodeTree')
def nodegroup_node_group_007(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Value', 0.5000),
            ('NodeSocketGeometry', 'Geometry', None)])
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Value"], 1: 2.0000}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide, 1: -0.5000})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add})
    
    transform_6 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': group_input.outputs["Geometry"], 'Translation': combine_xyz_4})
    
    transform_8 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_6, 'Translation': (0.0000, -5.5000, 0.0000)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform_8}, attrs={'is_active_output': True})

def shader_glass(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    object_info = nw.new_node(Nodes.ObjectInfo_Shader)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': object_info.outputs["Random"], 'Detail': 5.0000},
        attrs={'noise_dimensions': '4D'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': noise_texture.outputs["Fac"], 4: 0.2000})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.0000, 0.0000, 0.0000, 1.0000), 'Subsurface IOR': 0.0000, 'Roughness': map_range.outputs["Result"], 'Alpha': 0.3967})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_paralax(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    object_info_1 = nw.new_node(Nodes.ObjectInfo_Shader)
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': object_info_1.outputs["Random"]})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_3})
    colorramp_1.color_ramp.interpolation = "CONSTANT"
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements.new(0)
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.2500
    colorramp_1.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[2].position = 0.5000
    colorramp_1.color_ramp.elements[2].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_1.color_ramp.elements[3].position = 0.7500
    colorramp_1.color_ramp.elements[3].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_1.color_ramp.elements[4].position = 1.0000
    colorramp_1.color_ramp.elements[4].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    colorramp_4 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute_3})
    colorramp_4.color_ramp.interpolation = "CONSTANT"
    colorramp_4.color_ramp.elements.new(0)
    colorramp_4.color_ramp.elements[0].position = 0.0045
    colorramp_4.color_ramp.elements[0].color = [1.0000, 1.0000, 1.0000, 1.0000]
    colorramp_4.color_ramp.elements[1].position = 0.5000
    colorramp_4.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp_4.color_ramp.elements[2].position = 1.0000
    colorramp_4.color_ramp.elements[2].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    group_1 = nw.new_node(nodegroup_paralax().name)
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_1})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute_1},
        attrs={'image': bpy.data.images['Background.png.001']})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Value': 0.0000, 'Fac': 0.9750, 'Color': image_texture.outputs["Color"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': hue_saturation_value})
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 0.1000
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': value})
    
    principled_bsdf_4 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': reroute_4, 'Specular': 0.0000, 'Roughness': 0.6455, 'Emission': reroute_4, 'Emission Strength': reroute},
        attrs={'subsurface_method': 'BURLEY'})
    
    image_texture_1 = nw.new_node(Nodes.ShaderImageTexture, input_kwargs={'Vector': group_1}, attrs={'image': bpy.data.images['Room.png']})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: 1.0000}, attrs={'operation': 'SUBTRACT'})
    
    principled_bsdf_3 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': image_texture_1.outputs["Color"], 'Specular': 0.0000, 'Roughness': 0.6455, 'Emission': image_texture_1.outputs["Color"], 'Emission Strength': subtract},
        attrs={'subsurface_method': 'BURLEY'})
    
    mix_shader = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': colorramp_4.outputs["Color"], 1: principled_bsdf_4, 2: principled_bsdf_3})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 50.0000, 'Detail': 5.0000})
    
    hue_saturation_value_4 = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Saturation': 0.5000, 'Value': 0.0100, 'Color': noise_texture.outputs["Color"]})
    
    principled_bsdf_7 = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': hue_saturation_value_4, 'Specular': 0.0000, 'Roughness': 0.6455},
        attrs={'subsurface_method': 'BURLEY'})
    
    mix_shader_1 = nw.new_node(Nodes.MixShader,
        input_kwargs={'Fac': colorramp_1.outputs["Color"], 1: mix_shader, 2: principled_bsdf_7})
    
    material_output_2 = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader_1}, attrs={'is_active_output': True})

def shader_roof(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 256.0000, 'Detail': 15.0000, 'Roughness': 0.7500})
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture_1.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.0000
    colorramp_1.color_ramp.elements[0].color = [0.0169, 0.0169, 0.0169, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 1.0000
    colorramp_1.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 64.6000, 'Detail': 10.0000, 'Roughness': 0.6333})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': noise_texture.outputs["Fac"], 3: 0.6620, 4: 0.8270})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 420.0000, 'Detail': 15.0000, 'Roughness': 0.8000})
    
    brick_texture = nw.new_node(Nodes.BrickTexture,
        input_kwargs={'Color2': (1.0000, 1.0000, 1.0000, 1.0000), 'Scale': 3.0000, 'Mortar Size': 0.0020})
    
    bump_1 = nw.new_node(Nodes.Bump, input_kwargs={'Height': brick_texture.outputs["Fac"]}, attrs={'invert': True})
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.1000, 'Height': noise_texture_2.outputs["Fac"], 'Normal': bump_1})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp_1.outputs["Color"], 'Roughness': map_range.outputs["Result"], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_ground_2(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.1470, 0.1620, 0.1070, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_ground(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.4735, 0.4735, 0.3712, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_chimney(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': (0.0000, 0.0000, 0.0000, 1.0000)})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_degradable_metal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 10.0000, 'Detail': 5.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.4500
    colorramp.color_ramp.elements[0].color = [0.8528, 0.8528, 0.8528, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.8682
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    color = nw.new_node(nodegroup_node_group_017().name, label='Color')
    
    change_c2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: 1.0000, 6: color, 7: (1.0000, 0.8787, 0.7781, 1.0000)},
        label='ChangeC2',
        attrs={'data_type': 'RGBA'})
    
    color_opacity = nw.new_node(nodegroup_node_group_016().name, label='ColorOpacity')
    
    c2opacity = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.0000, 6: change_c2.outputs[2], 7: color_opacity},
        label='c2opacity',
        attrs={'data_type': 'RGBA', 'clamp_result': True})
    
    c2opacity_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp.outputs["Color"], 6: c2opacity.outputs[2], 7: (0.0698, 0.0083, 0.0031, 1.0000)},
        label='c2opacity',
        attrs={'data_type': 'RGBA', 'clamp_result': True})
    
    roughness = nw.new_node(nodegroup_node_group_015().name, input_kwargs={'Wear': 1.0000}, label='Roughness')
    
    bump = nw.new_node(nodegroup_node_group_008().name, input_kwargs={'Strength': 0.2000}, label='Bump')
    
    master = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': c2opacity_1.outputs[2], 'Metallic': 1.0000, 'Specular': 0.2182, 'Roughness': roughness, 'Sheen Tint': 0.0000, 'IOR': 21.4000, 'Normal': bump},
        label='Master',
        attrs={'subsurface_method': 'BURLEY'})
    
    output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': master}, label='Output', attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_13 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketInt', 'Width', 6),
            ('NodeSocketInt', 'Length', 6),
            ('NodeSocketInt', 'Height', 3),
            ('NodeSocketFloat', '1st floor seed', -5.1000),
            ('NodeSocketFloat', 'Amoount', 35.7000),
            ('NodeSocketFloat', 'Seed 11', 3.0000),
            ('NodeSocketFloat', 'Seed 2', 0.0000),
            ('NodeSocketFloat', 'Window seed', 0.0000),
            ('NodeSocketFloat', 'Seed 1', 0.5000),
            ('NodeSocketFloat', 'Seed 22', 0.5000),
            ('NodeSocketBool', 'Chimney', False),
            ('NodeSocketFloat', 'Seed', 0.8000),
            ('NodeSocketFloat', 'Amound', 44.0000),
            ('NodeSocketBool', 'Ground', False),
            ('NodeSocketFloat', 'Ground size', 45.0000),
            ('NodeSocketFloat', 'Curb size', 985.0000),
            ('NodeSocketFloat', 'Curb extrudion', 1.0000)])
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_13.outputs["Length"], 1: 1.0000},
        attrs={'operation': 'SUBTRACT'})
    
    subtract_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_13.outputs["Height"], 1: 1.0000},
        attrs={'operation': 'SUBTRACT'})
    
    grid_1 = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': subtract, 'Size Y': subtract_1, 'Vertices X': group_input_13.outputs["Length"], 'Vertices Y': group_input_13.outputs["Height"]})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid_1.outputs["Mesh"], 'Name': 'uv_map', 3: grid_1.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute_1, 'Rotation': (1.5708, 0.0000, 0.0000)})
    
    nodegroup_011 = nw.new_node(nodegroup_node_group_011().name,
        input_kwargs={'Value': group_input_13.outputs["Height"], 'Geometry': transform_3})
    
    nodegroup_012 = nw.new_node(nodegroup_node_group_012().name,
        input_kwargs={'Geometry': nodegroup_011.outputs["Inverted"], 'Value': group_input_13.outputs["Length"]})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Roof']})
    
    instance_on_points_19 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup_012.outputs["Selection"], 'Instance': object_info.outputs["Geometry"]})
    
    nodegroup_010 = nw.new_node(nodegroup_node_group_010().name,
        input_kwargs={'Geometry': nodegroup_011.outputs["Selection"], 'Value': group_input_13.outputs["Length"]})
    
    nodegroup_009 = nw.new_node(nodegroup_node_group_009().name,
        input_kwargs={'Value': group_input_13.outputs["Height"], 'Geometry': nodegroup_010.outputs["Selection"]})
    
    collection_info_7 = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['1st floor'], 'Separate Children': True, 'Reset Children': True})
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input_13.outputs["Seed 11"], 'Scale': 33.3000},
        attrs={'noise_dimensions': '4D'})
    
    ground = nw.new_node(nodegroup_random_picker_1st().name,
        input_kwargs={'W': group_input_13.outputs["1st floor seed"], 'Value': group_input_13.outputs["Amoount"], 'Vector': noise_texture_2.outputs["Fac"]},
        label='Ground')
    
    instance_on_points_16 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup_009.outputs["Inverted"], 'Instance': collection_info_7, 'Pick Instance': True, 'Instance Index': ground})
    
    object_info_9 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Corner']})
    
    instance_on_points_17 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup_010.outputs["Inverted"], 'Instance': object_info_9.outputs["Geometry"]})
    
    object_info_11 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Roof Corner']})
    
    instance_on_points_18 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup_012.outputs["Inverted"], 'Instance': object_info_11.outputs["Geometry"]})
    
    collection_info_6 = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['Walls'], 'Separate Children': True, 'Reset Children': True})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: group_input_13.outputs["Window seed"], 1: group_input_13.outputs[10]})
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'W': 4.0000, 'Scale': 33.3000}, attrs={'noise_dimensions': '4D'})
    
    ground_1 = nw.new_node(nodegroup_random_picker().name,
        input_kwargs={'W': add, 'Value': 35.7000, 'Vector': noise_texture_3.outputs["Fac"]},
        label='Ground')
    
    instance_on_points_20 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup_009.outputs["Selection"], 'Instance': collection_info_6, 'Pick Instance': True, 'Instance Index': ground_1})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [instance_on_points_19, instance_on_points_16, instance_on_points_17, instance_on_points_18, instance_on_points_20]})
    
    nodegroup_005 = nw.new_node(nodegroup_node_group_005().name,
        input_kwargs={0: group_input_13.outputs["Width"], 1: group_input_13.outputs["Width"], 'Geometry': join_geometry_3})
    
    subtract_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_13.outputs["Width"], 1: 1.0000},
        attrs={'operation': 'SUBTRACT'})
    
    subtract_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_13.outputs["Height"], 1: 1.0000},
        attrs={'operation': 'SUBTRACT'})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': subtract_2, 'Size Y': subtract_3, 'Vertices X': group_input_13.outputs["Width"], 'Vertices Y': group_input_13.outputs["Height"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'domain': 'CORNER', 'data_type': 'FLOAT_VECTOR'})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute, 'Rotation': (1.5708, 0.0000, 0.0000)})
    
    nodegroup_002 = nw.new_node(nodegroup_node_group_002().name,
        input_kwargs={'Geometry': transform, 'Value': group_input_13.outputs["Height"]})
    
    nodegroup_001 = nw.new_node(nodegroup_node_group_001().name,
        input_kwargs={'Geometry': nodegroup_002.outputs["Selection"], 'Value': group_input_13.outputs["Width"]})
    
    nodegroup = nw.new_node(nodegroup_node_group().name,
        input_kwargs={'Geometry': nodegroup_001.outputs["Selection"], 'Value': group_input_13.outputs["Height"]})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['Walls'], 'Separate Children': True, 'Reset Children': True})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input_13.outputs["Window seed"], 1: group_input_13.outputs[9]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'W': 1.0000, 'Scale': 33.3000}, attrs={'noise_dimensions': '4D'})
    
    random_picker = nw.new_node(nodegroup_random_picker().name, input_kwargs={'W': add_1, 'Vector': noise_texture_1.outputs["Fac"]})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup.outputs["Selection"], 'Instance': collection_info, 'Pick Instance': True, 'Instance Index': random_picker})
    
    nodegroup_003 = nw.new_node(nodegroup_node_group_003().name,
        input_kwargs={'Geometry': nodegroup_002.outputs["Inverted"], 'Value': group_input_13.outputs["Width"]})
    
    object_info_3 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Roof']})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup_003.outputs["Selection"], 'Instance': object_info_3.outputs["Geometry"]})
    
    collection_info_1 = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['1st floor'], 'Separate Children': True, 'Reset Children': True})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input_13.outputs["Seed 22"], 'Scale': 33.3000},
        attrs={'noise_dimensions': '4D'})
    
    ground_2 = nw.new_node(nodegroup_random_picker_1st().name,
        input_kwargs={'W': group_input_13.outputs["1st floor seed"], 'Value': group_input_13.outputs["Amoount"], 'Vector': noise_texture.outputs["Fac"]},
        label='Ground')
    
    instance_on_points_3 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup.outputs["Inverted"], 'Instance': collection_info_1, 'Pick Instance': True, 'Instance Index': ground_2})
    
    object_info_2 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Roof Corner']})
    
    instance_on_points_4 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup_003.outputs["Inverted"], 'Instance': object_info_2.outputs["Geometry"]})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['Corner']})
    
    instance_on_points_5 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': nodegroup_001.outputs["Inverted"], 'Instance': object_info_1.outputs["Geometry"]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [instance_on_points_1, instance_on_points_2, instance_on_points_3, instance_on_points_4, instance_on_points_5]})
    
    nodegroup_004 = nw.new_node(nodegroup_node_group_004().name,
        input_kwargs={0: group_input_13.outputs["Length"], 1: group_input_13.outputs["Length"], 'Geometry': join_geometry})
    
    rooftop = nw.new_node(nodegroup_rooftop().name,
        input_kwargs={'Vertices X': group_input_13.outputs["Width"], 'Vertices Y': group_input_13.outputs["Length"], 2: group_input_13.outputs["Length"], 3: group_input_13.outputs["Width"], 4: group_input_13.outputs["Height"], 'W': group_input_13.outputs["Seed"], 7: group_input_13.outputs["Amound"], 'Switch': group_input_13.outputs["Chimney"]})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [nodegroup_005, nodegroup_004, rooftop]})
    
    nodegroup_007 = nw.new_node(nodegroup_node_group_007().name,
        input_kwargs={'Value': group_input_13.outputs["Height"], 'Geometry': join_geometry_4})
    
    ground_3 = nw.new_node(nodegroup_ground().name,
        input_kwargs={0: group_input_13.outputs["Length"], 1: group_input_13.outputs["Width"], 2: group_input_13.outputs["Width"], 3: group_input_13.outputs["Length"], 4: group_input_13.outputs["Ground size"], 5: group_input_13.outputs["Curb extrudion"], 6: group_input_13.outputs["Curb size"]})
    
    join_geometry_6 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [ground_3.outputs["Geometry2"], ground_3.outputs["Geometry1"]]})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': join_geometry_6, 'Translation': (0.0000, 0.0000, -0.0001)})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_13.outputs["Ground"], 15: transform_1})
    
    join_geometry_5 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [nodegroup_007, switch.outputs[6]]})
    
    group_output_1 = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_5}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_degradable_metal, selection=selection)
    surface.add_material(obj, shader_chimney, selection=selection)
    surface.add_material(obj, shader_ground, selection=selection)
    surface.add_material(obj, shader_ground_2, selection=selection)
    surface.add_material(obj, shader_roof, selection=selection)
    surface.add_material(obj, shader_paralax, selection=selection)
    surface.add_material(obj, shader_glass, selection=selection)
apply(bpy.context.active_object)
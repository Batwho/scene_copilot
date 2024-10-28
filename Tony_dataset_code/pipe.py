import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_paint_roughness_normal', singleton=False, type='ShaderNodeTree')
def nodegroup_paint_roughness_normal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Value', 0.2000),
            ('NodeSocketFloat', 'Scale', 0.0000)])
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': group_input.outputs["Scale"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mapping})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute},
        attrs={'projection': 'BOX', 'projection_blend': 0.4500, 'image': bpy.data.images['Dirt.jpg.001']})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: image_texture.outputs["Color"], 1: 0.4000, 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    musgrave_texture_1 = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': reroute, 'Scale': 200.0000, 'Lacunarity': 1.0000},
        attrs={'musgrave_type': 'MULTIFRACTAL'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: musgrave_texture_1, 1: 0.0300, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: multiply_1, 2: 0.0000})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: add, 1: group_input.outputs["Value"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    ambient_occlusion = nw.new_node(Nodes.AmbientOcclusion, input_kwargs={'Distance': 0.5000})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: ambient_occlusion.outputs["AO"], 2: 0.0000},
        attrs={'operation': 'SUBTRACT'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: subtract, 2: 0.0000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.0100, 'Height': musgrave_texture_1})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Roughness': add_1, 'Normal': bump}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_rusty_metal', singleton=False, type='ShaderNodeTree')
def nodegroup_rusty_metal(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    ambient_occlusion = nw.new_node(Nodes.AmbientOcclusion, input_kwargs={'Distance': 0.5000})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: 1.0000, 1: ambient_occlusion.outputs["AO"]},
        attrs={'operation': 'SUBTRACT'})
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': texture_coordinate.outputs["Object"]})
    
    image_texture = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': reroute_1},
        attrs={'projection': 'BOX', 'image': bpy.data.images['Dirt.jpg']})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: subtract, 1: image_texture.outputs["Color"]},
        attrs={'operation': 'MULTIPLY'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': reroute})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.7639, 0.8174, 0.6316, 0.0000]
    colorramp.color_ramp.elements[1].position = 0.1591
    colorramp.color_ramp.elements[1].color = [0.1046, 0.0210, 0.0087, 1.0000]
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketColor', 'Colour', (0.5000, 0.5000, 0.5000, 1.0000)),
            ('NodeSocketFloat', 'Matalic', 0.5000)])
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: colorramp.outputs["Alpha"], 6: group_input.outputs["Colour"], 7: (0.1046, 0.0210, 0.0087, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: colorramp.outputs["Alpha"], 1: group_input.outputs["Matalic"]})
    
    mix = nw.new_node(Nodes.Mix, input_kwargs={0: reroute, 2: 0.7000, 3: 0.2000})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix_1.outputs[2], 'Metallic': add, 'Roughness': mix.outputs["Result"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'BSDF': principled_bsdf}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_dirty_paint', singleton=False, type='ShaderNodeTree')
def nodegroup_dirty_paint(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketColor', 'Base Color', (0.0410, 0.0409, 0.0405, 1.0000)),
            ('NodeSocketFloatFactor', 'Roughness', 0.0000),
            ('NodeSocketFloat', 'Dirt', 0.0000),
            ('NodeSocketFloat', 'Scale', 1.0000)])
    
    group = nw.new_node(nodegroup_paint_roughness_normal().name,
        input_kwargs={'Value': group_input.outputs["Dirt"], 'Scale': group_input.outputs["Scale"]})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: group.outputs["Roughness"], 6: group_input.outputs["Base Color"], 7: (0.0000, 0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Roughness"], 1: group.outputs["Roughness"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Roughness': add, 'Normal': group.outputs["Normal"]},
        attrs={'subsurface_method': 'BURLEY'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'BSDF': principled_bsdf}, attrs={'is_active_output': True})

def shader_pipe(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_1 = nw.new_node(nodegroup_rusty_metal().name,
        input_kwargs={'Colour': (1.0000, 1.0000, 1.0000, 1.0000), 'Matalic': 0.0000})
    
    material_output_1 = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': group_1}, attrs={'target': 'EEVEE'})

@node_utils.to_nodegroup('nodegroup_instance_from_group', singleton=False, type='GeometryNodeTree')
def nodegroup_instance_from_group(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Points', None),
            ('NodeSocketVectorEuler', 'Rotation', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVectorXYZ', 'Scale', (1.0000, 1.0000, 1.0000))])
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Points"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    named_attribute_1 = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'Connection'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: named_attribute_1.outputs[1], 1: 10.0000}, attrs={'operation': 'MULTIPLY'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 0.9900}, attrs={'operation': 'SUBTRACT'})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['Connections'], 'Separate Children': True, 'Reset Children': True})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Rotation"]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Scale"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': reroute_2, 'Selection': subtract, 'Instance': collection_info, 'Pick Instance': True, 'Instance Index': subtract, 'Rotation': reroute_4, 'Scale': reroute_5})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Instances': instance_on_points}, attrs={'is_active_output': True})

def shader_paint_dirty_while(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group = nw.new_node(nodegroup_dirty_paint().name,
        input_kwargs={'Base Color': (0.6963, 0.6934, 0.6849, 1.0000), 'Roughness': 0.2000, 'Dirt': 3.0000, 'Scale': 4.0000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': group}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatDistance', 'Fillet', 0.2700),
            ('NodeSocketFloatDistance', 'Pipe Radius', 0.1100),
            ('NodeSocketInt', 'Resolution', 12),
            ('NodeSocketMaterial', 'Material', None)])#surface.shaderfunc_to_material(shader_pipe))])
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Geometry"]})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': reroute_7})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Fillet"]})
    
    named_attribute = nw.new_node(Nodes.NamedAttribute, input_kwargs={'Name': 'Fillet'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: named_attribute.outputs[1]}, attrs={'operation': 'MULTIPLY'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply})
    
    fillet_curve = nw.new_node(Nodes.FilletCurve, input_kwargs={'Curve': mesh_to_curve, 'Radius': reroute_1})
    
    curve_to_points = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': fillet_curve}, attrs={'mode': 'EVALUATED'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Resolution"]})
    
    fillet_curve_1 = nw.new_node(Nodes.FilletCurve,
        input_kwargs={'Curve': mesh_to_curve, 'Count': reroute_5, 'Radius': reroute_1},
        attrs={'mode': 'POLY'})
    
    curve_to_points_1 = nw.new_node(Nodes.CurveToPoints, input_kwargs={'Curve': fillet_curve_1}, attrs={'mode': 'EVALUATED'})
    
    sample_nearest = nw.new_node(Nodes.SampleNearest, input_kwargs={'Geometry': curve_to_points_1.outputs["Points"]})
    
    sample_index = nw.new_node(Nodes.SampleIndex,
        input_kwargs={'Geometry': curve_to_points_1.outputs["Points"], 3: curve_to_points_1.outputs["Rotation"], 'Index': sample_nearest},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Pipe Radius"]})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_3, 1: 10.0000}, attrs={'operation': 'MULTIPLY'})
    
    instance_from_group = nw.new_node(nodegroup_instance_from_group().name,
        input_kwargs={'Points': curve_to_points.outputs["Points"], 'Rotation': sample_index.outputs[2], 'Scale': multiply_1})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: 2.0000}, attrs={'operation': 'MULTIPLY'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': multiply_2, 'Radius': reroute_3})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': fillet_curve_1, 'Profile Curve': curve_circle.outputs["Curve"]})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [instance_from_group, curve_to_mesh]})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Material"]})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial, input_kwargs={'Geometry': join_geometry, 'Material': reroute_4})
    
    edge_angle = nw.new_node(Nodes.InputEdgeAngle)
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': set_material_1, 'Signed Angle': edge_angle.outputs["Signed Angle"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_paint_dirty_while, selection=selection)
apply(bpy.context.active_object)
import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_mio_sine_wave', singleton=False, type='GeometryNodeTree')
def nodegroup_mio_sine_wave(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'separate_xyz', 0.5000),
            ('NodeSocketFloat', 'Value1', 20.0000),
            ('NodeSocketFloat', 'Value2', 2.0000),
            ('NodeSocketFloat', 'multiply1', 3.0000),
            ('NodeSocketFloat', 'multiply2', 1.0000)])
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["separate_xyz"], 1: group_input.outputs['Value1']},
        attrs={'operation': 'SUBTRACT'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: group_input.outputs['Value2']}, attrs={'operation': 'MULTIPLY'})
    
    sine = nw.new_node(Nodes.Math, input_kwargs={0: multiply, 1: 2.0000}, attrs={'operation': 'SINE'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: sine, 1: group_input.outputs['multiply1']}, attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: group_input.outputs['multiply1']})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': add}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_m_i_o_noise_001', singleton=False, type='GeometryNodeTree')
def nodegroup_m_i_o_noise_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Scale', 5.0000),
            ('NodeSocketFloat', 'Detail', 2.0000),
            ('NodeSocketFloatFactor', 'Roughness', 0.5000),
            ('NodeSocketFloat', 'Distortion', 0.0000),
            ('NodeSocketFloat', 'Value', 0.5000)])
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Scale': group_input.outputs["Scale"], 'Detail': group_input.outputs["Detail"], 'Roughness': group_input.outputs["Roughness"], 'Distortion': group_input.outputs["Distortion"]})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': noise_texture.outputs["Fac"], 3: -0.5000, 4: 0.5000})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range.outputs["Result"], 1: group_input.outputs["Value"]},
        attrs={'operation': 'MULTIPLY'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Value': multiply}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_inverter', singleton=False, type='GeometryNodeTree')
def nodegroup_inverter(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketFloat', 'Value', 0.0000)])
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Value"]})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_2})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': multiply})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': reroute})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_1})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_1})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_2})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'X': combine_xyz_6, '-X': combine_xyz_7, 'Y': combine_xyz_3, '-Y': combine_xyz_2, 'Z': combine_xyz_5, '-Z': combine_xyz_4},
        attrs={'is_active_output': True})

def shader_light(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Emission': (1.0000, 1.0000, 1.0000, 1.0000), 'Emission Strength': 36.8000})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_m_e_t_a_l(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.8000, 0.6975, 0.4377, 1.0000), 'Metallic': 1.0000, 'Roughness': 0.0500})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Spacing', 0.7900),
            ('NodeSocketFloat', 'Len', 3.9400),
            ('NodeSocketInt', 'Count', 3),
            ('NodeSocketFloat', 'N_Scale', 1.5000),
            ('NodeSocketFloat', 'N_Seed', -2.7000),
            ('NodeSocketFloat', 'N_Strength', 1.0100),
            ('NodeSocketInt', 'Seed', 30),
            ('NodeSocketInt', 'P_Filler', 17),
            ('NodeSocketInt', 'P_Count', 17),
            ('NodeSocketFloat', 'P_Radious', 0.0000),
            ('NodeSocketFloat', 'L_Perfil', 0.5000),
            ('NodeSocketFloatDistance', 'L_Radious', 0.0800),
            ('NodeSocketFloatDistance', 'L_Resolution', 0.3200),
            ('NodeSocketCollection', 'Collection', None)])#bpy.data.collections['ciling'])])
    
    inverter = nw.new_node(nodegroup_inverter().name, input_kwargs={'Value': group_input.outputs["Spacing"]})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': inverter.outputs["X"], 'End': inverter.outputs["-X"]})
    
    resample_curve_1 = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': curve_line_1, 'Count': group_input.outputs["Count"], 'Length': 0.7000})
    
    inverter_1 = nw.new_node(nodegroup_inverter().name, input_kwargs={'Value': group_input.outputs["Len"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': inverter_1.outputs["Y"], 'End': inverter_1.outputs["-Y"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': curve_line, 'Length': group_input.outputs["L_Resolution"]},
        attrs={'mode': 'LENGTH'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': resample_curve_1, 'Instance': resample_curve})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points})
    
    mio_noise_001 = nw.new_node(nodegroup_m_i_o_noise_001().name,
        input_kwargs={'Scale': group_input.outputs["N_Scale"], 'Detail': 0.0000, 'Roughness': 0.0000, 'Distortion': group_input.outputs["N_Seed"], 'Value': group_input.outputs["N_Strength"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': mio_noise_001})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': realize_instances, 'Offset': combine_xyz})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    set_position_6 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_4, 'Offset': (0.0000, 0.0000, -0.0200)})
    
    resample_curve_3 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position_6, 'Count': 79})
    
    endpoint_selection_1 = nw.new_node(Nodes.EndpointSelection)
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': resample_curve_3, 'Selection': endpoint_selection_1})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': delete_geometry, 'Tilt': 0.7854})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': 0.0400})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_tilt, 'Profile Curve': curve_circle_1.outputs["Curve"], 'Fill Caps': True})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh_1, 'Material': surface.shaderfunc_to_material(shader_light)})
    
    curve_line_2 = nw.new_node(Nodes.CurveLine)
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line_2, 'Count': group_input.outputs["P_Count"]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    random_value = nw.new_node(Nodes.RandomValue, input_kwargs={'Seed': group_input.outputs["Seed"]})
    
    sample_curve = nw.new_node(Nodes.SampleCurve,
        input_kwargs={'Curves': reroute, 'Factor': random_value.outputs[1]},
        attrs={'use_all_curves': True})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': resample_curve_2, 'Position': sample_curve.outputs["Position"]})
    
    curve_line_3 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': (0.0000, 0.0000, 0.1000)})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': set_position_1, 'Instance': curve_line_3})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1})
    
    position = nw.new_node(Nodes.InputPosition)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': realize_instances_1, 1: position},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: 0.1000}, attrs={'operation': 'GREATER_THAN'})
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': group_input.outputs["Collection"], 'Reset Children': True},
        attrs={'transform_space': 'RELATIVE'})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': collection_info})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': realize_instances_2, 'Source Position': capture_attribute.outputs["Attribute"], 'Ray Direction': (0.0000, 0.0000, 1.0000)},
        attrs={'data_type': 'INT'})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': raycast.outputs["Hit Position"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Selection': greater_than, 'Position': reroute_3})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_2})
    
    resample_curve_4 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': reroute_5, 'Count': group_input.outputs["P_Filler"]})
    
    endpoint_selection_3 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 0, 'End Size': 14})
    
    delete_geometry_2 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': resample_curve_4, 'Selection': endpoint_selection_3})
    
    endpoint_selection_2 = nw.new_node(Nodes.EndpointSelection, input_kwargs={'Start Size': 14, 'End Size': 0})
    
    delete_geometry_1 = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': resample_curve_4, 'Selection': endpoint_selection_2})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [delete_geometry_2, delete_geometry_1]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["P_Radious"]})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_6, 1: 1.2000}, attrs={'operation': 'MULTIPLY'})
    
    curve_circle_3 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 19, 'Radius': multiply})
    
    curve_to_mesh_4 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': join_geometry_1, 'Profile Curve': curve_circle_3.outputs["Curve"], 'Fill Caps': True})
    
    curve_circle_2 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 21, 'Radius': reroute_6})
    
    curve_to_mesh_2 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': reroute_5, 'Profile Curve': curve_circle_2.outputs["Curve"], 'Fill Caps': True})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': reroute_4, 'Radius': group_input.outputs["L_Radious"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 34})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    less_than = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_3.outputs["Y"], 1: 0.0000, 2: 2.5500},
        attrs={'operation': 'LESS_THAN'})
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["L_Perfil"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1, 1: 1.7000}, attrs={'operation': 'MULTIPLY'})
    
    mio_sine_wave = nw.new_node(nodegroup_mio_sine_wave().name,
        input_kwargs={0: separate_xyz_3.outputs["X"], 1: 19.5200, 2: 1.6900, 3: multiply_2, 4: multiply_1})
    
    smooth_max = nw.new_node(Nodes.Math, input_kwargs={0: mio_sine_wave, 1: -4.2200, 2: 6.3500}, attrs={'operation': 'SMOOTH_MAX'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: smooth_max, 1: 0.9000, 2: 2.5500}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Y': multiply_3})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Selection': less_than, 'Offset': combine_xyz_5})
    
    multiply_4 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_2, 1: (1.0000, -1.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_4, 'Position': multiply_4.outputs["Vector"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': set_position_5, 'Fill Caps': True})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [curve_to_mesh_4, curve_to_mesh_2, curve_to_mesh]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': join_geometry_2, 'Material': surface.shaderfunc_to_material(shader_m_e_t_a_l)})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material_1, set_material]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': join_geometry, 'Shade Smooth': False})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_shade_smooth}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_m_e_t_a_l, selection=selection)
    surface.add_material(obj, shader_light, selection=selection)
apply(bpy.context.active_object)
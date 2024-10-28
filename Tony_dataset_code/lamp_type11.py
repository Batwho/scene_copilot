import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_m_i_o_inverter', singleton=False, type='GeometryNodeTree')
def nodegroup_m_i_o_inverter(nw: NodeWrangler):
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

def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'co'})
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': attribute.outputs["Vector"], 'Rotation': (0.0000, 0.0000, -0.7854)})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': mapping})
    
    less_than = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["X"], 1: 0.0100}, attrs={'operation': 'LESS_THAN'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: less_than, 1: 20.0000}, attrs={'operation': 'MULTIPLY'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (0.3311, 0.3311, 0.3311, 1.0000), 'Emission': (1.0000, 0.8983, 0.6305, 1.0000), 'Emission Strength': multiply})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Separation', 0.0000),
            ('NodeSocketFloat', 'Base', 0.1000),
            ('NodeSocketFloat', 'Tk', 0.0000),
            ('NodeSocketFloat', 'Higt', 0.6700)])
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Separation"]})
    
    arc = nw.new_node('GeometryNodeCurveArc', input_kwargs={'Resolution': 64, 'Radius': reroute, 'Sweep Angle': 3.1411})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Higt"]})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': arc.outputs["Curve"], 'Translation': combine_xyz_1, 'Rotation': (1.5708, 0.0000, 1.5708)})
    
    endpoint_selection = nw.new_node(Nodes.EndpointSelection)
    
    position = nw.new_node(Nodes.InputPosition)
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position, 1: (1.0000, 1.0000, 0.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Base"]})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: combine_xyz, 1: (0.0000, 0.0000, -0.0100)})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': transform, 'Selection': endpoint_selection, 'Position': multiply.outputs["Vector"], 'Offset': add.outputs["Vector"]})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_position, 'Radius': 0.1000})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 1: normal},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Rotation': (0.0000, 0.0000, 0.7854)})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': group_input.outputs["Tk"], 'Z': 1.0000})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_1, 'Scale': combine_xyz_2})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': transform_2, 'Fill Caps': True})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh, 'Shade Smooth': False})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_material)})
    
    mio_inverter = nw.new_node(nodegroup_m_i_o_inverter().name, input_kwargs={'Value': reroute})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'Start': mio_inverter.outputs["Y"], 'End': mio_inverter.outputs["-Y"]})
    
    curve_line_1 = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints, input_kwargs={'Points': curve_line, 'Instance': curve_line_1})
    
    set_curve_radius_1 = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': instance_on_points, 'Radius': 0.1200})
    
    curve_to_mesh_1 = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius_1, 'Profile Curve': transform_2, 'Fill Caps': True})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_material, curve_to_mesh_1]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry, 'Attribute': capture_attribute.outputs["Attribute"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material, selection=selection)
apply(bpy.context.active_object)
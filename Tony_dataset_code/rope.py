import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def geometry_r_o_p_e_g_e_n_e_r_a_t_o_r(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'thickness', 0.5000),
            ('NodeSocketFloat', 'rope count', 4.0000),
            ('NodeSocketBool', 'Switch', True)])
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Resolution': 44, 'Rotations': 5.9000, 'Start Radius': 2.3000, 'End Radius': 1.4000, 'Height': 8.6000})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["Switch"], 14: group_input.outputs["Geometry"], 15: spiral})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve,
        input_kwargs={'Curve': switch.outputs[6], 'Count': 40, 'Length': 0.1010},
        attrs={'mode': 'LENGTH'})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    spline_length = nw.new_node(Nodes.SplineLength)
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: spline_length.outputs["Length"], 1: 0.2000}, attrs={'operation': 'DIVIDE'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: curve_parameter.outputs["Factor"], 1: divide},
        attrs={'operation': 'MULTIPLY'})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': resample_curve, 'Tilt': multiply})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 50, 'Radius': 0.0100})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    curve_parameter_1 = nw.new_node(Nodes.SplineParameter)
    
    multiply_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: curve_parameter_1.outputs["Factor"], 1: group_input.outputs["rope count"]},
        attrs={'operation': 'MULTIPLY'})
    
    fract = nw.new_node(Nodes.Math, input_kwargs={0: multiply_1}, attrs={'operation': 'FRACT'})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': fract})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 1.0000), (0.3773, 0.6813), (0.4909, 0.2500), (0.6273, 0.6688), (1.0000, 1.0000)], handles=['AUTO', 'AUTO', 'VECTOR', 'AUTO', 'AUTO'])
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': float_curve})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0062), (0.1636, 0.0812), (0.5182, 0.7375), (1.0000, 1.0000)])
    
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["thickness"], 1: 50.0000},
        attrs={'operation': 'DIVIDE'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: divide_1}, attrs={'operation': 'MULTIPLY'})
    
    scale = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal, 'Scale': multiply_2}, attrs={'operation': 'SCALE'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Offset': scale.outputs["Vector"]})
    
    resample_curve_2 = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position, 'Count': 50})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_curve_tilt, 'Profile Curve': resample_curve_2})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': curve_to_mesh}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_r_o_p_e_g_e_n_e_r_a_t_o_r, selection=selection, attributes=[])
apply(bpy.context.active_object)
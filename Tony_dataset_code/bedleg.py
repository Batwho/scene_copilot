import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_material(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': (1.0000, 7.1000, 2.1000)})
    
    image_texture_1 = nw.new_node(Nodes.ShaderImageTexture,
        input_kwargs={'Vector': mapping},
        attrs={'image': bpy.data.images['aditya-joshi-aLmV1pc7y_o-unsplash.jpg']})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': image_texture_1.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0136
    colorramp.color_ramp.elements[0].color = [0.0000, 0.0000, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.0682
    colorramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': image_texture_1.outputs["Color"], 'Metallic': 0.4682, 'Specular': 0.2364, 'Roughness': colorramp.outputs["Color"]})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'height', 1.9000),
            ('NodeSocketFloat', 'tilt length Min', 32.8000),
            ('NodeSocketFloat', 'tilt length Max', 137.3000),
            ('NodeSocketFloat', 'tilt', 7.2000),
            ('NodeSocketInt', 'gon', 4),
            ('NodeSocketFloat', 'radius', 9.5000),
            ('NodeSocketFloat', 'bevel', 69.9000),
            ('NodeSocketMaterial', 'Material', None)]) #surface.shaderfunc_to_material(shader_material))])
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["height"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': curve_line, 'Count': 221})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    float_curve_1 = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve_1.mapping.curves[0], [(0.0000, 0.0000), (0.1409, 0.0000), (0.2727, 0.0000), (0.5818, 0.0000), (0.8273, 0.0000), (1.0000, 0.0000)])
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: float_curve_1, 1: 0.6000}, attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': resample_curve, 'Offset': multiply})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': curve_parameter.outputs["Factor"]})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.2063), (0.0390, 0.3562), (0.0969, 0.5125), (0.1656, 0.5875), (0.2353, 0.2875), (0.2474, 0.6000), (0.4200, 0.8438), (0.5952, 0.8937), (0.6788, 0.6813), (0.7359, 0.4750), (0.7363, 0.6375), (0.7597, 0.7687), (0.8038, 0.6688), (0.8571, 0.4375), (0.8722, 0.6750), (0.9347, 0.7187), (1.0000, 0.5812)])
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_position, 'Radius': float_curve})
    
    index = nw.new_node(Nodes.Index)
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': index, 1: group_input.outputs["tilt length Min"], 2: group_input.outputs["tilt length Max"], 4: group_input.outputs["tilt"]})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': set_curve_radius, 'Tilt': map_range.outputs["Result"]})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: 0.0100, 1: group_input.outputs["radius"]}, attrs={'operation': 'MULTIPLY'})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': group_input.outputs["gon"], 'Radius': multiply_1})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: group_input.outputs["bevel"]}, attrs={'operation': 'DIVIDE'})
    
    fillet_curve = nw.new_node(Nodes.FilletCurve,
        input_kwargs={'Curve': curve_circle.outputs["Curve"], 'Count': 28, 'Radius': divide, 'Limit Radius': True},
        attrs={'mode': 'POLY'})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_tilt, 'Profile Curve': fillet_curve, 'Fill Caps': True})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': group_input.outputs["Material"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_material, selection=selection)
apply(bpy.context.active_object)
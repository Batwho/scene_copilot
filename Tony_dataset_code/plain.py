import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_wood(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 29.6200, 'Distortion': 2.2000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.4000
    colorramp.color_ramp.elements[0].color = [0.1077, 0.0386, 0.0244, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.5891
    colorramp.color_ramp.elements[1].color = [0.3702, 0.2269, 0.1195, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': colorramp.outputs["Color"]})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketGeometry', 'Geometry', None)])
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': group_input.outputs["Geometry"]})
    
    set_curve_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': mesh_to_curve, 'Tilt': 0.7854})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 4, 'Radius': 0.0500})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_tilt, 'Profile Curve': curve_circle.outputs["Curve"], 'Fill Caps': True})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': curve_to_mesh, 'Shade Smooth': False})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_wood)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_wood, selection=selection)
apply(bpy.context.active_object)
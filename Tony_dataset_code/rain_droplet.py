import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_falling_droplet_shader(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: 0.3000, 1: 1.0000}, attrs={'operation': 'DIVIDE'})
    
    wave_texture = nw.new_node(Nodes.WaveTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': divide},
        attrs={'bands_direction': 'Z'})
    
    color_ramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': wave_texture.outputs["Fac"]})
    color_ramp.color_ramp.elements[0].position = 0.0000
    color_ramp.color_ramp.elements[0].color = [0.5000, 0.5000, 0.5000, 1.0000]
    color_ramp.color_ramp.elements[1].position = 1.0000
    color_ramp.color_ramp.elements[1].color = [1.0000, 1.0000, 1.0000, 1.0000]
    
    glass_bsdf = nw.new_node(Nodes.GlassBSDF, input_kwargs={'IOR': 1.3300})
    
    transparent_bsdf = nw.new_node(Nodes.TransparentBSDF)
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': color_ramp.outputs["Color"], 1: glass_bsdf, 2: transparent_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_2 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Length', 1.0000),
            ('NodeSocketFloat', 'Radius', 0.0500)])
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': 5, 'Radius': group_input_2.outputs["Radius"], 'Depth': group_input_2.outputs["Length"]},
        attrs={'fill_type': 'NONE'})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': cylinder.outputs["Mesh"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': surface.shaderfunc_to_material(shader_falling_droplet_shader)})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_material}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_falling_droplet_shader, selection=selection)
apply(bpy.context.active_object)
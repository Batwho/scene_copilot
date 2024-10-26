import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_randomize_colors', singleton=False, type='ShaderNodeTree')
def nodegroup_randomize_colors(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Blade_Random'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': attribute.outputs["Fac"], 3: 0.4500, 4: 0.5500},
        attrs={'clamp': False})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': attribute.outputs["Fac"], 3: 0.7500, 4: 1.2500},
        attrs={'clamp': False})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': attribute.outputs["Fac"], 3: 0.7500, 4: 1.2500},
        attrs={'clamp': False})
    
    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloatFactor', 'Randomize', 1.0000),
            ('NodeSocketFloatFactor', 'Dry', 0.0000),
            ('NodeSocketFloatFactor', 'Bump', 1.0000)])
    
    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Blade_UV'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: attribute_1.outputs["Vector"], 1: (0.2500, 1.0000, 1.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': multiply.outputs["Vector"], 'Scale': 20.0000, 'Detail': 5.0000, 'Roughness': 0.2500, 'Distortion': 1.0000})
    
    mix_2 = nw.new_node(Nodes.Mix,
        input_kwargs={0: noise_texture.outputs["Fac"], 6: (0.0864, 0.2509, 0.0000, 1.0000), 7: (0.0496, 0.1174, 0.0000, 1.0000)},
        attrs={'data_type': 'RGBA', 'clamp_result': True})
    
    mix_1 = nw.new_node(Nodes.Mix,
        input_kwargs={0: noise_texture.outputs["Fac"], 6: (0.4008, 0.3437, 0.0898, 1.0000), 7: (0.0988, 0.0728, 0.0284, 1.0000)},
        attrs={'data_type': 'RGBA', 'clamp_result': True})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: group_input.outputs["Dry"], 6: mix_2.outputs[2], 7: mix_1.outputs[2]},
        attrs={'data_type': 'RGBA', 'clamp_result': True})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Hue': map_range.outputs["Result"], 'Saturation': map_range_1.outputs["Result"], 'Value': map_range_2.outputs["Result"], 'Fac': group_input.outputs["Randomize"], 'Color': mix.outputs[2]})
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': group_input.outputs["Bump"], 'Height': noise_texture.outputs["Fac"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Color': hue_saturation_value, 'Normal': bump},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_randomize_blades', singleton=False, type='GeometryNodeTree')
def nodegroup_randomize_blades(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_1 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'ID', 0),
            ('NodeSocketFloat', 'Length Min', 0.4000),
            ('NodeSocketFloat', 'Length Max', 1.0000),
            ('NodeSocketInt', 'Lenght Seed', 57),
            ('NodeSocketFloat', 'Width Min', 0.0100),
            ('NodeSocketFloat', 'Width Max', 0.0500),
            ('NodeSocketInt', 'Width Seed', 38),
            ('NodeSocketFloat', 'Bend Min', 0.2000),
            ('NodeSocketFloat', 'Bend Max', 1.6000),
            ('NodeSocketInt', 'Bend Seed', 24)])
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input_1.outputs["Length Min"], 3: group_input_1.outputs["Length Max"], 'ID': group_input_1.outputs["ID"], 'Seed': group_input_1.outputs["Lenght Seed"]})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input_1.outputs["Width Min"], 3: group_input_1.outputs["Width Max"], 'ID': group_input_1.outputs["ID"], 'Seed': group_input_1.outputs["Width Seed"]})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={2: group_input_1.outputs["Bend Min"], 3: group_input_1.outputs["Bend Max"], 'ID': group_input_1.outputs["ID"], 'Seed': group_input_1.outputs["Bend Seed"]})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Length': random_value.outputs[1], 'Width': random_value_2.outputs[1], 'Bend': random_value_1.outputs[1], 'ID': group_input_1.outputs["ID"]},
        attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_blade', singleton=False, type='GeometryNodeTree')
def nodegroup_blade(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_output = nw.new_node(Nodes.GroupOutput, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_displace_bunch', singleton=False, type='GeometryNodeTree')
def nodegroup_displace_bunch(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'Displace', 0.0000),
            ('NodeSocketFloat', 'Scale', 20.0000),
            ('NodeSocketFloat', 'Seed', 0.0000)])
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input.outputs["Seed"], 'Scale': group_input.outputs["Scale"], 'Detail': 15.0000, 'Roughness': 1.0000},
        attrs={'noise_dimensions': '4D'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: noise_texture.outputs["Color"], 1: (-0.5000, -0.5000, -0.5000)})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add.outputs["Vector"], 1: (-0.5000, -0.5000, -0.5000), 'Scale': group_input.outputs["Displace"]},
        attrs={'operation': 'SCALE'})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: scale.outputs["Vector"], 1: (1.0000, 1.0000, 0.0000)},
        attrs={'operation': 'MULTIPLY'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': multiply.outputs["Vector"]}, attrs={'is_active_output': True})

def shader_blades(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group = nw.new_node(nodegroup_randomize_colors().name, input_kwargs={'Randomize': 0.5000, 'Dry': 0.5000, 'Bump': 0.1500})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': group.outputs["Color"], 'Roughness': 0.6500, 'IOR': 1.5000, 'Emission Strength': 0.0000, 'Normal': group.outputs["Normal"]},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS', 'distribution': 'MULTI_GGX'})
    
    hue_saturation_value = nw.new_node(Nodes.HueSaturationValue,
        input_kwargs={'Saturation': 0.7500, 'Value': 2.0000, 'Color': group.outputs["Color"]})
    
    translucent_bsdf = nw.new_node(Nodes.TranslucentBSDF, input_kwargs={'Color': hue_saturation_value, 'Normal': group.outputs["Normal"]})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': 0.2500, 1: principled_bsdf, 2: translucent_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def geometry_nodes01(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Bunch: Overall Scale', 0.1500),
            ('NodeSocketInt', 'Bunch: Number Of Blades', 16),
            ('NodeSocketFloatDistance', 'Bunch: Radius', 0.0300),
            ('NodeSocketFloat', 'Bunch Displace: Amount', 0.4500),
            ('NodeSocketFloat', 'Bunch Displace: Scale', 25.3000),
            ('NodeSocketFloat', 'Bunch Displace: Seed', 0.1000),
            ('NodeSocketBool', 'Blades: Add Thickness', False),
            ('NodeSocketFloat', 'Blades: Thickness', 1.0000),
            ('NodeSocketBool', 'Blades: Curved Profile', True),
            ('NodeSocketFloat', 'Blades: Profile Offset', 2.0000),
            ('NodeSocketInt', 'Blades: Subdivision Level', 0),
            ('NodeSocketFloatDistance', 'Blades: Resolution', 0.0500),
            ('NodeSocketFloat', 'Blades Displacement: Amount', 0.2000),
            ('NodeSocketFloat', 'Blades Displacement: Scale', 4.0000),
            ('NodeSocketFloat', 'Blades Length: Min', 0.3000),
            ('NodeSocketFloat', 'Blades Length: Max', 1.0000),
            ('NodeSocketInt', 'Blades Lenght: Seed', 57),
            ('NodeSocketFloat', 'Blades Width: Min', 0.0100),
            ('NodeSocketFloat', 'Blades Width: Max', 0.0500),
            ('NodeSocketInt', 'Blades Width: Seed', 38),
            ('NodeSocketFloat', 'Blades Bend(Deg): Min', 45.0000),
            ('NodeSocketFloat', 'Blades Bend(Deg): Max', 120.0000),
            ('NodeSocketInt', 'Blades Bend: Seed', 24)])
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bunch: Number Of Blades"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': reroute_3, 'Radius': group_input.outputs["Bunch: Radius"]})
    
    displace_bunch = nw.new_node(nodegroup_displace_bunch().name,
        input_kwargs={'Displace': group_input.outputs["Bunch Displace: Amount"], 'Scale': group_input.outputs["Bunch Displace: Scale"], 'Seed': group_input.outputs["Bunch Displace: Seed"]})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Offset': displace_bunch})
    
    index_don_t_change = nw.new_node(Nodes.Integer, label="Index (Don't Change)")
    index_don_t_change.integer = 0
    
    repeat_input = nw.new_node('NodeUndefined',
        input_kwargs={'Iterations': reroute_3, 'Geometry': set_position_1, 'Index Counter': index_don_t_change})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': repeat_input.outputs["Geometry"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    index = nw.new_node(Nodes.Index)
    
    equal = nw.new_node(Nodes.Compare,
        input_kwargs={2: index, 3: repeat_input.outputs["Index Counter"], 6: (0.8000, 0.8000, 0.8000, 1.0000), 7: (0.8000, 0.8000, 0.8000, 1.0000)},
        attrs={'data_type': 'INT', 'operation': 'EQUAL'})
    
    separate_geometry = nw.new_node(Nodes.SeparateGeometry,
        input_kwargs={'Geometry': repeat_input.outputs["Geometry"], 'Selection': equal},
        attrs={'domain': 'INSTANCE'})
    
    randomize_blades = nw.new_node(nodegroup_randomize_blades().name,
        input_kwargs={'ID': repeat_input.outputs["Index Counter"], 'Length Min': group_input.outputs["Blades Length: Min"], 'Length Max': group_input.outputs["Blades Length: Max"], 'Lenght Seed': group_input.outputs["Blades Lenght: Seed"], 'Width Min': group_input.outputs["Blades Width: Min"], 'Width Max': group_input.outputs["Blades Width: Max"], 'Width Seed': group_input.outputs["Blades Width: Seed"], 'Bend Min': group_input.outputs["Blades Bend(Deg): Min"], 'Bend Max': group_input.outputs["Blades Bend(Deg): Max"], 'Bend Seed': group_input.outputs["Blades Bend: Seed"]})
    
    blade = nw.new_node(nodegroup_blade().name,
        input_kwargs={'Resolution': group_input.outputs["Blades: Resolution"], 'Length': randomize_blades.outputs["Length"], 'Blade Width': randomize_blades.outputs["Width"], 'Bend': randomize_blades.outputs["Bend"], 'Blade Displace Seed': randomize_blades.outputs["ID"], 'Add Thickness': group_input.outputs["Blades: Add Thickness"], 'Blade Displace': group_input.outputs["Blades Displacement: Amount"], 'Blade Displace Scale': group_input.outputs["Blades Displacement: Scale"], 'Blede Subdivision Level': group_input.outputs["Blades: Subdivision Level"], 'Blade Thickness': group_input.outputs["Blades: Thickness"], 'Blade Curved Profile': group_input.outputs["Blades: Curved Profile"], 'Curved Profile Offset': group_input.outputs["Blades: Profile Offset"]})
    
    curve_tangent = nw.new_node(Nodes.CurveTangent)
    
    align_euler_to_vector = nw.new_node(Nodes.AlignEulerToVector, input_kwargs={'Vector': curve_tangent})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': separate_geometry.outputs["Selection"], 'Selection': equal, 'Instance': blade, 'Rotation': align_euler_to_vector})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_2, instance_on_points]})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': repeat_input.outputs["Index Counter"]})
    
    index_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute, 1: 1.0000}, label='Index+1')
    
    repeat_output = nw.new_node('NodeUndefined', input_kwargs={'Geometry': join_geometry, 'Index Counter': index_1})
    
    separate_components = nw.new_node(Nodes.SeparateComponents, input_kwargs={'Geometry': repeat_output.outputs["Geometry"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': separate_components.outputs["Instances"], 'Name': 'Blade_Random'},
        attrs={'domain': 'INSTANCE'})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': store_named_attribute})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': realize_instances})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': group_input.outputs["Bunch: Overall Scale"], 'Y': group_input.outputs["Bunch: Overall Scale"], 'Z': group_input.outputs["Bunch: Overall Scale"]})
    
    transform_geometry = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_shade_smooth, 'Scale': combine_xyz})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': transform_geometry}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes01, selection=selection, attributes=[])
    surface.add_material(obj, shader_blades, selection=selection)
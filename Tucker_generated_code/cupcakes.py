import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_cream_pink(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': 7.2000, 'Detail': 7.0000, 'Roughness': 0.8750})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': noise_texture_1.outputs["Fac"], 1: 0.4700, 2: 0.5700, 3: 0.6300, 4: 0.3700})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': 12.0000, 'Detail': 3.5000})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0200, 'Height': noise_texture.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': (1.0000, 0.1261, 0.1650, 1.0000), 'Subsurface': 0.2545, 'Subsurface Color': (1.0000, 0.0000, 0.0265, 1.0000), 'Roughness': map_range.outputs["Result"], 'Normal': bump},
        attrs={'subsurface_method': 'RANDOM_WALK_FIXED_RADIUS'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_dough(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    fresnel = nw.new_node(Nodes.Fresnel)
    
    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': 3.5000, 'Detail': 6.7000, 'Roughness': 0.7750})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': noise_texture_2.outputs["Fac"], 1: 0.4200, 2: 0.6500, 4: 1.0000})
    
    colorramp_3 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': map_range.outputs["Result"]})
    colorramp_3.color_ramp.elements[0].position = 0.0000
    colorramp_3.color_ramp.elements[0].color = [0.2508, 0.0230, 0.0012, 1.0000]
    colorramp_3.color_ramp.elements[1].position = 1.0000
    colorramp_3.color_ramp.elements[1].color = [0.2670, 0.1071, 0.0379, 1.0000]
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': texture_coordinate.outputs["Object"]})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute, 'Scale': 8.0200, 'Detail': 10.0000})
    
    noise_texture_3 = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': reroute, 'Scale': 3.0000, 'Detail': 10.0000})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: 0.4917, 6: noise_texture_1.outputs["Fac"], 7: noise_texture_3.outputs["Fac"]},
        attrs={'data_type': 'RGBA', 'blend_type': 'ADD'})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Distance': 0.0300, 'Height': mix.outputs[2]})
    
    subsurface_scattering = nw.new_node('ShaderNodeSubsurfaceScattering',
        input_kwargs={'Color': colorramp_3.outputs["Color"], 'Scale': 0.2700, 'Normal': bump},
        attrs={'falloff': 'RANDOM_WALK_FIXED_RADIUS'})
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': noise_texture_1.outputs["Fac"], 1: 0.3800, 2: 0.6800, 3: 0.2600, 4: 0.8300})
    
    glossy_bsdf = nw.new_node(Nodes.GlossyBSDF, input_kwargs={'Roughness': map_range_1.outputs["Result"], 'Normal': bump})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': fresnel, 1: subsurface_scattering, 2: glossy_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def shader_paper(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    musgrave_texture = nw.new_node(Nodes.MusgraveTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': 3.1000, 'Detail': 0.0000, 'Dimension': 0.0000},
        attrs={'musgrave_type': 'RIDGED_MULTIFRACTAL'})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': musgrave_texture, 1: 0.0100, 2: 0.0000})
    
    less_than = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range.outputs["Result"], 1: 0.8500, 2: 0.0000},
        attrs={'operation': 'LESS_THAN'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: less_than, 6: (0.0532, 0.0065, 0.0302, 1.0000), 7: (0.4497, 0.0767, 0.1018, 1.0000)},
        attrs={'data_type': 'RGBA'})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': mix.outputs[2], 'Roughness': 0.0909},
        attrs={'subsurface_method': 'BURLEY'})
    
    translucent_bsdf = nw.new_node(Nodes.TranslucentBSDF, input_kwargs={'Color': mix.outputs[2]})
    
    mix_shader = nw.new_node(Nodes.MixShader, input_kwargs={'Fac': 0.0000, 1: principled_bsdf, 2: translucent_bsdf})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': mix_shader}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloatDistance', 'Radius', 1.0000),
            ('NodeSocketFloat', 'Dough Sourface', 0.0900),
            ('NodeSocketFloat', 'Dough Height', 0.2500),
            ('NodeSocketInt', 'Cup Folds', 32),
            ('NodeSocketFloatDistance', 'Cup Height', 1.0000),
            ('NodeSocketFloat', 'Cup Base', 0.0000),
            ('NodeSocketFloatDistance', 'Cream Height', 0.7000),
            ('NodeSocketFloat', 'Cream Rotations', 3.0000),
            ('NodeSocketFloat', 'Cream Thickness', 1.2100),
            ('NodeSocketFloat', 'Cream Tip', 0.1900),
            ('NodeSocketFloat', 'Cream Width', 0.6900),
            ('NodeSocketFloat', 'Cream offset', 0.0000),
            ('NodeSocketFloat', 'Cupcake Sprinkles', 1.0000),
            ('NodeSocketFloat', 'Floor Sprinkles', 1.0000),
            ('NodeSocketMaterial', 'Paper', None), #surface.shaderfunc_to_material(shader_paper)
            ('NodeSocketMaterial', 'Dough', None), #surface.shaderfunc_to_material(shader_dough)
            ('NodeSocketMaterial', 'Cream', None)]) #surface.shaderfunc_to_material(shader_cream_pink)
    
    reroute_93 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cream Rotations"]})
    
    reroute_94 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_93})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Radius"]})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_48})
    
    reroute_85 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_49})
    
    reroute_88 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cream Width"]})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_88})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: reroute_85, 1: reroute_17, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_86 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cream Height"]})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_86})
    
    reroute_78 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    spiral = nw.new_node('GeometryNodeCurveSpiral',
        input_kwargs={'Rotations': reroute_94, 'Start Radius': multiply, 'End Radius': 0.0000, 'Height': reroute_78})
    
    reroute_87 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cream offset"]})
    
    reroute_84 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_87})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_84})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': spiral, 'Translation': combine_xyz_6})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    rgb_curves_1 = nw.new_node(Nodes.RGBCurve, input_kwargs={'Color': curve_parameter.outputs["Factor"]})
    node_utils.assign_curve(rgb_curves_1.mapping.curves[0], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_1.mapping.curves[1], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_1.mapping.curves[2], [(0.0000, 0.0000), (1.0000, 1.0000)])
    node_utils.assign_curve(rgb_curves_1.mapping.curves[3], [(0.0000, 0.0000), (0.0740, 0.5312), (0.1534, 0.8250), (0.2635, 0.8562), (0.3556, 0.9187), (0.4982, 0.8063), (0.6318, 0.9125), (0.7383, 0.9125), (0.7834, 0.8750), (0.8339, 0.8000), (0.9097, 0.7562), (0.9567, 0.4812), (1.0000, 0.0000)])
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cream Thickness"]})
    
    reroute_89 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    reroute_91 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_89})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: rgb_curves_1, 1: reroute_91, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': transform, 'Radius': multiply_1})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cream Tip"]})
    
    reroute_90 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    reroute_92 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_90})
    
    reroute_100 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_92})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_100})
    
    map_range_2 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': curve_parameter.outputs["Factor"], 1: 0.9000})
    
    scale = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: combine_xyz_1, 1: (0.0000, 0.0000, 0.2400), 'Scale': map_range_2.outputs["Result"]},
        attrs={'operation': 'SCALE'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_curve_radius, 'Offset': scale.outputs["Vector"]})
    
    star = nw.new_node('GeometryNodeCurveStar', input_kwargs={'Inner Radius': 0.1500, 'Outer Radius': 0.2000})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh, input_kwargs={'Curve': set_position_3, 'Profile Curve': star.outputs["Curve"]})
    
    cube = nw.new_node(Nodes.MeshCube)
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances,
        input_kwargs={'Geometry': store_named_attribute_2},
        attrs={'legacy_behavior': True})
    
    mesh_subdivide = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': realize_instances_2, 'Level': 3})
    
    position_6 = nw.new_node(Nodes.InputPosition)
    
    normalize = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_6}, attrs={'operation': 'NORMALIZE'})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_subdivide, 'Position': normalize.outputs["Vector"]})
    
    subdivision_surface_4 = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': set_position_2, 'Level': 3})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cup Folds"]})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_51})
    
    snap = nw.new_node(Nodes.Math, input_kwargs={0: reroute_15, 1: 2.0000, 2: 0.0000}, attrs={'operation': 'SNAP'})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_49})
    
    reroute_50 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cup Height"]})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_50})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    cylinder_1 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': snap, 'Fill Segments': 3, 'Radius': reroute_24, 'Depth': reroute_2})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder_1.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_2}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_2})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_4})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    set_position_6 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': store_named_attribute_1, 'Offset': reroute_25})
    
    index_4 = nw.new_node(Nodes.Index)
    
    capture_attribute = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': set_position_6, 5: index_4},
        attrs={'data_type': 'INT'})
    
    normal_1 = nw.new_node(Nodes.InputNormal)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': normal_1})
    
    compare = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_1.outputs["Z"], 1: 1.0000, 2: 0.0000},
        attrs={'operation': 'COMPARE'})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': compare})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_28})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': capture_attribute.outputs["Geometry"], 'Selection': reroute_29},
        attrs={'domain': 'FACE'})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute.outputs[5]})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_35})
    
    pingpong = nw.new_node(Nodes.Math, input_kwargs={0: reroute_14, 1: 1.0000}, attrs={'operation': 'PINGPONG'})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': pingpong})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 0.9300, 'Y': 0.9300, 'Z': 1.0000})
    
    multiply_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_1, 1: combine_xyz}, attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': delete_geometry, 'Selection': reroute_34, 'Position': multiply_3.outputs["Vector"]})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': set_position})
    
    separate_xyz_6 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Max"]})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_6.outputs["Z"]})
    
    cup_max_value_on_z = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39}, label='Cup Max value on Z')
    
    reroute_59 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': cup_max_value_on_z})
    
    reroute_60 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_59})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_60})
    
    reroute_61 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_5})
    
    reroute_62 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_61})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_48})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_72 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Dough Height"]})
    
    reroute_73 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_72})
    
    multiply_add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_73, 1: 0.2500, 2: 0.2500}, attrs={'operation': 'MULTIPLY_ADD'})
    
    reroute_75 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_add})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_4, 'Y': reroute_4, 'Z': reroute_75})
    
    reroute_63 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_2})
    
    reroute_64 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_63})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': subdivision_surface_4, 'Translation': reroute_62, 'Scale': reroute_64})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Scale': 10.0000, 'Detail': 0.0000, 'Roughness': 0.0000})
    
    subtract = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: noise_texture.outputs["Color"], 1: (0.5000, 0.5000, 0.5000)},
        attrs={'operation': 'SUBTRACT'})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Dough Sourface"]})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_47})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_46, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_56 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_4})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_56})
    
    multiply_5 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract.outputs["Vector"], 1: combine_xyz_3},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_5.outputs["Vector"]})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_52})
    
    normal_2 = nw.new_node(Nodes.InputNormal)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': normal_2})
    
    scale_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: reroute_53, 'Scale': separate_xyz.outputs["Z"]},
        attrs={'operation': 'SCALE'})
    
    reroute_67 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_1.outputs["Vector"]})
    
    reroute_68 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_67})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': transform_1, 'Offset': reroute_68})
    
    position = nw.new_node(Nodes.InputPosition)
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': position})
    
    separate_xyz_7 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    separate_xyz_5 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Min"]})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Cup Base"]})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    n = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1}, label='N')
    
    map_range_1 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_7.outputs["Z"], 1: reroute_39, 2: separate_xyz_5.outputs["Z"], 3: 1.0000, 4: n})
    
    scale_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: reroute_12, 'Scale': map_range_1.outputs["Result"]},
        attrs={'operation': 'SCALE'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position, 'Position': scale_2.outputs["Vector"]})
    
    separate_xyz_4 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': reroute_12})
    
    compare_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_4.outputs["Z"], 1: -0.0000, 2: 0.0000},
        attrs={'operation': 'COMPARE'})
    
    split_edges = nw.new_node(Nodes.SplitEdges, input_kwargs={'Mesh': set_position_1, 'Selection': compare_1})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': split_edges, 'Level': 2, 'Edge Crease': 0.4858})
    
    set_shade_smooth_1 = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': subdivision_surface})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth_1, 'Material': group_input.outputs["Paper"]})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_1})
    
    reroute_69 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_70 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_69})
    
    cup_geometry = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_70}, label='Cup Geometry')
    
    geometry_proximity = nw.new_node(Nodes.Proximity, input_kwargs={'Target': cup_geometry})
    
    map_range_5 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': geometry_proximity.outputs["Distance"], 2: 0.2000, 3: 1.0000, 4: 0.0000})
    
    position_4 = nw.new_node(Nodes.InputPosition)
    
    multiply_6 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_4, 1: (0.7500, 0.7500, 1.0000), 'Scale': 0.4800},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_7 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position_4, 1: (0.9700, 0.9700, 1.0000), 'Scale': 0.4800},
        attrs={'operation': 'MULTIPLY'})
    
    mix = nw.new_node(Nodes.Mix,
        input_kwargs={0: map_range_5.outputs["Result"], 6: multiply_6.outputs["Vector"], 7: multiply_7.outputs["Vector"]},
        attrs={'data_type': 'RGBA'})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_4, 'Position': mix.outputs[2]})
    
    subdivision_surface_2 = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': set_position_5})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': subdivision_surface_2})
    
    bounding_box_1 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': set_shade_smooth})
    
    separate_xyz_8 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_1.outputs["Max"]})
    
    reroute_76 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz_8.outputs["Z"]})
    
    reroute_77 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_76})
    
    reroute_79 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_77})
    
    reroute_80 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_79})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': reroute_80})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': curve_to_mesh, 'Translation': combine_xyz_7})
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': transform_2, 'Level': 2, 'Edge Crease': 0.1692})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': subdivision_surface_1, 'Material': group_input.outputs["Cream"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_2})
    
    reroute_108 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_shade_smooth, 'Material': group_input.outputs["Dough"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material})
    
    reroute_106 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_109 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_108, reroute_106, reroute_109]})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': 10.0000, 'Size Y': 10.0000, 'Vertices X': 100, 'Vertices Y': 100})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': grid.outputs["Mesh"], 'Name': 'uv_map', 3: grid.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': store_named_attribute, 'Translation': (0.0000, 0.0000, 0.0200)})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    length = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_3}, attrs={'operation': 'LENGTH'})
    
    greater_than = nw.new_node(Nodes.Math,
        input_kwargs={0: length.outputs["Value"], 1: group_input.outputs["Radius"]},
        attrs={'operation': 'GREATER_THAN'})
    
    multiply_8 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Floor Sprinkles"], 1: 4.0000},
        attrs={'operation': 'MULTIPLY'})
    
    map_range_6 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': length.outputs["Value"], 2: 5.0000, 3: 1.0000, 4: 0.0000})
    
    mask_sprinkles_fade_with_distance = nw.new_node(Nodes.Reroute,
        input_kwargs={'Input': map_range_6.outputs["Result"]},
        label='Mask sprinkles fade with distance')
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': transform_3, 'Selection': greater_than, 'Distance Min': 0.0700, 'Density Max': multiply_8, 'Density Factor': mask_sprinkles_fade_with_distance, 'Seed': 50},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['chip'], 'As Instance': True})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.0000, 0.0000, -3.1416), 1: (0.0000, 0.0000, 3.1416)},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (0.0000, 0.0000, -3.1416), 1: (0.0000, 0.0000, 3.1416), 2: 1.8000, 3: 2.0000})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Instance': object_info.outputs["Geometry"], 'Rotation': random_value.outputs["Value"], 'Scale': random_value_1.outputs[1]})
    
    reroute_110 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_1})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_110})
    
    reroute_111 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_113 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_111})
    
    reroute_107 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_106})
    
    position_5 = nw.new_node(Nodes.InputPosition)
    
    capture_attribute_1 = nw.new_node(Nodes.CaptureAttribute,
        input_kwargs={'Geometry': reroute_107, 1: position_5},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'FACE'})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_113, capture_attribute_1.outputs["Geometry"]]})
    
    reroute_112 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_1})
    
    multiply_9 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Cupcake Sprinkles"], 1: 100.0000},
        attrs={'operation': 'MULTIPLY'})
    
    reroute_115 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': capture_attribute_1.outputs["Attribute"]})
    
    geometry_proximity_1 = nw.new_node(Nodes.Proximity,
        input_kwargs={'Target': reroute_111, 'Source Position': reroute_115},
        attrs={'target_element': 'POINTS'})
    
    greater_than_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: geometry_proximity_1.outputs["Distance"], 1: 0.1300},
        attrs={'operation': 'GREATER_THAN', 'use_clamp': True})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': normal})
    
    map_range = nw.new_node(Nodes.MapRange, input_kwargs={'Value': separate_xyz_2.outputs["Z"], 1: 0.3000})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_10 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    reroute_114 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_112})
    
    bounding_box_2 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_114})
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_2.outputs["Min"]})
    
    separate_xyz_9 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_2.outputs["Max"]})
    
    map_range_4 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': separate_xyz_10.outputs["Z"], 1: separate_xyz_3.outputs["Z"], 2: separate_xyz_9.outputs["Z"], 3: 1.0000, 4: 0.0000})
    
    multiply_10 = nw.new_node(Nodes.Math,
        input_kwargs={0: map_range.outputs["Result"], 1: map_range_4.outputs["Result"], 2: 0.0000},
        attrs={'operation': 'MULTIPLY'})
    
    multiply_11 = nw.new_node(Nodes.Math, input_kwargs={0: greater_than_1, 1: multiply_10, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_112, 'Distance Min': 0.0700, 'Density Max': multiply_9, 'Density Factor': multiply_11},
        attrs={'distribute_method': 'POISSON', 'use_legacy_normal': True})
    
    object_info_1 = nw.new_node(Nodes.ObjectInfo, input_kwargs={'Object': bpy.data.objects['chip'], 'As Instance': True})
    
    random_value_2 = nw.new_node(Nodes.RandomValue, input_kwargs={2: 1.5000, 3: 2.0000})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': object_info_1.outputs["Geometry"], 'Rotation': distribute_points_on_faces.outputs["Rotation"], 'Scale': random_value_2.outputs[1]})
    
    random_value_3 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: (-0.1000, -0.1000, -3.1416), 1: (0.1000, 0.1000, 3.1416), 2: 0.8000},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    rotate_instances = nw.new_node(Nodes.RotateInstances,
        input_kwargs={'Instances': instance_on_points, 'Rotation': random_value_3.outputs["Value"]})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': rotate_instances})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [join_geometry, reroute_9, reroute_10]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': join_geometry_2}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_paper, selection=selection)


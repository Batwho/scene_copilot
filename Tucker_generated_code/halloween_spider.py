import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_spherical_u_v_hack', singleton=False, type='ShaderNodeTree')
def nodegroup_spherical_u_v_hack(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput, expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000))])
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': group_input.outputs["Vector"], 'Rotation': (0.0000, 0.0000, 3.1416)},
        attrs={'rotation_type': 'EULER_XYZ'})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': vector_rotate})
    
    arctan2 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["X"], 1: separate_xyz.outputs["Y"]},
        attrs={'operation': 'ARCTAN2'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: arctan2, 1: 6.2832}, attrs={'operation': 'DIVIDE'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: divide})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"], 1: 0.0500}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': add, 'Y': multiply})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': combine_xyz}, attrs={'is_active_output': True})

@node_utils.to_nodegroup('nodegroup_vector_transform', singleton=False, type='GeometryNodeTree')
def nodegroup_vector_transform(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketVector', 'Vector', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Translate', (0.2400, 6.6000, 0.0000)),
            ('NodeSocketVector', 'Scale', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVectorEuler', 'Rotation', (-0.4730, 2.1694, 0.5969))])
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: group_input.outputs["Vector"], 1: group_input.outputs["Translate"]})
    
    multiply = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: add.outputs["Vector"], 1: group_input.outputs["Scale"], 'Scale': 0.3900},
        attrs={'operation': 'MULTIPLY'})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': multiply.outputs["Vector"], 'Rotation': group_input.outputs["Rotation"]},
        attrs={'rotation_type': 'EULER_XYZ'})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Vector': vector_rotate}, attrs={'is_active_output': True})

def shader_material_003(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord, attrs={'object': bpy.data.objects['Pumpkin']})
    
    mapping = nw.new_node(Nodes.Mapping,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': (1.0000, 1.0000, 0.1000)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': mapping, 'Scale': 11.5000, 'Roughness': 0.8000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.4348
    colorramp.color_ramp.elements[0].color = [0.2058, 0.1007, 0.0447, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.7029
    colorramp.color_ramp.elements[1].color = [0.2636, 0.3383, 0.2090, 1.0000]
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.1000, 'Distance': 0.0100, 'Height': noise_texture.outputs["Fac"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF, input_kwargs={'Base Color': colorramp.outputs["Color"], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_material_001(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    attribute = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'Color'})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': attribute.outputs["Fac"]})
    colorramp.color_ramp.interpolation = "EASE"
    colorramp.color_ramp.elements[0].position = 0.0399
    colorramp.color_ramp.elements[0].color = [0.8000, 0.1056, 0.0000, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.2862
    colorramp.color_ramp.elements[1].color = [0.8000, 0.4634, 0.0471, 1.0000]
    
    noise_texture_2 = nw.new_node(Nodes.NoiseTexture)
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': noise_texture_2.outputs["Fac"], 1: 0.3000, 3: 0.4000, 4: 0.7000})
    
    attribute_1 = nw.new_node(Nodes.Attribute, attrs={'attribute_name': 'pos'})
    
    group = nw.new_node(nodegroup_spherical_u_v_hack().name, input_kwargs={'Vector': attribute_1.outputs["Vector"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': group, 'Scale': 34.2000, 'Detail': 0.0000},
        attrs={'noise_dimensions': '2D'})
    
    noise_texture_1 = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': group, 'Scale': 61.9000, 'Detail': 8.0000},
        attrs={'noise_dimensions': '2D'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Fac"], 1: noise_texture_1.outputs["Fac"]})
    
    bump = nw.new_node(Nodes.Bump, input_kwargs={'Strength': 0.3600, 'Distance': 0.0200, 'Height': add})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Subsurface': 0.0600, 'Subsurface Color': (0.8000, 0.4634, 0.0471, 1.0000), 'Roughness': map_range.outputs["Result"], 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_pumpkin(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_6 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'Crease', 10.0000),
            ('NodeSocketInt', 'Segments', 128),
            ('NodeSocketInt', 'Rings', 64),
            ('NodeSocketVector', 'Noise_Location', (0.2400, 6.6000, 0.0000)),
            ('NodeSocketFloat', 'Noise_Scale', 0.0000),
            ('NodeSocketInt', 'Noise Seed', 618),
            ('NodeSocketBool', 'Face', True),
            ('NodeSocketInt', 'Eyes Shape', 0),
            ('NodeSocketFloat', 'Mouth Shape', 4.0000),
            ('NodeSocketFloat', 'Boundry Threshold', 0.0800),
            ('NodeSocketFloat', 'Stem Size', 0.5000),
            ('NodeSocketVectorTranslation', 'Stem Offset', (0.0000, 0.0000, 1.3000)),
            ('NodeSocketFloat', 'Stem Twist', 2.0000)])
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_6.outputs["Stem Size"]})
    
    curve_line = nw.new_node(Nodes.CurveLine, input_kwargs={'End': combine_xyz_2})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_line, 'Offset': group_input_6.outputs["Stem Offset"]})
    
    resample_curve = nw.new_node(Nodes.ResampleCurve, input_kwargs={'Curve': set_position_1})
    
    curve_parameter = nw.new_node(Nodes.SplineParameter)
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: curve_parameter.outputs["Factor"], 1: group_input_6.outputs["Stem Twist"]},
        attrs={'operation': 'MULTIPLY'})
    
    set_tilt = nw.new_node(Nodes.SetCurveTilt, input_kwargs={'Curve': resample_curve, 'Tilt': multiply})
    
    map_range_1 = nw.new_node(Nodes.MapRange, input_kwargs={'Value': curve_parameter.outputs["Factor"], 3: 0.1600, 4: 0.0500})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': map_range_1.outputs["Result"]})
    
    set_curve_radius = nw.new_node(Nodes.SetCurveRadius, input_kwargs={'Curve': set_tilt, 'Radius': reroute_4})
    
    star = nw.new_node('GeometryNodeCurveStar', input_kwargs={'Points': 7})
    
    fillet_curve = nw.new_node(Nodes.FilletCurve,
        input_kwargs={'Curve': star.outputs["Curve"], 'Count': 2, 'Radius': 0.3300, 'Limit Radius': True},
        attrs={'mode': 'POLY'})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_curve_radius, 'Profile Curve': fillet_curve, 'Fill Caps': True})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_material_003)})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere,
        input_kwargs={'Segments': group_input_6.outputs["Segments"], 'Rings': group_input_6.outputs["Rings"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz.outputs["Z"]}, attrs={'operation': 'ABSOLUTE'})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': absolute})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    map_range_2 = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': reroute_2, 1: 0.8000, 2: 2.0000, 3: 1.0000, 4: -1.0000},
        attrs={'interpolation_type': 'SMOOTHSTEP'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': 1.0000, 'Y': 1.0000, 'Z': map_range_2.outputs["Result"]})
    
    multiply_1 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_3, 1: combine_xyz_1}, attrs={'operation': 'MULTIPLY'})
    
    set_position = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': store_named_attribute, 'Position': multiply_1.outputs["Vector"]})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    value = nw.new_node(Nodes.Value)
    value.outputs[0].default_value = 0.0000
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={'ID': value, 'Seed': group_input_6.outputs["Noise Seed"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    add = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: group_input_6.outputs["Noise_Location"], 1: random_value.outputs["Value"]})
    
    vector_transform = nw.new_node(nodegroup_vector_transform().name,
        input_kwargs={'Vector': position_1, 'Translate': add.outputs["Vector"], 'Scale': group_input_6.outputs["Noise_Scale"], 'Rotation': (0.0000, 0.0000, 0.0000)})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': vector_transform, 'Scale': 1.0000})
    
    arctan2 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz.outputs["X"], 1: separate_xyz.outputs["Y"]},
        attrs={'operation': 'ARCTAN2'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: arctan2, 1: 6.2832}, attrs={'operation': 'DIVIDE'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: divide})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: group_input_6.outputs["Crease"]}, attrs={'operation': 'MULTIPLY'})
    
    fract = nw.new_node(Nodes.Math, input_kwargs={0: multiply_2, 1: -0.5000}, attrs={'operation': 'FRACT'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: fract}, attrs={'operation': 'SUBTRACT'})
    
    absolute_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: -0.5000}, attrs={'operation': 'ABSOLUTE'})
    
    float_curve = nw.new_node(Nodes.FloatCurve, input_kwargs={'Value': absolute_1})
    node_utils.assign_curve(float_curve.mapping.curves[0], [(0.0000, 0.0000), (0.5000, 1.0000), (1.0000, 0.0000)])
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: float_curve, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': reroute_2, 1: 0.8000, 2: 0.9000, 3: 0.6900, 4: 0.1000},
        attrs={'interpolation_type': 'SMOOTHSTEP'})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: multiply_3, 1: map_range.outputs["Result"]},
        attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: noise_texture.outputs["Fac"], 1: multiply_4})
    
    normal_1 = nw.new_node(Nodes.InputNormal)
    
    multiply_5 = nw.new_node(Nodes.VectorMath, input_kwargs={0: add_2, 1: normal_1}, attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_3, 1: multiply_5.outputs["Vector"]})
    
    set_position_6 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position, 'Position': add_3.outputs["Vector"]})
    
    material_assign = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': set_position_6, 'Material': surface.shaderfunc_to_material(shader_material_001)})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth, input_kwargs={'Geometry': material_assign})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_shade_smooth})
    
    curve_circle_1 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': 3, 'Radius': 0.0600})
    
    transform_1 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': curve_circle_1.outputs["Curve"], 'Translation': (0.0000, -0.1600, 0.0000), 'Rotation': (0.0000, 0.0000, -0.5236)})
    
    curve_circle_3 = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': 0.4300})
    
    index_1 = nw.new_node(Nodes.Index)
    
    less_than = nw.new_node(Nodes.Compare, input_kwargs={0: index_1, 1: 16.0000}, attrs={'operation': 'LESS_THAN'})
    
    position = nw.new_node(Nodes.InputPosition)
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': group_input_6.outputs["Mouth Shape"]})
    
    vector_rotate = nw.new_node(Nodes.VectorRotate,
        input_kwargs={'Vector': position, 'Rotation': combine_xyz},
        attrs={'rotation_type': 'EULER_XYZ'})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': curve_circle_3.outputs["Curve"], 'Selection': less_than, 'Position': vector_rotate})
    
    transform_3 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': set_position_4, 'Translation': (0.0000, -0.2700, 0.0000), 'Scale': (0.9600, 0.5200, 0.0000)})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Radius': 0.1300})
    
    index = nw.new_node(Nodes.Index)
    
    less_than_1 = nw.new_node(Nodes.Compare,
        input_kwargs={0: index, 1: group_input_6.outputs["Eyes Shape"]},
        attrs={'operation': 'LESS_THAN'})
    
    delete_geometry_1 = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': curve_circle.outputs["Curve"], 'Selection': less_than_1})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': delete_geometry_1, 'Offset': (-0.2500, 0.0000, 0.0000)})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_position_5, 'Scale': (-1.0000, 1.0000, 1.0000)})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_5, transform_2]})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [transform_1, transform_3, join_geometry_2]})
    
    fill_curve = nw.new_node(Nodes.FillCurve, input_kwargs={'Curve': join_geometry_1})
    
    transform = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': fill_curve, 'Translation': (0.0000, -2.0000, 0.3200), 'Rotation': (1.5708, 0.0000, 0.0000), 'Scale': (2.0000, 2.0000, 2.0000)})
    
    subdivide_mesh = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': transform, 'Level': 2})
    
    raycast = nw.new_node(Nodes.Raycast,
        input_kwargs={'Target Geometry': set_shade_smooth, 'Ray Direction': (0.0000, 1.0000, 0.0000)})
    
    set_position_2 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': subdivide_mesh, 'Position': raycast.outputs["Hit Position"]})
    
    geometry_proximity = nw.new_node(Nodes.Proximity, input_kwargs={'Target': set_position_2})
    
    less_equal = nw.new_node(Nodes.Compare,
        input_kwargs={0: geometry_proximity.outputs["Distance"], 1: 0.0160},
        attrs={'operation': 'LESS_EQUAL'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry, input_kwargs={'Geometry': reroute_6, 'Selection': less_equal})
    
    less_equal_1 = nw.new_node(Nodes.Compare,
        input_kwargs={0: geometry_proximity.outputs["Distance"], 1: group_input_6.outputs["Boundry Threshold"]},
        attrs={'operation': 'LESS_EQUAL'})
    
    geometry_proximity_1 = nw.new_node(Nodes.Proximity, input_kwargs={'Target': set_position_2}, attrs={'target_element': 'EDGES'})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': delete_geometry, 'Selection': less_equal_1, 'Position': geometry_proximity_1.outputs["Position"]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_6.outputs["Face"], 14: reroute_6, 15: set_position_3})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_5, switch.outputs[6]]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': multiply_3})
    
    position_5 = nw.new_node(Nodes.InputPosition)
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': join_geometry, 'Color': reroute_1, 'Position': position_5},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_pumpkin, selection=selection, attributes=[])
    surface.add_material(obj, shader_material_001, selection=selection)
    surface.add_material(obj, shader_material_003, selection=selection)
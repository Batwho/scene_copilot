import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_glass(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    glass_bsdf = nw.new_node(Nodes.GlassBSDF,
        input_kwargs={'Color': (0.8567, 0.8240, 0.7984, 1.0000), 'Roughness': 0.1615, 'IOR': 1.5000},
        attrs={'distribution': 'MULTI_GGX'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': glass_bsdf}, attrs={'is_active_output': True})

def shader_stopper(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    voronoi_texture = nw.new_node(Nodes.VoronoiTexture,
        input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': 46.9000, 'Randomness': 0.8250})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': voronoi_texture.outputs["Distance"]})
    colorramp.color_ramp.elements[0].position = 0.3500
    colorramp.color_ramp.elements[0].color = [0.0298, 0.0133, 0.0057, 1.0000]
    colorramp.color_ramp.elements[1].position = 1.0000
    colorramp.color_ramp.elements[1].color = [0.3196, 0.1009, 0.0415, 1.0000]
    
    bump = nw.new_node(Nodes.Bump,
        input_kwargs={'Strength': 0.4583, 'Distance': 0.4000, 'Height': colorramp.outputs["Color"]})
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Specular': 0.0136, 'Roughness': 0.9227, 'Normal': bump})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def shader_potion_health(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    rgb = nw.new_node(Nodes.RGB)
    rgb.outputs[0].default_value = (0.7678, 0.0000, 0.0022, 1.0000)
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': rgb, 'Subsurface Color': (0.8000, 0.0000, 0.0000, 1.0000), 'Specular': 0.5500, 'Roughness': 0.2455, 'IOR': 1.3000, 'Transmission': 1.0000, 'Emission': rgb, 'Emission Strength': 0.0100})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input_7 = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Bottle Type', 0),
            ('NodeSocketVector', 'Bottle Size', (1.0000, 1.0000, 1.0000)),
            ('NodeSocketInt', 'Bottle Resolution', 8),
            ('NodeSocketVector', 'Bezier Bottom', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Bezier Top', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketFloat', 'Opening Size', 0.2000),
            ('NodeSocketFloat', 'Nozzle Height', 0.3000),
            ('NodeSocketFloat', 'Nozzle Thickness', 0.0000),
            ('NodeSocketFloat', 'Lip Height', 0.1000),
            ('NodeSocketFloat', 'Lip Overhang', 0.5000),
            ('NodeSocketFloat', 'Wall Thickness', 0.9000),
            ('NodeSocketBool', 'Potion', True),
            ('NodeSocketMaterial', 'Potion Material', None),#surface.shaderfunc_to_material(shader_potion_health)),
            ('NodeSocketFloat', 'Potion Fill', 1.0000),
            ('NodeSocketFloat', 'Potion Fill Noise', 0.0000),
            ('NodeSocketFloat', 'Potion Noise Scroll', 0.0000),
            ('NodeSocketInt', 'Bottle Subdivision', 0),
            ('NodeSocketFloat', 'Bottle Edge Crease', 0.0000),
            ('NodeSocketBool', 'Stopper', True),
            ('NodeSocketMaterial', 'Stopper Material', None),#surface.shaderfunc_to_material(shader_stopper)),
            ('NodeSocketInt', 'Stopper Z Resolution', 3),
            ('NodeSocketFloat', 'Stopper Profile', 0.5000),
            ('NodeSocketFloat', 'Stopper Offset', 0.0500),
            ('NodeSocketFloat', 'Stopper Flare', 1.4000),
            ('NodeSocketFloat', 'Stopper Travel', 0.0000),
            ('NodeSocketInt', 'Stopper Subdivision', 0),
            ('NodeSocketFloat', 'Stopper Edge Crease', 0.0000),
            ('NodeSocketBool', 'Shade Smooth', True),
            ('NodeSocketBool', 'Finalize Geometry', True)])
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: group_input_7.outputs["Bottle Type"], 3: 1}, attrs={'data_type': 'INT'})
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={2: group_input_7.outputs["Bottle Type"]}, attrs={'data_type': 'INT'})
    
    cube = nw.new_node(Nodes.MeshCube,
        input_kwargs={'Size': group_input_7.outputs["Bottle Size"], 'Vertices X': group_input_7.outputs["Bottle Resolution"], 'Vertices Y': group_input_7.outputs["Bottle Resolution"], 'Vertices Z': group_input_7.outputs["Bottle Resolution"]})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Bottle Resolution"]})
    
    length = nw.new_node(Nodes.VectorMath, input_kwargs={0: group_input_7.outputs["Bottle Size"]}, attrs={'operation': 'LENGTH'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: length.outputs["Value"], 1: 3.0000}, attrs={'operation': 'DIVIDE'})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Segments': reroute_24, 'Rings': reroute_24, 'Radius': divide})
    
    switch = nw.new_node(Nodes.Switch,
        input_kwargs={1: greater_than_1, 14: cube.outputs["Mesh"], 15: uv_sphere.outputs["Mesh"]})
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': group_input_7.outputs["Bottle Resolution"], 'Radius': group_input_7.outputs["Opening Size"]})
    
    bezier_segment = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Resolution': group_input_7.outputs["Bottle Resolution"], 'Start': (0.0000, 0.0000, 0.0000), 'Start Handle': group_input_7.outputs["Bezier Bottom"], 'End Handle': group_input_7.outputs["Bezier Top"], 'End': (0.0000, 0.0000, 1.0000)})
    
    transform_5 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': bezier_segment, 'Translation': (0.0000, 0.6000, 0.0000), 'Rotation': (1.5708, 0.0000, 0.0000), 'Scale': group_input_7.outputs["Bottle Size"]})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_circle.outputs["Curve"], 'Profile Curve': transform_5, 'Fill Caps': True})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': curve_to_mesh})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Bottle Resolution"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Opening Size"]})
    
    mesh_circle_1 = nw.new_node(Nodes.MeshCircle,
        input_kwargs={'Vertices': reroute_21, 'Radius': reroute_7},
        attrs={'fill_type': 'TRIANGLE_FAN'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_circle_1, 'Offset': (0.0000, 0.0000, -0.6000)})
    
    flip_faces_1 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position_1})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [flip_faces, flip_faces_1]})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': join_geometry_3})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than, 14: switch.outputs[6], 15: reroute_26})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_1.outputs[6]})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_35})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Wall Thickness"]})
    
    equal = nw.new_node(Nodes.Compare,
        input_kwargs={2: group_input_7.outputs["Bottle Type"], 3: 1},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Wall Thickness"], 1: 1.0500},
        attrs={'operation': 'MULTIPLY'})
    
    clamp_4 = nw.new_node(Nodes.Clamp, input_kwargs={'Value': multiply, 'Max': 0.9900})
    
    switch_9 = nw.new_node(Nodes.Switch,
        input_kwargs={0: equal, 2: clamp_4, 3: group_input_7.outputs["Wall Thickness"]},
        attrs={'input_type': 'FLOAT'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_38, 'Y': reroute_38, 'Z': switch_9.outputs["Output"]})
    
    transform_geometry_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_11, 'Scale': combine_xyz_7})
    
    flip_faces_2 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': transform_geometry_2})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': flip_faces_2})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_3})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Bottle Type"]})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_33})
    
    not_equal = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_32, 3: 2}, attrs={'operation': 'NOT_EQUAL', 'data_type': 'INT'})
    
    divide_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Bottle Resolution"], 1: 6.0000},
        attrs={'operation': 'DIVIDE'})
    
    clamp_1 = nw.new_node(Nodes.Clamp, input_kwargs={'Value': divide_1, 'Min': 1.0000, 'Max': 32.0000})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': group_input_7.outputs["Bottle Resolution"], 'Side Segments': clamp_1, 'Radius': group_input_7.outputs["Opening Size"], 'Depth': group_input_7.outputs["Nozzle Height"]},
        attrs={'fill_type': 'NONE'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Selection': cylinder.outputs["Bottom"]},
        attrs={'domain': 'FACE'})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': delete_geometry})
    
    bounding_box_2 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_6})
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_2.outputs["Min"]})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    bounding_box_1 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_16})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_1.outputs["Max"]})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_3.outputs["Z"], 1: separate_xyz_2.outputs["Z"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_1})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_6, 'Offset': combine_xyz_4})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_3})
    
    multiply_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Lip Overhang"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: group_input_7.outputs["Opening Size"], 1: multiply_2})
    
    cylinder_3 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': group_input_7.outputs["Bottle Resolution"], 'Fill Segments': 2, 'Radius': add, 'Depth': group_input_7.outputs["Lip Height"]},
        attrs={'fill_type': 'TRIANGLE_FAN'})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': cylinder_3.outputs["Mesh"]})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    bounding_box_3 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_10})
    
    separate_xyz_4 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_3.outputs["Min"]})
    
    bounding_box_5 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': set_position_3})
    
    separate_xyz_8 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_5.outputs["Max"]})
    
    subtract_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_4.outputs["Z"], 1: separate_xyz_8.outputs["Z"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_1, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_3})
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_10, 'Offset': combine_xyz_5})
    
    union = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 2': [reroute_31, set_position_5]}, attrs={'operation': 'UNION'})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': union.outputs["Mesh"]})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_22})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_20})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_34, reroute_14]})
    
    equal_1 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_33, 3: 1}, attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    multiply_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Opening Size"], 1: -0.3000},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_4})
    
    transform_geometry_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_22, 'Translation': combine_xyz_1})
    
    switch_8 = nw.new_node(Nodes.Switch, input_kwargs={1: equal_1, 14: reroute_34, 15: transform_geometry_1})
    
    union_1 = nw.new_node(Nodes.MeshBoolean,
        input_kwargs={'Mesh 2': [switch_8.outputs[6], reroute_20]},
        attrs={'operation': 'UNION'})
    
    switch_7 = nw.new_node(Nodes.Switch, input_kwargs={1: not_equal, 14: join_geometry_2, 15: union_1.outputs["Mesh"]})
    
    merge_by_distance_2 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': switch_7.outputs[6]})
    
    join_geometry_4 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_15, merge_by_distance_2]})
    
    equal_2 = nw.new_node(Nodes.Compare,
        input_kwargs={2: group_input_7.outputs["Bottle Type"], 3: 1},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    divide_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Bottle Resolution"], 1: 6.0000},
        attrs={'operation': 'DIVIDE'})
    
    clamp_2 = nw.new_node(Nodes.Clamp, input_kwargs={'Value': divide_2, 'Min': 1.0000, 'Max': 32.0000})
    
    add_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Nozzle Height"], 1: group_input_7.outputs["Lip Height"]})
    
    separate_xyz_9 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': group_input_7.outputs["Bottle Size"]})
    
    multiply_5 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_9.outputs["Z"], 1: 1.0000}, attrs={'operation': 'MULTIPLY'})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: add_1, 1: multiply_5})
    
    cylinder_2 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': group_input_7.outputs["Bottle Resolution"], 'Side Segments': clamp_2, 'Radius': group_input_7.outputs["Opening Size"], 'Depth': add_2},
        attrs={'fill_type': 'NONE'})
    
    bounding_box_7 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': cylinder_2.outputs["Mesh"]})
    
    separate_xyz_11 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_7.outputs["Min"]})
    
    bounding_box_6 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_8})
    
    separate_xyz_10 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_6.outputs["Max"]})
    
    subtract_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_11.outputs["Z"], 1: separate_xyz_10.outputs["Z"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_6 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_2, 1: -1.0000, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_6})
    
    set_position_8 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': cylinder_2.outputs["Mesh"], 'Offset': combine_xyz_6})
    
    set_position_10 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': set_position_8, 'Selection': cylinder_2.outputs["Bottom"], 'Offset': (0.0000, 0.0000, -0.2000)})
    
    switch_5 = nw.new_node(Nodes.Switch, input_kwargs={1: equal_2, 14: set_position_8, 15: set_position_10})
    
    subtract_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Wall Thickness"], 1: group_input_7.outputs["Nozzle Thickness"]},
        attrs={'operation': 'SUBTRACT'})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_3})
    
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_36, 'Y': reroute_36, 'Z': 1.0000})
    
    transform_geometry_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': switch_5.outputs[6], 'Scale': combine_xyz_10})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_geometry_3})
    
    difference = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': join_geometry_4, 'Mesh 2': reroute_25})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': difference.outputs["Mesh"]})
    
    switch_4 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input_7.outputs["Finalize Geometry"], 14: join_geometry_4, 15: merge_by_distance})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': switch_4.outputs[6], 'Material': surface.shaderfunc_to_material(shader_glass)})
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': set_material_2, 'Level': group_input_7.outputs["Bottle Subdivision"], 'Edge Crease': group_input_7.outputs["Bottle Edge Crease"]})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Bottle Resolution"]})
    
    multiply_7 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Opening Size"], 1: 0.9450},
        attrs={'operation': 'MULTIPLY'})
    
    cylinder_1 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': reroute_29, 'Side Segments': group_input_7.outputs["Stopper Z Resolution"], 'Radius': multiply_7, 'Depth': 0.2000})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': cylinder_1.outputs["Mesh"]})
    
    bounding_box_9 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute})
    
    separate_xyz_13 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_9.outputs["Max"]})
    
    bounding_box_8 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': set_position_5})
    
    separate_xyz_12 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_8.outputs["Max"]})
    
    subtract_4 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_13.outputs["Z"], 1: separate_xyz_12.outputs["Z"]},
        attrs={'operation': 'SUBTRACT'})
    
    multiply_8 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_4, 1: -1.0000, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_8})
    
    set_position_9 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute, 'Offset': combine_xyz})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': cylinder_1.outputs["Top"]})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Stopper Flare"]})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': set_position_9, 'Selection': reroute_4, 'Scale': reroute_2})
    
    multiply_9 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Stopper Profile"], 1: 0.1000},
        attrs={'operation': 'MULTIPLY'})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': scale_elements_1, 'Selection': reroute_4, 'Offset Scale': multiply_9})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': 0.5000, 'Axis': (-1.4000, 0.3000, 8.2000)})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': cylinder_1.outputs["Bottom"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Nozzle Height"]})
    
    multiply_10 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_5, 1: -0.5000, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Stopper Travel"]})
    
    multiply_11 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_10, 1: multiply_11})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_3})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': scale_elements, 'Selection': reroute_9, 'Offset': combine_xyz_3})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    extrude_mesh_1 = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': set_position_4, 'Selection': reroute_30, 'Offset Scale': 0.1000})
    
    scale_elements_2 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh_1.outputs["Mesh"], 'Selection': extrude_mesh_1.outputs["Top"], 'Scale': 0.8000})
    
    subtract_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Wall Thickness"], 1: group_input_7.outputs["Nozzle Thickness"]},
        attrs={'operation': 'SUBTRACT'})
    
    subtract_6 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_5, 1: 0.0100}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_13 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract_6, 'Y': subtract_6, 'Z': 1.0000})
    
    transform_geometry_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': scale_elements_2, 'Scale': combine_xyz_13})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': transform_geometry_4, 'Material': group_input_7.outputs["Stopper Material"]})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input_7.outputs["Stopper Offset"]})
    
    transform_12 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_material, 'Translation': combine_xyz_9})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_7.outputs["Stopper"], 15: transform_12})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': switch_2.outputs[6], 'Level': group_input_7.outputs["Stopper Subdivision"], 'Edge Crease': group_input_7.outputs["Stopper Edge Crease"]})
    
    greater_than_2 = nw.new_node(Nodes.Compare, input_kwargs={2: group_input_7.outputs["Bottle Type"], 3: 1}, attrs={'data_type': 'INT'})
    
    mesh_circle_2 = nw.new_node(Nodes.MeshCircle,
        input_kwargs={'Vertices': reroute_21, 'Radius': reroute_7},
        attrs={'fill_type': 'TRIANGLE_FAN'})
    
    flip_faces_4 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': mesh_circle_2})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': flip_faces_4})
    
    position_1 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_1})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': join_geometry_3})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Max"]})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_1.outputs["X"], 'Y': separate_xyz_1.outputs["Y"], 'Z': separate_xyz.outputs["Z"]})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_12, 'Position': combine_xyz_2})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_26, set_position_2]})
    
    merge_by_distance_1 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry})
    
    switch_3 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than_2, 14: switch.outputs[6], 15: merge_by_distance_1})
    
    subtract_7 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Wall Thickness"], 1: 0.0100},
        attrs={'operation': 'SUBTRACT'})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': subtract_7})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_40})
    
    equal_3 = nw.new_node(Nodes.Compare,
        input_kwargs={2: group_input_7.outputs["Bottle Type"], 3: 1},
        attrs={'operation': 'EQUAL', 'data_type': 'INT'})
    
    multiply_12 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_7, 1: 1.0500}, attrs={'operation': 'MULTIPLY'})
    
    clamp_3 = nw.new_node(Nodes.Clamp, input_kwargs={'Value': multiply_12, 'Max': 0.9900})
    
    switch_10 = nw.new_node(Nodes.Switch, input_kwargs={0: equal_3, 2: clamp_3, 3: reroute_40}, attrs={'input_type': 'FLOAT'})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': reroute_41, 'Y': reroute_41, 'Z': switch_10.outputs["Output"]})
    
    transform_geometry = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': switch_3.outputs[6], 'Scale': combine_xyz_8})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_geometry})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    bounding_box_4 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_18})
    
    separate_xyz_5 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_4.outputs["Max"]})
    
    multiply_13 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_5.outputs["X"], 1: 2.5000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_14 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_5.outputs["Y"], 1: 2.5000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_15 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input_7.outputs["Bottle Resolution"]},
        attrs={'operation': 'MULTIPLY'})
    
    clamp = nw.new_node(Nodes.Clamp, input_kwargs={'Value': multiply_15, 'Min': 2.0000, 'Max': 64.0000})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': clamp})
    
    grid = nw.new_node(Nodes.MeshGrid,
        input_kwargs={'Size X': multiply_13, 'Size Y': multiply_14, 'Vertices X': reroute_28, 'Vertices Y': reroute_28})
    
    flip_faces_6 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': grid.outputs["Mesh"]})
    
    position = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_7 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position})
    
    separate_xyz_6 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_4.outputs["Min"]})
    
    subtract_8 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_6.outputs["Z"], 1: 0.2000}, attrs={'operation': 'SUBTRACT'})
    
    map_range = nw.new_node(Nodes.MapRange,
        input_kwargs={'Value': group_input_7.outputs["Potion Fill"], 3: subtract_8, 4: separate_xyz_5.outputs["Z"]})
    
    combine_xyz_11 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': separate_xyz_7.outputs["X"], 'Y': separate_xyz_7.outputs["Y"], 'Z': map_range.outputs["Result"]})
    
    set_position_6 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': flip_faces_6, 'Position': combine_xyz_11})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input_7.outputs["Potion Fill Noise"]})
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'W': group_input_7.outputs["Potion Noise Scroll"], 'Scale': reroute_37},
        attrs={'noise_dimensions': '4D'})
    
    multiply_16 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_37, 1: 0.1000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_17 = nw.new_node(Nodes.Math,
        input_kwargs={0: noise_texture.outputs["Fac"], 1: multiply_16},
        attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_12 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_17})
    
    set_position_7 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': set_position_6, 'Offset': combine_xyz_12})
    
    difference_1 = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': reroute_13, 'Mesh 2': set_position_7})
    
    set_material_6 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': difference_1.outputs["Mesh"], 'Material': group_input_7.outputs["Potion Material"]})
    
    subdivision_surface_2 = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': set_material_6, 'Level': group_input_7.outputs["Bottle Subdivision"], 'Edge Crease': group_input_7.outputs["Bottle Edge Crease"]})
    
    switch_6 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input_7.outputs["Potion"], 15: subdivision_surface_2})
    
    join_geometry_5 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [subdivision_surface_1, subdivision_surface, switch_6.outputs[6]]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': join_geometry_5, 'Shade Smooth': group_input_7.outputs["Shade Smooth"]})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_shade_smooth})
    
    bounding_box_10 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_39})
    
    separate_xyz_14 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_10.outputs["Min"]})
    
    multiply_18 = nw.new_node(Nodes.Math, input_kwargs={0: separate_xyz_14.outputs["Z"], 1: -1.0000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_14 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_18})
    
    set_position_11 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_39, 'Offset': combine_xyz_14})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_position_11}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
apply(bpy.context.active_object)
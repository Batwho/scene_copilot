import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



def shader_stopper(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    voronoi_texture = nw.new_node(Nodes.VoronoiTexture, input_kwargs={'Scale': 46.9000, 'Randomness': 0.8250})
    
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

def shader_glass(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    glass_bsdf = nw.new_node(Nodes.GlassBSDF,
        input_kwargs={'Color': (0.8567, 0.8240, 0.7984, 1.0000), 'Roughness': 0.1615, 'IOR': 1.5000},
        attrs={'distribution': 'MULTI_GGX'})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': glass_bsdf}, attrs={'is_active_output': True})

def shader_potion_health(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    rgb = nw.new_node(Nodes.RGB)
    rgb.outputs[0].default_value = (0.7678, 0.0000, 0.0022, 1.0000)
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': rgb, 'Subsurface Color': (0.8000, 0.0000, 0.0000, 1.0000), 'Specular': 0.5500, 'Roughness': 0.2455, 'IOR': 1.3000, 'Transmission': 1.0000, 'Emission': rgb, 'Emission Strength': 0.0100})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketInt', 'Potion Type', 0),
            ('NodeSocketInt', 'Potion Resolution', 8),
            ('NodeSocketBool', 'Stopper', True),
            ('NodeSocketBool', 'Potion', True),
            ('NodeSocketInt', 'Stopper Subdivisions', 0),
            ('NodeSocketFloat', 'Stopper Edge Crease', 0.0000),
            ('NodeSocketFloat', 'Stopper Profile', 0.1000),
            ('NodeSocketFloat', 'Stopper Offset', 0.0000),
            ('NodeSocketFloat', 'Stopper Flare', 1.4000),
            ('NodeSocketFloat', 'Stopper Travel', 0.0000),
            ('NodeSocketFloat', 'Nozzle Height', 0.3000),
            ('NodeSocketInt', 'Cube Resolution', 4),
            ('NodeSocketVector', 'Bottle Size', (1.0000, 1.0000, 1.0000)),
            ('NodeSocketFloat', 'Bottle Opening Size', 0.2000),
            ('NodeSocketVector', 'Bezier Bottom', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketVector', 'Bezier Top', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketBool', 'Shade Smooth', False)])
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Potion Type"]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_16, 3: 1}, attrs={'data_type': 'INT'})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': greater_than})
    
    reroute_54 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_54})
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={2: reroute_15}, attrs={'data_type': 'INT'})
    
    reroute_41 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': greater_than_1})
    
    reroute_38 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bottle Size"]})
    
    cube = nw.new_node(Nodes.MeshCube,
        input_kwargs={'Size': reroute_38, 'Vertices X': group_input.outputs["Cube Resolution"], 'Vertices Y': group_input.outputs["Cube Resolution"], 'Vertices Z': group_input.outputs["Cube Resolution"]})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cube.outputs["Mesh"], 'Name': 'uv_map', 3: cube.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': store_named_attribute})
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface, input_kwargs={'Mesh': reroute_12})
    
    reroute_39 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Potion Resolution"]})
    
    reroute_40 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_39})
    
    reroute_27 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_40})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_27})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_24, 1: 2.0000})
    
    reroute_42 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_24})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_38})
    
    length = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_25}, attrs={'operation': 'LENGTH'})
    
    divide = nw.new_node(Nodes.Math, input_kwargs={0: length.outputs["Value"], 1: 3.0000}, attrs={'operation': 'DIVIDE'})
    
    uv_sphere = nw.new_node(Nodes.MeshUVSphere, input_kwargs={'Segments': add, 'Rings': reroute_42, 'Radius': divide})
    
    store_named_attribute_1 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': uv_sphere.outputs["Mesh"], 'Name': 'uv_map', 3: uv_sphere.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_41, 14: subdivision_surface_1, 15: store_named_attribute_1})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Bottle Opening Size"]})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_29 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_18})
    
    curve_circle = nw.new_node(Nodes.CurveCircle, input_kwargs={'Resolution': reroute_42, 'Radius': reroute_29})
    
    bezier_segment = nw.new_node(Nodes.CurveBezierSegment,
        input_kwargs={'Resolution': group_input.outputs["Potion Resolution"], 'Start': (0.0000, 0.0000, 0.0000), 'Start Handle': group_input.outputs["Bezier Bottom"], 'End Handle': group_input.outputs["Bezier Top"], 'End': (0.0000, 0.0000, 1.0000)})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_25})
    
    transform_5 = nw.new_node(Nodes.Transform,
        input_kwargs={'Geometry': bezier_segment, 'Translation': (0.0000, 0.6000, 0.0000), 'Rotation': (1.5708, 0.0000, 0.0000), 'Scale': reroute_22})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': curve_circle.outputs["Curve"], 'Profile Curve': transform_5, 'Fill Caps': True})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': curve_to_mesh})
    
    flip_faces = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={1: greater_than, 14: switch.outputs[6], 15: flip_faces})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': switch_1.outputs[6]})
    
    scale_elements_5 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': reroute_9, 'Scale': 0.8500},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_9 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements_5, 'Scale': 0.8500, 'Axis': (0.0000, 1.0000, 0.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_10 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements_9, 'Scale': 0.9000, 'Axis': (0.0000, 0.0000, 1.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    reroute_31 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': scale_elements_10})
    
    reroute_43 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_31})
    
    reroute_49 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_43})
    
    set_material_3 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': reroute_49, 'Material': surface.shaderfunc_to_material(shader_potion_health)})
    
    reroute_47 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_3})
    
    switch_6 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Potion"], 15: reroute_47})
    
    reroute_55 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Potion"]})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Potion Resolution"]})
    
    multiply = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Bottle Opening Size"], 1: 0.9000},
        attrs={'operation': 'MULTIPLY'})
    
    mesh_circle_2 = nw.new_node(Nodes.MeshCircle,
        input_kwargs={'Vertices': reroute_21, 'Radius': multiply},
        attrs={'fill_type': 'TRIANGLE_FAN'})
    
    flip_faces_4 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': mesh_circle_2})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': flip_faces_4})
    
    reroute_11 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    scale_elements_6 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': reroute_11, 'Scale': 0.9000},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_7 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements_6, 'Scale': 0.9000, 'Axis': (0.0000, 1.0000, 0.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    scale_elements_8 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': scale_elements_7, 'Scale': 0.9500, 'Axis': (0.0000, 0.0000, 1.0000)},
        attrs={'scale_mode': 'SINGLE_AXIS'})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Potion Resolution"]})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_7})
    
    reroute_51 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_51})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_26})
    
    reroute_34 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Nozzle Height"]})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_34})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    cylinder = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': reroute_3, 'Radius': reroute_19, 'Depth': reroute_2},
        attrs={'fill_type': 'NONE'})
    
    store_named_attribute_3 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    delete_geometry = nw.new_node(Nodes.DeleteGeometry,
        input_kwargs={'Geometry': store_named_attribute_3, 'Selection': cylinder.outputs["Bottom"]},
        attrs={'domain': 'FACE'})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_19, 1: 0.0500})
    
    cylinder_3 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': reroute_3, 'Fill Segments': 2, 'Radius': add_1, 'Depth': 0.1000},
        attrs={'fill_type': 'TRIANGLE_FAN'})
    
    store_named_attribute_2 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder_3.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder_3.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_2})
    
    multiply_add = nw.new_node(Nodes.Math, input_kwargs={0: reroute_1, 2: 0.0500}, attrs={'operation': 'MULTIPLY_ADD'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_add})
    
    transform_2 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_2, 'Translation': combine_xyz_1})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [delete_geometry, transform_2]})
    
    reroute_33 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_51})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_26, 1: 0.9500}, attrs={'operation': 'MULTIPLY'})
    
    cylinder_2 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': reroute_33, 'Radius': multiply_1, 'Depth': 0.2000},
        attrs={'fill_type': 'NONE'})
    
    store_named_attribute_5 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder_2.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder_2.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    transform_4 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_5, 'Scale': (0.9500, 0.9500, 0.9500)})
    
    reroute_36 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_6})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_36})
    
    multiply_add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_10, 2: 0.0320}, attrs={'operation': 'MULTIPLY_ADD'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_add_1})
    
    transform_7 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': transform_4, 'Translation': combine_xyz})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_13, 1: -1.0000, 2: 0.2000}, attrs={'operation': 'MULTIPLY'})
    
    combine_xyz_7 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': multiply_2})
    
    set_position_5 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': transform_7, 'Selection': cylinder_2.outputs["Bottom"], 'Offset': combine_xyz_7})
    
    reroute_44 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_5})
    
    difference = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': join_geometry_2, 'Mesh 2': reroute_44})
    
    set_material_1 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': difference.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_glass)})
    
    reroute_14 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_material_1})
    
    reroute_28 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    multiply_3 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_28, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    bounding_box = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_9})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box.outputs["Max"]})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_3, 1: separate_xyz.outputs["Z"]})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_2})
    
    transform_6 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_14, 'Translation': combine_xyz_4})
    
    bounding_box_2 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': transform_6})
    
    separate_xyz_3 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_2.outputs["Min"]})
    
    bounding_box_3 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': scale_elements_8})
    
    separate_xyz_4 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_3.outputs["Max"]})
    
    subtract = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_3.outputs["Z"], 1: separate_xyz_4.outputs["Z"]},
        attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_10 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': subtract})
    
    transform_geometry = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': scale_elements_8, 'Translation': combine_xyz_10})
    
    reroute_30 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_geometry})
    
    bounding_box_1 = nw.new_node(Nodes.BoundingBox, input_kwargs={'Geometry': reroute_30})
    
    separate_xyz_2 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_1.outputs["Max"]})
    
    combine_xyz_6 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': separate_xyz_2.outputs["Z"]})
    
    set_position_3 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_20, 'Offset': combine_xyz_6})
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': bounding_box_1.outputs["Min"]})
    
    combine_xyz_5 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': separate_xyz_1.outputs["Z"]})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': reroute_20, 'Offset': combine_xyz_5})
    
    join_geometry_7 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_30, set_position_2]})
    
    merge_by_distance_1 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_7})
    
    join_geometry = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [set_position_3, merge_by_distance_1]})
    
    merge_by_distance_2 = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry})
    
    flip_faces_5 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': merge_by_distance_2})
    
    set_material_4 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': flip_faces_5, 'Material': surface.shaderfunc_to_material(shader_potion_health)})
    
    geometry_to_instance = nw.new_node('GeometryNodeGeometryToInstance', input_kwargs={'Geometry': set_material_4})
    
    scale_instances = nw.new_node(Nodes.ScaleInstances,
        input_kwargs={'Instances': geometry_to_instance, 'Scale': (0.9900, 0.9900, 0.9900)})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': scale_instances})
    
    switch_5 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_55, 15: realize_instances})
    
    switch_4 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_23, 14: switch_6.outputs[6], 15: switch_5.outputs[6]})
    
    not_equal = nw.new_node(Nodes.Compare,
        input_kwargs={2: group_input.outputs["Potion Type"], 3: 1},
        attrs={'operation': 'NOT_EQUAL', 'data_type': 'INT'})
    
    cylinder_1 = nw.new_node('GeometryNodeMeshCylinder',
        input_kwargs={'Vertices': reroute_33, 'Side Segments': 2, 'Radius': multiply_1, 'Depth': 0.2000})
    
    store_named_attribute_4 = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': cylinder_1.outputs["Mesh"], 'Name': 'uv_map', 3: cylinder_1.outputs["UV Map"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'CORNER'})
    
    transform = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': store_named_attribute_4, 'Scale': (0.9000, 0.9000, 0.9000)})
    
    scale_elements_1 = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': transform, 'Selection': cylinder_1.outputs["Top"], 'Scale': group_input.outputs["Stopper Flare"]})
    
    reroute_37 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Stopper Profile"]})
    
    reroute_45 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_37})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_45})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute})
    
    extrude_mesh = nw.new_node(Nodes.ExtrudeMesh,
        input_kwargs={'Mesh': scale_elements_1, 'Selection': cylinder_1.outputs["Top"], 'Offset Scale': reroute_4})
    
    scale_elements = nw.new_node(Nodes.ScaleElements,
        input_kwargs={'Geometry': extrude_mesh.outputs["Mesh"], 'Selection': extrude_mesh.outputs["Top"], 'Scale': 0.5000, 'Axis': (-1.4000, 0.3000, 8.2000)})
    
    transform_1 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': scale_elements, 'Translation': combine_xyz})
    
    reroute_35 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_13})
    
    multiply_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_35, 1: -0.5000, 2: 0.0000}, attrs={'operation': 'MULTIPLY'})
    
    multiply_5 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Stopper Travel"], 1: -1.0000},
        attrs={'operation': 'MULTIPLY'})
    
    add_3 = nw.new_node(Nodes.Math, input_kwargs={0: multiply_4, 1: multiply_5})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_3})
    
    set_position_4 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': transform_1, 'Selection': cylinder_1.outputs["Bottom"], 'Offset': combine_xyz_3})
    
    subdivision_surface = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': set_position_4, 'Level': group_input.outputs["Stopper Subdivisions"], 'Edge Crease': group_input.outputs["Stopper Edge Crease"]})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': subdivision_surface, 'Material': surface.shaderfunc_to_material(shader_stopper)})
    
    combine_xyz_9 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["Stopper Offset"]})
    
    transform_12 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': set_material, 'Translation': combine_xyz_9})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={1: group_input.outputs["Stopper"], 15: transform_12})
    
    reroute_32 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': separate_xyz.outputs["Z"]})
    
    multiply_add_2 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_28, 2: -0.0500}, attrs={'operation': 'MULTIPLY_ADD'})
    
    add_4 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_32, 1: multiply_add_2})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_4})
    
    transform_10 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': switch_2.outputs[6], 'Translation': combine_xyz_2})
    
    transform_9 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': switch_2.outputs[6], 'Translation': combine_xyz_4})
    
    switch_8 = nw.new_node(Nodes.Switch, input_kwargs={1: not_equal, 14: transform_10, 15: transform_9})
    
    not_equal_1 = nw.new_node(Nodes.Compare,
        input_kwargs={2: group_input.outputs["Potion Type"], 3: 1},
        attrs={'operation': 'NOT_EQUAL', 'data_type': 'INT'})
    
    transform_3 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_14, 'Translation': combine_xyz_2})
    
    switch_3 = nw.new_node(Nodes.Switch, input_kwargs={1: not_equal_1, 14: transform_3, 15: transform_6})
    
    reroute_52 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    scale_elements_2 = nw.new_node(Nodes.ScaleElements, input_kwargs={'Geometry': reroute_31, 'Scale': 1.0100})
    
    flip_faces_2 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': scale_elements_2})
    
    join_geometry_3 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_52, flip_faces_2]})
    
    reroute_46 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_44})
    
    combine_xyz_8 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': add_2})
    
    transform_8 = nw.new_node(Nodes.Transform, input_kwargs={'Geometry': reroute_46, 'Translation': combine_xyz_8})
    
    reroute_53 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': transform_8})
    
    difference_1 = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': join_geometry_3, 'Mesh 2': reroute_53})
    
    set_material_2 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': difference_1.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_glass)})
    
    reroute_57 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_11})
    
    mesh_circle_1 = nw.new_node(Nodes.MeshCircle,
        input_kwargs={'Vertices': reroute_21, 'Radius': group_input.outputs["Bottle Opening Size"]},
        attrs={'fill_type': 'TRIANGLE_FAN'})
    
    set_position_1 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': mesh_circle_1, 'Offset': (0.0000, 0.0000, -0.6000)})
    
    flip_faces_1 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': set_position_1})
    
    flip_faces_3 = nw.new_node(Nodes.FlipFaces, input_kwargs={'Mesh': merge_by_distance_1})
    
    switch_9 = nw.new_node(Nodes.Switch,
        input_kwargs={1: group_input.outputs["Potion"], 14: flip_faces_3, 15: merge_by_distance_1})
    
    join_geometry_6 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_57, flip_faces_1, switch_9.outputs[6]]})
    
    reroute_58 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_53})
    
    reroute_48 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_58})
    
    reroute_56 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_48})
    
    difference_2 = nw.new_node(Nodes.MeshBoolean, input_kwargs={'Mesh 1': join_geometry_6, 'Mesh 2': reroute_56})
    
    set_material_5 = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': difference_2.outputs["Mesh"], 'Material': surface.shaderfunc_to_material(shader_glass)})
    
    switch_10 = nw.new_node(Nodes.Switch, input_kwargs={1: reroute_54, 14: set_material_2, 15: set_material_5})
    
    join_geometry_9 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [switch_3.outputs[6], switch_10.outputs[6]]})
    
    merge_by_distance = nw.new_node(Nodes.MergeByDistance, input_kwargs={'Geometry': join_geometry_9})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry,
        input_kwargs={'Geometry': [switch_4.outputs[6], switch_8.outputs[6], merge_by_distance]})
    
    set_shade_smooth = nw.new_node(Nodes.SetShadeSmooth,
        input_kwargs={'Geometry': join_geometry_1, 'Shade Smooth': group_input.outputs["Shade Smooth"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': set_shade_smooth}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_potion_health, selection=selection)
apply(bpy.context.active_object)
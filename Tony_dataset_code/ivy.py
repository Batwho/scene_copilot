import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_ivy', singleton=False, type='GeometryNodeTree')
def nodegroup_ivy(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketFloat', 'branchDensity', 3.0000),
            ('NodeSocketVectorTranslation', 'branch direction', (1.0000, 4.4000, 0.0000)),
            ('NodeSocketCollection', 'target',None),# bpy.data.collections['Collection 2.002']),
            ('NodeSocketFloat', 'gravity', 0.0000),
            ('NodeSocketFloat', 'straight branch lenght', 0.0000),
            ('NodeSocketInt', 'Level', 3),
            ('NodeSocketFloat', 'ivy Density', 300.0000),
            ('NodeSocketFloat', 'leaf size', 0.0000),
            ('NodeSocketGeometry', 'Profile Curve', None),
            ('NodeSocketInt', 'Seed', 0)])
    
    collection_info = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': group_input.outputs["target"]},
        attrs={'transform_space': 'RELATIVE'})
    
    realize_instances_1 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': collection_info}, attrs={'legacy_behavior': True})
    
    reroute_3 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': realize_instances_1})
    
    reroute_19 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["Seed"]})
    
    reroute_1 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    distribute_points_on_faces = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_3, 'Density': group_input.outputs["branchDensity"], 'Seed': reroute_1},
        attrs={'use_legacy_normal': True})
    
    mesh_line = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': 2, 'Offset': group_input.outputs["branch direction"]})
    
    reroute_5 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': mesh_line})
    
    reroute_2 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_5})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces.outputs["Points"], 'Instance': reroute_2, 'Scale': (1.8000, 1.8000, 1.8000)})
    
    realize_instances = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points}, attrs={'legacy_behavior': True})
    
    position = nw.new_node(Nodes.InputPosition)
    
    geometry_proximity = nw.new_node(Nodes.Proximity, input_kwargs={'Target': realize_instances_1, 'Source Position': position})
    
    reroute_8 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': geometry_proximity.outputs["Position"]})
    
    reroute_9 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_8})
    
    reroute_10 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_9})
    
    reroute_4 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_10})
    
    set_position = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': realize_instances, 'Position': reroute_4})
    
    subdivide_mesh = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': set_position})
    
    reroute_25 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': geometry_proximity.outputs["Distance"]})
    
    greater_than = nw.new_node(Nodes.Math, input_kwargs={0: reroute_25, 1: 0.1000}, attrs={'operation': 'GREATER_THAN'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["gravity"]})
    
    reroute_23 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': combine_xyz_1})
    
    reroute_26 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_23})
    
    set_position_1 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': subdivide_mesh, 'Selection': greater_than, 'Offset': reroute_26})
    
    realize_instances_3 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': set_position_1}, attrs={'legacy_behavior': True})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["branchDensity"]}, attrs={'operation': 'MULTIPLY'})
    
    reroute = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_1})
    
    distribute_points_on_faces_2 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_3, 'Density': multiply, 'Seed': reroute},
        attrs={'use_legacy_normal': True})
    
    mesh_line_1 = nw.new_node(Nodes.MeshLine, input_kwargs={'Count': 2})
    
    instance_on_points_2 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_2.outputs["Points"], 'Instance': mesh_line_1, 'Scale': (1.8000, 1.8000, 1.8000)})
    
    realize_instances_4 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_2}, attrs={'legacy_behavior': True})
    
    index = nw.new_node(Nodes.Index)
    
    modulo = nw.new_node(Nodes.Math, input_kwargs={0: index, 1: 2.0000}, attrs={'operation': 'MODULO'})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'Z': group_input.outputs["straight branch lenght"]})
    
    set_position_3 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': realize_instances_4, 'Selection': modulo, 'Offset': combine_xyz})
    
    reroute_6 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_3})
    
    distribute_points_on_faces_1 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_3, 'Density': multiply, 'Seed': reroute},
        attrs={'use_legacy_normal': True})
    
    instance_on_points_1 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': distribute_points_on_faces_1.outputs["Points"], 'Instance': reroute_2, 'Scale': (1.8000, 1.8000, 1.8000)})
    
    realize_instances_2 = nw.new_node(Nodes.RealizeInstances, input_kwargs={'Geometry': instance_on_points_1}, attrs={'legacy_behavior': True})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': realize_instances_2, 'Position': reroute_4})
    
    subdivide_mesh_2 = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': set_position_2})
    
    greater_than_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_25, 1: 0.1000}, attrs={'operation': 'GREATER_THAN'})
    
    add = nw.new_node(Nodes.VectorMath, input_kwargs={0: reroute_26, 1: (0.0000, 0.0000, 2.0000)})
    
    set_position_6 = nw.new_node(Nodes.SetPosition,
        input_kwargs={'Geometry': subdivide_mesh_2, 'Selection': greater_than_1, 'Offset': add.outputs["Vector"]})
    
    reroute_7 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_6})
    
    join_geometry_2 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [realize_instances_3, reroute_6, reroute_7]})
    
    subdivision_surface_1 = nw.new_node(Nodes.SubdivisionSurface,
        input_kwargs={'Mesh': join_geometry_2, 'Level': group_input.outputs["Level"]})
    
    subdivide_mesh_1 = nw.new_node(Nodes.SubdivideMesh, input_kwargs={'Mesh': subdivision_surface_1})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture,
        input_kwargs={'Vector': position_2, 'Scale': 1.9000, 'Detail': 9.1000, 'Roughness': 0.2933, 'Distortion': -0.1000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Color"]})
    colorramp.color_ramp.elements[0].position = 0.0000
    colorramp.color_ramp.elements[0].color = [0.5641, 0.5641, 0.5641, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.4493
    colorramp.color_ramp.elements[1].color = [0.0000, 0.0000, 0.0000, 1.0000]
    
    set_position_5 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': subdivide_mesh_1, 'Offset': colorramp.outputs["Color"]})
    
    reroute_21 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': set_position_5})
    
    reroute_22 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_21})
    
    mesh_to_curve = nw.new_node(Nodes.MeshToCurve, input_kwargs={'Mesh': reroute_22})
    
    set_spline_type = nw.new_node(Nodes.SplineType, input_kwargs={'Curve': mesh_to_curve}, attrs={'spline_type': 'BEZIER'})
    
    set_handle_type = nw.new_node(Nodes.SetHandleType, input_kwargs={'Curve': set_spline_type}, attrs={'handle_type': 'FREE'})
    
    curve_to_mesh = nw.new_node(Nodes.CurveToMesh,
        input_kwargs={'Curve': set_handle_type, 'Profile Curve': group_input.outputs["Profile Curve"]})
    
    reroute_17 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': curve_to_mesh})
    
    reroute_12 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_17})
    
    reroute_13 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_12})
    
    reroute_20 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_19})
    
    distribute_points_on_faces_4 = nw.new_node(Nodes.DistributePointsOnFaces,
        input_kwargs={'Mesh': reroute_13, 'Density': group_input.outputs["ivy Density"], 'Seed': reroute_20},
        attrs={'use_legacy_normal': True})
    
    set_position_4 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': distribute_points_on_faces_4.outputs["Points"]})
    
    collection_info_1 = nw.new_node(Nodes.CollectionInfo,
        input_kwargs={'Collection': bpy.data.collections['ivy leafs'], 'Separate Children': True, 'Reset Children': True},
        attrs={'transform_space': 'RELATIVE'})
    
    align_euler_to_vector_1 = nw.new_node(Nodes.AlignEulerToVector,
        input_kwargs={'Rotation': distribute_points_on_faces_4.outputs["Rotation"], 'Factor': 0.7333, 'Vector': (0.0000, 0.0000, -1.0000)},
        attrs={'axis': 'Y'})
    
    reroute_24 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': group_input.outputs["leaf size"]})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: reroute_24, 1: -0.1000})
    
    random_value_2 = nw.new_node(Nodes.RandomValue,
        input_kwargs={1: (0.2000, 0.2000, 0.2000), 2: add_1, 3: reroute_24, 'Seed': reroute_20})
    
    instance_on_points_4 = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': set_position_4, 'Instance': collection_info_1, 'Pick Instance': True, 'Rotation': align_euler_to_vector_1, 'Scale': random_value_2.outputs[1]})
    
    reroute_16 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': instance_on_points_4})
    
    reroute_15 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_16})
    
    reroute_18 = nw.new_node(Nodes.Reroute, input_kwargs={'Input': reroute_15})
    
    set_material = nw.new_node(Nodes.SetMaterial,
        input_kwargs={'Geometry': curve_to_mesh, 'Material': surface.shaderfunc_to_material(shader_branches)})
    
    join_geometry_1 = nw.new_node(Nodes.JoinGeometry, input_kwargs={'Geometry': [reroute_18, set_material]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Mesh': join_geometry_1}, attrs={'is_active_output': True})

def shader_branches(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    texture_coordinate = nw.new_node(Nodes.TextureCoord)
    
    noise_texture = nw.new_node(Nodes.NoiseTexture, input_kwargs={'Vector': texture_coordinate.outputs["Object"], 'Scale': 25.0000})
    
    colorramp = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp.color_ramp.elements[0].position = 0.4420
    colorramp.color_ramp.elements[0].color = [0.0531, 0.0228, 0.0151, 1.0000]
    colorramp.color_ramp.elements[1].position = 0.8696
    colorramp.color_ramp.elements[1].color = [0.2230, 0.1293, 0.0854, 1.0000]
    
    colorramp_1 = nw.new_node(Nodes.ColorRamp, input_kwargs={'Fac': noise_texture.outputs["Fac"]})
    colorramp_1.color_ramp.elements[0].position = 0.4420
    colorramp_1.color_ramp.elements[0].color = [0.0531, 0.0531, 0.0531, 1.0000]
    colorramp_1.color_ramp.elements[1].position = 0.8696
    colorramp_1.color_ramp.elements[1].color = [0.2230, 0.2230, 0.2230, 1.0000]
    
    principled_bsdf = nw.new_node(Nodes.PrincipledBSDF,
        input_kwargs={'Base Color': colorramp.outputs["Color"], 'Roughness': colorramp_1.outputs["Alpha"]})
    
    material_output = nw.new_node(Nodes.MaterialOutput, input_kwargs={'Surface': principled_bsdf}, attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    node = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Geometry', None),
            ('NodeSocketFloat', 'branch Density', 3.0000),
            ('NodeSocketVectorTranslation', 'branch direction', (1.0000, 4.4000, 0.0000)),
            ('NodeSocketCollection', 'Collection', None),#bpy.data.collections['Collection 2.002']),
            ('NodeSocketFloat', 'gravity', -4.0000),
            ('NodeSocketFloat', 'straight branch lenght', -3.8000),
            ('NodeSocketInt', 'subsurf Level', 3),
            ('NodeSocketFloat', 'ivy Density', 300.0000),
            ('NodeSocketFloat', 'leaf size', 0.0000),
            ('NodeSocketInt', 'branch Resolution', 4),
            ('NodeSocketFloatDistance', 'branch radius', 0.0100),
            ('NodeSocketInt', 'Seed', 0)])
    
    curve_circle = nw.new_node(Nodes.CurveCircle,
        input_kwargs={'Resolution': node.outputs["branch Resolution"], 'Radius': node.outputs["branch radius"]})
    
    ivy = nw.new_node(nodegroup_ivy().name,
        input_kwargs={'branchDensity': node.outputs["branch Density"], 'branch direction': node.outputs["branch direction"], 'target': node.outputs["Collection"], 'gravity': node.outputs["gravity"], 'straight branch lenght': node.outputs["straight branch lenght"], 'Level': node.outputs["subsurf Level"], 'ivy Density': node.outputs["ivy Density"], 'leaf size': node.outputs["leaf size"], 'Profile Curve': curve_circle.outputs["Curve"], 'Seed': node.outputs["Seed"]})
    
    group_output = nw.new_node(Nodes.GroupOutput, input_kwargs={'Geometry': ivy}, attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
    surface.add_material(obj, shader_branches, selection=selection)
apply(bpy.context.active_object)
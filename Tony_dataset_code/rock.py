import bpy
import bpy
import mathutils
from numpy.random import uniform, normal, randint
from infinigen.core.nodes.node_wrangler import Nodes, NodeWrangler
from infinigen.core.nodes import node_utils
from infinigen.core.util.color import color_category
from infinigen.core import surface



@node_utils.to_nodegroup('nodegroup_voxel_remesh', singleton=False, type='GeometryNodeTree')
def nodegroup_voxel_remesh(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    group_input = nw.new_node(Nodes.GroupInput,
        expose_input=[('NodeSocketGeometry', 'Mesh', None),
            ('NodeSocketFloatDistance', 'Voxel Size', 0.3000),
            ('NodeSocketFloatDistance', 'Exterior Band Width', 0.0000),
            ('NodeSocketFloatDistance', 'Interior Band Width', 0.0000),
            ('NodeSocketBool', 'Fill Volume', True),
            ('NodeSocketVector', 'Transfer Attribute', (0.0000, 0.0000, 0.0000)),
            ('NodeSocketString', 'Face UV Map', '')])
    
    mesh_to_volume_1 = nw.new_node('GeometryNodeMeshToVolume',
        input_kwargs={'Mesh': group_input.outputs["Mesh"], 'Voxel Size': group_input.outputs["Voxel Size"], 'Exterior Band Width': group_input.outputs["Exterior Band Width"], 'Interior Band Width': group_input.outputs["Interior Band Width"], 'Fill Volume': group_input.outputs["Fill Volume"]},
        attrs={'resolution_mode': 'VOXEL_SIZE'})
    
    volume_to_mesh_1 = nw.new_node(Nodes.VolumeToMesh, input_kwargs={'Volume': mesh_to_volume_1})
    
    position_2 = nw.new_node(Nodes.InputPosition)
    
    separate_xyz_1 = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': position_2})
    
    snap = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_1.outputs["X"], 1: group_input.outputs["Voxel Size"]},
        attrs={'operation': 'SNAP'})
    
    subtract = nw.new_node(Nodes.Math, input_kwargs={0: snap, 1: separate_xyz_1.outputs["X"]}, attrs={'operation': 'SUBTRACT'})
    
    absolute = nw.new_node(Nodes.Math, input_kwargs={0: subtract}, attrs={'operation': 'ABSOLUTE'})
    
    multiply = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Voxel Size"]}, attrs={'operation': 'MULTIPLY'})
    
    greater_than = nw.new_node(Nodes.Compare, input_kwargs={0: absolute, 1: multiply})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: snap, 1: group_input.outputs["Voxel Size"]})
    
    switch = nw.new_node(Nodes.Switch, input_kwargs={0: greater_than, 2: snap, 3: add}, attrs={'input_type': 'FLOAT'})
    
    snap_1 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_1.outputs["Y"], 1: group_input.outputs["Voxel Size"]},
        attrs={'operation': 'SNAP'})
    
    subtract_1 = nw.new_node(Nodes.Math, input_kwargs={0: snap_1, 1: separate_xyz_1.outputs["Y"]}, attrs={'operation': 'SUBTRACT'})
    
    absolute_1 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_1}, attrs={'operation': 'ABSOLUTE'})
    
    multiply_1 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Voxel Size"]}, attrs={'operation': 'MULTIPLY'})
    
    greater_than_1 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute_1, 1: multiply_1})
    
    add_1 = nw.new_node(Nodes.Math, input_kwargs={0: snap_1, 1: group_input.outputs["Voxel Size"]})
    
    switch_1 = nw.new_node(Nodes.Switch, input_kwargs={0: greater_than_1, 2: snap_1, 3: add_1}, attrs={'input_type': 'FLOAT'})
    
    snap_2 = nw.new_node(Nodes.Math,
        input_kwargs={0: separate_xyz_1.outputs["Z"], 1: group_input.outputs["Voxel Size"]},
        attrs={'operation': 'SNAP'})
    
    subtract_2 = nw.new_node(Nodes.Math, input_kwargs={0: snap_2, 1: separate_xyz_1.outputs["Z"]}, attrs={'operation': 'SUBTRACT'})
    
    absolute_2 = nw.new_node(Nodes.Math, input_kwargs={0: subtract_2}, attrs={'operation': 'ABSOLUTE'})
    
    multiply_2 = nw.new_node(Nodes.Math, input_kwargs={0: group_input.outputs["Voxel Size"]}, attrs={'operation': 'MULTIPLY'})
    
    greater_than_2 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute_2, 1: multiply_2})
    
    add_2 = nw.new_node(Nodes.Math, input_kwargs={0: snap_2, 1: group_input.outputs["Voxel Size"]})
    
    switch_2 = nw.new_node(Nodes.Switch, input_kwargs={0: greater_than_2, 2: snap_2, 3: add_2}, attrs={'input_type': 'FLOAT'})
    
    combine_xyz_1 = nw.new_node(Nodes.CombineXYZ,
        input_kwargs={'X': switch.outputs["Output"], 'Y': switch_1.outputs["Output"], 'Z': switch_2.outputs["Output"]})
    
    set_position_2 = nw.new_node(Nodes.SetPosition, input_kwargs={'Geometry': volume_to_mesh_1, 'Position': combine_xyz_1})
    
    normal = nw.new_node(Nodes.InputNormal)
    
    dot_product = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normal, 1: (0.0000, 0.0000, 1.0000)},
        attrs={'operation': 'DOT_PRODUCT'})
    
    absolute_3 = nw.new_node(Nodes.Math, input_kwargs={0: dot_product.outputs["Value"]}, attrs={'operation': 'ABSOLUTE'})
    
    greater_than_3 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute_3, 1: 0.5000})
    
    dot_product_1 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normal, 1: (0.0000, 1.0000, 0.0000)},
        attrs={'operation': 'DOT_PRODUCT'})
    
    absolute_4 = nw.new_node(Nodes.Math, input_kwargs={0: dot_product_1.outputs["Value"]}, attrs={'operation': 'ABSOLUTE'})
    
    greater_than_4 = nw.new_node(Nodes.Compare, input_kwargs={0: absolute_4, 1: 0.5000})
    
    dot_product_2 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: normal, 1: (1.0000, 0.0000, 0.0000)},
        attrs={'operation': 'DOT_PRODUCT'})
    
    greater_than_5 = nw.new_node(Nodes.Compare, input_kwargs={0: dot_product_2.outputs["Value"], 1: 0.5000})
    
    position = nw.new_node(Nodes.InputPosition)
    
    evaluate_on_domain = nw.new_node(Nodes.EvaluateonDomain,
        input_kwargs={2: position},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'FACE'})
    
    subtract_3 = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: position, 1: evaluate_on_domain.outputs[2]},
        attrs={'operation': 'SUBTRACT'})
    
    divide = nw.new_node(Nodes.VectorMath,
        input_kwargs={0: subtract_3.outputs["Vector"], 1: group_input.outputs["Voxel Size"]},
        attrs={'operation': 'DIVIDE'})
    
    add_3 = nw.new_node(Nodes.VectorMath, input_kwargs={0: divide.outputs["Vector"], 1: (0.5000, 0.5000, 0.5000)})
    
    separate_xyz = nw.new_node(Nodes.SeparateXYZ, input_kwargs={'Vector': add_3.outputs["Vector"]})
    
    subtract_4 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: separate_xyz.outputs["Y"]}, attrs={'operation': 'SUBTRACT'})
    
    combine_xyz_4 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': subtract_4, 'Y': separate_xyz.outputs["Z"]})
    
    combine_xyz = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': separate_xyz.outputs["Y"], 'Y': separate_xyz.outputs["Z"]})
    
    switch_3 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than_5, 1: True, 8: combine_xyz_4, 9: combine_xyz},
        attrs={'input_type': 'VECTOR'})
    
    greater_than_6 = nw.new_node(Nodes.Compare, input_kwargs={0: dot_product_1.outputs["Value"], 1: 0.5000})
    
    subtract_5 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: separate_xyz.outputs["X"]}, attrs={'operation': 'SUBTRACT'})
    
    switch_5 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than_6, 2: separate_xyz.outputs["X"], 3: subtract_5},
        attrs={'input_type': 'FLOAT'})
    
    combine_xyz_2 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': switch_5.outputs["Output"], 'Y': separate_xyz.outputs["Z"]})
    
    switch_7 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than_4, 1: True, 8: switch_3.outputs[3], 9: combine_xyz_2},
        attrs={'input_type': 'VECTOR'})
    
    greater_than_7 = nw.new_node(Nodes.Compare, input_kwargs={0: dot_product.outputs["Value"], 1: 0.5000})
    
    subtract_6 = nw.new_node(Nodes.Math, input_kwargs={0: 1.0000, 1: separate_xyz.outputs["Y"]}, attrs={'operation': 'SUBTRACT'})
    
    switch_6 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than_7, 2: subtract_6, 3: separate_xyz.outputs["Y"]},
        attrs={'input_type': 'FLOAT'})
    
    combine_xyz_3 = nw.new_node(Nodes.CombineXYZ, input_kwargs={'X': separate_xyz.outputs["X"], 'Y': switch_6.outputs["Output"]})
    
    switch_4 = nw.new_node(Nodes.Switch,
        input_kwargs={0: greater_than_3, 1: True, 8: switch_7.outputs[3], 9: combine_xyz_3},
        attrs={'input_type': 'VECTOR'})
    
    store_named_attribute = nw.new_node(Nodes.StoreNamedAttribute,
        input_kwargs={'Geometry': set_position_2, 'Name': group_input.outputs["Face UV Map"], 3: switch_4.outputs[3]},
        attrs={'data_type': 'FLOAT2', 'domain': 'CORNER'})
    
    position_3 = nw.new_node(Nodes.InputPosition)
    
    normal_1 = nw.new_node(Nodes.InputNormal)
    
    multiply_3 = nw.new_node(Nodes.Math,
        input_kwargs={0: group_input.outputs["Voxel Size"], 1: -0.5000},
        attrs={'operation': 'MULTIPLY'})
    
    scale = nw.new_node(Nodes.VectorMath, input_kwargs={0: normal_1, 'Scale': multiply_3}, attrs={'operation': 'SCALE'})
    
    add_4 = nw.new_node(Nodes.VectorMath, input_kwargs={0: position_3, 1: scale.outputs["Vector"]})
    
    evaluate_on_domain_1 = nw.new_node(Nodes.EvaluateonDomain,
        input_kwargs={2: add_4.outputs["Vector"]},
        attrs={'data_type': 'FLOAT_VECTOR', 'domain': 'FACE'})
    
    sample_nearest_surface_1 = nw.new_node(Nodes.SampleNearestSurface,
        input_kwargs={'Mesh': group_input.outputs["Mesh"], 3: group_input.outputs["Transfer Attribute"], 'Sample Position': evaluate_on_domain_1.outputs[2]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Mesh': store_named_attribute, 'Attribute': sample_nearest_surface_1.outputs[2]},
        attrs={'is_active_output': True})

def geometry_nodes(nw: NodeWrangler):
    # Code generated using version 2.6.5 of the node_transpiler

    number_of_cut = nw.new_node(Nodes.GroupInput,
        label='Number of Cut',
        expose_input=[('NodeSocketInt', 'Number of Cuts', 4),
            ('NodeSocketFloatDistance', 'Size', 1.0000),
            ('NodeSocketInt', 'Seed', 0),
            ('NodeSocketFloat', 'Min', 1.0000)])
    
    mesh_line = nw.new_node(Nodes.MeshLine,
        input_kwargs={'Count': number_of_cut.outputs["Number of Cuts"], 'Offset': (0.0000, 0.0000, 0.0000)})
    
    ico_sphere_1 = nw.new_node(Nodes.MeshIcoSphere, input_kwargs={'Radius': number_of_cut.outputs["Size"]})
    
    add = nw.new_node(Nodes.Math, input_kwargs={0: number_of_cut.outputs["Seed"], 1: 1.0000})
    
    random_value = nw.new_node(Nodes.RandomValue,
        input_kwargs={1: (6.2830, 6.2830, 6.2830), 'Seed': add},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    random_value_1 = nw.new_node(Nodes.RandomValue,
        input_kwargs={0: number_of_cut.outputs["Min"], 1: (1.5000, 1.5000, 1.5000), 'Seed': number_of_cut.outputs["Seed"]},
        attrs={'data_type': 'FLOAT_VECTOR'})
    
    instance_on_points = nw.new_node(Nodes.InstanceOnPoints,
        input_kwargs={'Points': mesh_line, 'Instance': ico_sphere_1.outputs["Mesh"], 'Rotation': random_value.outputs["Value"], 'Scale': random_value_1.outputs["Value"]})
    
    voxel_remesh = nw.new_node(nodegroup_voxel_remesh().name,
        input_kwargs={'Mesh': instance_on_points, 'Voxel Size': 0.5000, 'Exterior Band Width': 1.0000})
    
    intersect = nw.new_node(Nodes.MeshBoolean,
        input_kwargs={'Mesh 2': voxel_remesh.outputs["Mesh"]},
        attrs={'operation': 'INTERSECT'})
    
    group_output = nw.new_node(Nodes.GroupOutput,
        input_kwargs={'Geometry': intersect.outputs["Mesh"]},
        attrs={'is_active_output': True})



def apply(obj, selection=None, **kwargs):
    surface.add_geomod(obj, geometry_nodes, selection=selection, attributes=[])
apply(bpy.context.active_object)
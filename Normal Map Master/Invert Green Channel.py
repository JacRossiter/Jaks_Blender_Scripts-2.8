import bpy

if bpy.context.object.active_material.node_tree.nodes["Invert"].inputs[0].default_value == 1:
    bpy.context.object.active_material.node_tree.nodes["Invert"].inputs[0].default_value = 0
elif bpy.context.object.active_material.node_tree.nodes["Invert"].inputs[0].default_value == 0:
    bpy.context.object.active_material.node_tree.nodes["Invert"].inputs[0].default_value = 1
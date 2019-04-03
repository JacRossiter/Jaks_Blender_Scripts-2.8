import bpy

bpy.ops.object.modifier_remove(modifier="Subdivision")
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 2
bpy.context.object.modifiers["Subdivision"].show_only_control_edges = True
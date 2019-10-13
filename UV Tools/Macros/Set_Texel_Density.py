import bpy

for ob in bpy.context.selected_objects:     # Loops through selected objects
         bpy.context.view_layer.objects.active = ob
         bpy.ops.object.texel_density_set()
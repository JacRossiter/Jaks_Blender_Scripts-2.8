import bpy

for obj in bpy.context.selected_objects:
    bpy.context.render_layer.objects.active = obj
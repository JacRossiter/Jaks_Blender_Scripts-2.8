import bpy

for obj in bpy.context.selected_objects:
    bpy.context.view_layer.objects.active = obj

    newName = (bpy.context.view_layer.objects.active.name+"_high"); bpy.context.view_layer.objects.active.name = newName
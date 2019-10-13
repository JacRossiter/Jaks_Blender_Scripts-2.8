import bpy

for ob in bpy.context.scene.objects:
    bpy.context.view_layer.objects.active = ob
    bpy.ops.gpencil.palettecolor_remove()

    
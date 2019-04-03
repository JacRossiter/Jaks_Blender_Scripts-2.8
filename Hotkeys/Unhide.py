import bpy

for ob in bpy.context.collection.objects:
    ob.hide_view_clear(select=True)
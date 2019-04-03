import bpy 

if bpy.context.mode != 'EDIT_MESH':
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
else:
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.ops.object.editmode_toggle()
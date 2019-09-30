import bpy

if bpy.context.space_data.overlay.show_edge_bevel_weight == False:
    bpy.ops.transform.edge_bevelweight(value=1)
    bpy.context.space_data.overlay.show_edge_bevel_weight = False

elif bpy.context.space_data.overlay.show_edge_bevel_weight == True:
    bpy.ops.transform.edge_bevelweight(value=1)
    bpy.context.space_data.overlay.show_edge_bevel_weight = True


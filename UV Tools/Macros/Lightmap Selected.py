import bpy



def uv_repack():
	bpy.ops.object.mode_set(mode='EDIT')
	bpy.ops.mesh.select_all(action='SELECT')
	bpy.ops.mesh.mark_seam(clear=True)
	bpy.ops.uv.seams_from_islands()
	bpy.ops.uv.unwrap(method='CONFORMAL', fill_holes=True, correct_aspect=True, margin=0.02)
	bpy.ops.object.mode_set(mode='OBJECT')

def uv_lightmap():
	bpy.ops.mesh.mark_seam(clear=True)
	bpy.ops.uv.cube_project(cube_size=0.1, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)
	bpy.ops.uv.average_islands_scale()
	bpy.ops.uv.pack_islands(rotate=False, margin=0.02)

def uv_shotpack():
	bpy.ops.object.mode_set(mode='EDIT')
	bpy.context.scene.s_packing.quality = 'GOOD'
	bpy.context.scene.s_packing.tex_width = 512
	bpy.context.scene.s_packing.tex_height = 512
	bpy.context.scene.s_packing.pixel_margin = 2
	bpy.ops.uv.shotgunpack()
	bpy.ops.uv.seams_from_islands()
	bpy.ops.object.mode_set(mode='OBJECT')


for obj in bpy.context.selected_objects: # Creates list of uv maps
	bpy.context.view_layer.objects.active = obj
	uvmaps = obj.data.uv_layers
	if len(uvmaps) > 1:
		uvmaps[0].name = "UVMap"
		uvmaps[1].name = "Lightmap" # Rename UV Channel
		uvmaps['Lightmap'].active = True
		uv_repack()
		uv_shotpack()
	
	else:
		uvmaps[0].name = "UVMap"
		uvmaps.new(name="Lightmap", do_init=True) # Create UV Channel
		uvmaps['Lightmap'].active = True
		uv_lightmap()
		uv_shotpack()


bpy.ops.object.mode_set(mode='EDIT')
		
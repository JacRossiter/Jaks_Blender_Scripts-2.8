import bpy

## Set image texture to non-color inside the image editor(Not the node editor) This is required because of a 2.8 Beta Bug
##https://developer.blender.org/T60990

for tx in bpy.data.images:
    if 'Normal' in tx.name:
        #print(tx.name, "Is a Normal Map")
        tx.colorspace_settings.name = 'Non-Color'

    elif 'normal' in tx.name:
        print(tx.name, "Is a normal Map")
        #tx.colorspace_settings.name = 'Non-Color'
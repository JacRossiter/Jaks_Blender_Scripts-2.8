import bpy

material = bpy.context.object.active_material 

## Normal Map
 
input = bpy.context.object.active_material.node_tree.nodes["Principled BSDF"].inputs['Normal']
output =  material.node_tree.nodes.new(type = 'ShaderNodeNormalMap')
output.location = (-400,0) #move it otherwise it overlaps

material.node_tree.links.new(output.outputs[0], input)

## CombineRGB

input =  bpy.context.object.active_material.node_tree.nodes["Normal Map"].inputs['Color']
output =  material.node_tree.nodes.new(type = 'ShaderNodeCombineRGB')
output.location = (-800,0) #move it otherwise it overlaps
#output.color_space = 'NONE'

material.node_tree.links.new(output.outputs[0], input)

## Invert Green Channel

input =  bpy.context.object.active_material.node_tree.nodes["Combine RGB"].inputs[1]
output =  material.node_tree.nodes.new(type = 'ShaderNodeInvert')
output.location = (-1000,100) #move it otherwise it overlaps
output.inputs[0].default_value = 0

material.node_tree.links.new(output.outputs[0], input)

## SeparateRGB      

output =  material.node_tree.nodes.new(type = 'ShaderNodeSeparateRGB')
output.location = (-1200,0) #move it otherwise it overlaps

                    #Connect R Channel
input =  bpy.context.object.active_material.node_tree.nodes["Combine RGB"].inputs[0]
material.node_tree.links.new(output.outputs[0], input)

                    #Connect B Channel
input =  bpy.context.object.active_material.node_tree.nodes["Combine RGB"].inputs[2]
material.node_tree.links.new(output.outputs[2], input)

                    #Connect G Channel
input =  bpy.context.object.active_material.node_tree.nodes["Invert"].inputs[1]
material.node_tree.links.new(output.outputs[1], input)

## Image Texture

input =  bpy.context.object.active_material.node_tree.nodes["Separate RGB"].inputs['Image']
output =  material.node_tree.nodes.new(type = 'ShaderNodeTexImage')
output.location = (-1600,0) #move it otherwise it overlaps
output.color_space = 'NONE' #Set color space to None-Color Data

material.node_tree.links.new(output.outputs[0], input)


##

#bpy.data.node_groups["Shader Nodetree"].nodes["Principled BSDF"].inputs[0].default_value = (0.214041, 0.214041, 0.214041, 1)

bpy.context.object.active_material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.214041, 0.214041, 0.214041, 1)
bpy.context.object.active_material.node_tree.nodes["Principled BSDF"].inputs[7].default_value = 0.75
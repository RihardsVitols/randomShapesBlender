# by Rihards Vitols 2022
# Creates a cube and selects a random face for extrution.

import bpy, bmesh
import random


# variables for cube
cubeSize = 2            # cube size, blender default 2
scaleX = 1              # x sacel in object creation
scaleY = 1              # y sacel in object creation
scaleZ = 1              # z sacel in object creation


# variables for the itteration
exTime = 15        # how many time will extrued the object
extrDistanceMax = 8    # max distance of extrution in m
extrDistanceMin = 2     # min distance of extrution in m
randomStep = 2          # step between values in random


# variables taht will reset in each itteration
faceCount =  6          # value that updates with each extrution, 6 for a cube


# create a cube and go in to edit mode
bpy.ops.mesh.primitive_cube_add(
    size= cubeSize, 
    enter_editmode=False, 
    align='WORLD', 
    location=(0, 0, 0), 
    scale=(scaleX, scaleY, scaleZ)
    )  


# need these 3 lines so we have seleted faces
bpy.ops.object.mode_set(mode='EDIT')     # goes in to edit mode
bpy.ops.mesh.select_mode(type="FACE")
bpy.ops.object.mode_set(mode='OBJECT')     # goes back to object mode


#sets active object for face count after each extrution
obj = bpy.context.active_object


# magic happens here
for n in range(exTime):
    
    # finds out how many faces there are
    objData = obj.data                    # get data from object
    faceCount = len(objData.polygons)     # counts how many vertex object has
    
    # deselcts all the faces 
    for i in range(faceCount):
        obj.data.polygons[i].select = False

    # extrution happens here
    obj.data.polygons[random.randrange(0, faceCount)].select = True       # selects a specific face
    bpy.ops.object.mode_set(mode='EDIT')     # goes in to edit mode
    bpy.ops.mesh.extrude_faces_move(TRANSFORM_OT_shrink_fatten={"value":random.randrange(extrDistanceMin, extrDistanceMax, randomStep)})   # extrution
    bpy.ops.object.mode_set(mode='OBJECT')     # goes back to object mode


# removes doubles from the object
bpy.ops.object.mode_set(mode='EDIT')       # goes in to edit mode
bpy.ops.mesh.select_mode(type="FACE")      # choose faces as selection 
bpy.ops.mesh.select_all(action='SELECT')   # selects all the faces
bpy.ops.mesh.remove_doubles()              # removes doubles
bpy.ops.object.mode_set(mode='OBJECT')     # goes back to object mode
import bpy
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

obj_in = argv[0]
file_name = argv[1]

bpy.context.preferences.view.show_splash = False

bpy.ops.import_scene.obj(filepath=obj_in, axis_forward='-Z', axis_up='Y', split_mode='OFF')

obj = bpy.context.selected_objects[0]#bpy.context.object
bpy.context.view_layer.objects.active = obj

bpy.context.object.data.polygons.foreach_set('use_smooth',  [True] * len(bpy.context.object.data.polygons))
bpy.context.object.data.update()

bpy.ops.object.mode_set(mode='EDIT')

blend_out = file_name.replace('.obj', '.blend')
bpy.ops.wm.save_as_mainfile(filepath=blend_out)
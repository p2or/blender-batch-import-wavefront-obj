# Batch import [Wavefront .obj files](https://en.wikipedia.org/wiki/Wavefront_.obj_file) 

A simple Blender add-on that allows to **multiple OBJ files at once** and comes with the usual settings.

<img width="761" alt="main_image-blender-2 92" src="https://user-images.githubusercontent.com/512368/180400220-e96f1e7f-201f-4b33-bbe9-6e52c9b1bd7f.png">

It's basically just a wrapper of [`import_scene.obj`](https://docs.blender.org/api/blender_python_api_2_74_5/bpy.ops.import_scene.html?highlight=import_scene.obj#bpy.ops.import_scene.obj) operator until importing multiple `.obj` files is supported officially.

## Installation

1. Download the [correct release of the add-on](../../tree/main) to match your version of Blender
1. In Blender open up *Preferences > Addons*
1. Click *Install*, select `io_batch_import_objs.py` and activate the Add-on

----

*This repository has emerged from: [How to batch import Wavefront OBJ files?](https://blender.stackexchange.com/q/5064)*

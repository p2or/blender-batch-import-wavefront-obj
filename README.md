# Batch import [Wavefront .obj files](https://en.wikipedia.org/wiki/Wavefront_.obj_file) 

A simple Blender add-on that allows to **multiple OBJ files at once** and comes with the usual settings.

<img width="754" alt="Batch Import Obj - Blender 3.4" src="https://user-images.githubusercontent.com/512368/195837831-969144c3-131e-44ef-afb7-7ccb3c370f88.png">

It's basically just a wrapper of [`wm.obj_import`](https://docs.blender.org/api/current/bpy.ops.wm.html?highlight=obj_import#bpy.ops.wm.obj_import) operator until importing multiple `.obj` files is supported officially.

## Installation

1. Download the [correct release of the add-on](../../tree/main) to match your version of Blender
1. In Blender open up *Preferences > Addons*
1. Click *Install*, select `io_batch_import_objs.py` and activate the Add-on

----

*This repository has emerged from: [How to batch import Wavefront OBJ files?](https://blender.stackexchange.com/q/5064)*

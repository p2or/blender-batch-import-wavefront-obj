# Batch import [Wavefront .obj files](https://en.wikipedia.org/wiki/Wavefront_.obj_file)

A simple Blender add-on that allows to **multiple OBJ files at once** and comes with the usual settings. 

### Background

This repository has emerged from [*How to batch import Wavefront OBJ files?*](https://blender.stackexchange.com/q/5064) to keep track of all the changes over the years and having all downloads in one place. The add-on itself is basically just a wrapper of [`wm.obj_import`](https://docs.blender.org/api/current/bpy.ops.wm.html?highlight=obj_import#bpy.ops.wm.obj_import) or [`import_scene.obj`](https://docs.blender.org/api/blender_python_api_2_74_5/bpy.ops.import_scene.html?highlight=import_scene.obj#bpy.ops.import_scene.obj) operator in versions prior to Blender `3.2.0` until importing multiple .obj files is supported officially.

## Versions

| Blender/Branch | Latest Version | Release | 
| :------ | :--- | :------ |
| [Blender 2.65+](../../tree/Blender-2.65+)      | 0.1.0 | [Download](../../releases/download/v0.1.0/io_batch_import_objs.py) |
| [Blender 2.80+](../../tree/Blender-2.80+)      | 0.2.0 | [Download](../../releases/download/v0.2.0/io_batch_import_objs.py) |
| [Blender 2.92+](../../tree/Blender-2.92+)      | 0.3.0 | [Download](../../releases/download/v0.3.0/io_batch_import_objs.py) |
| [Blender 3.2+](../../tree/Blender-3.2+)        | 0.4.0 | [Download](../../releases/download/v0.4.0/io_batch_import_objs.py) |
| [Blender 3.3 (Alpha)](../../tree/Blender-3.3+) | 0.5.0 | [Download](../../releases/download/v0.5.0/io_batch_import_objs.py) |

<!-- [All Releases](../../releases/) -->

## Installation

1. Download the correct [release version of the add-on](#Versions) to match your version of Blender
1. In Blender open up *Preferences > Addons*
1. Click *Install*, select `io_batch_import_objs.py` and activate the add-on

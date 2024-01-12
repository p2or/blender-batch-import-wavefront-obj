# Batch import [Wavefront .obj files](https://en.wikipedia.org/wiki/Wavefront_.obj_file)

A tiny add-on for Blender that allows to import **multiple OBJ files at once** and comes with the usual settings. 

| <img width="754" alt="Batch Import Obj - Blender 3.4" src="https://user-images.githubusercontent.com/512368/195837831-969144c3-131e-44ef-afb7-7ccb3c370f88.png"> | <img width="771" alt="main_image-blender-3-2" src="https://user-images.githubusercontent.com/512368/180396256-1f927624-7046-4385-ad1a-1450f9582246.png"> | 
|:--:|:--:|
| *Blender 3.4+* | *Blender 3.2+* | 
| <img width="761" alt="main_image-blender-2.92" src="https://user-images.githubusercontent.com/512368/180400220-e96f1e7f-201f-4b33-bbe9-6e52c9b1bd7f.png"> | <img width="772" alt="main_image-blender-2.79" src="https://user-images.githubusercontent.com/512368/180402784-d1007731-054f-4380-aede-a5de8945c505.png">|
| *Blender 2.80 - Blender 3.1* | *Blender 2.65 - Blender 2.79* |

### Background

This repository has emerged from [*How to batch import Wavefront OBJ files?*](https://blender.stackexchange.com/q/5064) to keep track of all the changes over the years and having all downloads in one place. The add-on itself is basically just a wrapper of [`wm.obj_import`](https://docs.blender.org/api/current/bpy.ops.wm.html?highlight=obj_import#bpy.ops.wm.obj_import) or [`import_scene.obj`](https://docs.blender.org/api/blender_python_api_2_74_5/bpy.ops.import_scene.html?highlight=import_scene.obj#bpy.ops.import_scene.obj) operator in versions prior to Blender `3.2.0` until importing multiple .obj files is supported officially.

## Versions

| Blender/Branch | Latest Version | Release | 
| :------ | :--- | :------ |
| [Blender 2.65+](../../tree/Blender-2.65+)      | 0.1.0 | [Download](../../releases/download/v0.1.0/io_batch_import_objs.py) |
| [Blender 2.80+](../../tree/Blender-2.80+)      | 0.2.0 | [Download](../../releases/download/v0.2.0/io_batch_import_objs.py) |
| [Blender 2.92+](../../tree/Blender-2.92+)      | 0.3.0 | [Download](../../releases/download/v0.3.0/io_batch_import_objs.py) |
| [Blender 3.2+](../../tree/Blender-3.2+)      | 0.4.0 | [Download](../../releases/download/v0.4.0/io_batch_import_objs.py) |
| [Blender 3.3+](../../tree/Blender-3.3+)      | 0.5.0 | [Download](../../releases/download/v0.5.0/io_batch_import_objs.py) |
| [Blender 3.4+](../../tree/Blender-3.4+)      | 0.6.1 | [Download](../../releases/download/v0.6.1/io_batch_import_objs.py) |
| [Blender 3.5+](../../tree/Blender-3.5+)      | 0.7.0 | [Download](../../releases/download/v0.7.0/io_batch_import_objs.py) |

<!-- [All Releases](../../releases/) -->

**Note:** Version `0.3.0` still works in Blender 3.2+ if the old importer by Campbell and Bastien is *enabled* in the preferences.

<!-- <img width="683" alt="old-obj-importer" src="https://user-images.githubusercontent.com/512368/180616318-3de16656-161d-437a-b3c1-a90627887181.png"> -->



## Installation

1. Download the correct [release version of the add-on](#Versions) to match your version of Blender
1. In Blender open up *Preferences > Addons*
1. Click *Install*, select `io_batch_import_objs.py` and activate the add-on

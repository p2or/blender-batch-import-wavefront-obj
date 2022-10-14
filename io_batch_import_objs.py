# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
# <pep8 compliant>


bl_info = {
    "name": "Batch Import Wavefront (.obj)",
    "author": "p2or",
    "version": (0, 6, 1),
    "blender": (3, 4, 0),
    "location": "File > Import-Export",
    "description": "Import multiple OBJ files, UV's and their materials",
    "doc_url": "https://github.com/p2or/blender-batch-import-wavefront-obj",
    "tracker_url": "https://github.com/p2or/blender-batch-import-wavefront-obj",
    "category": "Import-Export"}


import bpy
from pathlib import Path

from bpy_extras.io_utils import ImportHelper

from bpy.props import (BoolProperty,
                       FloatProperty,
                       StringProperty,
                       EnumProperty,
                       CollectionProperty)


class WM_OT_batchWavefront(bpy.types.Operator, ImportHelper):
    """Batch Import Wavefront"""
    bl_idname = "wm.obj_import_batch"
    bl_label = "Import multiple OBJ's"
    bl_options = {'PRESET', 'UNDO'}

    filename_ext = ".obj"

    filter_glob = StringProperty(
            default="*.obj",
            options={'HIDDEN'})

    files: CollectionProperty(type=bpy.types.PropertyGroup)

    global_scale_setting: FloatProperty(
            name="Scale",
            description="Value by which to enlarge or shrink" \
                    "the objects with respect to the world origin",
            min=0.0001, max=10000.0,
            soft_min=0.01, soft_max=1000.0,
            default=1.0)

    clamp_size_setting: FloatProperty(
            name="Clamp Bounding Box",
            description="Resize the objects to keep bounding box" \
                    "under this value. Value 0 diables clamping",
            min=0.0, max=1000.0,
            soft_min=0.0, soft_max=1000.0,
            default=0.0)
    
    axis_forward_setting: EnumProperty(
            name="Forward Axis",
            items=(('X', "X", ""),
                   ('Y', "Y", ""),
                   ('Z', "Z", ""),
                   ('NEGATIVE_X', "-X", ""),
                   ('NEGATIVE_Y', "-Y", ""),
                   ('NEGATIVE_Z', "-Z", ""),
                   ),
            default='NEGATIVE_Z')
            
    axis_up_setting: EnumProperty(
            name="Up Axis",
            items=(('X', "X", ""),
                   ('Y', "Y", ""),
                   ('Z', "Z", ""),
                   ('NEGATIVE_X', "-X", ""),
                   ('NEGATIVE_Y', "-Y", ""),
                   ('NEGATIVE_Z', "-Z", ""),
                   ),
            default='Y')
            
    validate_setting: BoolProperty(
            name="Validate Meshes",
            description="Check imported mesh objects for invalid data")
    
    vgroup_setting: BoolProperty(
            name="Vertex Groups",
            description="Import OBJ groups as vertex groups")
            
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.
        
        box = layout.box()
        box.label(text="Transform", icon='OBJECT_DATA')
        col = box.column()
        col.prop(self, "global_scale_setting")
        col.prop(self, "clamp_size_setting")
        col.separator()
        col.row().prop(self, "axis_forward_setting", expand=True)
        col.separator(factor=0.5)
        col.row().prop(self, "axis_up_setting", expand=True)
        col.separator()
        
        box = layout.box()
        box.label(text="Options", icon='EXPORT')
        col = box.column()
        col.prop(self, "vgroup_setting")
        col.prop(self, "validate_setting")

    def execute(self, context):
        folder = Path(self.filepath)
        for selection in self.files:
            fp = Path(folder.parent, selection.name)
            if fp.suffix == '.obj':
                bpy.ops.wm.obj_import(
                                filepath = str(fp),
                                global_scale = self.global_scale_setting,
                                clamp_size = self.clamp_size_setting,
                                forward_axis = self.axis_forward_setting,
                                up_axis = self.axis_up_setting,
                                import_vertex_groups = self.vgroup_setting,
                                validate_meshes = self.validate_setting
                                )
        return {'FINISHED'}


def menu_func_import(self, context):
    self.layout.operator(
                WM_OT_batchWavefront.bl_idname, 
                text="Wavefront Batch (.obj)")

def register():
    bpy.utils.register_class(WM_OT_batchWavefront)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(WM_OT_batchWavefront)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.wm.obj_import_batch('INVOKE_DEFAULT')

# 「3Dビュー」エリア > 「オブジェクト」モード > 「Ctrl + A」キー
# "3D View" Area > "Object" Mode > "Ctrl + A" Key

import bpy

################
# オペレーター #
################


class TransformApplyAll(bpy.types.Operator):
    bl_idname = "object.transform_apply_all"
    bl_label = "Apply Location/Rotation/Scale"
    bl_description = "Applies to object position / rotation / Pan"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        return {'FINISHED'}

################
# メニュー追加 #
################

# メニューのオン/オフの判定


def IsMenuEnable(self_id):
    for id in bpy.context.user_preferences.addons["Scramble Addon"].preferences.disabled_menu.split(','):
        if (id == self_id):
            return False
    else:
        return True

# メニューを登録する関数


def menu(self, context):
    if (IsMenuEnable(__name__.split('.')[-1])):
        self.layout.separator()
        operator = self.layout.operator(TransformApplyAll.bl_idname, text="Location & Rotation & Scale", icon="PLUGIN")
    if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
        self.layout.separator()
        self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]

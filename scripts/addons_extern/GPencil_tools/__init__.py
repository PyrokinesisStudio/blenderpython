

bl_info = {
    "name": "IMDJS_GP_tools",
    "author": "imdjs",
    "version": (0, 1,2),
    "blender": (2, 77,0),
    "location":"View3D > Tool Shelf > IMDJS_GP_tools",
    "description": "---",
    "wiki_url": "---"
                "---",
    "tracker_url": "---"
                   "",
    "category": "Add Mesh"}
    #category": All  User  Enabled  Disabled  3D View  Add  Add Curve  Add Mesh  Animation  Compositing  Development  Game Engine  Import-Export  Material  Mesh  Node  Nodes  Object  Outliner  Paint  Particle  Render  Rigging  Scene  Sculpting  Sequencer  Surface  System  Text Editor  UI  UV  User Interface  Listener
    



from .GPtools import *

path目录GP = os.path.dirname(__file__);
文件夹此GP=os.path.basename(path目录GP);

#//////////////////////////////////////////////////
class 卐GP_TOOLS卐Panel(bpy.types.Panel):
    bl_label = "IMDJS_GP_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'addons' #Animation  Tools addons        
        
    @classmethod 
    def poll(self,context):
        return  context.active_gpencil_layer;
    
    def draw(self, context):        
        layout = self.layout;
        uil行=layout.row(align=False);
        uil行.prop(data=context.scene,property='fp精简角度s',text='angle',translate=True,icon='NONE',expand=False,slider=True,toggle=False,icon_only=False,event=False,full_event=False,emboss=True,index=-1,icon_value=0);
        uil行=layout.row(align=False);
        uil行.prop(data=context.scene,property='bp是保留线段s',text='keep lines',text_ctxt='',translate=True,icon='NONE',expand=False,slider=False,toggle=True,icon_only=False,event=False,full_event=False,emboss=True,index=-1,icon_value=0);   
        uil行.prop(data=context.scene,property='bp不切割s',text='dont cut',text_ctxt='',translate=True,icon='NONE',expand=False,slider=False,toggle=True,icon_only=False,event=False,full_event=False,emboss=True,index=-1,icon_value=0);            
        layout.operator(卐GP生成线段卐Operator.bl_idname,translate=True, icon = "OUTLINER_DATA_CURVE");
        
#//////////////////////////////////////////////////
def register():
    bpy.utils.register_module(__name__);
    bpy.types.Scene.fp精简角度s=FloatProperty(name='degrees',description='Decimate angle',default=170.0,min=0.0,max=180.0,step=2,precision=1,subtype='NONE',unit='NONE',update=None,get=None,set=None);
    #ΔΔ注册按键LIB();
    bpy.types.Scene.bp是保留线段s=BoolProperty(name='keep lines',description='keep the lines which generated by GPencil',default=False,subtype='NONE',update=None,get=None,set=None);
    bpy.types.Scene.bp不切割s=BoolProperty(name='dont cut',description='dont cut the active object',default=False,subtype='NONE',update=None,get=None,set=None);
    
Ls模块名=[文件夹此GP+".GPtools",文件夹此GP];
def unregister():
    #bpy.ops.dell.sk_dll('INVOKE_DEFAULT',);
    print("sys.modules==",sys.modules.keys());
    for s in Ls模块名:
        try:
        #if(s in sys.modules):
            del sys.modules[s];
            print("DEL MODULE==",s);
        except:
            print("ERROR DEL MODULE==",s); 
    bpy.utils.unregister_module(__name__);
    

        
if (__name__ == "__main__"):
    register()

    
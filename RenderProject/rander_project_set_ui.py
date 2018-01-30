#coding:cp949
from render_ui import Rander_Form

float


try:
    from PySide2 import QtWidgets, QtCore
    from shiboken2 import wrapInstance
    from maya import OpenMayaUI as omui
    import maya.mel as mel
    import maya.cmds as cmds
    import pymel.core as pm
    from PySide2.QtCore import Qt
    # from maya import cmds as cmds
except:
    from PyQt5 import QtWidgets

import os
import string

#mayaMainWindowPtr = omui.MQtUtil.mainWindow()
#mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)
def getMayaWindow():
    try:
        mayaMainWindowPtr = omui.MQtUtil.mainWindow()
        mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)

    except:
        mayaMainWindow = None
    return mayaMainWindow

class randerForm(QtWidgets.QWidget):
    def __init__(self, parent = None ):
        QtWidgets.QWidget.__init__(self, parent=parent)

        # self.setParent(mayaMainWindow)
        self.setWindowFlags(Qt.Dialog)


        self.ui = Rander_Form()
        self.ui.setupUi(self)
        self.serverList = ["Z:", "Y:", "V:"]
        self.ver_index = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]

        self.ui.comboBox.currentIndexChanged.connect(self.SuverChange)

        self.ui.comboBox.addItems(self.serverList)

        self.ui.comboBox_5.currentIndexChanged.connect(self.PartChage)

        self.ui.comboBox_3.currentIndexChanged.connect(self.ChoiseChage)

        self.ui.comboBox_4.addItems(self.ver_index)





        self.ui.pushButton.clicked.connect(self.buttonClick)
        self.ui.pushButton_2.clicked.connect(self.buttonClick2)
        self.ui.pushButton_3.clicked.connect(self.buttonClick3)
        self.ui.pushButton_4.clicked.connect(self.buttonClick4)
        self.ui.pushButton_5.clicked.connect(self.buttonClick5)
        self.ui.unknownnode.clicked.connect(self.unknownnode)
        self.ui.pushButton_7.clicked.connect(self.buttonClick7)
        self.ui.pushButton_8.clicked.connect(self.buttonClick8)
        self.ui.pushButton_9.clicked.connect(self.buttonClick9)
        self.ui.pushButton_10.clicked.connect(self.buttonClick10)
        self.ui.pushButton_11.clicked.connect(self.buttonClick11)
        self.ui.pushButton_12.clicked.connect(self.buttonClick12)
        self.ui.pushButton_13.clicked.connect(self.buttonClick13)
        self.ui.pushButton_14.clicked.connect(self.buttonClick14)
        self.ui.pushButton_15.clicked.connect(self.buttonClick15)
        self.ui.unknownplugin.clicked.connect(self.UnknownPlugin_remove)
        self.ui.open.clicked.connect(self.open)
        self.ui.save_ma.clicked.connect(self.save_ma)
        self.ui.pushButton_16.clicked.connect(self.pushButton_16)
        self.ui.pushButton_17.clicked.connect(self.pushButton_17)
        self.ui.pushButton_18.clicked.connect(self.pushButton_18)
        self.ui.pushButton_19.clicked.connect(self.pushButton_19)
        # self.ui.rad_sky.clicked.connect(self.rad_sky)
        self.prefixPath = ("<Scene>/<Layer>")

        stA = cmds.playbackOptions(q=1, min=1)
        self.ui.lineEdit_2.setText(str(stA))

        edA = cmds.playbackOptions(q=1, max=1)
        self.ui.lineEdit_3.setText(str(edA))






    def SuverChange(self, index):

        # self.ui.comboBox_5.clear()
        # self.ui.comboBox_3.clear()



        # if self.ui.comboBox.currentText() == "Z:":
        #
        #
        #     for file in os.listdir(os.path.join(self.ui.comboBox.currentText(), "NPC", "post", "01_rendering")):
        #         # print file
        #         if os.path.isdir(os.path.join(self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", file)) == True and file.startswith('$') == False:
        #         #     print file
        #             self.ui.comboBox_3.addItem(file)


        if self.ui.comboBox.currentText() == "Z:":
            self.ui.comboBox_3.clear()

            # print 'Y'
            # print os.listdir(os.path.join(self.ui.comboBox.currentText(), "NPC", "prod"))
            # print os.path.isdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod"]))
            # print os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod"]))

            for file in os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "post", "01_rendering"])):
                # print file
                # and file.startswith('$') == False:
                if os.path.isdir('/'.join([self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", file])) == True and file.startswith('$') == False:
                   # print file
                    self.ui.comboBox_3.addItem(file)








        if self.ui.comboBox.currentText() == "Y:":

            # print 'Y'
            # print os.listdir(os.path.join(self.ui.comboBox.currentText(), "NPC", "prod"))
            # print os.path.isdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod"]))
            # print os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod"]))

            for file in os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod"])):
                # print file
                # and file.startswith('$') == False:
                if os.path.isdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod",file])) == True and file.startswith('$') == False:
                    #print file
                    self.ui.comboBox_5.addItem(file)










    def PartChage(self, index):
          self.ui.comboBox_3.clear()

          if self.ui.comboBox_5.currentText() == "04_lighting":
              #print 'yes'
              for file in os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", "04_lighting"])):
                  if os.path.isdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", "04_lighting",file])) == True and file.startswith('$') == False:
                      #     print file
                      self.ui.comboBox_3.addItem(file)

          if self.ui.comboBox_5.currentText() == "02_animation":
              #print 'yes'
              for file in os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", "02_animation"])):
                  if os.path.isdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", "02_animation",file])) == True and file.startswith('$') == False:
                      #     print file
                      self.ui.comboBox_3.addItem(file)





    def ChoiseChage(self, index):
        self.ui.comboBox_2.clear()

        if self.ui.comboBox.currentText() == "Z:":

            for file in os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "post", "01_rendering"])):
                if self.ui.comboBox_3.currentText() == file:
                    # print "yes"
                    for file in  os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", self.ui.comboBox_3.currentText()])):

                        if os.path.isdir('/'.join([self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", self.ui.comboBox_3.currentText(),file])) == True and file.startswith('$') == False:

                            self.ui.comboBox_2.addItem(file)

        if self.ui.comboBox.currentText() == "Y:":

            for file in os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", self.ui.comboBox_5.currentText()])):
                # print file
                if self.ui.comboBox_3.currentText() == file:
                    #print "no"
                    for file in os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", self.ui.comboBox_5.currentText(), self.ui.comboBox_3.currentText()])):

                        if os.path.isdir(os.path.join('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", self.ui.comboBox_5.currentText(), self.ui.comboBox_3.currentText(),file]))) == True and file.startswith('$') == False:
                            self.ui.comboBox_2.addItem(file)






    def buttonClick(self):
        # pm.mel.unifiedRenderGlobalsWindow()
        # pm.mel.unifiedRenderGlobalsWindow()
        pm.setAttr("defaultRenderGlobals.currentRenderer", "vray", type="string")
        path ='/'.join([self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", self.ui.comboBox_3.currentText(),self.ui.comboBox_2.currentText()])

        pm.mel.setProject(path)
        if pm.objExists('vraySettings'):
            pm.setAttr("vraySettings.vfbOn", 1)
            # out put file format type change.
            pm.setAttr("vraySettings.imageFormatStr", "exr (multichannel)", type="string")
            pm.setAttr("vraySettings.imgOpt_exr_compression", 4)

            # set prefix path.
            pm.setAttr("vraySettings.fileNamePrefix", self.prefixPath, type="string")
            pm.setAttr("vraySettings.globopt_render_viewport_subdivision", 1)

            # vary
            # pm.setAttr("vraySettings.samplerType", 4)
            # pm.setAttr("vraySettings.minShadeRate", 1)
            # pm.setAttr("vraySettings.renderMaskMode", 0)
            # pm.setAttr("vraySettings.aaFilterType", 1)
            # pm.setAttr("vraySettings.aaFilterSize", 2)
            # pm.setAttr("vraySettings.useFixedSampler", 0)
            # pm.setAttr("vraySettings.dmcMinSubdivs", 1)
            # pm.setAttr("vraySettings.dmcMaxSubdivs", 6)
            # pm.setAttr("vraySettings.dmcThreshold", 0.01)
            # pm.setAttr("vraySettings.dmcs_timeDependent", 1)
            # pm.setAttr("vraySettings.dmcs_useLocalSubdivs", 0)
            # pm.setAttr("vraySettings.dmcs_adaptiveAmount", 0.9)
            # pm.setAttr("vraySettings.dmcs_adaptiveThreshold", 0.01)
            # pm.setAttr("vraySettings.dmcs_adaptiveMinSamples", 8)
            # pm.setAttr("vraySettings.cmap_type", 6)
            # pm.setAttr("vraySettings.cmap_darkMult", 1)
            # pm.setAttr("vraySettings.cmap_brightMult", 1)
            # pm.setAttr("vraySettings.cmap_gamma", 2.2)
            # pm.setAttr("vraySettings.cmap_affectBackground", 1)
            # pm.setAttr("vraySettings.cmap_adaptationOnly", 1)
            # pm.setAttr("vraySettings.cmap_clampOutput", 1)
            # pm.setAttr("vraySettings.cmap_clampLevel", 1)
            # pm.setAttr("vraySettings.cmap_subpixelMapping", 0)
            # pm.setAttr("vraySettings.cmap_linearworkflow", 0)
            # pm.setAttr("vraySettings.cmap_affectSwatches", 0)
            # pm.setAttr("vraySettings.sys_regsgen_xylocked", 1)
            # pm.setAttr("vraySettings.sys_regsgen_xc", 64)
            # pm.setAttr("vraySettings.sys_regsgen_autoscale", 1)
            # pm.setAttr("vraySettings.sys_regsgen_dynamicsplit", 1)
            # pm.setAttr("vraySettings.sys_regsgen_xymeans", 0)
            # pm.setAttr("vraySettings.sys_regsgen_seqtype", 4)
            # pm.setAttr("vraySettings.sys_regsgen_reverse", 0)
            # # GI
            # pm.setAttr("vraySettings.giOn", 0)
            # # setting
            # pm.setAttr("vraySettings.ddisplac_edgeLength", 4)
            # pm.setAttr("vraySettings.ddisplac_viewDependent", 1)
            # pm.setAttr("vraySettings.ddisplac_maxSubdivs", 4)
            # pm.setAttr("vraySettings.ddisplac_tightBounds", 1)
            # pm.setAttr("vraySettings.ddisplac_amount", 1)
            # pm.setAttr("vraySettings.sys_distributed_rendering_on", 0)
            # pm.setAttr("vraySettings.ui_render_swatches", 1)
            # pm.setAttr("vraySettings.ui_use_defaultbg", 1)
            # pm.setAttr("vraySettings.abortOnMissingAsset", 0)
            # pm.setAttr("vraySettings.sys_rayc_dynMemLimit", 5000)
            # pm.setAttr("vraySettings.sys_rayc_defaultGeometryType", 2)
            # pm.setAttr("vraySettings.sys_rayc_useGlobalHairTree", 1)
            # pm.setAttr("vraySettings.sys_embreeUse", 1)
            # pm.setAttr("vraySettings.sys_embreeUseMB", 1)
            # pm.setAttr("vraySettings.sys_embreeHair", 1)
            # pm.setAttr("vraySettings.sys_embreeLowMemory", 0)
            # pm.setAttr("vraySettings.sys_embreeRayPackets", 0)
            # pm.setAttr("vraySettings.stamp_on", 0)
            # pm.setAttr("vraySettings.sys_message_level", 3)
            # pm.setAttr("vraySettings.sys_progress_increment", 10)
            # pm.setAttr("vraySettings.sys_texture_cache_size", 4000)
            # pm.setAttr("vraySettings.sys_rayc_minLeafSize", 0)
            # pm.setAttr("vraySettings.sys_rayc_faceLevelCoef", 1)
            # pm.setAttr("vraySettings.sys_max_threads", 0)
            # pm.setAttr("vraySettings.sys_low_thread_priority", 0)
            # # #Overrides
            # pm.setAttr("vraySettings.cam_type", 0)
            # pm.setAttr("vraySettings.cam_overrideFov", 0)
            # pm.setAttr("vraySettings.cam_dofOn", 0)
            # pm.setAttr("vraySettings.cam_mbOn", 0)
            # pm.setAttr("vraySettings.cam_mbPrepassSamples", 1)
            # pm.setAttr("vraySettings.cam_mbGeomSamples", 2)
            # pm.setAttr("vraySettings.globopt_geom_displacement", 1)
            # pm.setAttr("vraySettings.globopt_subdivision", 1)
            # pm.setAttr("vraySettings.globopt_render_viewport_subdivision", 1)
            # pm.setAttr("vraySettings.globopt_hairFur", 1)
            # pm.setAttr("vraySettings.globopt_vray_proxy", 1)
            # pm.setAttr("vraySettings.globopt_particles", 1)
            # pm.setAttr("vraySettings.globopt_plugin_geom", 1)
            # pm.setAttr("vraySettings.globopt_geom_doHidden", 1)
            # pm.setAttr("vraySettings.globopt_light_doLights", 1)
            # pm.setAttr("vraySettings.globopt_light_doHiddenLights", 1)
            # pm.setAttr("vraySettings.globopt_light_doDefaultLights", 1)
            # pm.setAttr("vraySettings.globopt_light_doShadows", 1)
            # pm.setAttr("vraySettings.globopt_light_ignoreLightLinking", 0)
            # pm.setAttr("vraySettings.globopt_light_disableSelfIllumination", 0)
            # pm.setAttr("vraySettings.photometricScale", 20)
            # pm.setAttr("vraySettings.globopt_probabilistic_lights_on", 2)
            # pm.setAttr("vraySettings.globopt_num_probabilistic_lights", 8)
            # pm.setAttr("vraySettings.renderMaskMode", 0)
            # pm.setAttr("vraySettings.primaryMultiplier", 0.95)
            # pm.setAttr("vraySettings.secondaryEngine", 3)
            # pm.setAttr("vraySettings.secondaryMultiplier", 0.7)
            # pm.setAttr("vraySettings.sys_rayc_maxLevels", 80)
            #
            # if pm.objExists('vraySettings'):
            #     pm.setAttr("vraySettings.width", 960)
            #     pm.setAttr("vraySettings.height", 540)
            #     pm.setAttr("vraySettings.aspectRatio", 1.778)
            #     pm.setAttr("vraySettings.pixelAspect", 1.000)
            #     pm.setAttr("vraySettings.imap_currentPreset", 4)
            #
            # if pm.objExists('AO'):
            #     pm.setAttr("AO.subdivs", 16)

    def buttonClick2(self):
        pm.setAttr("defaultRenderGlobals.currentRenderer", "vray", type="string")
        if pm.mel.unifiedRenderGlobalsWindow() == False:
            pm.mel.unifiedRenderGlobalsWindow()

        mel.eval('loadNodePresets "test_pucca";')
        pm.setAttr("vraySettings.animBatchOnly", 1)

        pm.setAttr("vraySettings.animType", 1)

        pm.setAttr("defaultRenderGlobals.startFrame", self.start_fram)
        pm.setAttr("defaultRenderGlobals.endFrame", self.end_fram)

        # if pm.objExists('vraySettings'):
        #     pm.setAttr("vraySettings.vfbOn", 1)
        #     pm.setAttr("vraySettings.imageFormatStr", "exr (multichannel)", type="string")
        #     pm.setAttr("vraySettings.imgOpt_exr_compression", 4)
        #     # set prefix path.
        #     pm.setAttr("vraySettings.globopt_render_viewport_subdivision", 1)
        #     #vary
        #     pm.setAttr("vraySettings.samplerType", 4)
        #     pm.setAttr("vraySettings.minShadeRate", 1)
        #     pm.setAttr("vraySettings.renderMaskMode", 0)
        #     pm.setAttr("vraySettings.aaFilterType", 1)
        #     pm.setAttr("vraySettings.aaFilterSize", 2)
        #     pm.setAttr("vraySettings.useFixedSampler", 0)
        #     pm.setAttr("vraySettings.dmcMinSubdivs", 1)
        #     pm.setAttr("vraySettings.dmcMaxSubdivs", 6)
        #     pm.setAttr("vraySettings.dmcThreshold", 0.01)
        #     pm.setAttr("vraySettings.dmcs_timeDependent", 1)
        #     pm.setAttr("vraySettings.dmcs_useLocalSubdivs", 0)
        #     pm.setAttr("vraySettings.dmcs_adaptiveAmount", 0.9)
        #     pm.setAttr("vraySettings.dmcs_adaptiveThreshold", 0.01)
        #     pm.setAttr("vraySettings.dmcs_adaptiveMinSamples", 8)
        #     pm.setAttr("vraySettings.cmap_type", 6)
        #     pm.setAttr("vraySettings.cmap_darkMult", 1)
        #     pm.setAttr("vraySettings.cmap_brightMult", 1)
        #     pm.setAttr("vraySettings.cmap_gamma", 2.2)
        #     pm.setAttr("vraySettings.cmap_affectBackground", 1)
        #     pm.setAttr("vraySettings.cmap_adaptationOnly", 1)
        #     pm.setAttr("vraySettings.cmap_clampOutput", 1)
        #     pm.setAttr("vraySettings.cmap_clampLevel", 1)
        #     pm.setAttr("vraySettings.cmap_subpixelMapping", 0)
        #     pm.setAttr("vraySettings.cmap_linearworkflow", 0)
        #     pm.setAttr("vraySettings.cmap_affectSwatches", 0)
        #     pm.setAttr("vraySettings.sys_regsgen_xylocked", 1)
        #     pm.setAttr("vraySettings.sys_regsgen_xc", 64)
        #     pm.setAttr("vraySettings.sys_regsgen_autoscale", 1)
        #     pm.setAttr("vraySettings.sys_regsgen_dynamicsplit", 1)
        #     pm.setAttr("vraySettings.sys_regsgen_xymeans", 0)
        #     pm.setAttr("vraySettings.sys_regsgen_seqtype", 4)
        #     pm.setAttr("vraySettings.sys_regsgen_reverse", 0)
        #     #GI
        #     pm.setAttr("vraySettings.giOn", 0)
        #     #setting
        #     pm.setAttr("vraySettings.ddisplac_edgeLength", 4)
        #     pm.setAttr("vraySettings.ddisplac_viewDependent", 1)
        #     pm.setAttr("vraySettings.ddisplac_maxSubdivs", 4)
        #     pm.setAttr("vraySettings.ddisplac_tightBounds", 1)
        #     pm.setAttr("vraySettings.ddisplac_amount", 1)
        #     pm.setAttr("vraySettings.sys_distributed_rendering_on", 0)
        #     pm.setAttr("vraySettings.ui_render_swatches", 1)
        #     pm.setAttr("vraySettings.ui_use_defaultbg", 1)
        #     pm.setAttr("vraySettings.abortOnMissingAsset", 0)
        #     pm.setAttr("vraySettings.sys_rayc_dynMemLimit", 5000)
        #     pm.setAttr("vraySettings.sys_rayc_defaultGeometryType", 2)
        #     pm.setAttr("vraySettings.sys_rayc_useGlobalHairTree", 1)
        #     pm.setAttr("vraySettings.sys_embreeUse", 1)
        #     pm.setAttr("vraySettings.sys_embreeUseMB", 1)
        #     pm.setAttr("vraySettings.sys_embreeHair", 1)
        #     pm.setAttr("vraySettings.sys_embreeLowMemory", 0)
        #     pm.setAttr("vraySettings.sys_embreeRayPackets", 0)
        #     pm.setAttr("vraySettings.stamp_on", 0)
        #     pm.setAttr("vraySettings.sys_message_level", 3)
        #     pm.setAttr("vraySettings.sys_progress_increment", 10)
        #     pm.setAttr("vraySettings.sys_texture_cache_size", 4000)
        #     pm.setAttr("vraySettings.sys_rayc_maxLevels", 80)
        #     pm.setAttr("vraySettings.sys_rayc_minLeafSize", 0)
        #     pm.setAttr("vraySettings.sys_rayc_faceLevelCoef", 1)
        #     pm.setAttr("vraySettings.sys_max_threads", 0)
        #     pm.setAttr("vraySettings.sys_low_thread_priority", 0)
        #     # #Overrides
        #     pm.setAttr("vraySettings.cam_type", 0)
        #     pm.setAttr("vraySettings.cam_overrideFov", 0)
        #     pm.setAttr("vraySettings.cam_dofOn", 0)
        #     pm.setAttr("vraySettings.cam_mbOn", 0)
        #     pm.setAttr("vraySettings.cam_mbPrepassSamples", 1)
        #     pm.setAttr("vraySettings.cam_mbGeomSamples", 2)
        #     pm.setAttr("vraySettings.globopt_geom_displacement", 1)
        #     pm.setAttr("vraySettings.globopt_subdivision", 1)
        #     pm.setAttr("vraySettings.globopt_render_viewport_subdivision", 1)
        #     pm.setAttr("vraySettings.globopt_hairFur", 1)
        #     pm.setAttr("vraySettings.globopt_vray_proxy", 1)
        #     pm.setAttr("vraySettings.globopt_particles", 1)
        #     pm.setAttr("vraySettings.globopt_plugin_geom", 1)
        #     pm.setAttr("vraySettings.globopt_geom_doHidden", 1)
        #     pm.setAttr("vraySettings.globopt_light_doLights", 1)
        #     pm.setAttr("vraySettings.globopt_light_doHiddenLights", 1)
        #     pm.setAttr("vraySettings.globopt_light_doDefaultLights", 1)
        #     pm.setAttr("vraySettings.globopt_light_doShadows", 1)
        #     pm.setAttr("vraySettings.globopt_light_ignoreLightLinking", 0)
        #     pm.setAttr("vraySettings.globopt_light_disableSelfIllumination", 0)
        #     pm.setAttr("vraySettings.photometricScale", 20)
        #     pm.setAttr("vraySettings.globopt_probabilistic_lights_on", 2)
        #     pm.setAttr("vraySettings.globopt_num_probabilistic_lights", 8)
        #     pm.setAttr("vraySettings.renderMaskMode", 0)
        #     pm.setAttr("vraySettings.primaryMultiplier", 0.95)
        #     pm.setAttr("vraySettings.secondaryEngine", 3)
        #     pm.setAttr("vraySettings.secondaryMultiplier", 0.7)
        #     pm.setAttr("vraySettings.sys_rayc_maxLevels", 80)
        #
        #     if pm.objExists('vraySettings'):
        #         pm.setAttr("vraySettings.width", 960)
        #         pm.setAttr("vraySettings.height", 540)
        #         pm.setAttr("vraySettings.aspectRatio", 1.778)
        #         pm.setAttr("vraySettings.pixelAspect", 1.000)
        #         pm.setAttr("vraySettings.imap_currentPreset", 4)
        #
        #     if pm.objExists('AO'):
        #         pm.setAttr("AO.subdivs", 16)


    def buttonClick3(self):
        pm.setAttr("defaultRenderGlobals.currentRenderer", "vray", type="string")
        if pm.mel.unifiedRenderGlobalsWindow() == False:
            pm.mel.unifiedRenderGlobalsWindow()



        #colorManegment on
        if pm.colorManagementPrefs(q=True,cmEnabled=True) == False:
            pm.colorManagementPrefs(e=1, cmEnabled=1)
        mel.eval('loadNodePresets "final_pucca";')
        pm.setAttr("vraySettings.animType", 1)
        pm.setAttr("defaultRenderGlobals.startFrame", self.start_fram)
        pm.setAttr("defaultRenderGlobals.endFrame", self.end_fram)
        pm.editRenderLayerAdjustment("vraySettings.sys_embreeUse")
        pm.setAttr("vraySettings.sys_embreeUse", 0)
        pm.editRenderLayerGlobals(currentRenderLayer='CH_color')
        pm.editRenderLayerAdjustment("vraySettings.giOn")
        pm.setAttr("vraySettings.giOn", 1)

        # if pm.objExists('vraySettings'):
        #     pm.setAttr("vraySettings.vfbOn", 1)
        #     pm.setAttr("vraySettings.imageFormatStr", "exr (multichannel)", type="string")
        #     pm.setAttr("vraySettings.imgOpt_exr_compression", 4)
        #     # set prefix path.
        #     pm.setAttr("vraySettings.globopt_render_viewport_subdivision", 1)
        #     #vary
        #     pm.setAttr("vraySettings.samplerType", 4)
        #     pm.setAttr("vraySettings.minShadeRate", 2)
        #     pm.setAttr("vraySettings.renderMaskMode", 0)
        #     pm.setAttr("vraySettings.aaFilterType", 1)
        #     pm.setAttr("vraySettings.aaFilterSize", 2)
        #     pm.setAttr("vraySettings.useFixedSampler", 0)
        #     pm.setAttr("vraySettings.dmcMinSubdivs", 1)
        #     pm.setAttr("vraySettings.dmcMaxSubdivs", 25)
        #     pm.setAttr("vraySettings.dmcThreshold", 0.005)
        #     pm.setAttr("vraySettings.dmcs_timeDependent", 1)
        #     pm.setAttr("vraySettings.dmcs_useLocalSubdivs", 0)
        #     pm.setAttr("vraySettings.dmcs_adaptiveAmount", 0.9)
        #     pm.setAttr("vraySettings.dmcs_adaptiveThreshold", 0.005)
        #     pm.setAttr("vraySettings.dmcs_adaptiveMinSamples", 32)
        #     pm.setAttr("vraySettings.cmap_type", 6)
        #     pm.setAttr("vraySettings.cmap_darkMult", 1)
        #     pm.setAttr("vraySettings.cmap_brightMult", 1)
        #     pm.setAttr("vraySettings.cmap_gamma", 2.2)
        #     pm.setAttr("vraySettings.cmap_affectBackground", 1)
        #     pm.setAttr("vraySettings.cmap_adaptationOnly", 1)
        #     pm.setAttr("vraySettings.cmap_clampOutput", 1)
        #     pm.setAttr("vraySettings.cmap_clampLevel", 1)
        #     pm.setAttr("vraySettings.cmap_subpixelMapping", 0)
        #     pm.setAttr("vraySettings.cmap_linearworkflow", 0)
        #     pm.setAttr("vraySettings.cmap_affectSwatches", 0)
        #     pm.setAttr("vraySettings.sys_regsgen_xylocked", 1)
        #     pm.setAttr("vraySettings.sys_regsgen_xc", 64)
        #     pm.setAttr("vraySettings.sys_regsgen_autoscale", 1)
        #     pm.setAttr("vraySettings.sys_regsgen_dynamicsplit", 1)
        #     pm.setAttr("vraySettings.sys_regsgen_xymeans", 0)
        #     pm.setAttr("vraySettings.sys_regsgen_seqtype", 4)
        #     pm.setAttr("vraySettings.sys_regsgen_reverse", 0)
        #     #GI
        #     pm.setAttr("vraySettings.giOn", 0)
        #
        #     #setting
        #     pm.setAttr("vraySettings.ddisplac_edgeLength", 4)
        #     pm.setAttr("vraySettings.ddisplac_viewDependent", 1)
        #     pm.setAttr("vraySettings.ddisplac_maxSubdivs", 4)
        #     pm.setAttr("vraySettings.ddisplac_tightBounds", 1)
        #     pm.setAttr("vraySettings.ddisplac_amount", 1)
        #     pm.setAttr("vraySettings.sys_distributed_rendering_on", 0)
        #     pm.setAttr("vraySettings.ui_render_swatches", 1)
        #     pm.setAttr("vraySettings.ui_use_defaultbg", 1)
        #     pm.setAttr("vraySettings.abortOnMissingAsset", 0)
        #     pm.setAttr("vraySettings.sys_rayc_dynMemLimit", 5000)
        #     pm.setAttr("vraySettings.sys_rayc_defaultGeometryType", 2)
        #     pm.setAttr("vraySettings.sys_rayc_useGlobalHairTree", 1)
        #     pm.setAttr("vraySettings.sys_embreeUse", 1)
        #     pm.setAttr("vraySettings.sys_embreeUseMB", 1)
        #     pm.setAttr("vraySettings.sys_embreeHair", 1)
        #     pm.setAttr("vraySettings.sys_embreeLowMemory", 0)
        #     pm.setAttr("vraySettings.sys_embreeRayPackets", 0)
        #     pm.setAttr("vraySettings.stamp_on", 0)
        #     pm.setAttr("vraySettings.sys_message_level", 3)
        #     pm.setAttr("vraySettings.sys_progress_increment", 10)
        #     pm.setAttr("vraySettings.sys_texture_cache_size", 4000)
        #     pm.setAttr("vraySettings.sys_rayc_maxLevels", 80)
        #     pm.setAttr("vraySettings.sys_rayc_minLeafSize", 0)
        #     pm.setAttr("vraySettings.sys_rayc_faceLevelCoef", 1)
        #     pm.setAttr("vraySettings.sys_max_threads", 0)
        #     pm.setAttr("vraySettings.sys_low_thread_priority", 0)
        #     # #Overrides
        #     pm.setAttr("vraySettings.cam_type", 0)
        #     pm.setAttr("vraySettings.cam_overrideFov", 0)
        #     pm.setAttr("vraySettings.cam_dofOn", 0)
        #     pm.setAttr("vraySettings.cam_mbOn", 0)
        #     pm.setAttr("vraySettings.cam_mbPrepassSamples", 1)
        #     pm.setAttr("vraySettings.cam_mbGeomSamples", 2)
        #     pm.setAttr("vraySettings.globopt_geom_displacement", 1)
        #     pm.setAttr("vraySettings.globopt_subdivision", 1)
        #     pm.setAttr("vraySettings.globopt_render_viewport_subdivision", 1)
        #     pm.setAttr("vraySettings.globopt_hairFur", 1)
        #     pm.setAttr("vraySettings.globopt_vray_proxy", 1)
        #     pm.setAttr("vraySettings.globopt_particles", 1)
        #     pm.setAttr("vraySettings.globopt_plugin_geom", 1)
        #     pm.setAttr("vraySettings.globopt_geom_doHidden", 1)
        #     pm.setAttr("vraySettings.globopt_light_doLights", 1)
        #     pm.setAttr("vraySettings.globopt_light_doHiddenLights", 1)
        #     pm.setAttr("vraySettings.globopt_light_doDefaultLights", 1)
        #     pm.setAttr("vraySettings.globopt_light_doShadows", 1)
        #     pm.setAttr("vraySettings.globopt_light_ignoreLightLinking", 0)
        #     pm.setAttr("vraySettings.globopt_light_disableSelfIllumination", 0)
        #     pm.setAttr("vraySettings.photometricScale", 20)
        #     pm.setAttr("vraySettings.globopt_probabilistic_lights_on", 2)
        #     pm.setAttr("vraySettings.globopt_num_probabilistic_lights", 8)
        #     pm.setAttr("vraySettings.renderMaskMode", 0)
        #     pm.setAttr("vraySettings.primaryMultiplier", 0.95)
        #     pm.setAttr("vraySettings.secondaryEngine", 3)
        #     pm.setAttr("vraySettings.secondaryMultiplier", 0.7)
        #     pm.setAttr("vraySettings.sys_rayc_maxLevels", 80)
        #
        #     if pm.objExists('vraySettings'):
        #         pm.setAttr("vraySettings.width", 1920)
        #         pm.setAttr("vraySettings.height", 1080)
        #         pm.setAttr("vraySettings.aspectRatio", 1.778)
        #         pm.setAttr("vraySettings.pixelAspect", 1.000)
        #         pm.setAttr("vraySettings.imap_currentPreset", 4)
        #
        #     if pm.objExists('AO'):
        #         pm.setAttr("AO.subdivs", 32)

    def buttonClick4(self):



        dividenum = self.ui.lineEdit.text()

        dvlevel = int(dividenum)
        SelectedOBJ = pm.ls(sl=1)
        for i in range(0, len(SelectedOBJ)):
            pm.polySmooth(SelectedOBJ[i],
                          kb=0, c=1,
                          ch=1, kmb=1, sl=1,
                          bnr=1, kt=1,
                          dpe=1, suv=1,
                          mth=0,
                          peh=0,
                          ksb=1, dv=dvlevel,
                          ro=1,
                          khe=0,
                          ps=0.1)
            print "!!!!!!!!!!! Smooth complete !!!!!!!!!!!굈"

    def buttonClick5(self):

        pm.lockNode('TurtleDefaultBakeLayer', lock=False)
        pm.delete('TurtleDefaultBakeLayer')

        # if pm.objExists('vraySettings'):
        #
        #     cacheDir = 'Y:/NPC/prod/03_lightingSet/ep01/day_light_set_03.ma'
        #
        #     mel.eval('file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "%s";' % cacheDir)

    def unknownnode(self):
        unknownNodes = pm.ls(type="unknown")
        for nd in unknownNodes:
            print "Unlocking ", nd
            pm.lockNode(nd, lock=False)
            print "Deleting ", nd
            pm.delete(nd)

    def buttonClick12(self):
        print "ffame set"
        pm.setAttr("defaultRenderGlobals.currentRenderer", "vray", type="string")
        pm.setAttr("vraySettings.animType", 1)
        startenum = self.ui.lineEdit_2.text()

        endenum = self.ui.lineEdit_3.text()

        self.st = int(startenum)

        self.en = int(endenum)

        pm.playbackOptions(e=1, ast=self.st)
        self.start_fram = int(pm.playbackOptions(min=self.st))
        pm.playbackOptions(e=1, aet=self.en)
        self.end_fram = int(pm.playbackOptions(max=self.en))

        pm.setAttr("defaultRenderGlobals.startFrame", self.start_fram)
        pm.setAttr("defaultRenderGlobals.endFrame", self.end_fram)

    def buttonClick7(self):
        pm.setAttr("defaultRenderGlobals.currentRenderer", "vray", type="string")
        if pm.objExists('vraySettings'):

            cacheDirB = "Y:/NPC/prod/03_lightingSet/ep00/light_set/timelight_set/Layer_set.ma"

            mel.eval('file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "%s";' % cacheDirB)

        self.start_fram = int(pm.playbackOptions(min=self.st))
        self.end_fram = int(pm.playbackOptions(max=self.en))

        pm.setAttr("defaultRenderGlobals.startFrame", self.start_fram)
        pm.setAttr("defaultRenderGlobals.endFrame", self.end_fram)









    def buttonClick8(self):
        print 'dddd'

        pm.mel.unifiedRenderGlobalsWindow()
        mel.eval('SubmitJobToDeadline')

    def buttonClick9(self):

        import maya.cmds as cmds

        stA = cmds.playbackOptions(q=1, min=1)
        start = int(stA)
        print start

        edA = cmds.playbackOptions(q=1, max=1)
        end = int(edA)
        print end
        sel=cmds.ls(sl=1)[0].replace('|','A')
        print sel
        root = ""
        for name in cmds.ls(sl=1):
            root += " -root |" + str(name)
            print root
        print 'dddd'
        self.camerafile= os.path.join(self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", self.ui.comboBox_3.currentText(), self.ui.comboBox_2.currentText(),"camera")
        # if os.path.join(self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", self.ui.comboBox_3.currentText(),self.ui.comboBox_2.currentText(),"camera") == False:
        # os.makedirs(os.path.join(self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", self.ui.comboBox_3.currentText(), self.ui.comboBox_2.currentText(),"camera"))
        if os.path.isdir(os.path.join(self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", self.ui.comboBox_3.currentText(), self.ui.comboBox_2.currentText(),"camera")) == False:
            os.makedirs(self.camerafile)

        elif os.path.isdir(os.path.join(self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", self.ui.comboBox_3.currentText(), self.ui.comboBox_2.currentText(),"camera")) == True:
            print 'exist'


        save_name = '/'.join([self.ui.comboBox.currentText(), "NPC", "post", "01_rendering", self.ui.comboBox_3.currentText(), self.ui.comboBox_2.currentText(),"camera", "%s.abc" % str(sel)])
        print save_name



        # print save_name
        cmds.AbcExport(j="-frameRange %d %d -writeVisibility -writeUVSets -dataFormat ogawa  %s -file %s" % (start, end, root, save_name))


    def buttonClick10(self):

        if len(pm.ls(sl=1)) > 0:
            text = "CH"
            vray_Asop = pm.vray('objectProperties', 'add_single')

            CH_name=pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)

            pm.setAttr("%s.objectIDEnabled" % CH_name, 1)
            pm.setAttr("%s.objectID" % CH_name, 101)
        # targetsel = pm.ls(['CH','PR','BG'],typ='transform')
        #
        # for i in range(len(targetsel)):
        #
        #     if "CH" in targetsel:
        #         if targetsel[i] == "CH":
        #             print "CH"
        #             pm.select(targetsel[i])
        #             text = "CH"
        #             vray_Asop = pm.vray('objectProperties', 'add_single')
        #
        #             pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)
        #
        #             cmds.editRenderLayerGlobals(currentRenderLayer='shadow')
        #
        #             if cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ) == 'shadow':
        #
        #                 pm.editRenderLayerAdjustment("CH_vrayobjectproperties.primaryVisibility")
        #
        #                 pm.setAttr("CH_vrayobjectproperties.primaryVisibility", 0)
        #
        #
        #
        #         if targetsel[i] == "PR":
        #             print "PR"
        #             pm.select(targetsel[i])
        #             text = "PR"
        #             vray_Asop = pm.vray('objectProperties', 'add_single')
        #
        #             pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)
        #
        #             cmds.editRenderLayerGlobals(currentRenderLayer='shadow')
        #
        #             if cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'shadow':
        #                 pm.editRenderLayerAdjustment("PR_vrayobjectproperties.primaryVisibility")
        #
        #                 pm.setAttr("PR_vrayobjectproperties.primaryVisibility", 0)
        #
        #             cmds.editRenderLayerGlobals(currentRenderLayer='CH_rim')
        #
        #             if cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'CH_rim':
        #                 pm.editRenderLayerAdjustment("PR_vrayobjectproperties.matteSurface")
        #
        #                 pm.setAttr("PR_vrayobjectproperties.matteSurface", 1)
        #                 pm.editRenderLayerAdjustment("PR_vrayobjectproperties.alphaContribution")
        #
        #                 pm.setAttr("PR_vrayobjectproperties.alphaContribution", -1)
        #                 pm.editRenderLayerAdjustment("PR_vrayobjectproperties.reflectionAmount")
        #
        #                 pm.setAttr("PR_vrayobjectproperties.reflectionAmount", 0)
        #                 pm.editRenderLayerAdjustment("PR_vrayobjectproperties.refractionAmount")
        #
        #                 pm.setAttr("PR_vrayobjectproperties.refractionAmount", 0)
        #
        #         if targetsel[i] == "BG":
        #             print "BG"
        #             pm.select(targetsel[i])
        #             text = "BG"
        #             vray_Asop = pm.vray('objectProperties', 'add_single')
        #
        #             pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)
        #
        #             cmds.editRenderLayerGlobals(currentRenderLayer='shadow')
        #
        #             if cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'shadow':
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.matteSurface")
        #
        #                 pm.setAttr("BG_vrayobjectproperties.matteSurface", 1)
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.alphaContribution")
        #
        #                 pm.setAttr("BG_vrayobjectproperties.alphaContribution", -1)
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.shadows")
        #
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.affectAlpha")
        #
        #                 pm.setAttr("BG_vrayobjectproperties.shadows", 1)
        #                 pm.setAttr("BG_vrayobjectproperties.affectAlpha", 1)
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.reflectionAmount")
        #
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.refractionAmount")
        #
        #                 pm.setAttr("BG_vrayobjectproperties.reflectionAmount", 0)
        #                 pm.setAttr("BG_vrayobjectproperties.refractionAmount", 0)
        #
        #             cmds.editRenderLayerGlobals(currentRenderLayer='CH_color')
        #
        #             if cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'CH_color':
        #
        #
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.matteSurface")
        #
        #                 pm.setAttr("BG_vrayobjectproperties.matteSurface", 1)
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.alphaContribution")
        #
        #                 pm.setAttr("BG_vrayobjectproperties.alphaContribution", -1)
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.reflectionAmount")
        #
        #                 pm.editRenderLayerAdjustment("BG_vrayobjectproperties.refractionAmount")
        #
        #                 pm.setAttr("BG_vrayobjectproperties.reflectionAmount", 0)
        #                 pm.setAttr("BG_vrayobjectproperties.refractionAmount", 0)












                        # for i in range(len(targetsel)):
        #
        #     if "CH" in targetsel:
        #         if targetsel[i] == "CH":
        #             print "CH"
        #
        #             text = "CH"
        #             vray_Asop = pm.vray('objectProperties', 'add_single')
        #
        #             CH_name=pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)
        #
        #             cmds.editRenderLayerGlobals(currentRenderLayer='shadow')
        #
        #             if cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ) == 'shadow':
        #
        #                 pm.editRenderLayerAdjustment("CH_vrayobjectproperties.primaryVisibility")
        #
        #                 pm.setAttr("CH_vrayobjectproperties.primaryVisibility", 0)
        #
        #     if "CH" in targetsel:
        #         if targetsel[i] == "PR":
        #             print "PR"
        #
        #             text = "PR"
        #             vray_Asop = pm.vray('objectProperties', 'add_single')
        #
        #             CH_name = pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)
        #
        #             cmds.editRenderLayerGlobals(currentRenderLayer='shadow')
        #
        #             if cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'shadow':
        #                 pm.editRenderLayerAdjustment("PR_vrayobjectproperties.primaryVisibility")
        #
        #                 pm.setAttr("PR_vrayobjectproperties.primaryVisibility", 0)
        #
        #     if "PR" in targetsel:
        #         if targetsel[i] == "PR":
        #             print "PR"
        #
        #             text = "PR"
        #             vray_Asop = pm.vray('objectProperties', 'add_single')
        #
        #             CH_name = pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)
        #
        #             cmds.editRenderLayerGlobals(currentRenderLayer='shadow')
        #
        #             if cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'shadow':
        #                 pm.editRenderLayerAdjustment("CH_vrayobjectproperties.primaryVisibility")
        #
        #                 pm.setAttr("CH_vrayobjectproperties.primaryVisibility", 0)




    def buttonClick11(self):

        if len(pm.ls(sl=1)) > 0:
            text = "PR"
            vray_Asop = pm.vray('objectProperties', 'add_single')

            PR_name=pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)

            pm.setAttr("%s.objectIDEnabled" % PR_name, 1)
            pm.setAttr("%s.objectID" % PR_name, 102)





    # def buttonClick12(self):
    #     print "ffame set"
    #     pm.setAttr("defaultRenderGlobals.currentRenderer", "vray", type="string")
    #     pm.setAttr("vraySettings.animType", 1)
    #     startenum = self.ui.lineEdit_2.text()
    #
    #     endenum = self.ui.lineEdit_3.text()
    #
    #     st = int(startenum)
    #
    #     en = int(endenum)
    #
    #
    #     pm.playbackOptions(e=1, ast=st)
    #     self.start_fram=int(pm.playbackOptions(min=st))
    #     pm.playbackOptions(e=1, aet=en)
    #     self.end_fram=int(pm.playbackOptions(max=en))
    #
    #     pm.setAttr("defaultRenderGlobals.startFrame", self.start_fram)
    #     pm.setAttr("defaultRenderGlobals.endFrame", self.end_fram)


        # pm.playbackOptions(q=1, min=1)
        # pm.playbackOptions(q=1, max=1)
        # for i in sel:
        #     start = pm.playbackOptions(q=1, min=1)
        #     end = pm.playbackOptions(q=1, max=1)
        #     startFrame = start
        #     endFrame = end
        #     pm.currentTime(startFrame)
        #     pm.currentTime(endFrame)
        #     pm.setAttr("vraySettings.animType", 1)







    def buttonClick13(self):
        print "in"

        if pm.objExists("BG") and pm.objExists("CH") and pm.objExists("PR") == True:

           pm.select(['BG', 'CH', 'PR'])


        elif pm.objExists("BG") and pm.objExists("CH") == True:

            pm.select(['BG', 'CH'])

        elif pm.objExists("CH") and pm.objExists("PR") == True:

            pm.select(['CH', 'PR'])

        elif pm.objExists("BG") and pm.objExists("PR") == True:

            pm.select(['BG', 'PR'])


        elif pm.objExists("CH") == True:

            pm.select('CH')

        elif pm.objExists("BG") == True:

            pm.select('BG')

        elif pm.objExists("PR") == True:

            pm.select('PR')

        i = ""
        sel = pm.ls(sl=1)
        for i in sel:

            if i == 'BG':
                pm.editRenderLayerMembers('BG_color', ['BG'], noRecurse=1)

            elif i == 'BG' == False:
                print '아웃라이너에 BG가 없다'

        for i in sel:
            if i == 'CH':
                pm.editRenderLayerMembers('CH_color', ['CH'], noRecurse=1)

            elif i == ['CH'] == False:
                print '아웃라이너에 CH가 없다'

        for i in sel:
            if i == 'BG':
                pm.editRenderLayerMembers('CH_color', ['BG'], noRecurse=1)

            elif i == ['BG'] == False:
                print '아웃라이너에 BG가 없다'

        for i in sel:
            if i == 'PR':
                pm.editRenderLayerMembers('CH_color', ['PR'], noRecurse=1)

            elif i == ['PR'] == False:
                print '아웃라이너에 PR가 없다'

        for i in sel:
            if i == 'CH':
                pm.editRenderLayerMembers('shadow', ['CH'], noRecurse=1)

            elif i == ['CH'] == False:
                print '아웃라이너에 CH가 없다'

        for i in sel:
            if i == 'BG':
                pm.editRenderLayerMembers('shadow', ['BG'], noRecurse=1)

            elif i == ['BG'] == False:
                print '아웃라이너에 BG가 없다'

        for i in sel:
            if i == 'PR':
                pm.editRenderLayerMembers('shadow', ['PR'], noRecurse=1)

            elif i == ['PR'] == False:
                print '아웃라이너에 PR가 없다'
        for i in sel:
            if i == 'CH':
                pm.editRenderLayerMembers('CH_rim', ['CH'], noRecurse=1)

            elif i == ['CH'] == False:
                print '아웃라이너에 CH가 없다'

        for i in sel:
            if i == 'PR':
                pm.editRenderLayerMembers('CH_rim', ['PR'], noRecurse=1)

            elif i == ['PR'] == False:
                print '아웃라이너에 PR가 없다'
                            #CH_rim_VRayMt_assign
                    #pm.mel.hookShaderOverride("CH_rim", "VRayMtl", "")


    def buttonClick14(self):
        print "TEST"
        i = ""
        sel = pm.ls(sl=1)
        print sel

        for i in sel:
            i
            pm.editRenderLayerAdjustment("%s.matteSurface" % (i))
            pm.setAttr("%s.matteSurface" % str(i), 1)

            pm.editRenderLayerAdjustment("%s.alphaContribution" % (i))
            pm.setAttr("%s.alphaContribution" % (i), -1)

            pm.editRenderLayerAdjustment("%s.shadows" % (i))
            pm.setAttr("%s.shadows" % (i), 1)

            pm.editRenderLayerAdjustment("%s.affectAlpha" % (i))
            pm.setAttr("%s.affectAlpha" % (i), 1)

            pm.editRenderLayerAdjustment("%s.reflectionAmount" % (i))
            pm.setAttr("%s.reflectionAmount" % (i), 0)

            pm.editRenderLayerAdjustment("%s.refractionAmount" % (i))
            pm.setAttr("%s.refractionAmount" % (i), 0)


    def buttonClick15(self):

        if len(pm.ls(sl=1)) > 0:
            text = "BG"
            vray_Asop = pm.vray('objectProperties', 'add_single')

            BG_name=pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)

            pm.setAttr("%s.objectIDEnabled" % BG_name, 1)
            pm.setAttr("%s.objectID" % BG_name, 103)





    def UnknownPlugin_remove(self):

        findplugin = pm.unknownPlugin(q=True, l=True)

        try:
            for i in findplugin:
                pm.unknownPlugin(i, remove=1)
        except:
            pm.confirmDialog( b='지워졌어요!!!!', m='메세지:지웠음')



    def open(self):

        # print "open"
        openlist = []
        if self.ui.comboBox.currentText() == "Y:":
            ani_fn_file= '/'.join([self.ui.comboBox.currentText(), "NPC", "prod", "02_animation", self.ui.comboBox_3.currentText(), self.ui.comboBox_2.currentText()])
            print ani_fn_file
            for file in os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", "02_animation", self.ui.comboBox_3.currentText(), self.ui.comboBox_2.currentText()])):
                # print file

                if 'fn' in file:
                    print file
                    print ani_fn_file + "/" + file
                    pm.cmds.file(str(ani_fn_file + "/" +file), ignoreVersion=1, typ="mayaAscii", options="v=0;", o=1, f=1)
                    pm.mel.addRecentFile(str(ani_fn_file + "/" +file), "mayaAscii")

    def save_ma(self):
        print 'save'

        FOLDER_PATH = '/'.join([self.ui.comboBox.currentText(), "NPC", "prod", self.ui.comboBox_5.currentText(),self.ui.comboBox_3.currentText(), self.ui.comboBox_2.currentText()])
        VOLDER_PATH = '/'.join(["V:", "NPC", "prod", self.ui.comboBox_5.currentText(),self.ui.comboBox_3.currentText(), self.ui.comboBox_2.currentText()])
        print FOLDER_PATH
        print VOLDER_PATH
        # 파일 type 경로 알아내기
        fileKind = cmds.file(q=1, type=1)
        # 타입이 'mayaBinary'와 같다면 fileEnder는 .mb 'mayaAscii'와 같다면 .ma 다
        if fileKind[0] == 'mayaBinary':
            fileEnder = '.mb'
            print fileEnder
        elif fileKind[0] == 'mayaAscii':
            fileEnder = '.ma'
            print fileEnder

        # 현제 파일이름 알아오기
        current_file = cmds.file(q=1, sn=1, shn=1)
        print current_file

        # 콤마 기준으로 앞에 이름 인덱스로 가져오기
        theFileName = current_file.rpartition('.')[0]
        print theFileName
        # theFileName = mel.eval('basenameEx("%s")' % current_file)



        # fileLists = os.listdir(FOLDER_PATH + '_back')
        # if fileLists:
        # 빈 버전숫자 리스트 만들기 나중에 appand 함수로 숫자를 담음


        # create a confirm dialog with a yes and no button. Specif
        # check response
        ex = ['proxy', 'ver']
        # 경로에 있는  폴더 리스를 file에 담고 prox시 파일이 잇으면 제외한 나머지를 보여달라
        for self.file in os.listdir(FOLDER_PATH):
            virCount_list = []

            # 경로에 있는  폴더 리스를 file에 담고['prox','ver']시 파일이 잇으면

            if str(current_file) in self.file:
                print 'tttt'

                for self.file in os.listdir(FOLDER_PATH):

                    if self.file in ex: continue
                    print file




                    # _v를 기준으로 앞에 이름 들고 오고 이름 바꾸기
                    baseName = self.file.rpartition('_v')[0].replace('ani_fn', 'lit')
                    print baseName

                    # _v기준으로 마지막 인덱스 그리고 .기준으로 앞에 글자에 int으로 감싸서 숫자로 만듬
                    virCount = self.file.rpartition('_v')[-1].rpartition('.')[0]
                    print virCount
                    # print int(virCount)
                    #
                    # vircount리스트에 버전 숫자 담
                    virCount_list.append(virCount)
                #     # 제일 높은 숫자를 변수에 담기
                maxNum = max(virCount_list)
                print maxNum
                # 네임에 _V를 붙이고 시퀀스 2자리로 맞추고 높은 숫자 와 1더하기 (파일이름 만들기)
                self.newName = baseName + '_v' + '%02d' % (int(maxNum) + 1)

                print self.newName
                # 파일이름 리네임함 위에서
        #
                response = cmds.confirmDialog(title="Confirm",
                                              cancelButton="cencel",
                                              defaultButton="version_Overlay",
                                              button=["version_Overlay", "version_up"],
                                              message="덮을래? 올릴래?", dismissString="cencel")
                # cmds.file(rename=(FOLDER_PATH + '/' + newName + fileEnder))
                if response == "version_Overlay":
                    print 'overlay'
                    print str(FOLDER_PATH + '/' + current_file.replace('ani_fn', 'lit'))
                    cmds.file(rename=str(VOLDER_PATH + '/' + current_file.replace('ani_fn', 'lit'))) and cmds.file(save=1, type=fileKind[0])
                    print 'V:_save'
                    cmds.file(rename=str(FOLDER_PATH + '/' + current_file.replace('ani_fn', 'lit'))) and cmds.file(save=1, type=fileKind[0])
                    print 'Y:_save'




                    # pm.saveAs(FOLDER_PATH + '/' + current_file.replace('ani_fn', 'lit'), f=True)

                elif response == "version_up":
                    print 'iii'
                    # if pm.saveAs(FOLDER_PATH + '/' + newName + fileEnder) == True:
                    #     pm.saveAs(VOLDER_PATH + '/' + newName + fileEnder)
                    cmds.file(rename=str(VOLDER_PATH + '/' + self.newName + fileEnder)) and cmds.file(save=1, type=fileKind[0])
                    print 'V:_save'

                    cmds.file(rename=str(FOLDER_PATH + '/' + self.newName + fileEnder)) and cmds.file(save=1, type=fileKind[0])
                    print 'Y:_save'



                    # pm.saveAs(FOLDER_PATH + '/' + current_file.rpartition('_v')[0] + '_v01' + fileEnder, f=True)
        if len(os.listdir(FOLDER_PATH)) <= 2:
            print 'oooooooooooooo'
            print current_file.replace('ani_fn', 'lit').rpartition('_v')[0] + '_v01' + fileEnder
            cmds.file(rename=str(VOLDER_PATH + '/' + current_file.replace('ani_fn', 'lit').rpartition('_v')[0] + '_v01' + fileEnder)) and cmds.file(save=1, type=fileKind[0])
            print 'V:_save'
            cmds.file(rename=str(FOLDER_PATH + '/' + current_file.replace('ani_fn', 'lit').rpartition('_v')[0] + '_v01' + fileEnder)) and cmds.file(save=1, type=fileKind[0])
            print 'Y:_save'






    def pushButton_16(self):
        print 'master'
        targetsel = pm.ls(['CH', 'PR', 'BG'], typ='transform')
        for i in range(len(targetsel)):

            if "CH" in targetsel:
                if targetsel[i] == "CH":
                    print "CH"
                    pm.select(targetsel[i])
                    text = "CH"
                    vray_Asop = pm.vray('objectProperties', 'add_single')

                    CH_name = pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)

                    pm.setAttr("%s.objectIDEnabled" % CH_name, 1)

                    pm.setAttr("%s.objectID" % CH_name, 101)

                    cmds.editRenderLayerGlobals(currentRenderLayer='shadow')

                    if cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ) == 'shadow':

                        pm.editRenderLayerAdjustment("CH_vrayobjectproperties.primaryVisibility")

                        pm.setAttr("CH_vrayobjectproperties.primaryVisibility", 0)



                if targetsel[i] == "PR":

                    print "PR"
                    pm.select(targetsel[i])
                    text = "PR"
                    vray_Asop = pm.vray('objectProperties', 'add_single')

                    PR_name=pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)

                    pm.setAttr("%s.objectIDEnabled" % PR_name, 1)

                    pm.setAttr("%s.objectID" % PR_name, 102)

                    pm.editRenderLayerGlobals(currentRenderLayer='shadow')

                    if pm.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'shadow':
                        pm.editRenderLayerAdjustment("PR_vrayobjectproperties.primaryVisibility")

                        pm.setAttr("PR_vrayobjectproperties.primaryVisibility", 0)

                    cmds.editRenderLayerGlobals(currentRenderLayer='CH_rim')

                    if pm.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'CH_rim':
                        pm.editRenderLayerAdjustment("PR_vrayobjectproperties.matteSurface")

                        pm.setAttr("PR_vrayobjectproperties.matteSurface", 1)
                        pm.editRenderLayerAdjustment("PR_vrayobjectproperties.alphaContribution")

                        pm.setAttr("PR_vrayobjectproperties.alphaContribution", -1)
                        pm.editRenderLayerAdjustment("PR_vrayobjectproperties.reflectionAmount")

                        pm.setAttr("PR_vrayobjectproperties.reflectionAmount", 0)
                        pm.editRenderLayerAdjustment("PR_vrayobjectproperties.refractionAmount")

                        pm.setAttr("PR_vrayobjectproperties.refractionAmount", 0)
                #
                if targetsel[i] == "BG":
                    print "BG"
                    pm.select(targetsel[i])
                    text = "BG"
                    vray_Asop = pm.vray('objectProperties', 'add_single')

                    BG_name=pm.rename(vray_Asop, '%s_vrayobjectproperties' % text)

                    pm.setAttr("%s.objectIDEnabled" % BG_name, 1)

                    pm.setAttr("%s.objectID" % BG_name, 103)

                    cmds.editRenderLayerGlobals(currentRenderLayer='shadow')

                    if cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'shadow':
                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.matteSurface")

                        pm.setAttr("BG_vrayobjectproperties.matteSurface", 1)
                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.alphaContribution")

                        pm.setAttr("BG_vrayobjectproperties.alphaContribution", -1)
                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.shadows")

                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.affectAlpha")

                        pm.setAttr("BG_vrayobjectproperties.shadows", 1)
                        pm.setAttr("BG_vrayobjectproperties.affectAlpha", 1)
                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.reflectionAmount")

                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.refractionAmount")

                        pm.setAttr("BG_vrayobjectproperties.reflectionAmount", 0)
                        pm.setAttr("BG_vrayobjectproperties.refractionAmount", 0)

                        pm.editRenderLayerGlobals(currentRenderLayer='CH_color')

                    if pm.editRenderLayerGlobals(query=True, currentRenderLayer=True) == 'CH_color':


                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.matteSurface")

                        pm.setAttr("BG_vrayobjectproperties.matteSurface", 1)
                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.alphaContribution")

                        pm.setAttr("BG_vrayobjectproperties.alphaContribution", -1)
                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.reflectionAmount")

                        pm.editRenderLayerAdjustment("BG_vrayobjectproperties.refractionAmount")

                        pm.setAttr("BG_vrayobjectproperties.reflectionAmount", 0)
                        pm.setAttr("BG_vrayobjectproperties.refractionAmount", 0)


    def pushButton_17(self):
        print "outside"
        if pm.objExists('vraySettings'):

            cacheDirC = "Y:/NPC/prod/03_lightingSet/ep00/light_set/timelight_set/sun_light_set.ma"

            mel.eval('file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "%s";' % cacheDirC)

            pm.editRenderLayerMembers('CH_color', 'daylight_set', noRecurse=1)

            pm.editRenderLayerMembers('shadow', 'key_light', noRecurse=1)

            pm.editRenderLayerMembers('BG_color', 'daylight_set', noRecurse=1)

        self.start_fram = int(pm.playbackOptions(min=self.st))
        self.end_fram = int(pm.playbackOptions(max=self.en))

        pm.setAttr("defaultRenderGlobals.startFrame", self.start_fram)
        pm.setAttr("defaultRenderGlobals.endFrame", self.end_fram)

    # def rad_sky(self):
    #     print "rad_sky"
    #     if pm.objExists('vraySettings'):
    #         cacheDirC = "Y:/NPC/prod/03_lightingSet/ep00/light_set/timelight_set/radsky_light_set.ma"
    #
    #         mel.eval(
    #             'file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "%s";' % cacheDirC)
    #
    #         pm.editRenderLayerMembers('CH_color', 'daylight_set', noRecurse=1)
    #
    #
    #
    #         pm.editRenderLayerMembers('shadow', 'key_light', noRecurse=1)
    #
    #         pm.editRenderLayerMembers('BG_color', 'daylight_set', noRecurse=1)
    #
    #     self.start_fram = int(pm.playbackOptions(min=self.st))
    #     self.end_fram = int(pm.playbackOptions(max=self.en))
    #
    #     pm.setAttr("defaultRenderGlobals.startFrame", self.start_fram)
    #     pm.setAttr("defaultRenderGlobals.endFrame", self.end_fram)


    def pushButton_18(self):
        print "holl"
        if pm.objExists('vraySettings'):

            cacheDirD = "Y:/NPC/prod/03_lightingSet/ep00/light_set/hall_light_set.ma"

            mel.eval('file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "%s";' % cacheDirD)

            pm.editRenderLayerMembers('CH_color', 'center_light', 'sp_light', 'box_light', noRecurse=1)

            pm.editRenderLayerMembers('BG_color', 'center_light', 'sp_light', 'box_light', noRecurse=1)

            pm.editRenderLayerMembers('shadow', 'center_light', 'sp_light', 'box_light', noRecurse=1)



        self.start_fram = int(pm.playbackOptions(min=self.st))
        self.end_fram = int(pm.playbackOptions(max=self.en))

        pm.setAttr("defaultRenderGlobals.startFrame", self.start_fram)
        pm.setAttr("defaultRenderGlobals.endFrame", self.end_fram)


    def pushButton_19(self):
        print "room"
        if pm.objExists('vraySettings'):

            cacheDirE = "Y:/NPC/prod/03_lightingSet/ep00/light_set/room_light_set.ma"

            mel.eval('file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash true -namespace ":" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "%s";' % cacheDirE)

            pm.editRenderLayerMembers('CH_color', 'fl_light', 'gr_room_light', noRecurse=1)

            pm.editRenderLayerMembers('BG_color', 'fl_light', 'gr_room_light', noRecurse=1)

            pm.editRenderLayerMembers('shadow', 'fl_light', 'sp_light', noRecurse=1)



        self.start_fram = int(pm.playbackOptions(min=self.st))
        self.end_fram = int(pm.playbackOptions(max=self.en))

        pm.setAttr("defaultRenderGlobals.startFrame", self.start_fram)
        pm.setAttr("defaultRenderGlobals.endFrame", self.end_fram)

import sys

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#
#     form = randerForm(None)
#
#     form.show()
#     sys.exit(app.exec_())

def standaloneMain():
    '''
    마야 말고 그냥 윈도우에서 띄울욚 쓰는 Qt 방식
    PyQt 쓸대
    :return:
    '''
    app = QtWidgets.QApplication(sys.argv)
    form = randerForm(None)
    form.show()
    sys.exit(app.exec_())

def mayaMain():
    '''
    마야에서 띄우고 싶을욚 쓰는 Qt방식
    PySide 쓸때
    :return:
    '''
    global form
    form = randerForm(getMayaWindow())
    form.show()

<<<<<<< HEAD

# MayaAction.py, HoudiniAction.py
# def ImportAction():






=======
>>>>>>> 36825ea971ffc5d2c79a2cdd12bdd70acd47d378

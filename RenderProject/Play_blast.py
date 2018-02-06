#coding:cp949
#-*- coding: utf-8 -*-
import sys

from playblast_ui import Play_Form
from maya import cmds as cmds
import maya.mel as mel





try:
    import subprocess
    from PySide2 import QtWidgets, QtCore
    from shiboken2 import wrapInstance
    from maya import OpenMayaUI as omui
    import maya.mel as mel
    import maya.cmds as cmds
    import pymel.core as pm
    from PySide2.QtCore import Qt
    from maya import cmds as cmds
    import maya.mel as mel

except:
    from PyQt5 import QtWidgets

import os
import string

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)
def getMayaWindow():
    try:
        mayaMainWindowPtr = omui.MQtUtil.mainWindow()
        mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)

    except:
        mayaMainWindow = None
    return mayaMainWindow

class playblast_Form(QtWidgets.QWidget):
    def __init__(self, parent = None ):
        QtWidgets.QWidget.__init__(self, parent=parent)

        # self.setParent(mayaMainWindow)
        self.setWindowFlags(Qt.Dialog)


        self.ui = Play_Form()
        self.ui.setupUi(self)
        self.serverList = ["Y:"]
        #
        #
        self.ui.comboBox.currentIndexChanged.connect(self.SuverChange)

        self.ui.comboBox.addItems(self.serverList)

        self.ui.pushButton.clicked.connect(self.stepFrmaePlayblast)



    def SuverChange(self, index):

        # self.ui.comboBox_5.clear()
        # self.ui.comboBox_3.clear()

        if self.ui.comboBox.currentText() == "Y:":
            self.ui.comboBox_2.clear()

            # print 'Y'
            # print os.listdir(os.path.join(self.ui.comboBox.currentText(), "NPC", "prod"))
            # print os.path.isdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod"]))
            # print os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod"]))

            for file in os.listdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", "02_animation"])):
                # print file
                # and file.startswith('$') == False:
                if os.path.isdir('/'.join([self.ui.comboBox.currentText(), "NPC", "prod", "02_animation", file])) == True and file.startswith('$') == False:
                   # print file
                    self.ui.comboBox_2.addItem(file)

    def stepFrmaePlayblast(self):
        stepFrame = 2
        mediaPlayer = "C:굚Program Files굚Zurbrigg굚Keyframe MP굚bin굚keyframe_mp.exe"
        mediaScale = 50
        # find out the highlighted range we playblast
        mel.eval("global string $gPlayBackSlider;")
        selectedRange = mel.eval("timeControl -q -rangeArray $gPlayBackSlider;")
        print '1:', selectedRange
        startFrame = int(selectedRange[0])
        print '2:',startFrame
        endFrame = int(selectedRange[1])
        # if no highlighted rang, find animation frame range
        if mel.eval("timeControl -q -rangeVisible $gPlayBackSlider;") == 0:
            startFrame = int(cmds.playbackOptions(q=True, minTime=True))
            print '3:', startFrame
            endFrame = int(cmds.playbackOptions(q=True, maxTime=True))
            print '4:', endFrame
        # find out selected ctrls for keyframe to render
        selectedObj = cmds.ls(sl=True)
        print '5:', selectedObj
        # find out stepped frames to render
        if len(selectedObj) == 0:
            stepFrame = stepFrame
            print '6', stepFrame
            renderedFrame = []

            for frame in range(startFrame, endFrame, stepFrame):
                renderedFrame.append(frame)
                print '7', renderedFrame

        # find keyframe on selected ctrl
        elif len(selectedObj) == 1:
            selectedObj = selectedObj[0]

            keyframeNumbers = cmds.keyframe(selectedObj, time=(startFrame, endFrame), query=True, timeChange=True)
            if len(keyframeNumbers) == 0: cmds.error("the selected ctrl do not have any animation key on")

            renderedFrame = []
            for keyframeNumber in keyframeNumbers:
                if not keyframeNumber in renderedFrame:
                    renderedFrame.append(int(keyframeNumber))


        else:
            cmds.error("please select only one ctrl, that has an animation key to playblast")

        # excute playblast
        print "playblast will render this frames : " + str(renderedFrame)

        #filename = cmds.playblast( clearCache=1, frame=renderedFrame , f= "C:/Users/bum/Desktop/ddd.mov" ,fo=True, format="avi", c="none", rfn=True, p =mediaScale, viewer =0)
        filename = cmds.playblast(fp=4, clearCache=1, showOrnaments=1, frame=renderedFrame, format='avi', percent=100,viewer=1, quality=100, widthHeight=(1280, 720), compression="none", f="C:/Users/bum/Desktop/ddd.mov", p=mediaScale, rfn=True)

        # print playblast information
        print "----------- playblast info -------------"
        print "playblast will render this frames : " + str(renderedFrame)
        print "playblast is saved as : " + filename + ".avi"
        print "----------------------------------------"

        # open media player
        import subprocess
        subprocess.call(mediaPlayer + " " + filename + ".avi")






import sys

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#
#     form = playblast_Form(None)
#
#     form.show()
#     sys.exit(app.exec_())

def standaloneMain():

    app = QtWidgets.QApplication(sys.argv)
    form = playblast_Form(None)
    form.show()
    sys.exit(app.exec_())

def mayaMain():

    global form
    form = playblast_Form(getMayaWindow())
    form.show()


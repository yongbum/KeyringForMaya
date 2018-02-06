import maya.cmds as cmds
import maya.mel as mel


def stepFrmaePlayblast(stepFrame=2, mediaPlayer="C:/Program Files/Zurbrigg/Keyframe MP/bin/keyframe_mp.exe",
                       mediaScale=50):
    # find out the highlighted range we playblast
    mel.eval("global string $gPlayBackSlider;")
    selectedRange = mel.eval("timeControl -q -rangeArray $gPlayBackSlider;")
    startFrame = int(selectedRange[0])
    endFrame = int(selectedRange[1])
    # if no highlighted rang, find animation frame range
    if mel.eval("timeControl -q -rangeVisible $gPlayBackSlider;") == 0:
        startFrame = int(cmds.playbackOptions(q=True, minTime=True))
        endFrame = int(cmds.playbackOptions(q=True, maxTime=True))
    # find out selected ctrls for keyframe to render
    selectedObj = cmds.ls(sl=True)

    # find out stepped frames to render
    if len(selectedObj) == 0:
        stepFrame = stepFrame
        renderedFrame = []

        for frame in range(startFrame, endFrame, stepFrame):
            renderedFrame.append(frame)

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
    filename = cmds.playblast(clearCache=1, frame=renderedFrame, filename="C:/Users/bum/Desktop/sdsdsds.mov", fo=True,
                              format="avi", widthHeight=(1280, 720), quality=100, compression="H.264",
                              c="none", rfn=True, p=mediaScale)

    # print playblast information
    print "----------- playblast info -------------"
    print "playblast will render this frames : " + str(renderedFrame)
    print "playblast is saved as : " + filename + ".avi"
    print "----------------------------------------"

    # open media player
    import subprocess
    subprocess.call(mediaPlayer + " " + filename + ".avi")


stepFrmaePlayblast(stepFrame=2, mediaPlayer="C:/Program Files/Zurbrigg/Keyframe MP/bin/keyframe_mp.exe", mediaScale=50)
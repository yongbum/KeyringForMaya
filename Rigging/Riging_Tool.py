
import pymel.core as pm

windowname = 'RigingTool'
windowW = 300
windowH = 800


class Riging():
    def __init__(self, parent=None):
        self.sellist = []

        with pm.window(t=windowname, h=windowH, w=windowW):
            with pm.columnLayout(adj=True):
                with pm.frameLayout(label='Ctrl Color', backgroundColor=[0.4, 0.4, 0.4]):
                    pm.separator(h=10, style='out')
                    with pm.rowColumnLayout(numberOfRows=2, rowHeight=((1, 30), (2, 30))):
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Misty Rose.png',
                                          command=lambda: self.colorselct(20))  # up1 #color:20
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Sky blue.png',
                                          command='colorselct(18)')  # down1 #color:18
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Brown.png',
                                          command='colorselct(12)')  # up2 color:12
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Dodger Blue.png',
                                          command='colorselct(29)')  # down2 #color:29
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/rad.png',
                                          command='colorselct(13)')  # up3 #color:13
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/blue.png',
                                          command='colorselct(6)')  # down3 #color:6
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/yellow.png',
                                          command='colorselct(22)')  # up4 #color:22
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Dark blue.png',
                                          command='colorselct(5)')  # down4 #color:5
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/pink.png',
                                          command='colorselct(9)')  # up5 #color:9
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Dark Goldenrod.png',
                                          command='colorselct(24)')  # down5 color:24
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Dark Violet.png',
                                          command='colorselct(30)')  # up6 #color:30
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Alice Blue.png',
                                          command='colorselct(25)')  # down6 #color:25
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Indigo.png',
                                          command='colorselct(8)')  # up7 # color:8
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Bisque.png',
                                          command='colorselct(21)')  # down7 #color:21
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Aquamarine.png',
                                          command='colorselct(19)')  # up8 #color:19
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/White.png',
                                          command='colorselct(16)')  # down8 #color:16
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/lightgreen.png',
                                          command='colorselct(14)')  # up9 #color:14
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Gray.png',
                                          command='colorselct(3)')  # down9 #color:3
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Dark green.png',
                                          command='colorselct(26)')  # up10 #color:26
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Dark Gray.png',
                                          command='colorselct(2)')  # down10 #color:2
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Medium Sea Green.png',
                                          command='colorselct(23)')  # up11 #color:23
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/black.png',
                                          command='colorselct(1)')  # down11 #color:1
                        pm.setParent('..')
                        with pm.columnLayout(adj=True):
                            pm.separator(h=10, style='out')
                            with pm.frameLayout(label='Ctrl Color', backgroundColor=[0.4, 0.4, 0.4]):
                                pm.separator(h=10, style='out')
                                with pm.columnLayout(adj=True):
                                    pm.gridLayout(numberOfColumns=9, cellWidthHeight=(40, 40), width=300)
                                    # icons of the "controllers"
                                    pm.symbolButton(image='mz_icons/ccButton01.PNG', command='Ctrl_Create(A)')
                                    pm.symbolButton(image='mz_icons/ccButton02.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton03.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton04.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton05.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton06.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton07.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton08.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton09.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton10.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton11.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton12.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton13.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton14.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton15.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton16.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton17.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton18.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton19.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton20.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton21.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton22.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton23.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton24.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton25.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton26.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton27.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton28.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton29.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton30.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton31.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton32.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton33.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton34.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton35.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton36.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton37.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton38.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton39.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton40.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton41.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton42.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton43.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton44.PNG')
                                    pm.symbolButton(image='mz_icons/ccButton45.PNG')
                                    pm.setParent('..')
                                    pm.separator(h=10, style='out')

                                    with pm.columnLayout(adj=True):
                                        with pm.rowColumnLayout(numberOfRows=1, rowHeight=((1, 20), (2, 20))):
                                            pm.separator(h=10, style='out')
                                            pm.text('                    ')
                                            pm.checkBox(label='    ')
                                            pm.button(label='change', w=50, h=20)
                                            pm.text('                    ')
                                            pm.checkBox(label='    ')
                                            pm.button(label='change', w=50, h=20)
                                            pm.setParent('..')
                                            with pm.columnLayout(adj=True):
                                                pm.separator(h=10, style='out')

    def colorselct(self, number):
        SelectTarget = pm.ls(sl=1)

        for ctrl in SelectTarget:
            print ctrl
            shape = pm.listRelatives(ctrl, s=1)[0]
            print shape
            pm.setAttr('%s.overrideEnabled' % shape, 1)
            pm.setAttr('%s.overrideColor' % shape, number)


def Ctrl_Create(self, *args):


    -        self.A = pm.circle(c=(0, 0, 0), nr=(0, 1, 0))

-        self.B = pm.curve(p=[(1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, 1.011106),(1.011106, 1.011106, 1.011106), (1.011106, 1.011106, -1.011106),(1.011106, -1.011106, -1.011106),(-1.011106, -1.011106, -1.011106), (-1.011106, 1.011106, -1.011106),(-1.011106, 1.011106, 1.011106),(-1.011106, -1.011106, 1.011106), (-1.011106, -1.011106, -1.011106),(1.011106, -1.011106, -1.011106),
       -               (1.011106, -1.011106, 1.011106), (1.011106, 1.011106, 1.011106), (-1.011106, 1.011106, 1.011106),
       -               (-1.011106, -1.011106, 1.011106), (1.011106, -1.011106, 1.011106)],
    -                     k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], d = 1)
+
if args == 'A':
    +            pm.circle(c=(0, 0, 0), nr=(0, 1, 0))
+
if args == 'B':
    +            pm.curve(
        p=[(1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, 1.011106),
           +                   (1.011106, 1.011106, 1.011106), (1.011106, 1.011106, -1.011106),
           (1.011106, -1.011106, -1.011106),
           +                   (-1.011106, -1.011106, -1.011106), (-1.011106, 1.011106, -1.011106),
           (-1.011106, 1.011106, 1.011106),
           +                   (-1.011106, -1.011106, 1.011106), (-1.011106, -1.011106, -1.011106),
           (1.011106, -1.011106, -1.011106),
           +                   (1.011106, -1.011106, 1.011106), (1.011106, 1.011106, 1.011106),
           (-1.011106, 1.011106, 1.011106),
           +                   (-1.011106, -1.011106, 1.011106), (1.011106, -1.011106, 1.011106)],
        +                         k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], d = 1)




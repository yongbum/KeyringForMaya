#coding:cp949
import pymel.core as pm
''''
========================================================================================
runcode
import sys 
sys.path.append('Q:굚yongbum굚PYTHON_PATH굚KeyringForMaya굚Rigging')
import Riging_Tool
reload(Riging_Tool)
Riging_Tool.Riging()

=======================================================================================

질문입니다
1.함수가  Create() 실행이 왜 안 될까요?
2.class 안에서 인자 값을 넣고 이수값을 넣는 방법을 잘 모르겠습니다 
3.혹시 iconTextButton 버튼과  symbolButton 버튼의 이벤트 발생하는 스크립트 방식이 다른가요?

===========================================================================================

'''''

windowname = 'RigingTool'
windowW = 300
windowH = 800


class Riging():
    def __init__(self):
        pass


        with pm.window(t=windowname, h=windowH, w=windowW):
            with pm.columnLayout(adj=True):
                with pm.frameLayout(label='Ctrl Color', backgroundColor=[0.4, 0.4, 0.4]):
                    pm.separator(h=10, style='out')
                    with pm.rowColumnLayout(numberOfRows=2, rowHeight=((1, 30), (2, 30))):
                        pm.iconTextButton(style='iconAndTextVertical', image1='icons/Misty Rose.png',
                                          command=lambda:self.colorselct(20))  # up1 #color:20
                        pm.iconTextButton(style='iconAndTextVertical', image1='Sky blue.png',
                                          command=lambda:self.colorselct(18))  # down1 #color:18
                        pm.iconTextButton(style='iconAndTextVertical', image1='Brown.png',
                                          command=lambda:self.colorselct(12))  # up2 color:12
                        pm.iconTextButton(style='iconAndTextVertical', image1='Dodger Blue.png',
                                          command=lambda:self.colorselct(29))  # down2 #color:29
                        pm.iconTextButton(style='iconAndTextVertical', image1='rad.png',
                                          command=lambda:self.colorselct(13))  # up3 #color:13
                        pm.iconTextButton(style='iconAndTextVertical', image1='blue.png',
                                          command=lambda:self.olorselct(6))  # down3 #color:6
                        pm.iconTextButton(style='iconAndTextVertical', image1='yellow.png',
                                          command=lambda:self.colorselct(22))  # up4 #color:22
                        pm.iconTextButton(style='iconAndTextVertical', image1='Dark blue.png',
                                          command=lambda:self.colorselct(5))  # down4 #color:5
                        pm.iconTextButton(style='iconAndTextVertical', image1='pink.png',
                                          command=lambda:self.colorselct(9))  # up5 #color:9
                        pm.iconTextButton(style='iconAndTextVertical', image1='Dark Goldenrod.png',
                                          command=lambda:self.colorselct(24))  # down5 color:24
                        pm.iconTextButton(style='iconAndTextVertical', image1='Dark Violet.png',
                                          command=lambda:self.colorselct(30))  # up6 #color:30
                        pm.iconTextButton(style='iconAndTextVertical', image1='Alice Blue.png',
                                          command=lambda:self.colorselct(25))  # down6 #color:25
                        pm.iconTextButton(style='iconAndTextVertical', image1='Indigo.png',
                                          command=lambda:self.colorselct(8))  # up7 # color:8
                        pm.iconTextButton(style='iconAndTextVertical', image1='Bisque.png',
                                          command=lambda:self.colorselct(21))  # down7 #color:21
                        pm.iconTextButton(style='iconAndTextVertical', image1='Aquamarine.png',
                                          command=lambda:self.colorselct(19))  # up8 #color:19
                        pm.iconTextButton(style='iconAndTextVertical', image1='White.png',
                                          command=lambda:self.colorselct(16))  # down8 #color:16
                        pm.iconTextButton(style='iconAndTextVertical', image1='lightgreen.png',
                                          command=lambda:self.colorselct(14))  # up9 #color:14
                        pm.iconTextButton(style='iconAndTextVertical', image1='Gray.png',
                                          command=lambda:self.colorselct(3))  # down9 #color:3
                        pm.iconTextButton(style='iconAndTextVertical', image1='Dark green.png',
                                          command=lambda:self.colorselct(26))  # up10 #color:26
                        pm.iconTextButton(style='iconAndTextVertical', image1='Dark Gray.png',
                                          command=lambda :self.colorselct(2))  # down10 #color:2
                        pm.iconTextButton(style='iconAndTextVertical', image1='Medium Sea Green.png',
                                          command=lambda:self.colorselct(23))  # up11 #color:23
                        pm.iconTextButton(style='iconAndTextVertical', image1='black.png',
                                          command=lambda:self.colorselct(1))  # down11 #color:1

                    with pm.columnLayout(adj=True):
                        pm.separator(h=10, style='out')
                        with pm.frameLayout(label='Ctrl Color', backgroundColor=[0.4, 0.4, 0.4]):
                            pm.separator(h=10, style='out')
                            with pm.columnLayout(adj=True):
                                pm.gridLayout(numberOfColumns=9, cellWidthHeight=(40, 40), width=300)
                                # icons of the "controllers"
                                pm.symbolButton(image='mz_icons/ccButton01.PNG', command=lambda :self.colorselct(A=True))
                                pm.symbolButton(image='mz_icons/ccButton02.PNG', command=lambda :self.colorselct(B=True))
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

                            with pm.columnLayout(adj=True):
                                pm.separator(h=10, style='out')
                                with pm.rowColumnLayout(numberOfRows=1, rowHeight=((1, 20), (2, 20))):

                                    pm.text('                    ')
                                    pm.checkBox(label='    ')
                                    pm.button(label='change', w=50, h=20)
                                    pm.text('                    ')
                                    pm.checkBox(label='    ')
                                    pm.button(label='change', w=50, h=20)
                                    pm.separator(h=10, style='out')

                                with pm.columnLayout(adj=True):
                                    pm.separator(h=10, style='out')

    def colorselct(self, number):
        #컨트롤러 선택
        SelectTarget = pm.ls(sl=1)
        #졩트롤러 쉐입에 대한 색상 바꾸기
        for ctrl in SelectTarget:
            print ctrl
            shape = pm.listRelatives(ctrl, s=1)[0]
            print shape
            pm.setAttr('%s.overrideEnabled' % shape, 1)
            pm.setAttr('%s.overrideColor' % shape, number)

    def Create(self, A=None, B=None):
        #A가 True일때 Ctrl를 생성
        if A == True:

            pm.circle(c=(0, 0, 0), nr=(0, 1, 0))

        # B가 True일때 Ctrl를 생성
        if B == True:
            pm.curve(
                p=[(1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, 1.011106),
                   (1.011106, 1.011106, 1.011106), (1.011106, 1.011106, -1.011106), (1.011106, -1.011106, -1.011106),
                   (-1.011106, -1.011106, -1.011106), (-1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, 1.011106),
                   (-1.011106, -1.011106, 1.011106), (-1.011106, -1.011106, -1.011106),
                   (1.011106, -1.011106, -1.011106),
                   (1.011106, -1.011106, 1.011106), (1.011106, 1.011106, 1.011106), (-1.011106, 1.011106, 1.011106),
                   (-1.011106, -1.011106, 1.011106), (1.011106, -1.011106, 1.011106)],
                k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], d=1)






''''
========================================================================================
runcode
import sys 
sys.path.append('Q:굚yongbum굚PYTHON_PATH굚KeyringForMaya굚Rigging')
import Riging_Tool
reload(Riging_Tool)
Riging_Tool.Riging()

=======================================================================================

질문입니다
1.함수가  Create() 실행이 왜 안 될까요?
2.class 안에서 인자 값을 넣고 이수값을 넣는 방법을 잘 모르겠습니다 
3.혹시 iconTextButton 버튼과  symbolButton 버튼의 이벤트 발생하는 스크립트 방식이 다른가요?

===========================================================================================

'''''





















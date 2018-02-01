#coding:cp949
import pymel.core as pm

try:
    pm.deleteUI(windowname)
except:
    pass
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

        with pm.window(windowname, t=windowname, h=windowH, w=windowW):
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
                                pm.symbolButton(image='mz_icons/ccButton01.PNG', command=lambda *args:self.Create(A=True,B=None,C=None,D=None,E=None,F=None,G=None,H=None,I=None,J=None))
                                pm.symbolButton(image='mz_icons/ccButton02.PNG', command=lambda *args:self.Create(A=None,B=True,C=None,D=None,E=None,F=None,G=None,H=None,I=None,J=None))
                                pm.symbolButton(image='mz_icons/ccButton03.PNG', command=lambda *args:self.Create(A=None,B=None,C=True,D=None,E=None,F=None,G=None,H=None,I=None,J=None))
                                pm.symbolButton(image='mz_icons/ccButton04.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=True,E=None,F=None,G=None,H=None,I=None,J=None))
                                pm.symbolButton(image='mz_icons/ccButton05.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=True,F=None,G=None,H=None,I=None,J=None))
                                pm.symbolButton(image='mz_icons/ccButton06.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None,F=True,G=None,H=None,I=None,J=None))
                                pm.symbolButton(image='mz_icons/ccButton07.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None,F=None,G=True,H=None,I=None,J=None))
                                pm.symbolButton(image='mz_icons/ccButton08.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None,F=None,G=None,H=True,I=None,J=None))
                                pm.symbolButton(image='mz_icons/ccButton09.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None,F=None,G=None,H=None,I=True,J=None))
                                pm.symbolButton(image='mz_icons/ccButton10.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None,F=None,G=None,H=None,I=None,J=True))
                                # pm.symbolButton(image='mz_icons/ccButton11.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None))
                                # pm.symbolButton(image='mz_icons/ccButton12.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None))
                                # pm.symbolButton(image='mz_icons/ccButton13.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None))
                                # pm.symbolButton(image='mz_icons/ccButton14.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None))
                                # pm.symbolButton(image='mz_icons/ccButton15.PNG', command=lambda *args:self.Create(A=None,B=None,C=None,D=None,E=None))
                                # pm.symbolButton(image='mz_icons/ccButton16.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton17.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton18.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton19.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton20.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton21.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton22.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton23.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton24.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton25.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton26.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton27.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton28.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton29.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton30.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton31.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton32.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton33.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton34.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton35.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton36.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton37.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton38.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton39.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton40.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton41.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton42.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton43.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton44.PNG')
                                # pm.symbolButton(image='mz_icons/ccButton45.PNG')

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

    def Create(self, A=None, B=None,C=None,D=None,E=None,F=None,G=None,H=None,I=None,J=None):
        #A가 True일때 Ctrl를 생성
        if A == True:

            pm.circle(c=(0, 0, 0), nr=(0, 1, 0))

        # B가 True일때 Ctrl를 생성
        if B == True:
            pm.curve(p=[(1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, 1.011106),
                   (1.011106, 1.011106, 1.011106), (1.011106, 1.011106, -1.011106), (1.011106, -1.011106, -1.011106),
                   (-1.011106, -1.011106, -1.011106), (-1.011106, 1.011106, -1.011106), (-1.011106, 1.011106, 1.011106),
                   (-1.011106, -1.011106, 1.011106), (-1.011106, -1.011106, -1.011106),
                   (1.011106, -1.011106, -1.011106),
                   (1.011106, -1.011106, 1.011106), (1.011106, 1.011106, 1.011106), (-1.011106, 1.011106, 1.011106),
                   (-1.011106, -1.011106, 1.011106), (1.011106, -1.011106, 1.011106)],
                k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], d=1)
        if C == True:
            pm.curve(p=[(0, 0, 0), (-1.5, 3, 0), (1.5, 3, 0), (0, 0, 0), (0, 3, 0), (0, 3, -1.5), (0, 0, 0), (0, 3, 1.5),
                   (0, 3, 0)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], d=1)

        if D == True:
            pm.curve(degree=1, knot=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], point=[(-4, 0, 0), (-2, 0, -2), (-2, 0, -1), (2, 0, -1), (2, 0, -2), (4, 0, 0), (2, 0, 2), (2, 0, 1), (-2, 0, 1), (-2, 0, 2), (-4, 0, 0)])

        if E == True:
            pm.curve(degree=1, knot=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43],
                     point=[(-2.1213199999999999, 0, 2.1213199999999999), (-2.4275890000000002, 0, 1.760219), (-2.6713830000000001, 0, 1.3581639999999999), (-2.8528880000000001, 0, 0.91765300000000005),
                            (-2.9599489999999999, 0, 0.47963099999999997), (-2.9999920000000002, 0, 0.0065315299999999998), (-2.9641760000000001, 0, -0.453565), (-2.8391410000000001, 0, -0.95904599999999995),
                            (-2.6717170000000001, 0, -1.357504), (-2.4336000000000002, 0, -1.751819), (-2.1309930000000001, 0, -2.1116009999999998), (-1.7928569999999999, 0, -2.4038110000000001), (-1.387964, 0, -2.6561140000000001),
                            (-0.942438, 0, -2.844735), (-0.46542499999999998, 0, -2.9622820000000001), (0.0084003199999999993, 0, -2.9999880000000001), (0.45493899999999998, 0, -2.963959), (0.94169899999999995, 0, -2.8449810000000002),
                            (1.3494409999999999, 0, -2.6757759999999999), (1.7573289999999999, 0, -2.429662), (2.1288819999999999, 0, -2.1137299999999999), (2.411311, 0, -1.782662), (2.6613889999999998, 0, -1.377759),
                            (2.8479290000000002, 0, -0.93281199999999997), (2.9608530000000002, 0, -0.47417700000000002), (2.9999989999999999, 0, 0.00169319), (2.964737, 0, 0.449986), (2.8521960000000002, 0, 0.91978700000000002), (2.6751839999999998, 0, 1.3506199999999999),
                            (2.4316279999999999, 0, 1.7545809999999999), (2.124565, 0, 2.1180699999999999), (1.7739180000000001, 0, 2.417691), (1.3726860000000001, 0, 2.6639930000000001), (0.92380099999999998, 0, 2.8508870000000002), (0.40900599999999998, 0, 2.9708540000000001),
                            (0, 0, 3), (0.62022299999999997, 0.59294500000000006, 3), (-1, 0, 3), (0.62022299999999997, -0.59294500000000006, 3), (0, 0, 3), (0.62022299999999997, 0, 2.4070550000000002), (-1, 0, 3), (0.62022299999999997, 0, 3.5929449999999998), (0, 0, 3)])

        if F == True:
            pm.curve(degree=1, knot=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
                     point=[(-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016),(-2.9915446383506463, 2.5597753382632042, 0.23863999999999944),
                            (-2.6540560067191499, 2.2222867066317078, 0.23863999999999949), (-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016),
                            (-2.6540560067191499, 2.2222867066317078, 0.23863999999999949), (-2.6540560067191499, 2.2222867066317078, -0.23864000000000049),
                            (-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016), (-2.6540560067191499, 2.2222867066317078, -0.23864000000000049),
                            (-2.9915446383506463, 2.5597753382632042, -0.23864000000000055), (-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016),
                            (-2.9915446383506463, 2.5597753382632042, 0.23863999999999944), (-2.9915446383506463, 2.5597753382632042, -0.23864000000000055),
                            (-3.9723250783801669, 1.2415055594954061, -2.756696114703874e-016), (-2.6069153189377863, 2.6069153189377867, -5.7885148206655284e-016),
                            (-1.9614611780028937, 3.1216480434482845, -6.931451065224713e-016), (-1.2176513122320769, 3.4798485398075156, -7.7268159422050689e-016),
                            (-0.41278348301258339, 3.663554174453, -8.1347243928786562e-016), (0.41278348301258405, 3.6635541744529996, -8.1347243928786552e-016),
                            (1.2176513122320776, 3.4798485398075156, -7.7268159422050689e-016), (1.9614611780028941, 3.1216480434482841, -6.931451065224712e-016),
                            (2.6069153189377867, 2.6069153189377863, -5.7885148206655274e-016), (3.9723250783801674, 1.2415055594954054, -2.7566961147038725e-016),
                            (2.6540560067191499, 2.2222867066317069, 0.23863999999999949), (2.9915446383506463, 2.5597753382632034, 0.23863999999999944),
                            (3.9723250783801674, 1.2415055594954054, -2.7566961147038725e-016), (2.9915446383506463, 2.5597753382632034, 0.23863999999999944),
                            (2.9915446383506463, 2.5597753382632034, -0.23864000000000055), (3.9723250783801674, 1.2415055594954054, -2.7566961147038725e-016),
                            (2.6540560067191499, 2.2222867066317069, -0.23864000000000049), (2.9915446383506463, 2.5597753382632034, -0.23864000000000055),
                            (2.6540560067191499, 2.2222867066317069, -0.23864000000000049), (2.6540560067191499, 2.2222867066317069, 0.23863999999999949)])





        if G == True:
            pm.curve(degree=1, knot=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                     point=[(-2.187163, -0.5, -0.5), (-2.187163, -0.5, 0.5), (-2.187163, 0.5, 0.5), (-2.187163, 0.5, -0.5),
                            (-2.187163, -0.5, -0.5), (-3.812837, 0, 0), (-2.187163, -0.5, 0.5), (-2.187163, 0.5, 0.5),
                            (-3.812837, 0, 0), (-2.187163, 0.5, -0.5), (-3.812837, 0, 0), (0, 0, 0), (3.812837, 0, 0),
                            (2.187163, 0.5, 0.5), (2.187163, 0.5, -0.5), (3.812837, 0, 0), (2.187163, 0.5, -0.5), (2.187163, -0.5, -0.5),
                            (3.812837, 0, 0), (2.187163, -0.5, -0.5), (2.187163, -0.5, 0.5), (3.812837, 0, 0), (2.187163, -0.5, 0.5),
                            (2.187163, 0.5, 0.5)])



        if H == True:
            pm.curve(degree=1,
                     knot=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                           24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
                           46, 47, 48, 49, 50, 51, 52, 53, 54, 55],
                     point=[(0.93448699999999996, 1.2758370000000001, 2.0165799999999999e-008), (0.932697, 1.2471760000000001, -0.35686000000000001),
                            (0.92075200000000001, 1.1728350000000001, -0.68600300000000003), (0.89147600000000005, 1.068829, -0.97843500000000005),
                            (0.84007600000000004, 0.94667800000000002, -1.2319290000000001), (0.76359100000000002, 0.81499100000000002, -1.4457660000000001),
                            (0.66171500000000005, 0.68111100000000002, -1.621424), (0.53715500000000005, 0.551427, -1.765671),
                            (0.38761699999999999, 0.43313299999999999, -1.880322), (0.20958599999999999, 0.33878000000000003, -1.961541),
                            (0, 0.29736299999999999, -1.9937469999999999), (-0.20958599999999999, 0.33878000000000003, -1.961541),
                            (-0.38761699999999999, 0.43313299999999999, -1.880322), (-0.53715500000000005, 0.551427, -1.765671),
                            (-0.66171500000000005, 0.68111100000000002, -1.621424), (-0.76359100000000002, 0.81499100000000002, -1.4457660000000001),
                            (-0.84007600000000004, 0.94667800000000002, -1.2319290000000001), (-0.89147600000000005, 1.068829, -0.97843500000000005),
                            (-0.92075200000000001, 1.1728350000000001, -0.68600300000000003), (-0.932697, 1.2471760000000001, -0.35686000000000001),
                            (-0.93448699999999996, 1.2758370000000001, 2.0165799999999999e-008), (-0.91757200000000005, 1.4706170000000001, 0),
                            (-0.85697100000000004, 1.6571290000000001, 0), (-0.75891600000000004, 1.826965, 0), (-0.62769200000000003, 1.972704, 0),
                            (-0.46903600000000001, 2.087974, 0), (-0.28988000000000003, 2.1677390000000001, 0), (-0.098055100000000006, 2.2085129999999999, 0),
                            (0.098055100000000006, 2.2085129999999999, 0), (0.28988000000000003, 2.1677390000000001, 0), (0.46903600000000001, 2.087974, 0),
                            (0.62769200000000003, 1.972704, 0), (0.75891600000000004, 1.826965, 0), (0.85697100000000004, 1.6571290000000001, 0),
                            (0.91757200000000005, 1.4706170000000001, 0), (0.93448699999999996, 1.2758370000000001, 2.0165799999999999e-008),
                            (0.932697, 1.2471760000000001, 0.35686000000000001), (0.92075200000000001, 1.1728339999999999, 0.68600300000000003),
                            (0.89147600000000005, 1.0688299999999999, 0.97843500000000005), (0.84007600000000004, 0.94667800000000002, 1.23193),
                            (0.76359100000000002, 0.81499200000000005, 1.445765), (0.66171500000000005, 0.68110999999999999, 1.621426),
                            (0.53715500000000005, 0.55142999999999998, 1.7656689999999999), (0.38761699999999999, 0.43312699999999998, 1.8803259999999999),
                            (0.20958599999999999, 0.33878799999999998, 1.9615359999999999), (0, 0.29731800000000003, 1.9937750000000001),
                            (-0.20958599999999999, 0.33878799999999998, 1.9615359999999999), (-0.38761699999999999, 0.43312699999999998, 1.8803259999999999),
                            (-0.53715500000000005, 0.55142999999999998, 1.7656689999999999), (-0.66171500000000005, 0.68110999999999999, 1.621426),
                            (-0.76359100000000002, 0.81499200000000005, 1.445765),(-0.84007600000000004, 0.94667800000000002, 1.23193),
                            (-0.89147600000000005, 1.0688299999999999, 0.97843500000000005), (-0.92075200000000001, 1.1728339999999999, 0.68600300000000003),
                            (-0.932697, 1.2471760000000001, 0.35686000000000001), (-0.93448699999999996, 1.2758370000000001, 2.0165799999999999e-008)])

        if I == True:
            pm.curve(degree=1,
                     knot=[0, 1, 2, 3, 4, 5, 6, 7],
                     point=[(-2, 0, 0),
                            (2, 0, 0),
                            (0, 0, 0),
                            (0, 0, 2),
                            (0, 0, -2),
                            (0, 0, 0),
                            (0, 2, 0),
                            (0, -2, 0)])

        if J == True:
            pm.curve(degree=1,
                     knot=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                     39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52],
                     point=[(0, 1, 0),
                     (0, 0.92388000000000003, 0.382683),
                     (0, 0.70710700000000004, 0.70710700000000004),
                     (0, 0.382683, 0.92388000000000003),
                     (0, 0, 1),
                     (0, -0.382683, 0.92388000000000003),
                     (0, -0.70710700000000004, 0.70710700000000004),
                     (0, -0.92388000000000003, 0.382683),
                     (0, -1, 0),
                     (0, -0.92388000000000003, -0.382683),
                     (0, -0.70710700000000004, -0.70710700000000004),
                     (0, -0.382683, -0.92388000000000003),
                     (0, 0, -1),
                     (0, 0.382683, -0.92388000000000003),
                     (0, 0.70710700000000004, -0.70710700000000004),
                     (0, 0.92388000000000003, -0.382683),
                     (0, 1, 0),
                     (0.382683, 0.92388000000000003, 0),
                     (0.70710700000000004, 0.70710700000000004, 0),
                     (0.92388000000000003, 0.382683, 0),
                     (1, 0, 0),
                     (0.92388000000000003, -0.382683, 0),
                     (0.70710700000000004, -0.70710700000000004, 0),
                     (0.382683, -0.92388000000000003, 0),
                     (0, -1, 0),
                     (-0.382683, -0.92388000000000003, 0),
                     (-0.70710700000000004, -0.70710700000000004, 0),
                     (-0.92388000000000003, -0.382683, 0),
                     (-1, 0, 0),
                     (-0.92388000000000003, 0.382683, 0),
                     (-0.70710700000000004, 0.70710700000000004, 0),
                     (-0.382683, 0.92388000000000003, 0),
                     (0, 1, 0),
                     (0, 0.92388000000000003, -0.382683),
                     (0, 0.70710700000000004, -0.70710700000000004),
                     (0, 0.382683, -0.92388000000000003),
                     (0, 0, -1),
                     (-0.382683, 0, -0.92388000000000003),
                     (-0.70710700000000004, 0, -0.70710700000000004),
                     (-0.92388000000000003, 0, -0.382683),
                     (-1, 0, 0),
                     (-0.92388000000000003, 0, 0.382683),
                     (-0.70710700000000004, 0, 0.70710700000000004),
                     (-0.382683, 0, 0.92388000000000003),
                     (0, 0, 1),
                     (0.382683, 0, 0.92388000000000003),
                     (0.70710700000000004, 0, 0.70710700000000004),
                     (0.92388000000000003, 0, 0.382683),
                     (1, 0, 0),
                     (0.92388000000000003, 0, -0.382683),
                     (0.70710700000000004, 0, -0.70710700000000004),
                     (0.382683, 0, -0.92388000000000003),
                     (0, 0, -1)])


''''
========================================================================================
runcode
import sys 
sys.path.append('Q:굚yongbum굚PYTHON_PATH굚KeyringForMaya굚Rigging')
import Riging_Tool
reload(Riging_Tool)
Riging_Tool.Riging()



'''''





















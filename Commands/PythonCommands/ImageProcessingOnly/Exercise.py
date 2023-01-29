#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button, Hat
from Commands.PythonCommandBase import ImageProcPythonCommand


# 一生エクササイズする
class Exercise(ImageProcPythonCommand):
    NAME = 'エクササイズ'

    def __init__(self, cam):
        super().__init__(cam)

    def do(self):
        # 無限エクササイズを選択
        print('select menu')
        self.press(Button.A, wait=2.5)
        self.press(Button.A, wait=1.0)
        self.press(Button.A, wait=1.0)
        self.press(Button.A, wait=1.0)
        self.press(Hat.BTM, wait=1.0)
        self.press(Button.A, wait=1.0)
        self.press(Button.A, wait=1.0)
        self.press(Button.A, wait=1.0)
        self.wait(16.0)
        
        # エクササイズ
        print('start exercise')
        while True:
            # テキストの変化を遷移のトリガーとする
            if not self.isContainTemplate('../Captures/Exercise/text.png', 0.9):
                # テキストが変化してから完全に表示されるまで待機する
                self.wait(0.3)
                self.camera.saveCapture(filename="Exercise/text", crop=1, crop_ax=[440, 100, 900, 155])

                if self.isContainTemplate('Exercise/happy.png', 0.9):
                    print('happy')
                    self.press(Button.A)
                elif self.isContainTemplate('Exercise/surprised.png', 0.9):
                    print('surprised')
                    self.press(Button.B)
                elif self.isContainTemplate('Exercise/angry.png', 0.9):
                    print('angry')
                    self.press(Button.X)
                elif self.isContainTemplate('Exercise/enjoy.png', 0.9):
                    print('enjoy')
                    self.press(Button.Y)
                elif self.isContainTemplate('Exercise/levelup.png', 0.9):
                    print('levelup')
                    self.press(Button.A)
                else:
                    print('not macth...')
            else:
                print('no change')
            print('wait')
            self.wait(0.3)

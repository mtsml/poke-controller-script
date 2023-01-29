#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button, Hat
from Commands.PythonCommandBase import ImageProcPythonCommand


# 一生レイドバトルする
class Raid(ImageProcPythonCommand):
    NAME = 'レイドバトル'

    def __init__(self, cam):
        super().__init__(cam)

    def do(self):
        self.wait(1.0)
        cnt = 0
        while True:
            cnt += 1

            # レイドを調べる
            self.press(Button.A, wait=2.0)
            while not self.isContainTemplate('Raid/star3.png', 0.8, use_gray=False) \
                or not self.isContainTemplate('Raid/star4.png', 0.8, use_gray=False):
                print('raid not found')
                self.press(Button.B, wait=1.0)
                self.change_date()
                self.wait(2.0)
                self.press(Button.A, wait=2.0)

            # 「ひとりで挑戦」を選択してレイドバトル
            self.press(Hat.BTM, wait=1.0)
            self.press(Button.A, wait=1.0)
            self.raid_battle()

            print(f'{cnt}回目')
            self.wait(20.0)

    def change_date(self):
        print('change date')
         # ホーム画面 > 設定 > 本体
        self.press(Button.HOME, wait=1.0)
        self.press(Hat.BTM)
        self.press(Hat.RIGHT)
        self.press(Hat.RIGHT)
        self.press(Hat.RIGHT)
        self.press(Hat.RIGHT)
        self.press(Hat.RIGHT)
        self.press(Button.A, wait=1.5)  
        self.press(Hat.BTM, duration=2.0, wait=1.0)
        self.press(Button.A, wait=1.0)

        # 日付と時刻の設定を探す
        while not self.isContainTemplate('Raid/datetime_settings.png', 0.8):
            self.press(Hat.BTM, wait=1.0)
        self.press(Button.A, wait=1.0)

        # 日付を1日進めてゲーム画面に戻る
        self.press(Hat.BTM)
        self.press(Hat.BTM)
        self.press(Button.A, wait=1.0)
        self.press(Hat.RIGHT)
        self.press(Hat.RIGHT)
        self.press(Hat.TOP)
        self.press(Button.A)
        self.press(Button.A)
        self.press(Button.A)
        self.press(Button.A)
        self.wait(0.5)
        self.press(Button.HOME, wait=1.0)
        self.press(Button.HOME, wait=1.0)

    def raid_battle(self):
        print('raid battle start')
        self.wait(10.0)

        while True:
            # 技選択画面
            if self.isContainTemplate('Raid/battle_menu.png', 0.8):
                print('atack')
                self.press(Button.A, wait=0.5)
                self.press(Button.A, wait=0.5)
                self.press(Button.A, wait=0.5)
            # 勝利画面
            if self.isContainTemplate('Raid/get_pokemon.png', 0.8):
                print('win')
                # つかまえない
                self.press(Hat.BTM, wait=0.5)
                self.press(Button.A, wait=0.5)
                # 報酬を受け取って終了
                self.wait(5.0)
                self.press(Button.A, wait=1.0)
                break
            # 負けることはない
            # if

            self.wait(3.0)

        print('raid batlle end')

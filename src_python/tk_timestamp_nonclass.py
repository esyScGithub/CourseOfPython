# -*- coding=utf-8 -*-

import tkinter as tk
from datetime import datetime as dt
import csv
import os


class Apprication(tk.Frame):
    """Tkinterメインウィンドウ
    Tkinterのフレームクラスを継承して、アプリケーションクラスを作成。
    （アプリケーションという名前は任意で決めて良い）

    フレームとしてできることに加えて、オリジナルのボタンを配置する。

    """

    def __init__(self, master=None):
        """コンストラクタ

        Args:
            master (tkinter.root, optional): TkInterのルートを指定. Defaults to None.
        """

        # frameオブジェクトのコンストラクタを呼んでおく。
        super().__init__(master)
        self.pack()
        self.createMainFrame()

    def createMainFrame(self):
        # 動的に変更するラベル用の変数を定義
        self.varLabel = tk.StringVar()
        self.varLabel.set("現在の記録数：0")

        # ラベル定義
        self.labelText = tk.Label(self, text="ログ")
        self.labelCounter = tk.Label(self, textvariable=self.varLabel)
        self.labelButton = tk.Label(self, text="操作ボタン")

        # 処理に使う変数の定義
        self.logCounter = 0
        self.timeData = []

        # 記録ボタンの定義
        self.addButton = tk.Button(self)
        self.addButton['text'] = '時間を記録'
        self.addButton['command'] = self.__addTime

        # 保存ボタンの定義
        self.saveButton = tk.Button(self)
        self.saveButton['text'] = '保存'
        self.saveButton['command'] = self.__saveFile

        # ログ出力領域の定義
        self.outputLog = tk.Text(self, width=75, height=20)

        # 各オブジェクトの配置（Pack）
        # self.outputLog.pack()
        # self.saveButton.pack(fill=tk.X)
        # self.addButton.pack(fill=tk.X)

        # 各オブジェクトの配置（Grid）
        self.labelText.grid(row=0, column=0, sticky=tk.W)
        self.labelCounter.grid(row=0, column=1, sticky=tk.E)
        self.outputLog.grid(row=1, columnspan=2)  # 2列分の大きさ
        self.labelButton.grid(row=2, sticky=tk.W)
        self.addButton.grid(row=3, column=0, sticky='ew')  # 横幅を最大にする
        self.saveButton.grid(row=3, column=1, sticky='ew')  # 横幅を最大にする

        # self.outputLog = tk.Text(width=300, textvariable=self.entryText)
        # self.outputLog.pack()

    def __addTime(self):
        """時間を記録する
        """

        # datetimeを使って現在時間を取得（returnはdatetimeオブジェクト）
        tempTime = dt.now()

        # ログのインデックスをインクリメント
        self.logCounter += 1
        self.varLabel.set("現在の記録数：" + str(self.logCounter))

        # 時間をListに追加
        self.timeData.append([self.logCounter, tempTime])

        # テキストボックスの終端に、記録した時間を追記。
        self.outputLog.insert(tk.END, '{0:3}'.format(
            str(self.logCounter))+": " + str(tempTime)+"\n")

    def __saveFile(self):
        """ログをCSVファイルに保存する
        """

        # CSVファイルをWriteモードで開く
        with open(os.path.dirname(__file__)+'/test.csv', 'w', encoding='utf-8') as f:
            # CSVライブラリの
            csvFile = csv.writer(f, lineterminator='\n')

            # リストの情報を一括でファイルに書き込む
            csvFile.writerows(self.timeData)
        # withを抜けると、自動的にファイルがクローズされる。


def main():
    # Tkinterのルートインスタンスを作成
    root = tk.Tk()

    # タイトル、ウィンドウサイズを設定
    root.title('タイムスタンプツール')
    root.geometry('530x400')

    # 配置位置をルートに設定してアプリケーションインスタンスを作成
    app = Apprication(master=root)

    # アプリケーション実行
    app.mainloop()


# いつもの
if __name__ == "__main__":
    main()

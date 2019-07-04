# -*- coding=utf-8 -*-

import tkinter as tk
from datetime import datetime as dt
import csv
import os


class Apprication(tk.Frame):
    """Tkinterメインウィンドウ"""

    def __init__(self, master=None):
        """コンストラクタ

        Args:
            master (tkinter.root, optional): TkInterのルートを指定. Defaults to None.
        """
        super().__init__(master)
        self.timeData = []
        self.entryText = tk.StringVar()
        self.addButton = tk.Button()
        self.addButton['text'] = '時間を記録'
        self.addButton['command'] = self.__addTime
        self.addButton.pack()

        self.saveButton = tk.Button()
        self.saveButton['text'] = '保存'
        self.saveButton['command'] = self.__saveFile
        self.saveButton.pack()

        self.outputLog = tk.Text(width=300, textvariable=self.entryText)
        self.outputLog.pack()

    def __addTime(self):
        self.timeData.append(dt.now())
        print(self.timeData)

    def __saveFile(self):
        self.entryText.set(self.timeData)
        with open(os.path.dirname(__file__)+'/test.csv', 'w') as f:
            csvFile = csv.writer(f)
            csvFile.writerows(str(self.timeData))


def main():
    root = tk.Tk()
    root.title('タイムスタンプツール')
    root.geometry('500x300')
    app = Apprication(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()

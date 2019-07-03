# -*- coding=utf-8 -*-

import tkinter as tk
from datetime import datetime as dt

class Application(tk.Frame):
    """アプリケーションクラス
    
    Args:
        tk (Tkinter.Frame): Tkinter
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self._bt = TkButton(master)
        self._bt.setLabel("tetetetete")

    def create_widgets(self):
        self.recordTimeButton = tk.Button(self)
        self.recordTimeButton["text"] = "時間を記録"
        self.recordTimeButton.pack(side="top")

class TkButton(tk.Button):
    """docstring for tkButton."""
    def __init__(self, master=None):
        super().__init__(master)
        self._bt = tk.Button(master)
        self._createWidget()
    
    def _createWidget(self):
        self._bt['text'] = "クラステストボタン"
        self._bt.pack()
    
    def setLabel(labelName):
        """ラベルを設定する
        
        Args:
            labelName (String): ラベル名
        """
        self._bt['text'] = labelName


def main():
    pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Time stamp tool with Tk")
    root.geometry("500x300")
    app = Application(master=root)
    app.mainloop()

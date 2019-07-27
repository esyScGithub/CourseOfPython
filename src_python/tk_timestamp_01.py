# -*- coding=utf-8 -*-

import tkinter as tk


def main():
    # Tkinterのルートインスタンスを作成
    root = tk.Tk()

    # タイトル、ウィンドウサイズを設定
    root.title('ハローワールド')
    root.geometry('525x300')

    # 01
    label = tk.Label(root, text="Hello world.")
    label.pack()

    # 02
    button = tk.Button(root, text="ボタン")
    button.pack()

    # アプリケーション実行
    root.mainloop()


# いつもの
if __name__ == "__main__":
    main()

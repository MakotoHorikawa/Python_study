import tkinter as tk

# ウインドウの作成
window = tk.Tk()
# ウインドウのサイズ指定
window.geometry("500x200")
window.title("ファイル解析")

buttonA = tk.Button(
    window, text = 'ボタンA').pack()

buttonB = tk.Button(
    window, text = 'ボタンB').pack(side = tk.LEFT)
 
buttonC = tk.Button(
    window, text = 'ボタンC').pack(side = tk.RIGHT)

# ウインドウ状態の維持
window.mainloop()
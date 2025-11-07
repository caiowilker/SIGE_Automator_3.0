import ttkbootstrap as tb
from interface.app import App

if __name__ == "__main__":
    app_style = tb.Style(theme="flatly")
    root = app_style.master
    App(root)
    root.mainloop()

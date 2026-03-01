from tkinter import *

t = Tk()

def main():
    t.title("My First GUI")
    t.geometry("400x400")
    btn = Button(t, text="Get", command=get_info)
    txt = Text(t, height=20, width=100)
    lbl = Label(t, text="Nothing")
    btn.pack()
    txt.pack()
    lbl.pack()
    t.mainloop()

def get_info():
    txt = t.children['!text'].get("1.0",END).strip()
    t.children['!label'].configure(text=txt)


if __name__ == "__main__":
    main()

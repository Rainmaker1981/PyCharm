from tkinter import *
from tkinter import filedialog
import os

GEO = "900x600"
t = Tk()

def main():
    init()
    set_content(t)
    t.mainloop()


def set_content(t):
    button_frame, save_btn, open_btn, clear_btn = get_button_frame()
    text = get_textarea()
    key_frame, key_area, label = get_key_frame()
    grid_widgets(save_btn, open_btn, clear_btn, text, key_area, label)
    return t


def get_key_frame():
    key_frame = Frame(t)
    key_frame.pack(fill=X, side=BOTTOM)
    key_area = Text(key_frame, height=1)
    label = Label(key_frame, text="Enter Encryption Integer: ")
    key_frame.columnconfigure(0, weight=1)
    key_frame.columnconfigure(1, weight=1)
    return key_frame, key_area, label


def grid_widgets(save_btn, open_btn, clear_btn, text, key_area, label):
    save_btn.grid(row=0, column=0, sticky=W + E)
    open_btn.grid(row=0, column=1, sticky=W + E)
    clear_btn.grid(row=0, column=2, sticky=W + E)
    label.grid(row=0, column=0, sticky=W + E)
    key_area.grid(row=0, column=1, sticky=W + E)
    text.pack(side=TOP)


def get_button_frame():
    button_frame = Frame(t)
    button_frame.pack(fill=X, side=TOP)
    save_btn, open_btn, clear_btn = get_buttons(button_frame)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)
    return button_frame, save_btn, open_btn, clear_btn


def get_buttons(button_frame):
    save_btn = Button(button_frame, text="Save", command=save_file)
    open_btn = Button(button_frame, text="Open", command=open_file)
    clear_btn = Button(button_frame, text="Clear", command=clear)
    return save_btn, open_btn, clear_btn


def get_textarea():
    width, height = GEO.split("x")
    hlines = int(height) // 8
    wchars = int(width) // 8
    text = Text(t, height=hlines, width=wchars)
    return text


def init():
    t.title("CryptoPad - Mark Meyer")
    t.geometry(GEO)

# Callbacks
def save_file():
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save")
    if ".txt" not in filename:
        filename += ".txt"
    content = t.children['!text'].get("1.0", END)
    enc = encrypt(content)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(enc)

    t.children['!text'].insert("1.0", "Saved")
    t.after(400, clear)


def open_file():
    print("Open")
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open")
    content = ""
    t.children['!text'].delete("1.0", END)
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                content += line
        cleartext = decrypt(content)
    except BaseException as e:
        print("Error opening")
        cleartext = "Please choose a file."
    t.children['!text'].insert("1.0", cleartext)


def decrypt(cipher):
    key = str(t.children['!frame2'].children['!text'].get("1.0", END)).strip()
    output = ""
    if key == "":
        t.children['!text'].insert("1.0", "ENTER A KEY!")
    else:
        for char in cipher:
            s = chr(ord(char) - int(key))
            output += s
    return output


def encrypt(cleartext):
    key = str(t.children['!frame2'].children['!text'].get("1.0", END))
    output = ""
    for char in cleartext.strip():
        s = chr(ord(char) + int(key))
        output += s
        print(str(char) + " ---> " + str(s))
    t.children['!frame2'].children['!text'].delete("1.0", END)
    return output


def clear():
    print("Clear")
    t.children['!text'].delete("1.0", END)


if __name__ == '__main__':
    main()

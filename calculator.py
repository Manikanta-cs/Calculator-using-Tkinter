from tkinter import *

expr = ''


def numpressed(num):
    global expr
    expr += str(num)
    txt.set(expr)


def clear():
    global expr
    expr = ''
    txt.set(expr)


def result():
    global expr
    try:
        txt.set(eval(expr))

    except:
        txt.set('Error')
    finally:
        expr = ''


if __name__ == '__main__':
    m_window = Tk()
    m_window.geometry("250x400")
    m_window.title("Calculator")

    txt = StringVar()

    lbl = Label(m_window, font=('arial', 20), textvariable=txt)

    lbl.pack(expand=True, fill="both")

    btnrow1 = Frame(m_window)
    btnrow1.pack(expand=True, fill="both")

    btnrow2 = Frame(m_window)
    btnrow2.pack(expand=True, fill="both")

    btnrow3 = Frame(m_window)
    btnrow3.pack(expand=True, fill="both")

    btnrow4 = Frame(m_window)
    btnrow4.pack(expand=True, fill="both")

    btn = Button(btnrow1, text="1", font=("arial", 20), border=0,
                 command=lambda: numpressed(1))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow1, text="2", font=("arial", 20), border=0,
                 command=lambda: numpressed(2))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow1, text="3", font=("arial", 20), border=0,
                 command=lambda: numpressed(3))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow1, text="+", font=("arial", 20), border=0,
                 command=lambda: numpressed('+'))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow2, text="4", font=("arial", 20), border=0,
                 command=lambda: numpressed(4))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow2, text="5", font=("arial", 20), border=0,
                 command=lambda: numpressed(5))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow2, text="6", font=("arial", 20), border=0,
                 command=lambda: numpressed(6))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow2, text="-", font=("arial", 20), border=0,
                 command=lambda: numpressed('-'))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow3, text="7", font=("arial", 20), border=0,
                 command=lambda: numpressed(7))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow3, text="8", font=("arial", 20), border=0,
                 command=lambda: numpressed(8))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow3, text="9", font=("arial", 20), border=0,
                 command=lambda: numpressed(9))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow3, text="x", font=("arial", 20), border=0,
                 command=lambda: numpressed('*'))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow4, text="C", font=("arial", 20), border=0,
                 command=clear)
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow4, text="0", font=("arial", 20), border=0,
                 command=lambda: numpressed(0))
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow4, text="=", font=("arial", 20), border=0,
                 command=result)
    btn.pack(side=LEFT, expand=True, fill="both")

    btn = Button(btnrow4, text="/", font=("arial", 20), border=0,
                 command=lambda: numpressed('/'))
    btn.pack(side=LEFT, expand=True, fill="both")

    m_window.mainloop()

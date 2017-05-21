from tkinter import *


def cpy_from_rezult():
    input_form.delete('1.0', END)
    input_form.insert('1.0', output_form.get('1.0', END)[:-1])
    output_form.delete('1.0', END)


main_window = Tk()
main_window.title('Перевод числа в строку и обратно')
x = (main_window.winfo_screenwidth() - main_window.winfo_reqwidth()) / 2.5
y = (main_window.winfo_screenheight() - main_window.winfo_reqheight()) / 2.5
main_window.wm_geometry("+%d+%d" % (x, y))
main_window.geometry('550x200+%d+%d' % (x, y))
main_window.resizable(False, False)

main_frame = Frame(main_window)
main_frame.pack(fill=BOTH, pady=10)

row = Frame(main_frame)
Label(row, text='Число', bd=3, width=10).pack(side=LEFT)
input_form = Text(row, height=4, wrap=WORD)
input_form.pack(side=RIGHT, expand=YES, fill=X, padx=10)
input_form.focus()
row.pack(side=TOP, fill=X)

Button(main_frame, text='▲', width=20, font='Arial 5', command=(lambda: cpy_from_rezult())).pack()

row2 = Frame(main_frame)
Label(row2, text='Результат', bd=3, width=10).pack(side=LEFT)
output_form = Text(row2, height=4, wrap=WORD)
output_form.pack(side=RIGHT, expand=YES, fill=X, padx=10)
row2.pack(fill=X)

start_btn = Button(main_frame, text='Преобразовать')
start_btn.pack(pady=5)

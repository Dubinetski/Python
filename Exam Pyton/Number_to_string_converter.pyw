# Написать программу, которая переводит число в слово:
# (н-р: 1991 = одна тысяча девятьсот девяносто один
# 1,5 = одна целая пять десятых)
# и обратно (н-р: одна тысяча девятьсот девяносто один = 1991)
# Реализовать отдельными модулями.
# Проверять корректность введенных данных (исключения).

if __name__ == '__main__':
    from Form import *
    from num_to_str import convert_to_string
    from str_to_num import convert_to_number


    def convert():
        number = input_form.get('1.0', END)[:-1]
        output_form.delete('1.0', END)
        try:
            float(number)
            string = convert_to_string(number)
        except ValueError:
            string = convert_to_number(number)
            if string == 0 and not number == '':
                string = 'Incorrect format'
        output_form.insert('1.0', string)


    start_btn.config(command=(lambda: convert()))

    main_window.mainloop()

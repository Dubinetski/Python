# Задание: реализовать поиск файла и вывести его содержимое на экран

# Программа предлагает ввести начальный каталог для поиска файла
# и имя (несколько символов из имени) данного файла. Поиск осуществляется
# в выбранной папке и во всех вложенных в нее.
# После поиска выводится список найденных совпадений 
# и предлагается выбрать один для прочтения.
# Постарался учесть возможные ошибки пользовательского ввода и чтения файла.

import os

print("Program search and read the file.\n")
while True:
    findList = []
    folder = input("Entering the path of folder where need search the file\n"
                   "(empty string or . - search in folder with program and subfolders)\n")
    if folder == '':
        folder = '.'
    filter = input("Entering the name of file which you want to find: ")
    findFileCount = 0
    # Поиск файлов, в названии которых присутствует данная строка
    for (dirName, subList, fileList) in os.walk(folder):
        for fileName in fileList:
            if fileName.count(filter):
                findList.append(os.path.join(dirName, fileName))

    findFileCount = len(findList)
    if findFileCount > 0:
        print('\nFind the ' + str(findFileCount) + ' files\n' + '=' * 20)
        for i in range(0, findFileCount):
            print(str(i + 1) + ' ' + findList[i])
        print('\n')
        while True:
            try:
                fileOpen = int(input("Put the number of file which you want read: "))
                if fileOpen <= findFileCount and fileOpen >= 1:
                    break
            except ValueError or NameError:
                print("Incorrect number. Please entering a number from 1 to " + str(len(findList)))
                continue

            print("Incorrect number. Please entering a number from 1 to " + str(len(findList)))

        with open(findList[fileOpen - 1]) as file:
            print('\n' + '=' * len(findList[fileOpen - 1]) + '\n' + findList[fileOpen - 1] + '\n' + '=' * len(
                findList[fileOpen - 1]))
            try:
                for line in file:
                    print(line.strip())
            except UnicodeDecodeError:
                print("Can't decode this file.")
        print('\n')
    else:
        print("File is not find. Maybe you put incorrect path of folder or file name. Try again?")
    try:
        if int(input("\n0 - EXIT\n1 - Search another file\n")):
            continue
        else:
            break
    except ValueError:
        break

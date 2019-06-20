import os

def write_file(work_file, file_name, numPP):
    j = 1
    for i in work_file:
        if j < 3:
            j += 1
        else:
            list = []
            list.append(numPP)      #сквозной номер
            list.append(j - 2)      #номер внутри файла
            list.append(file_name)  #имя исходного файла
            k = i.split()
            for g in range(len(k)):
                if g > 0:
                    x = '{:.6f}'.format(float(k[g]))
                    print('Значения x, y, z: ', x)
                    list.append(x)
                else:
                    list.append(k[g])

            print('list', list)
            final_file.write(';'.join(str(j) for j in list))
            final_file.write('\n')
            print(numPP)
            numPP += 1
            j += 1

    work_file.close()   #закрытие рабочего файла с исходными значениями
    return numPP

group = int(input('Введите номер группы файлов: '))          #номер группы файлов
path_name = str(input('Введите имя папки с исходными файлами: '))
print(path_name)

numPP = group * 10000 + 1          #сквозной номер, уникальный ID

files = [f for f in os.listdir(path_name) if f.endswith('.xyz')] #общий список рабочих файлов
os.chdir(path_name)  #переходим в папку с исходными файлами
print('путь', os.getcwd())

final_file = open(path_name + "_all.csv", "w")    #открываем файл для записи итогов

for i in range(len(files)):
    print('имя файла', i + 1, files[i]) #рабочий файл

    file = files[i]
    file_name = str(group) + file[:(len(file) - 4)]
    work_file = open(file)
    numPP = write_file(work_file, file_name, numPP)

final_file.close()  #закрытие итогового файла

input('Для выхода нажмите "Enter"')

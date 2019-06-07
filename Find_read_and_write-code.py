import os

def write_file(work_file, file_name, numPP):
    j = 1
    for i in work_file:
        if j < 3:
            j += 1
        else:
            list = []
            list.append(numPP)
            list.append(j - 2)
            list.append(file_name)
            k = i.split()
            for g in range(len(k)):
                if g > 0:
                    x = '{:.6f}'.format(float(k[g]))
                    print('Значения: ', x)
                    list.append(x)
                else:
                    list.append(k[g])

            print('list', list)
            final_file.write(';'.join(str(j) for j in list))
            final_file.write('\n')
            print(numPP)
            numPP += 1
            j += 1

    work_file.close()   #закрытие рабочего файла
    return numPP

final_file = open(r"Structures\structures_all.txt", "w")
numPP = 1

files = [f for f in os.listdir('Structures') if f.endswith('.xyz')] #общий список рабочих файлов

for i in range(len(files)):
    print('имя файла', i + 1, files[i]) #рабочий файл

    os.chdir(r"D:\tmp\projects\Structures")  #переходим в папку с исходными файлами
    print('путь', os.getcwd())

    file = files[i]
    file_name = file[:(len(file) - 4)]
    work_file = open(file)
    numPP = write_file(work_file, file_name, numPP)

final_file.close()  #закрытие итогового файла

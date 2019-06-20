# Find_read_and_write
Моя практика на Python

*****
In the folder with the source files, all files with the extension .xyz are searched for, 
all lines are copied from each file and written into the final file. 
The resulting file is named as the source folder name + _all.csv. 
For example, the user enters the name of the folder with the source files - Structures, 
then the resulting file will be called: Structures_all.csv.

- in each file the first and second lines are skipped
- columns are added to the final file:
a) pass-through number in order (unique ID within the result file, which is formed using the file group number entered by the user)
b) number in order for each specific file
c) file name (up to a point)
d) atom number (1 2 3 ..)
d) further recorded columns with information taken from the working file
- separator - one semicolon ";" as in csv format
accuracy - 6 decimal places.

*****
В папке с исходными файлами ищутся все файлы с расширением .xyz, 
из каждого файла копируются все строки и записываются в итоговый файл. 
Итоговый файл именуется, как имя папки с исходными файлами + _all.csv. 
Например, пользователь вводит имя папки с исходными файлами - Structures, 
тогда итоговый файл будет называться: Structures_all.csv.

- в каждом файле пропускается первая и вторая строки
- в итоговый файл добавляются столбцы: 
а) сквозной номер по порядку (уникальный ID в рамках итогового файла, формирующийся с помощью вводимого пользователем номера группы файлов) 
б) номер по порядку для каждого конкретного файла 
в) имя файла (до точки) 
г) номер атома (1 2 3 ..) 
д) дальше записываются столбцы с информацией, взятой из рабочего файла
- разделитель - одна точка с запятой ";" как в формате csv
точность - 6 знаков после запятой.

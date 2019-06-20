# Find_read_and_write
Моя практика на Python

*****
In the folder with the source files, we are looking for everything with the extension .xyz, 
from each file all the lines are copied and recorded in the final file. 
The resulting file is named as the source folder name + _all.csv. 
For example, the user entered "the name of the folder with the source files" - Structures, 
then the resulting file will be called: Structures_all.csv.

- in each file the first and second lines are skipped
- columns are added to the final file:
a) pass-through number in order (unique ID within the result file, which is formed using 
the file group number entered by the user)
b) number in order for each specific file
c) file name (to the full stop)
d) atom number (1 2 3 ..)
e) further there are columns with information taken from the working file
- separator - one semicolon ";" as in csv format
- accuracy - 6 decimal places.

*****
В папке с исходными файлами ищем все с расширением .xyz, 
из каждого файла копируются все строки и записываются в итоговый файл. 
Итоговый файл именуется, как имя папки с исходными файлами + _all.csv. 
Например, пользователь ввёл "имя папки с исходными файлами" - Structures, 
тогда итоговый файл будет называться: Structures_all.csv.

- в каждом файле пропускается первая и вторая строки
- в итоговый файл добавляются столбцы: 
а) сквозной номер по порядку (уникальный ID в рамках итогового файла, 
формирующийся с помощью вводимого пользователем номера группы файлов) 
б) номер по порядку для каждого конкретного файла
в) имя файла (до точки) 
г) номер атома (1 2 3 ..)
д) дальше идут столбцы с информацией, взятой из рабочего файла
- разделитель - одна точка с запятой ";" как в формате csv
- точность - 6 знаков после запятой.

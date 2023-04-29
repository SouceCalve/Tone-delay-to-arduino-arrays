ENG:
This little utility converts midi files into Arduino-readable arrays via an intermediate step with the tonal delay list from https://extramaster.net/tools/midiToArduino/.
Necessary:
python >= 3.10.10
Installation:
Just clone the repository and run)
Usage:
python3 conv.py
And get into mode:

1) Input file:
It will ask you to enter the path to the file and remember the arrays for output to the file.
Be sure to remove everything except structures
tone(tonePin, 659, 83.25);
delay(92.5);

2) Output to a file.
Outputs arrays to a file in the format:
1st array: Notes
2nd array: Note duration
3rd array: Length of pause between notes.
Be sure to point to an existing file, otherwise it will result in an error!

3) Exit.


RUS:
Эта небольшая утилита преобразует midi-файлы в массивы, читаемые Arduino, посредством промежуточного шага со списком тональной задержки из https://extramaster.net/tools/midiToArduino/.
Необходимый:
python >= 3.10.10
Установка:
Просто клонируй репозиторий и запускай)
Использование:
python3 conv.py

И выберите режим:
1) Входной файл:
Попросит ввести путь до файла и запомнит массивы для вывода в файл.
Обязательно уберите всё, кроме конструкций
tone(tonePin, 659, 83.25);
delay(92.5);

  2.Вывод в файл.
  Выводит массивы в файл в формате:
  1-й массив:Ноты
  2-й массив:Длительность ноты
  3-й массив: Длительность паузы между нотами.
  Обязательно указывайте на существующий файл, иначе это приведёт к ошибке!

  3.Выход.

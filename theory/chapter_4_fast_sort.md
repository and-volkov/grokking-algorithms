## Глава 4. Теория
### Быстрый поиск

* Базовые случаи: пустой массив или массив из одного элемента
* Массив делится на 3 части: 
  1) подмассив элементов меньше опорного  
  2) опорный элемент
  3) подмассив элементов больше опорного
* Далее к подмассивам рекурсивно применяется быстрая сортировка

```Шпаргалка```
* Стратегия резделяй и властвуй основана на разбиении задачи на уменьшающиеся фрагменты.
На примере списка базовый случай - пустой массив или массив из 1 элемента
* Выбирать случайный элемент для быстрой сортировки.
Среднее время выполнения - O(n log n)
* Константы в О-большом иногда могут иметь значение. 
Поэтому быстрая сортировка быстрее сортировки слиянием

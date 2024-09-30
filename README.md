# task_cli

## Описание

CLI приложение, которое:

1. Получает на вход N строк.
2. Определяет, является ли строка сыллкой.
3. Если срока не ссылка, выводит уведомление.
4. Если строка ссылка, проверяет доступные HTTP методы и сохраняет коды ответов.
5. Результат представлен в виде словаря с информацией и доспутных методах

## Стек

- Python
- Asyncio
- Poetry 
- Pytest,
- Coverage



## Покрытие тестов

| Файл                | Строки | Пропущено | Покрытие | Пропущенные строки |
|---------------------|--------|-----------|----------|---------------------|
| const.py            | 1      | 0         | 100%     | -                   |
| main.py             | 38     | 4         | 89%      | 26, 44, 49-50        |
| tests\__init__.py   | 0      | 0         | 100%     | -                   |
| tests\test_cli.py   | 39     | 0         | 100%     | -                   |

**Общее покрытие: 95%**

## Время выполнения задания 6 часов

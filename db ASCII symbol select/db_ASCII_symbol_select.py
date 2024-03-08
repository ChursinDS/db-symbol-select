import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port="")

# Создание объекта курсора
cur = conn.cursor()

# Получение имени таблицы от пользователя
table_name = input("Введите имя таблицы для анализа: ")

# Получение символа для поиска от пользователя
search_char = input("Введите символ для поиска в таблице: ")

# Получение списка колонок таблицы
cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
columns = [row[0] for row in cur.fetchall()]

# Формирование запроса для поиска символа в каждой колонке таблицы
query = f"SELECT * FROM {table_name} WHERE "

for col in columns:
    query += f"CAST({col} AS TEXT) LIKE '%{search_char}%' OR "

# Удаление последнего оператора OR
query = query[:-4]

# Выполнение запроса
cur.execute(query)
rows = cur.fetchall()

# Вывод результатов
if len(rows) == 0:
    print("Нет результатов для заданного символа.")
else:
    for row in rows:
        print(row)

# Закрытие соединения
cur.close()
conn.close()

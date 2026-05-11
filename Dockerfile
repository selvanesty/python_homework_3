# Використовуємо офіційний образ Python
FROM python:3.10-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файл з залежностями
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо сам скрипт
COPY main.py .

# Вказуємо команду яка виконається при старті контейнера
CMD ["python", "main.py"]
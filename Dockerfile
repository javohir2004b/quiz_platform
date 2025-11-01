# Rasmiy Python imiji
FROM python:3.12-slim

# Ishchi papka
WORKDIR /app

# Tizim yangilash va psycopg2 uchun kerakli kutubxonalar
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean

# Fayllarni konteynerga nusxalash
COPY requirements.txt .

# Kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani konteynerga nusxalash
COPY . .

# Django serverni ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

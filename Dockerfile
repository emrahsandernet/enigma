# Temel Python imajını kullan
FROM python:3.10-slim

# Çalışma dizinini oluştur ve ayarla
WORKDIR /app

# Bağımlılık dosyalarını ekle ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

# Django sunucusunu başlat
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

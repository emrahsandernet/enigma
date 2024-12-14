# Base image olarak resmi Python 3.11 imajını kullanıyoruz
FROM python:3.11-slim-buster

# GDAL bağımlılıklarını yükle




# Çalışma dizini oluşturma
WORKDIR /app

# Gereksinimlerin kopyalanması ve kurulumu
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarının kopyalanması
COPY . /app/



# Gerekli ortam değişkenlerinin ayarlanması
ENV PYTHONUNBUFFERED 1

# Uygulamanın çalıştırılması
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

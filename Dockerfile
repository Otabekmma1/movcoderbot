# Python versiyasini tanlang
FROM python:3.12

# Ish joyini belgilash
WORKDIR /app

# Talablar faylini nusxalash
COPY requirements.txt .

# Talablarni o'rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Kodni nusxalash
COPY . .

# Portni ochish
EXPOSE 8443

# Dastur ishga tushirish
CMD ["python", "bot.py"]  # 'bot.py' faylini ishga tushiring

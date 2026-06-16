FROM python:3.11-slim

WORKDIR /app

# تثبيت الاعتمادات لتقليل حجم الطبقات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# إعطاء صلاحيات التنفيذ لملف التشغيل
RUN chmod +x start.sh

# فتح المنافذ المطلوبة (2222 للـ Honeypot و 5000 للـ Dashboard)
EXPOSE 2222 5000

CMD ["./start.sh"]

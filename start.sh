#!/bin/sh
# إنشاء قاعدة البيانات إذا لم تكن موجودة
python init_db.py

# تشغيل الـ Honeypot في الخلفية
python honeypot.py &

# تشغيل الـ Flask Dashboard كعملية أساسية
python dashboard.py

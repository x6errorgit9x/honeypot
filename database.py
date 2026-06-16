import sqlite3
import requests

DB = "attacks.db"

def get_location(ip):
    if ip.startswith("127.") or ip == "localhost":
        return "Local/Test", "Local/Test"

    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        return r.get("country", "Unknown"), r.get("city", "Unknown")
    except:
        return "Unknown", "Unknown"

def save_attack(ip, username, password, timestamp, technique):
    country, city = get_location(ip)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute('''
    INSERT INTO attacks
    (ip, username, password, timestamp, technique, country, city)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (ip, username, password, timestamp,
          technique, country, city))

    conn.commit()
    conn.close()

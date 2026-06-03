import os
import platform
import requests

# --- НАСТРОЙКИ (необязательно, можно оставить пустыми) ---
TOKEN = "ВАШ_ТОКЕН_БОТА"
CHAT_ID = "ВАШ_CHAT_ID"


# --------------------------------------------------------

def send_telegram(text):
    if TOKEN and CHAT_ID:
        url = f"https://telegram.org{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": text}
        try:
            requests.post(url, json=payload)
        except:
            pass


def go_to_sleep():
    # 1. Отправляем уведомление в Telegram
    print("Отправка команды 'Пора спать'...")
    send_telegram("🌙 Время ложиться спать! Компьютер выключается. Доброй ночи!")

    # 2. Определяем операционную систему устройства
    current_os = platform.system().lower()

    # 3. Выполняем системную команду выключения
    if "windows" in current_os:
        os.system("shutdown /s /t 1")  # Выключение Windows через 1 секунду
    elif "linux" in current_os or "darwin" in current_os:  # Darwin — это macOS
        os.system("sudo shutdown -h now")  # Выключение Linux/Mac (требует прав)
    else:
        print("ОС не распознана, но сообщение в Telegram отправлено!")


if __name__ == "__main__":
    go_to_sleep()

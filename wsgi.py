# Импортируем app с нашими представлениями из файла app.py
from app import app

# Запуск нашего приложения
if __name__ == "__main__":
    app.run(debug=True)

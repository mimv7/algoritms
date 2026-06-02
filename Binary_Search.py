import os
from googleapiclient.discovery import build


class Terminator:
    # Переменная класса (общая для всех моделей)
    manufacturer = "Cyberdyne Systems"

    def __init__(self, model: str, series: int):
        """Инициализация нового Терминатора"""
        self.model = model  # Модель (например, 'T-800')
        self.series = series  # Серия (например, 101)
        self.hp = 100  # Очки здоровья (%)
        self._is_active = True  # Статус работы системы

        # Ключи для Google API (подтягиваются из переменных окружения вашего ПК)
        self.google_api_key = os.getenv("GOOGLE_API_KEY", "ВАШ_API_KEY")
        self.google_cx = os.getenv("GOOGLE_CX", "ВАШ_ID_ПОИСКОВОЙ_СИСТЕМЫ")

    def introduce(self) -> str:
        """Метод приветствия и самоидентификации"""
        return f"Я Терминатор модели {self.model}, серия {self.series}. Производитель: {self.manufacturer}."

    def take_damage(self, damage: int):
        """Метод обработки полученного урона"""
        if not self._is_active:
            print(f"[{self.model}] Система полностью отключена. Урон не может быть получен.")
            return

        self.hp -= damage
        print(f"[{self.model}] Внимание! Получено {damage}% урона. Текущая прочность брони: {self.hp}%")

        if self.hp <= 0:
            self._is_active = False
            print(f"[{self.model}] Критическая ошибка ядра. Система деактивирована. I'll be back.")

    def web_search_target(self, query: str) -> list:
        """Метод глобального поиска информации через Google Custom Search API"""
        if not self._is_active:
            print(f"[{self.model}] Ошибка: Модуль связи недоступен. Робот отключен.")
            return []

        print(f"\n[CONNECTING TO CYBERNET] Подключение к спутниковой сети... Запрос: '{query}'")

        # Простая проверка на дефолтные значения ключей
        if self.google_api_key == "ВАШ_API_KEY" or self.google_cx == "ВАШ_ID_ПОИСКОВОЙ_СИСТЕМЫ":
            print("[SYSTEM WARNING] Поиск невозможен: не указаны реальные Google API Key и CX ID.")
            print("[MOCK DATA] Имитация ответа SkyNet: Найдена цель 'Джон Коннор'. Локация: Лос-Анджелес.")
            return [{"title": "Имитация: Цель найдена", "link": "https://skynet.targets"}]

        try:
            # Создаем и запускаем клиент API
            service = build("customsearch", "v1", developerKey=self.google_api_key)
            result = service.cse().list(q=query, cx=self.google_cx).execute()

            # Извлекаем топ-3 результата
            search_items = result.get("items", [])
            extracted_data = []

            for item in search_items[:3]:
                extracted_data.append({
                    "title": item.get("title"),
                    "link": item.get("link")
                })
            return extracted_data

        except Exception as e:
            print(f"[CONNECTION ERROR] Не удалось связаться с серверами Google: {e}")
            return []


# ==========================================
# БЛОК ДЕМОНСТРАЦИИ (Запускается только напрямую)
# ==========================================
if __name__ == "__main__":
    print("--- Инициализация системы ---")
    # 1. Создаем объект легендарного Т-800
    t800 = Terminator(model="T-800", series=101)

    # 2. Робот представляется
    print(t800.introduce())

    # 3. Робот ищет информацию о цели в интернете
    search_results = t800.web_search_target("Джон Коннор")
    print(f"Результаты сканирования сети ({len(search_results)} шт.):")
    for res in search_results:
        print(f" -> {res['title']} | Ссылка: {res['link']}")

    print("\n--- Симуляция боевого столкновения ---")
    # 4. Робот получает повреждения в бою
    t800.take_damage(35)
    t800.take_damage(75)  # Суммарный урон > 100, робот должен отключиться

    # 5. Проверяем, может ли отключенный робот искать в сети
    t800.web_search_target("Сара Коннор")

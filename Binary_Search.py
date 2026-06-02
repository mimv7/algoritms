class Terminator:
    # Переменная класса (общая для всех терминаторов)
    manufacturer = "Cyberdyne Systems"

    def __init__(self, model: str, series: int):
        self.model = model  # Модель (например, 'T-800')
        self.series = series  # Серия (например, 101)
        self.hp = 100  # Очки здоровья
        self._is_active = True  # Статус (включен/выключен)

    def introduce(self) -> str:
        """Метод представления робота"""
        return f"Я Терминатор модели {self.model}, серия {self.series}. Производитель: {self.manufacturer}."

    def take_damage(self, damage: int):
        """Метод получения урона"""
        if not self._is_active:
            print(f"{self.model} уже деактивирован.")
            return

        self.hp -= damage
        print(f"{self.model} получил {damage} урона. Оставшаяся прочность: {self.hp}%")

        if self.hp <= 0:
            self._is_active = False
            print(f"Критическое повреждение. {self.model} уничтожен. I'll be back.")

    def scan_target(self, target_name: str) -> str:
        """Метод сканирования цели"""
        return f"[SCANNING] Поиск цели '{target_name}'... Цель обнаружена. Статус: Ликвидировать."

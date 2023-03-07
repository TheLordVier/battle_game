# Импортируем dataclass из библиотеки dataclasses
from dataclasses import dataclass
# Импортируем умения из файла skills.py
from skills import FuryPunch, HardShot, Skill


# Создаём базовый dataclass с показателями для персонажа
@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


# Инициализируем экземпляр класса WarriorClass и присваиваем ему необходимые значения аттрибутов
WarriorClass = UnitClass(
    name="Воин",
    max_health=60,
    max_stamina=30,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch()
)

# Инициализируем экземпляр класса ThiefClass и присваиваем ему необходимые значения аттрибутов
ThiefClass = UnitClass(
    name="Вор",
    max_health=50,
    max_stamina=25,
    attack=1.5,
    stamina=1.2,
    armor=1,
    skill=HardShot()
)

# Создаём словарь с нашими персонажами
unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}

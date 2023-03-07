# Импортируем стандартный модуль JSON
import json
# Импортируем стандартный модуль dataclass из стандартной библиотеки marshmallow_dataclass
from dataclasses import dataclass
# Импортируем функцию uniform из стандартной библиотеки random
from random import uniform
# Импортируем тип Optional из стандартной библиотеки typing
from typing import Optional
# Импортируем стандартную библиотеку marshmallow_dataclass
import marshmallow_dataclass


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    max_damage: float
    min_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    """
    Класс со списком оружия и брони
    """
    weapons: list[Weapon]
    armors: list[Armor]


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Optional[Weapon]:
        """
        Метод возврата объекта оружия по имени
        """
        for weapon in self.equipment.weapons:
            if weapon.name == weapon_name:
                return weapon
        return None

    def get_armor(self, armor_name) -> Optional[Armor]:
        """
        Метод возврата объекта брони по имени
        """
        for armor in self.equipment.armors:
            if armor.name == armor_name:
                return armor
        return None

    def get_weapons_names(self) -> list:
        """
        Метод возврата списка оружия
        """
        return [
            weapon.name for weapon in self.equipment.weapons
        ]

    def get_armors_names(self) -> list:
        """
        Метод возврата списка брони
        """
        return [
            armor.name for armor in self.equipment.armors
        ]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """
        Метод открытия json файла и загрузки json в переменную EquipmentData
        """
        with open("./data/equipment.json", "r", encoding='utf=8') as file:
            data = json.load(file)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
            return equipment_schema().load(data)

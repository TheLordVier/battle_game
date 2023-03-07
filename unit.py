# Импортируем annotations в наш модуль skills.py
from __future__ import annotations
# Импортируем тип ABC и abstractmethod из стандартной библиотеки abc для создания абстрактных классов и методов
from abc import ABC, abstractmethod
# Импортируем модуль генерации случайного числа-randint из стандартной библиотеки random
from random import randint
# Импортируем базовый dataclass Unitclass из файла classes.py
from classes import UnitClass
# Импортируем dataclass Armor и Weapon из файла equipment.py
from equipment import Armor, Weapon


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """

    def __init__(self, name: str, unit_class: UnitClass):
        """
        При инициализации класса Unit используем свойства класса UnitClass
        """
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = None
        self.armor = None
        self.is_skill_used = False

    @property
    def health_points(self):
        """
        Метод здоровья (hp)
        """
        return round(self.hp, 1)

    @property
    def stamina_points(self):
        """
        Метод выносливости (stamina)
        """
        return round(self.stamina, 1)

    def equip_weapon(self, weapon: Weapon):
        """
        Метод присваивания персонажу оружия
        """
        self.weapon = weapon

    def equip_armor(self, armor: Armor):
        """
        Метод присваивания персонажу брони
        """
        self.armor = armor

    def _count_damage(self, target: BaseUnit) -> int:
        """
        Метод расчёта урона игрока и расчёта брони цели
        """
        self.stamina -= self.weapon.stamina_per_hit
        damage = self.weapon.damage * self.unit_class.attack

        if target.stamina >= target.armor.stamina_per_turn * target.unit_class.stamina:
            target.stamina -= target.armor.stamina_per_turn * target.unit_class.stamina
            damage -= target.armor.defence * target.unit_class.armor

        damage = round(damage, 1)
        target.get_damage(damage)
        return damage

    def get_damage(self, damage: int):
        """
        Метод получения урона
        """
        if damage > 0:
            self.hp -= damage
            if self.hp < 0:
                self.hp = 0

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        Метод использования умения.
        """
        if self.is_skill_used:
            return "Навык уже был использован"

        result = self.unit_class.skill.use(self, target)
        self.is_skill_used = True
        return result


class PlayerUnit(BaseUnit):
    """
    Класс игрока
    """

    def hit(self, target: BaseUnit) -> str:
        """
        Метод удар игрока
        """
        if self.stamina < self.weapon.stamina_per_hit:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."

        damage = self._count_damage(target)
        if damage > 0:
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
        return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."


class EnemyUnit(BaseUnit):
    """
    Класс противника
    """

    def hit(self, target: BaseUnit) -> str:
        """
        Метод удар соперника
        """
        if not self.is_skill_used and self.stamina >= self.unit_class.skill.stamina and randint(0, 100) < 10:
            return self.use_skill(target)

        if self.stamina < self.weapon.stamina_per_hit:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."

        damage = self._count_damage(target)
        if damage > 0:
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона."
        return f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает."

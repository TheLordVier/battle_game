# Импортируем annotations в наш модуль skills.py
from __future__ import annotations
# Импортируем тип ABC и abstractmethod из стандартной библиотеки abc для создания абстрактных классов и методов
from abc import ABC, abstractmethod


class Skill(ABC):
    """
    Базовый класс умения
    """

    def __init__(self):
        self.user = None
        self.target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self):
        return self.user.stamina >= self.stamina

    def use(self, user, target) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class FuryPunch(Skill):
    """
    Класс умения 'Свирепый пинок' и эффект от его использования
    """
    name = "Свирепый пинок"
    stamina = 6
    damage = 12

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."


class HardShot(Skill):
    """
    Класс умения 'Мощный укол' и эффект от его использования
    """
    name = "Мощный укол"
    stamina = 5
    damage = 15

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage
        return f"{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику."

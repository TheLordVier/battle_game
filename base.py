# Импортируем базовый класс BaseUnit из файла unit.py
from unit import BaseUnit


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Arena(metaclass=BaseSingleton):
    STAMINA_PER_ROUND = 1
    player = None
    enemy = None
    game_is_running = False
    battle_result = None

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        """
        Метод начала игры с атрибутами "игрок", "противник" и "началась ли игра"
        """
        self.player = player
        self.enemy = enemy
        self.game_is_running = True

    def _check_players_hp(self):
        """
        Метод проверки здоровья (hp) "игрока" и "противника"
        """
        if self.player.hp > 0 and self.enemy.hp > 0:
            return None

        if self.player.hp <= 0 and self.enemy.hp <= 0:
            self.battle_result = "Ничья"
        elif self.player.hp <= 0:
            self.battle_result = "Противник победил"
        else:
            self.battle_result = "Игрок победил"

        return self._end_game()

    def _stamina_regeneration(self):
        """
        Метод проверки регенерации выносливости (stamina) за ход для "игрока" и "противника"
        """
        units = (self.player, self.enemy)

        for unit in units:
            if unit.stamina + self.STAMINA_PER_ROUND > unit.unit_class.max_stamina:
                unit.stamina = unit.unit_class.max_stamina
            else:
                unit.stamina += self.STAMINA_PER_ROUND

    def next_turn(self):
        """
        Метод следующего хода для "игрока" при пропуске хода или нанесении удара
        """
        result = self._check_players_hp()
        if result is not None:
            return result
        if self.game_is_running:
            self._stamina_regeneration()
            return self.enemy.hit(self.player)

    def _end_game(self):
        """
        Метод завершения игры и возврата результата битвы
        """
        self._instances = {}
        self.game_is_running = False
        return self.battle_result

    def player_hit(self):
        """
        Метод удара "игрока" и возврата результата удара
        """
        # TODO КНОПКА УДАР ИГРОКА -> return result: str
        # TODO получаем результат от функции self.player.hit
        # TODO запускаем следующий ход
        # TODO возвращаем результат удара строкой
        result = self.player.hit(self.enemy)
        turn_result = self.next_turn()
        return f"{result}<br>{turn_result}"

    def player_use_skill(self):
        """
        Метод использования умения "игроком" и возврата результата умения
        """
        result = self.player.use_skill(self.enemy)
        turn_result = self.next_turn()
        return f"{result}<br>{turn_result}"

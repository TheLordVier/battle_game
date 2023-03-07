# Импортируем фреймворк Flask и его функции
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
# Импортируем Арену из файла base.py
from base import Arena
# Импортируем Экипировку из файла equipment.py
from equipment import Equipment
# Импортируем классы наших персонажей из файла classes.py
from classes import unit_classes
# Импортируем PlayerUnit и EnemyUnit из файла unit.py
from unit import PlayerUnit, EnemyUnit

# Инициализируем Flask приложение
app = Flask(__name__)

# Создаём словарь для хранения выбранного героя и противника
heroes = {
    "player": ...,
    "enemy": ...,
}

# Инициализируем класс арены
arena = Arena()


@app.route("/")
def menu_page():
    """
    Представление (view) главного меню (шаблон index.html)
    """
    return render_template("index.html")


@app.route("/fight/")
def start_fight():
    """
    Представление (view) экрана боя (шаблон fight.html)
    """
    arena.start_game(player=heroes["player"], enemy=heroes["enemy"])
    return render_template("fight.html", heroes=heroes)


@app.route("/fight/hit")
def hit():
    """
    Представление (view) обновления экрана боя и нанесения удара (шаблон fight.html)
    """
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.battle_result

    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/use-skill")
def use_skill():
    """
    Представление (view) обновления экрана боя и использования умения персонажа (шаблон fight.html)
    """
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.battle_result

    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/pass-turn")
def pass_turn():
    """
    Представление (view) пропуска хода (шаблон fight.html)
    """
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.battle_result

    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/end-fight")
def end_fight():
    """
    Представление (view) завершения игры и перехода в главное меню (шаблон index.html)
    """
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['POST', 'GET'])
def choose_hero():
    """
    Представление (view) выбора героя и редиректа на эндпоинт choose enemy
    """
    if request.method == "GET":
        header = "Выберите героя"
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        result = {
            "header": header,
            "weapons": weapons,
            "armors": armors,
            "classes": unit_classes,
        }
        return render_template("hero_choosing.html", result=result)
    if request.method == "POST":
        name = request.form["name"]
        weapon_name = request.form["weapon"]
        armor_name = request.form["armor"]
        unit_class_name = request.form["unit_class"]

        player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class_name))

        player.equip_armor(Equipment().get_armor(armor_name))
        player.equip_weapon(Equipment().get_weapon(weapon_name))

        heroes["player"] = player
        return redirect(url_for("choose_enemy"))


@app.route("/choose-enemy/", methods=['POST', 'GET'])
def choose_enemy():
    """
    Представление (view) выбора противника и редиректа на начало битвы
    """
    if request.method == "GET":
        header = "Выберите противника"
        equipment = Equipment()
        weapons = equipment.get_weapons_names()
        armors = equipment.get_armors_names()
        result = {
            "header": header,
            "weapons": weapons,
            "armors": armors,
            "classes": unit_classes,
        }
        return render_template("hero_choosing.html", result=result)
    if request.method == "POST":
        name = request.form["name"]
        weapon_name = request.form["weapon"]
        armor_name = request.form["armor"]
        unit_class_name = request.form["unit_class"]

        enemy = EnemyUnit(name=name, unit_class=unit_classes.get(unit_class_name))

        enemy.equip_armor(Equipment().get_armor(armor_name))
        enemy.equip_weapon(Equipment().get_weapon(weapon_name))

        heroes["enemy"] = enemy
        return redirect(url_for("start_fight"))


if __name__ == "__main__":
    app.run(debug=True)

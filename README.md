## Battle game (a small game with a web interface about the battle of heroes in the style of old-school browser games)

Project developed by: Mikhailov Alexander

## Application structure:

**app.py** - *основное приложением с представлениями (views)*

**base.py** - *файл с классом Arena для нашего приложения*

**classes.py** - *файл с классами наших персонажей и их характеристиками*

**equipment.py** - *файл с оружием и броней и их показателями*

**skills.py** - *файл с умениями наших персонажей*

**unit.py** - *файл c основной логикой приложения (базовым классом, классом игрока и классом противника)*

**wsgi.py** - *файл для развёртывания приложения*

**requirements.txt** - *зависимости приложения*

**.gitignore** - *файлы и папки для игнорирования в системе контроля версий Git*


- **Директория data** - *Директория с исходными данными приложения*
    - **equipment.json** - *JSON-файл с данными по оружию и броне* <br>

- **Директория templates** - *Директория с шаблонами приложения (HTML)*
    - **fight.html** - *Шаблон меню арены приложения (HTML)* <br>
    - **here_choosing.html** - *Шаблон меню выбора персонажей (HTML)* <br>
    - **index.html** - *Шаблон главного меню приложения (HTML)* <br>
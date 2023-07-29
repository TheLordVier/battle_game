## Battle game (a small game with a web interface about the battle of heroes in the style of old-school browser games)

Project developed by: Mikhailov Alexander

## Application structure:

**app.py** - *main application with views*

**base.py** - *arena class file for our application*

**classes.py** - *a file with our character classes and their characteristics*

**equipment.py** - *file with weapons and armor and their performance*

**skills.py** - *file with the skills of our characters*

**unit.py** - *file with the main application logic (base class, player class and enemy class)*

**wsgi.py** - *application deployment file*

**requirements.txt** - *application dependencies*

**.gitignore** - *files and folders to ignore in Git version control*


- **Directory data** - *Directory with application source data*
    - **equipment.json** - *JSON file with weapon and armor data* <br>

- **Directory templates** - *Directory with application templates (HTML)*
    - **fight.html** - *App arena menu template (HTML)* <br>
    - **hero_choosing.html** - *Character selection menu template (HTML)* <br>
    - **index.html** - *Application main menu template (HTML)* <br>
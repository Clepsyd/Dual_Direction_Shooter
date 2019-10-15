# Dual_Direction_Shooter
### A very short firefighter game with squares and circles, made with pygame.
---

This is one of my first projects on pygame that sort of does something midly interesting.
You're a square firefighter and fires appear randomly on the screen. You need to put them out.

### **How to install and run:**

**I used python 3.7 and pygame 1.9.4.**

* Install python 3.7 => https://www.python.org/
* Install pipenv => https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv
* Install dependencies (pygame): `pipenv install`
* Activate virtual environment: `pipenv shell`
* Run the game through pipenv: `pipenv run python3 main.py`

### * How to play:

* Use WASD keys to move and the arrow keys to use your hose on the fires
* Put out as many fires as you can. The game is over when:
  - You run out of water
  - There's more than 3 fire sources.

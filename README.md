# Asteroids Game

A classic Asteroids-style arcade game built with Python and Pygame. Fly your ship, destroy asteroids, and avoid collisions!

## Features

### Core Gameplay
- **Ship controls** – Rotate with A/D, move forward/back with W/S, shoot with SPACE
- **Screen wrapping** – Player, asteroids, and shots wrap around screen edges
- **Asteroid splitting** – Large asteroids split into medium, medium into small; smaller asteroids move faster
- **Collision detection** – Circle-based hit detection for all game objects

### Upgrades & Polish
- **Scoring system** – 100 pts (large), 50 pts (medium), 25 pts (small)
- **Lives & respawning** – 3 lives with 2 seconds of invincibility after respawn
- **Main menu** – Start screen with Play and Quit options
- **Pause menu** – Press P or ESC to pause/resume
- **Game over screen** – Final score, high score, restart option
- **High score persistence** – Saves best score to `highscore.json`
- **Explosion effects** – Particle bursts when asteroids are destroyed
- **Starfield background** – Animated starfield for atmosphere
- **Thrust effect** – Flame visible when accelerating with W
- **Shot lifetime** – Bullets expire after 2 seconds to limit clutter

## Controls

| Key | Action |
|-----|--------|
| W | Move forward |
| S | Move backward |
| A | Rotate left |
| D | Rotate right |
| SPACE | Shoot |
| P / ESC | Pause |
| R / SPACE | Restart (on game over) |
| Q | Quit (on main menu) |

## Running the Game

### Using WSL (recommended for Windows)

Pygame needs a display server. Start XLaunch (VcXsrv) on Windows first, then:

```bash
cd /path/to/boot_astroids
uv run python main.py
```

If `uv` isn't in your WSL PATH:

```bash
wsl -e bash -c "cd '/mnt/c/Users/Cathy/OneDrive/Documents/Coding Exercises/Learning_Path/boot_astroids' && uv run python main.py"
```

### Direct (Linux/macOS)

```bash
uv run python main.py
```

## Project Structure

```
boot_astroids/
├── main.py          # Game loop, menus, state
├── player.py        # Ship movement, shooting, thrust
├── asteroid.py      # Asteroids, splitting, scoring
├── shot.py          # Bullets with lifetime
├── asteroidfield.py # Spawns asteroids from edges
├── circleshape.py   # Base class, collision, wrapping
├── explosion.py     # Particle effects
├── starfield.py     # Background
├── highscore.py     # Score persistence
├── constants.py     # Game configuration
├── logger.py        # Boot.dev logging
└── README.md
```

## Boot.dev

This project was created for the Boot.dev curriculum:

```
bootdev run 7228cde1-e519-4ee4-920e-1c50011197bb
```

## License

Educational project for learning Python and game development.

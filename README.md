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

## Boot.dev Learning Path vs. This Project

This project started from the [Boot.dev Backend Developer curriculum](https://boot.dev) Asteroids module. The base learning path covers OOP concepts, Pygame sprites, and game loop structure.

### What the Boot.dev Path Teaches (Base Game)

- **CircleShape** base class with position, velocity, radius, and collision detection
- **Player** as a triangle ship with rotation and movement (WASD)
- **Sprite groups** (updatable, drawable) for managing game objects
- **Asteroid** class with splitting (large → medium → small)
- **Shot** class with rate-limited shooting (spacebar)
- **Collision handling** – player hit ends the game; shots destroy asteroids
- Basic game loop with update and draw

The base game exits immediately on any asteroid collision (`sys.exit()`). There is no scoring, no lives, no menus, and no visual polish.

### What We Added (Beyond the Curriculum)

| Feature | Description |
|---------|-------------|
| **Screen wrapping** | Player, asteroids, and shots wrap around screen edges instead of drifting off |
| **Scoring system** | Points for destroying asteroids (100/50/25 by size) |
| **Lives & respawning** | 3 lives; respawn at center with 2 seconds of invincibility |
| **Main menu** | Start screen with Play and Quit before the game begins |
| **Pause menu** | Pause/resume with P or ESC |
| **Game over screen** | Final score, high score, and restart option instead of exiting |
| **High score persistence** | Best score saved to `highscore.json` across sessions |
| **Explosion effects** | Particle bursts when asteroids are destroyed |
| **Starfield background** | Animated starfield for atmosphere |
| **Thrust effect** | Visible flame when accelerating with W |
| **Shot lifetime** | Bullets expire after 2 seconds to limit on-screen clutter |

### New Files (Not in Base Path)

- `explosion.py` – Particle system for asteroid explosions
- `starfield.py` – Background starfield
- `highscore.py` – Load/save high score to disk

### Boot.dev Run Command

```
bootdev run 7228cde1-e519-4ee4-920e-1c50011197bb
```

## License

Educational project for learning Python and game development.

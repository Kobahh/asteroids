# Asteroids

A Python clone of the classic Asteroids arcade game, built with [Pygame](https://www.pygame.org/).

## Features

- Player-controlled ship with rotation and forward/backward movement
- Shooting with a rate-limited cooldown
- Circle-based collision detection between the player, shots, and asteroids
- Asteroids split into smaller asteroids when shot, down to a minimum size
- Randomly spawning asteroid field
- Event logging to `game_events.jsonl`

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (or `pip` + a virtual environment)
- Pygame

## Running the game

```bash
uv run main.py
```

If you're not using `uv`, install dependencies manually and run with Python directly:

```bash
pip install pygame
python main.py
```

## Controls

| Key       | Action           |
|-----------|------------------|
| `W`       | Move forward     |
| `S`       | Move backward    |
| `A`       | Rotate left      |
| `D`       | Rotate right     |
| `Space`   | Shoot            |

## Project structure

```
.
├── main.py          # Game loop and setup
├── player.py        # Player class (movement, rotation, shooting)
├── shot.py           # Shot (bullet) class
├── asteroid.py      # Asteroid class (movement, splitting)
├── asteroidfield.py # Spawns asteroids over time
├── circleshape.py   # Base class for all circular game objects
├── constants.py     # Game-wide constants (speeds, sizes, cooldowns)
└── logger.py        # Event logging (log_event, log_state)
```

## Gameplay

- Colliding with an asteroid ends the game (`Game over!`) and exits.
- Shooting an asteroid destroys it — if it's above the minimum radius, it splits into two smaller, faster-moving asteroids instead of disappearing entirely.

## Future ideas

- Scoring system
- Multiple lives and respawning
- Explosion effects
- Screen wrap instead of objects disappearing
- Power-ups (shield, speed)

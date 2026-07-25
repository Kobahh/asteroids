import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0.0
    score_counter = 0
    font = pygame.font.Font(None, 36)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                print(f"Final score: {score_counter}")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    score_counter += 1
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
            score_text = font.render(f"Score: {score_counter}", True, "white")
            screen.blit(score_text, (10, 10))
        pygame.display.flip()


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

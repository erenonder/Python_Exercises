import pygame
import random


class Game:
    def __init__(self):

        self.width = 20
        self.height = 20
        self.vel = 5
        self.win_x_max_limit = 500
        self.win_y_max_limit = 500
        self.win_x_min_limit = 0
        self.win_y_min_limit = 0
        self.x = int(self.win_x_max_limit / 2)
        self.y = int(self.win_y_max_limit / 2)
        self.bait_eaten = False
        self.bait_width = 5
        self.bait_height = 5
        self.score = 0
        self.win = None

        self.bait_pos_x = random.randint(
            self.win_x_min_limit, self.win_y_max_limit)
        self.bait_pos_y = random.randint(
            self.win_y_min_limit, self.win_y_max_limit)

    def start_game(self):
        pygame.init()

        self.win = pygame.display.set_mode(
            (self.win_x_max_limit, self.win_y_max_limit))
        pygame.display.set_caption('Pacman')

        pygame.image.load('pacman.png')

        run = True

        while run:
            pygame.time.delay(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.check_pressed_key()

            self.draw_new_display()

        pygame.quit()

    def check_pressed_key(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.x != self.win_x_min_limit:
                self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            if self.x != self.win_x_max_limit - self.width:
                self.x += self.vel
        if keys[pygame.K_UP]:
            if self.y != self.win_y_min_limit:
                self.y -= self.vel
        if keys[pygame.K_DOWN]:
            if self.y != self.win_y_max_limit - self.height:
                self.y += self.vel
        if keys[pygame.K_SPACE]:
            self.y -= 10 ** 2 / 2
            print(f'y is {self.y}')

    def draw_new_display(self):

        self.win.fill((0, 0, 0))
        pygame.draw.rect(self.win, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))

        self.check_bait_eaten()

        pygame.draw.rect(self.win, (0, 255, 0), (self.bait_pos_x,
                                                 self.bait_pos_y, self.bait_width, self.bait_height))
        pygame.display.update()

    def check_bait_eaten(self):
        if self.bait_eaten:
            self.bait_pos_x = random.randint(
                self.win_x_min_limit, self.win_y_max_limit)
            self.bait_pos_y = random.randint(
                self.win_y_min_limit, self.win_y_max_limit)

            self.bait_eaten = False

        if self.bait_pos_x > self.x and self.bait_pos_x < self.x + self.width:
            if self.bait_pos_y > self.y and self.bait_pos_y < self.y + self.height:
                self.bait_eaten = True
                self.score += 1


if __name__ == '__main__':
    game = Game()

    game.start_game()

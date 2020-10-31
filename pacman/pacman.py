import pygame
import random


class Game:
    def __init__(self):

        self.width = 57
        self.height = 57
        self.vel = 5
        self.win_x_max_limit = 1000
        self.win_y_max_limit = 1000
        self.win_x_min_limit = 0
        self.win_y_min_limit = 0
        self.x = int(self.win_x_max_limit / 2)
        self.y = int(self.win_y_max_limit / 2)
        self.bait_eaten = False
        self.bait_width = 5
        self.bait_height = 5
        self.score = 0
        self.win = None
        self.right = True
        self.left = False
        self.up = False
        self.down = False

        self.bait_pos_x = random.randint(
            self.win_x_min_limit, self.win_y_max_limit)
        self.bait_pos_y = random.randint(
            self.win_y_min_limit, self.win_y_max_limit)

    def start_game(self):
        pygame.init()

        self.win = pygame.display.set_mode(
            (self.win_x_max_limit, self.win_y_max_limit))
        pygame.display.set_caption('Pacman')

        self.load_images()

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
                self.right = False
                self.left = True
                self.up = False
                self.down = False
        if keys[pygame.K_RIGHT]:
            if self.x != self.win_x_max_limit - self.width:
                self.x += self.vel
                self.right = True
                self.left = False
                self.up = False
                self.down = False
        if keys[pygame.K_UP]:
            if self.y != self.win_y_min_limit:
                self.y -= self.vel
                self.right = False
                self.left = False
                self.up = True
                self.down = False
        if keys[pygame.K_DOWN]:
            if self.y != self.win_y_max_limit - self.height:
                self.y += self.vel
                self.right = False
                self.left = False
                self.up = False
                self.down = True

    def draw_new_display(self):

        self.win.fill((0, 0, 0))

        self.check_bait_eaten()

        if self.right:
            self.win.blit(self.pacman_right_image, (self.x, self.y))
        elif self.left:
            self.win.blit(self.pacman_left_image, (self.x, self.y))
        elif self.up:
            self.win.blit(self.pacman_up_image, (self.x, self.y))
        elif self.down:
            self.win.blit(self.pacman_down_image, (self.x, self.y))
        else:
            pass

        self.win.blit(self.ghost_image, (self.bait_pos_x, self.bait_pos_y))
        # pygame.draw.rect(self.win, (0, 255, 0), (self.bait_pos_x,
        #                                          self.bait_pos_y, self.bait_width, self.bait_height))
        pygame.display.update()

    def load_images(self):

        self.pacman_right_image = pygame.image.load('pacman_right.png')
        self.pacman_left_image = pygame.image.load('pacman_left.png')
        self.pacman_up_image = pygame.image.load('pacman_up.png')
        self.pacman_down_image = pygame.image.load('pacman_down.png')

        self.ghost_image = pygame.image.load('ghost.png')

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

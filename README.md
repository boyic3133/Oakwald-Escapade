# Oakwald-Escapade


https://www.pygame.org/project-Rect+Collision+Response-1061-.html 

class King(pygame.sprite.Sprite):
    """This class will contain the player"""

    # Initializing the class
    def __init__(self):
        super().__init__()

        # Loading the king image and putting it inside a rectangle to allow movement
        self.image = pygame.Surface([700, 600])
        self.image = pygame.image.load('king.png')
        self.rect = self.image.get_rect()

    def move_right(self):
        """Function to move the player right"""
        self.rect.x += 5  # Moves to the right by 5

        # If the player reaches the edge of the screen, they can't go further
        if self.rect.x >= 580:
            self.rect.x = 580

    def move_left(self):
        """Function to move the player left"""
        self.rect.x -= 5  # Moves to the left by 5

        # If the player reaches the edge of the screen, they can't go further
        if self.rect.x <= -50:
            self.rect.x = -50

    def update(self):
        """Updating the kings position on screen"""
        keys = pygame.key.get_pressed()  # Checks for an input by the user
        if keys[pygame.K_RIGHT]:
            king.move_right()  # Moves right if the user presses the right key

        if keys[pygame.K_LEFT]:
            king.move_left()  # Moves left if the user presses the left key

    def shoot(self):
        """Allows the player to shoot"""
        shots = Shooting(self.rect.centerx, self.rect.bottom)
        # Adding the shots to sprite lists created
        all_sprites_list.add(shots)
        shooting_list.add(shots)

import arcade
import random

from arcade.sprite_list import check_for_collision
ENEMY_SPEED = 4
# This margin controls how close the enemy gets to the left or right side
# before reversing direction.
ENEMY_VERTICAL_MARGIN = 15
SPRITE_SCALING_enemy = 0.10
# RIGHT_ENEMY_BORDER = 0 - ENEMY_VERTICAL_MARGIN
LEFT_ENEMY_BORDER = ENEMY_VERTICAL_MARGIN

# How many pixels to move the enemy down when reversing
ENEMY_MOVE_DOWN_AMOUNT = 30

class Enemy(arcade.Window):

    def __init__(self):

        # Variables that will hold sprite lists
        self.enemy_list = arcade.SpriteList()

        # Textures for the enemy
        self.enemy_textures = None

        # Enemy movement
        self.enemy_change_x = -ENEMY_SPEED

        self.right_enemy_border = - ENEMY_VERTICAL_MARGIN

    def set_width(self, width):
        self.right_enemy_border += width

    def load_enemy(self):
        # Load the textures for the enemies, one facing left, one right
        self.enemy_textures = []
        #:resources:images/space_shooter/playerShip1_green.png
        #assets/NicePng_spaceship-png_138961.png
        texture = arcade.load_texture("assets/nicePng_spaceship-png_138961.png", mirrored=True)
        self.enemy_textures.append(texture)
        texture = arcade.load_texture("assets/nicePng_spaceship-png_138961.png")
        self.enemy_textures.append(texture)

        # Create rows and columns of enemies
        x_count = 7
        x_start = 380
        x_spacing = 100
        y_count = 1
        y_start = 600
        y_spacing = 40
        for x in range(x_start, x_spacing * x_count + x_start, x_spacing):
            for y in range(y_start, y_spacing * y_count + y_start, y_spacing):
                # Create the enemy instance
                enemy = arcade.Sprite()
                # enemy._set_alpha("bob")
                enemy.scale = SPRITE_SCALING_enemy
                enemy.texture = self.enemy_textures[1]

                # Position the enemy
                enemy.center_x = x
                enemy.center_y = y
                enemy.angle = 180


                # Add the enemy to the lists
                self.enemy_list.append(enemy)
    
    def setup(self):
        # self.enemy_list = arcade.SpriteList()
        return self.enemy_list

    def collision_detect(self, player):
        hit_list = []
        hit_list = arcade.check_for_collision_with_list(player, self.enemy_list)
        # if len(hit_list) > 0:
        #     self.enemy_list.remove_from_sprite_lists()
        return  hit_list

    def update_enemies(self, player):
        # Move the enemy vertically
        for enemy in self.enemy_list:
            enemy.center_x += self.enemy_change_x

        # Check every enemy to see if any hit the edge. If so, reverse the
        # direction and flag to move down.
        move_down = False
        for enemy in self.enemy_list:
            if enemy.right > self.right_enemy_border and self.enemy_change_x > 0:
                self.enemy_change_x *= -1
                move_down = True
            if enemy.left < LEFT_ENEMY_BORDER and self.enemy_change_x < 0:
                self.enemy_change_x *= -1
                move_down = True

        # Did we hit the edge above, and need to move t he enemy down?
        if move_down:
            # Yes
            for enemy in self.enemy_list:
                # Move enemy down
                enemy.center_y -= ENEMY_MOVE_DOWN_AMOUNT
                # Flip texture on enemy so it faces the other way
                if self.enemy_change_x > 0:
                    enemy.texture = self.enemy_textures[0]
                else:
                    enemy.texture = self.enemy_textures[1]
        
 




import pygame

class Enemy:
    def __init__(self, x, y):
        self.x =x
        self.y = y
        self.animation_count = 0
        self.health = 1
        self.path = []

    def draw(self, win):
        """
        :param win: surface
        :return: None
        """

        pass

    def collide(self,x , y):

        """

        :param x: int
        :param y: int
        :return: Bool
        """

        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        pass
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True


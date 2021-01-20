import pygame
#from pygame.sprite import Sprite

class Bird:

	def __init__(self, FlappyBirdGame):
		self.settings = FlappyBirdGame.game_settings
		self.screen = FlappyBirdGame.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load("img/player.png")
		self.image_rect = self.image.get_rect()
		self.rect = self.image_rect

		self.re_transform_scale()

		self.image_rect.midleft = self.screen_rect.midleft
		self.image_rect.x = self.screen_rect.width//8 #atau bisa += 50

		self.y = self.image_rect.y

		self.is_fly = False
		self.is_fall = False

	def re_transform_scale(self):
		self.image = pygame.transform.scale(self.image, (1*self.image_rect.width//2,1*self.image_rect.height//2))

	def fly(self):
		self.y -= self.settings.bird_fly_speed
		self.image_rect.y = self.y

	def fall(self):
		self.y += self.settings.bird_fall_speed
		self.image_rect.y = self.y

	def move(self):
		if self.is_fly:
			self.fly()
		if self.is_fall:
			self.fall()

	def show_bird(self):
		self.screen.blit(self.image, self.image_rect)
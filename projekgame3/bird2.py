import pygame

class Bird2:

	def __init__(self, FlappyBirdGame):
		self.settings = FlappyBirdGame.game_settings
		self.screen = FlappyBirdGame.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load("img/player2.png")
		self.image_rect = self.image.get_rect()
		self.rect = self.image_rect

		self.re_transform_scale2()

		self.image_rect.midleft = self.screen_rect.midleft
		self.image_rect.x = self.screen_rect.width//30 #atau bisa += 50

		self.y = self.image_rect.y

		self.is_fly2 = False
		self.is_fall2 = False

	def re_transform_scale2(self):
		self.image = pygame.transform.scale(self.image, (1*self.image_rect.width//2,1*self.image_rect.height//2))

	def fly2(self):
		self.y -= self.settings.bird2_fly_speed
		self.image_rect.y = self.y

	def fall2(self):
		self.y += self.settings.bird2_fall_speed
		self.image_rect.y = self.y

	def move2(self):
		if self.is_fly2:
			self.fly2()
		if self.is_fall2:
			self.fall2()

	def show_bird2(self):
		self.screen.blit(self.image, self.image_rect)
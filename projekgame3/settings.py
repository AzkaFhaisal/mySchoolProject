import pygame

class Settings:

	def __init__(self):

		#GAME BASIC SETTINGS
		self.base_dimension = 30

		self.screen_width = 9*self.base_dimension
		self.screen_height = 16*self.base_dimension

		self.title = ("Flappy Bird Game")
		self.bg = pygame.image.load('img/bg.png')
		self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
		self.bg_color = (0, 0, 0)


		#PIPE SETTINGS
		self.pipe_width = 50
		self.pipe_height = 200
		self.pipe_color = [4, 233, 12]

		self.pipe_head_width = 60
		self.pipe_head_height = 25

		#self.pipe_number = 0


		#PLATFORM SETTINGS
		self.platform_speed = 1

		#BIRD SETTINGS
		self.bird_fly_speed = 5
		self.bird_fall_speed = 2
		self.bird_life = 3

		#BIRD2 SETTINGS
		self.bird2_fly_speed = 5
		self.bird2_fall_speed = 2
		self.bird2_life = 3
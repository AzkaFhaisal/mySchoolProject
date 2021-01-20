import pygame
import pygame.font
from pygame.sprite import Group
 
class Scoreboard:
 
	def __init__(self, FlappyBirdGame):
		self.settings = FlappyBirdGame.game_settings
		self.stats = FlappyBirdGame.game_stat
		self.screen = FlappyBirdGame.screen
		self.screen_rect = self.screen.get_rect()
		self.font = pygame.font.SysFont(None, 48) 
		self.text_color = (255, 255, 255)
 
		self.high_score = 0
		self.level = 1
		self.score = 0
 
		self.show_score()
		self.show_high_score()
		self.show_level()
 
	def show_score(self):
		round_score = round(self.score, -1)
		score_string = "{:,}".format(round_score)
		self.score_image = self.font.render(score_string, True, self.text_color)
 
		self.score_rect_image = self.score_image.get_rect()
		self.score_rect_image.center = self.screen_rect.center
		self.score_rect_image.top = 10
 
	def draw_score(self):
		self.screen.blit(self.score_image, self.score_rect_image)
		#self.screen.blit(self.high_score_image, self.high_score_rect_image)
		#self.screen.blit(self.level_image, self.level_rect_image)
 
	def show_high_score(self):
		round_high_score = round(self.stats.high_score, -1)
		high_score_string = "{:,}".format(round_high_score)
		self.high_score_image = self.font.render(high_score_string, True, self.text_color, self.settings.bg_color)
 
		self.high_score_rect_image = self.high_score_image.get_rect()
		self.high_score_rect_image.midtop = self.screen_rect.midtop
 
	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.show_high_score()

	def show_level(self):
		level_string = str(self.stats.level)
		self.level_image = self.font.render(level_string, True, self.text_color, self.settings.bg_color)

		self.level_rect_image = self.level_image.get_rect()
		self.level_rect_image.left = self.screen_rect.left + 30
		self.level_rect_image.top = 50
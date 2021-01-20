import sys
import pygame
from random import randint
import time
#OUR OWN MODULE
from settings import Settings
from score_board import Scoreboard
from game_stats import GameStats
from button import Button 

from platform import Platform
from pipe import Pipe
from bird import Bird
from bird2 import Bird2

class FlappyBirdGame:

	def __init__(self):
		pygame.init()
		########################################
		#OBJECT yang INVISIBLE behind the screen
		########################################
		self.game_settings = Settings()
		self.game_stat = GameStats(self)

		self.screen = pygame.display.set_mode([self.game_settings.screen_width, self.game_settings.screen_height])
		#################################################
		#SINGLE OBJEK ATAU MODELS IN OUR GAME (Object in Object)
		#################################################
		
		self.game_bird = Bird(self)
		self.game_bird2 = Bird2(self)
		self.play_button = Button(self, "PLAY")
		self.game_platform = Platform(self)

		#################################################
		#GROUP OBJEK ATAU MODELS IN OUR GAME (Object in Object)
		#################################################
		self.game_pipes = pygame.sprite.Group()
		self.create_pipes()

		self.score_board = Scoreboard(self)

		self.title = pygame.display.set_caption(self.game_settings.title)
		self.bg_screen = self.game_settings.bg

		self.running = True

	####################
	#PROPERTY GAME UTAMA
	####################
	def run_game(self):
		while self.running:
			self.rg_check_event()
			self.rg_update_screen()

	def rg_check_event(self):
		events = pygame.event.get()
		#print(events)

		for event in events:
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				self.rg_e_check_keydown(event)
			elif event.type == pygame.KEYUP:
				self.rg_e_check_keyup(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)



	def start_game(self):
		status_game_active = self.game_stat.game_active
		if not status_game_active:
			self.game_stat.reset_game_stat()
			self.game_stat.game_active = True

			self.game_bird.reset_game_stat()
			pygame.mouse.set_visible(False)

	def rg_e_check_keydown(self, event):
		if event.key == pygame.K_SPACE:
			self.game_bird.is_fly = True
		if event.key == pygame.K_w:
			self.game_bird2.is_fly2 = True

		if event.key == pygame.K_q:
			sys.exit() 

		if event.key == pygame.K_p:
			self.start_game()

	def rg_e_check_keyup(self, event):
		if event.key == pygame.K_SPACE:
			self.game_bird.is_fly = False
			self.game_bird.is_fall = True

		if event.key == pygame.K_w:
			self.game_bird2.is_fly2 = False
			self.game_bird2.is_fall2 = True

	def rg_update_screen(self):
		self.screen.blit(self.bg_screen, [0,0])
		self.update_pipes()
		self.update_platform()

		self.update_bird()
		self.game_bird.show_bird()
		self.update_bird2()
		self.game_bird2.show_bird2()
		self.update_button()
		self.update_score()
		#self.play_button.show_button()
		pygame.display.flip()
		pygame.time.Clock().tick(60)

		#if not self.game_stat.game_active:
			#self.play_button._draw_button()

	def _check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		status_game_active = self.game_stat.game_active
		if button_clicked and not status_game_active:
			self.game_stat.reset_game_stat()
			self.game_stat.game_active = True
			self.score_board.show_score()
			pygame.mouse.set_visible(False)

	#def show_button(self):
		#self.show_button = False 

	def update_button(self):
		if not self.game_stat.game_active:
			self.play_button._draw_button()

	####################
	#SCORE
	###################

	def update_score(self):
		self.score_board.show_score()

	####################
	#BIRD
	####################
	def bird_hit_pipe(self):
		if pygame.sprite.spritecollideany(self.game_bird, self.game_pipes):
			return True
		else:
			return False

	def bird_on_platform(self):
		if self.game_bird.image_rect.bottom >= self.game_platform.image_rect.top :
			return True
		else:
			return False

	def bird_on_top_edge(self):
		screen_rect = self.screen.get_rect()
		if self.game_bird.image_rect.top <= screen_rect.top:
			return True
		else:
			return False

	def update_bird(self):
		if self.bird_on_platform() == False and self.bird_on_top_edge() == False and self.bird_hit_pipe() == False:
			self.game_bird.move()
			#self.show_button = True
			#self._bird_hit
		#self.game_bird.show_bird()

		#pointP1 = pygame.sprite.groupcollide(self.game_pipes, self.game_bird, True, True)

		#if pointP1:
			#for bird_pass in pointP1.values():
				#self.game_stat.score += (self.game_settings.bird_points * len(bird_pass) )
			#self.score_board.show_score()
		#self.show_button = True

	####################
	#BIRD2
	####################
	def bird_hit_pipe2(self):
		if pygame.sprite.spritecollideany(self.game_bird2, self.game_pipes):
			return True
		else:
			return False

	def bird_on_platform2(self):
		if self.game_bird2.image_rect.bottom >= self.game_platform.image_rect.top :
			return True
		else:
			return False

	def bird_on_top_edge2(self):
		screen_rect = self.screen.get_rect()
		if self.game_bird2.image_rect.top <= screen_rect.top:
			return True
		else:
			return False

	def update_bird2(self):
		if self.bird_on_platform2() == False and self.bird_on_top_edge2() == False and self.bird_hit_pipe2() == False:
			self.game_bird2.move2()
		self.game_bird2.show_bird2()

	###################
	#SCORE
	####################
	def update_score(self):
		self.score_board.draw_score()

	####################
	#PLATFORM
	####################
	def update_platform(self):
		self.game_platform.show_platform()
		self.game_platform.move()

	####################
	#PIPE
	####################
	def update_pipes(self):
		self.show_pipes()

	def check_pipes(self, pipe):
		if pipe.head.head_image.right <= 0:
			self.game_pipes.remove(pipe)
		if len(self.game_pipes) == 0:
			self.create_pipes()
			self.game_settings

	def show_pipes(self):
		pipes = self.game_pipes.sprites()
		for pipe in pipes:
			pipe.show_pipe()
			pipe.move()
			self.check_pipes(pipe)

	def create_pipes(self):
		#self.game_settings.pipe_number += 1
		screen_rect = self.screen.get_rect()
		platform_rect = self.game_platform.image_rect
		gap = screen_rect.height//5

		pipe_top = Pipe(self)
		pipe_bottom = Pipe(self)

		#Atur ulang tinggi pipe_top
		random_height_pipe_top = randint(screen_rect.height//5 + 100, 4*screen_rect.height//5) - (platform_rect.height+50)
		pipe_top.pipe_image.height = random_height_pipe_top
		pipe_top.head.head_image.midbottom = pipe_top.pipe_image.midbottom

		#Atur ulang tinggi pipe_bottom
		pipe_bottom.pipe_image.height = screen_rect.height - pipe_top.pipe_image.height - gap
		
		pipe_bottom.pipe_image.bottomright = screen_rect.bottomright
		pipe_bottom.pipe_image.x += 50
		pipe_bottom.head.head_image.midtop = pipe_bottom.pipe_image.midtop

		#pipe_bottom

		self.game_pipes.add(pipe_top)
		self.game_pipes.add(pipe_bottom)


game = FlappyBirdGame()
game.run_game()

class GameStats:

	def __init__(self, FlappyBirdGame):
		self.settings = FlappyBirdGame.game_settings
		self.reset_game_stat()

		self.game_active = False
		self.high_score = 0

	def reset_game_stat(self):
		self.bird_left = self.settings.bird_life
		self.bird2_left = self.settings.bird2_life
		self.bird_life = self.settings.bird_life
		self.score = 1
		self.current_level_score = 0
		self.level = 0

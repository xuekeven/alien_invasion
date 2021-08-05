
class GameStats():

    def __init__(self,ai_settings):

        self.ai_settings = ai_settings

        self.game_active = False
        self.highest_score = 0
        
        self.rest_stats()


    def rest_stats(self):

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0
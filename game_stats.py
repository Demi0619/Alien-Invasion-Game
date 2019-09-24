class Gamestats:
    ''' store game status'''
    def __init__(self,ai_game):
        self.settings=ai_game.setting1
        self.game_active=False
        self.reset_stats()
        self.high_score=0

    def reset_stats(self):
        self.ship_left=self.settings.ship_limit
        self.score=0
        self.level=1
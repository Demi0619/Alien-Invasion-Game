class Setting:
    '''overall setting info for project'''
    def __init__(self):
        #screen settting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #object setting

        self.bullet_width = 300
        self.bullet_height = 10
        self.bullet_color = (60,60,60)
        self.max_valid_bullet = 10
        self.alien_drop_speed = 20
        self.ship_limit = 3
        self.speedup=1.1
        self.score_speedup=1.5
        self.initialized_dynamic_setting()

    def initialized_dynamic_setting(self):
        self.alien_speed=1.0
        self.ship_speed = 5
        self.bullet_speed = 1
        self.direction=1
        self.hit_score=50

    def increase_speed(self):
        self.alien_speed*=self.speedup
        self.ship_speed*=self.speedup
        self.bullet_speed*=self.speedup
        self.hit_score=int(self.hit_score*self.score_speedup)


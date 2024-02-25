from direct.showbase.ShowBase import ShowBase
from hero import Hero
from mapmanager_colors import Mapmanager 

class Game(ShowBase):
    def init(self):
        ShowBase.init(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        base.camLens.setFov(90)

game = Game()
game.run()
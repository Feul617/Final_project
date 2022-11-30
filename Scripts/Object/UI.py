from Scripts.FrameWork.FrameWork_AFX import *

class UI(Object):
    score = 0
    def __init__(self):
        self.transform.position = Vector2(0, 0)
        self.font = load_font('ENCR10B.TTF', 16)
        self.font_color = [0 ,0, 0]

    def Draw(self):
        self.font.draw(UI.score, 70, 750, self.font_color)
        pass


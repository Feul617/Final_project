class Vector2:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        pass

    def __del__(self):
        pass

    def __add__(self, other):
        result = Vector2()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    pass

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

    def __sub__(self, other):
        result = Vector2()
        if type(other) is Vector2:
            result.x = self.x - other.x
            result.y = self.y - other.y
        else:
            result.x = self.x - other
            result.y = self.y - other
        return result

    def __eq__(self, other):
        if self.x is not other.x:
            return False
        if self.y is not other.y:
            return False
        return True

    def __ge__(self, other):
        if self.x < other.x:
            return False
        if self.y < other.y:
            return False
        return True

    def __mul__(self, other):
        result = Vector2()
        if type(other) is Vector2:
            result.x = self.x * other.x
            result.y = self.y * other.y
        else:
            result.x = self.x * other
            result.y = self.y * other
        return result

    def Copy(self):
        return Vector2(self.x, self.y)

    @staticmethod
    def Normalize(this):
        dis = ((this.x ** 2) + (this.y ** 2)) ** 0.5
        norm = Vector2(this.x / dis, this.y / dis)
        return norm

    pass

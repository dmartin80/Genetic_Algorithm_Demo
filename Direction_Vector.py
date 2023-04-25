import math
class vector:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def from_angle(self, angle):
        self.x = math.cos(angle)
        self.y = math.sin(angle)
    
    def add(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y

    def limit(self, limit):
        mag = math.sqrt(math.pow(self.x, 2) + math.pow(self.y,2))
        if mag > limit:
            self.x = (limit/mag)*self.x
            self.y = (limit/mag)*self.y

    def centerpoint(self, radius):
        self.x = self.x + radius
        self.y = self.y + radius

    def intersecting_circles(self, vector2, radius1, radius2):
        distance = math.fabs(math.sqrt(math.pow((vector2.x - self.x),2)+math.pow((vector2.y - self.y),2)))
        if distance > radius1-1 + radius2-1:
            return False
        else:
            return True
    
    def distance(self, vector2, radius1, radius2):
        distance = math.fabs(math.sqrt(math.pow((vector2.x - self.x),2)+math.pow((vector2.y - self.y),2)))
        return distance - (radius1-1 + radius2-1)

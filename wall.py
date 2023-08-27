from turtle import Turtle

class Wall:
    def __init__(self):
        self.wall_parts = []
        self.wall_positions = []

        x = 290
        y = 300
        for i in range(236):

            if i < 59:
                self.wall_positions.append((x,y))
                x -= 10
            elif i < 118:
                self.wall_positions.append((x, y))
                y -= 10
            elif i < 177:
                self.wall_positions.append((x, y))
                x += 10
            else:
                self.wall_positions.append((x, y))
                y += 10
            new_wall_part = Turtle("square")
            self.wall_parts.append(new_wall_part)
            self.wall_parts[i].penup()
            self.wall_parts[i].goto(self.wall_positions[i])
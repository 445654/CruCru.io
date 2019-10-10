from display import Display
from vector import Vect2d
from creature import Creature

class Player(Creature):
    mouse_pos = Vect2d()

    def __init__(self, pos) -> None:
        super().__init__(pos, "Player")

    def update(self, width, height) -> None:
        coeff_tps = 1
        dist_per_sec = 200

        if self.mouse_pos.lengthSq() > self.radius**2:
            coeff_dist_mouse = 1
        else:
            coeff_dist_mouse = self.mouse_pos.length()/self.radius

        v = self.mouse_pos.normalize()

        v = v*Display.frame_time*dist_per_sec/coeff_tps * coeff_dist_mouse**2

        max_speed_per_s = 100

        new_pos = self.pos + v

        if new_pos.x > self.radius and new_pos.x < width-self.radius:
            self.pos.x = new_pos.x

        if new_pos.y > self.radius and new_pos.y < height-self.radius:
            self.pos.y = new_pos.y

        self.radius = int(self.base_radius + self.score/10)

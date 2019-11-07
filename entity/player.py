if __name__ == "__main__":
    import sys
    sys.path.append("..")

from util.vector import Vect2d

from entity.creature import Creature

class Player(Creature):
    mouse_pos = Vect2d()

    def __init__(self, pos, name, color, id) -> None:
        super().__init__(pos, "Player", color, id)

    def update(self, size) -> None:
        coeff_tps = 1
        dist_per_sec = 200

        if self.mouse_pos.lengthSq() > self.radius**2:
            coeff_dist_mouse = 1
        else:
            coeff_dist_mouse = self.mouse_pos.length()/self.radius
            coeff_dist_mouse = coeff_dist_mouse**2

            if coeff_dist_mouse < 0.1:
                coeff_dist_mouse = 0

        direction = self.mouse_pos.normalize()*coeff_dist_mouse

        self.applyNewDirection(direction, size)

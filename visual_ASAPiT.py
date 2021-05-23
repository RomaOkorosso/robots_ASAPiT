from matplotlib import pyplot as plt
import matplotlib.patches as patches


class Robot:

    def __init__(self, pos: int, dir: str, moved: bool):
        self.pos = pos
        self.dir = dir
        self.moved = moved


pos_sum = 0


class Field:
    global pos_sum
    ps = pos_sum // 2
    places = [0] * 20
    length = 20
    mid = length // 2
    r_count = 7
    moved_r = 0
    plot_num = 0

    def draw_field(self):
        fig, ax = plt.subplots()
        sq = patches.Rectangle((0, 0), self.length, 1, edgecolor='r', )
        ax.plot(self.length, self.length)
        ax.add_patch(sq)

        for i in range(len(self.places)):
            if self.places[i] != 0:
                print(f"{self.places[i].pos}")
                circle = plt.Circle((self.places[i].pos - 0.5, 0.5), 0.5, color='r')
                ax.add_patch(circle)
        plt.savefig(f'{self.plot_num}.png')
        self.plot_num += 1
        plt.show()

    def zero_state(self):
        for f in self.places:
            if f != 0:
                f.moved = False

    def move(self):
        while 0 < self.r_count:
            i = 0
            while self.moved_r < self.r_count:
                if self.places[i] != 0:
                    robot = self.places[i]
                    if robot.moved is False:
                        if robot.dir == "+":
                            if robot.pos + 1 >= self.length:
                                self.r_count -= 1
                                self.places[i] = 0
                                self.draw_field()
                            elif self.places[i + 1] != 0:
                                robot2 = self.places[i + 1]
                                if robot2.dir == "-":
                                    robot.dir, robot2.dir = robot2.dir, robot.dir
                                    self.places[i], self.places[i + 1] = self.places[i + 1], self.places[i]
                                    robot.moved = robot2.moved = True
                                    self.moved_r += 2
                                else:
                                    pass
                            else:
                                robot.pos = i + 1
                                robot.moved = True
                                self.places[i] = 0
                                self.places[i + 1] = robot
                                self.moved_r += 1
                                self.draw_field()
                        else:
                            if robot.pos - 1 <= self.length:
                                self.r_count -= 1
                                self.places[i] = 0
                                self.draw_field()
                            elif self.places[i - 1] != 0:
                                robot2 = self.places[i - 1]
                                if robot2.dir == "+":
                                    robot.dir, robot2.dir = robot2.dir, robot.dir
                                    self.places[i], self.places[i - 1] = self.places[i - 1], self.places[i]
                                    robot.moved = robot2.moved = True
                                    self.moved_r += 2
                                else:
                                    pass
                            else:
                                robot.pos = i - 1
                                self.places[i] = 0
                                self.places[i - 1] = robot
                                robot.moved = True
                                self.moved_r += 1
                                self.draw_field()

                if i + 1 < self.length:
                    i += 1
                else:
                    i = 0
                    self.moved_r = 0
                    self.zero_state()
                self.moved_r = 0



def cast_cleaners(in_str, f: Field):
    pos = int(in_str)
    global pos_sum
    pos_sum += pos
    if pos <= f.mid:
        direction = "+"
    else:
        direction = "-"
    f.places[pos] = Robot(pos, direction, False)


field = Field()
robots_coord = [cast_cleaners(cleaner, field) for cleaner in input().split()]
field.draw_field()
field.move()

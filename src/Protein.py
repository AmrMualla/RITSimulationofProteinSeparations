class Protein:

    def __init__(self, name="notSet", full_name="notSet", abbr="notSet", mw=0, color=(0, 0, 255)):
        self.concentration = 1
        self.start_y = 0
        self.scale_factor = 0.0
        self.relative_migration = 0.0
        self.speed = 0.01
        self.mw = mw
        self.charge = 0.0
        self.name = name
        self.full_name = full_name
        self.abbr = abbr
        self.selected = False
        self.color = color
        self.x1 = 0
        self.y1 = 0
        self.width = 0
        self.height = 2
        self.y1_float = 0.0
        self.max_position = 0
        self.distance = 0.0
        self.decider = 1
        self.counter = 1
        self.plot_y_pos = 0
        self.plot_x_pos = 0

    def set_start_position(self, x, y):
        self.x1 = x
        self.y1 = y
        self.start_y = self.y1
        self.y1_float = float(self.y1)

    def reset_decider(self):
        self.decider = 1
        self.counter = 1

    def incr_position(self):
        if self.counter == self.decider:
            self.y1_float += self.speed
            self.counter = 1
        else:
            self.counter += 1
        self.y1 = int(self.y1_float)

    def match_position(self, x, y):
        x2 = self.x1 + self.width
        y2 = self.y1 + self.height
        range_val = 2
        return x >= self.x1 - range_val and x <= x2 + range_val and y >= self.y1 - range_val and y <= y2 + range_val

    def set_width(self, w):
        self.width = w

    def get_decider(self):
        return self.decider

    def set_decider(self, i):
        self.decider = i

    def set_host_scale_factor(self, f):
        self.scale_factor = f

    def set_max_position(self, i):
        self.max_position = i

    def set_concentration(self, i):
        self.concentration = i

    def match_plot_position(self, x, y):
        range_val = 3
        return x >= self.plot_x_pos - range_val and x <= self.plot_x_pos + range_val and y >= self.plot_y_pos - range_val and y <= self.plot_y_pos + range_val

    def get_distance(self):
        self.distance = self.scale_factor * (self.y1 - self.start_y)
        return self.distance

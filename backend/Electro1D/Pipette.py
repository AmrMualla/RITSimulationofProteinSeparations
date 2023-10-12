"""
Decompiled by DJ v3.10.10.93 Copyright 2007 Atanas Neshkov  Date: 4/29/2009 2:11:16 PM
Home Page: http://members.fortunecity.com/neshkov/dj.html  http://www.neshkov.com/dj.html
Check often for new version!
Decompiler options: packimports(3)
Source File Name:   D:\\Dave\\Java\\Electro1DMain\\Pipette.java
@author Landon Heatly
"""
from backend.Electro1D.Sample import Sample


class Pipette:
    # public Color sample_color;
    x1 = 0
    y1 = 0
    gap = 0
    sample_depth = 0
    init_tipLength = 0
    y1_float = float(0)
    max_y_position = 0
    well_bottom = 0
    speed = float(0)
    pipette_coords_x = []
    pipette_coords_y = []
    pipette_coords_y_f = []
    pts = 0
    empty_tip = 0
    drop_start = 0
    drop_length = 0
    dropped = False
    emptied = False
    has_sample = False
    retracted = False
    sample = Sample()

    """
    Initializes a new instance of the Protein class.
    """
    def __init__(self):
        # self.sample_color = Color.blue
        self.gap = 6
        self.speed = 2.0
        self.pipette_coords_x = [0, 0, 0, 0]
        self.pipette_coords_y = [0, 0, 0, 0]
        self.pipette_coords_y_f = [0, 0, 0, 0]
        self.empty_tip = 4
        self.sample = Sample()

    """
    Sets the sample depth.
    :param i: the sample depth
    """
    def set_sample_depth(self, i):
        self.sample_depth = i

    """
    Increase the position of the pipette.
    """
    def incr_position(self):
        i = self.y1
        self.y1_float += self.speed
        self.y1 = int(self.y1_float)
        j = self.y1 - i
        if j > 0:
            if not self.dropped:
                self.pipette_coords_y[1] += j
                self.pipette_coords_y[2] += j
                self.pipette_coords_y_f[1] -= self.empty_tip
                self.pipette_coords_y_f[2] -= self.empty_tip
                if self.pipette_coords_y[1] > self.sample_depth:
                    self.pipette_coords_y_f[0] += j
                    self.pipette_coords_y_f[3] += j
                if self.pipette_coords_y[1] > self.max_y_position:
                    self.dropped = True
                    self.drop_start = self.pipette_coords_y[1] - self.empty_tip
                    self.drop_length = self.well_bottom - self.drop_start
            elif not self.emptied:
                self.pipette_coords_y_f[0] += j
                self.pipette_coords_y_f[3] += j
                if self.pipette_coords_y_f[0] > self.max_y_position:
                    self.emptied = True
            elif not self.retracted:
                self.pipette_coords_y[1] -= j
                self.pipette_coords_y[2] -= j
                if self.pipette_coords_y[1] < 0:
                    self.retracted = True
        return not self.retracted

    """
    Fill the well and empty the pipette.
    :param g: Java Graphics, we are not dealing with GUI, any line using g is commented out
    """
    def fill_well(self, g):  # TODO: This method deals with GUI, figure out what to do with that
        # if not self.emptied:
            # g.setColor(self.sample_color)
            # g.fillPolygon(self.pipette_coords_x, self.pipette_coords_y_f, self.pts)
        # g.setColor(Color.black)
        # g.drawPolygon(self.pipette_coords_x, self.pipette_coords_y, self.pts)
        if self.dropped:
            self.sample.draw_switch(True)
            if not self.emptied:
                i = self.pipette_coords_y[1] - self.empty_tip
                # j = self.well_bottom - i
                # g.setColor(self.sample_color)
                # g.fillRect(self.pipette_coords_x[1], i, 4, j)
        if self.emptied:
            self.sample.draw_switch(False)
        return self.incr_position()

    """
    Sets the sample.
    :param sample1: The new sample
    """
    def set_sample(self, sample1):
        self.sample = sample1

    """
    Set the boolean flags to False.
    """
    def reset_flags(self):
        self.dropped = False
        self.emptied = False
        self.has_sample = False
        self.retracted = False

    """
    Sets the start position for x.
    :param i: The base position to set the start coordinates from
    """
    def set_start_x_position(self, i):
        self.reset_flags()
        self.x1 = i
        self.y1 = 0
        self.y1_float = 0.0
        self.pipette_coords_x[0] = self.x1 - 4
        self.pipette_coords_x[1] = self.x1 - 2
        self.pipette_coords_x[2] = self.x1 + 2
        self.pipette_coords_x[3] = self.x1 + 4
        j = 0
        while j < 4:
            self.pipette_coords_y[j] = 0
            self.pipette_coords_y_f[j] = 0
            j += 1

    """
    Sets the max position for y.
    :param i: The base position to set the edge coordinates from
    """
    def set_max_y_position(self, i):
        self.max_y_position = i - self.gap
        self.well_bottom = i

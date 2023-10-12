"""
This file contains the info on the Sample class
Note: This class is a helper for the GUI that hasn't been implemented yet
@author: Beck Anderson
"""


class Sample:

    """
    This initializes a new instance of a Sample.
    NOTE: If the protein is added to here, it will need to be a new
          variable that is passed in on creation
    """
    def __init__(self):
        self.samp_x = 0
        self.samp_y = 0
        self.max_y = 0
        self.samp_width = 0
        self.samp_height = 0
        self.fill_counter = 0
        self.fill_ratio = 0
        self.change_on = False
        self.fill_switch = False
        self.empty_switch = False
        # possibly add the protein that this represents?
        # i.e. self.protein = Protein

    """
    This function clears the sample back to its
    initial state
    """
    def reset(self):
        self.samp_x = 0
        self.samp_y = 0
        self.max_y = 0
        self.samp_width = 0
        self.samp_height = 0
        self.fill_counter = 0
        self.fill_ratio = 0
        self.change_on = False
        self.fill_switch = False
        self.empty_switch = False

    """
    Following functions are setters for the class.
    Best practice way to change the values of the instance.
    """

    """
    Sets the x position
    :param x: the new x position
    """
    def set_x_position(self, x):
        self.samp_x = x

    """
    Sets the y position
    :param y: the new y position
    """
    def set_y_position(self, y):
        self.samp_y = y

    """
    Sets the max y amount
    :param y: the new max y position
    """
    def set_max_y(self, y):
        self.max_y = y

    """
    Sets the width amount
    :param width: the new width amount
    """
    def set_width(self, width):
        self.samp_width = width

    """
    If we add a protein, it will need a setter.
    
    def set_protein(self, protein):
        self.protein = protein
    """

    """
    Sets the switch to be on or off
    :param flag: the new flag boolean
    
    :NOTE: possibly just have this flip between True or False?
        i.e. self.change_on = not self.change_on
    """
    def draw_switch(self, flag):
        self.change_on = flag

    """
    This will empty the sample 
    """
    def empty(self):
        self.fill_switch = False
        self.empty_switch = True
        # if protein is added to here, wipe it
        # i.e. self.protein = None

    """
    This function will modify the provided graphic
    to make it align with the info about the sample
    :@param graphic: the graphic to be modified
    """
    def draw_sample(self, graphic):

        if self.change_on:
            if self.fill_counter > self.fill_ratio:
                if self.fill_switch:
                    self.samp_y -= 1
                    self.samp_height += 1
                if self.empty_switch:
                    self.samp_y += 1
                    self.samp_height -= 1
                self.fill_counter = 0
            else:
                self.fill_counter += 1
            if self.empty_switch and (self.samp_y > self.max_y):
                self.change_on = False
                self.samp_height = 0
        if self.samp_height > 0:
            # set values for graphic that doesn't exist yet
            # graphic.setColor(Color.blue)
            # graphic.filRect(self.samp_x, self.samp_y, self.samp_width, self.samp_height)
            temp = None

# Protein Class represents properties and behaviors related to a protein.
# Note: GUI-related fragments have been removed from this class.
# @author Amr Mualla & Bader Alharbi
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
class Protein:

    # Initializes a new instance of the Protein class.
    # @param name: Short name of the protein. Defaults to "notSet".
    # @param full_name: Full name of the protein. Defaults to "notSet".
    # @param abbr: Abbreviation for the protein. Defaults to "notSet".
    # @param mw: Molecular weight of the protein. Defaults to 0.
    # @param color: Color representation (RGB) of the protein. Defaults to blue.
    def __init__(self, name="notSet", full_name="notSet", abbr="notSet", mw=0, color=(0, 0, 255)):
        self.concentration = 1   # Default concentration of the protein.
        self.start_y = 0         # Starting y-coordinate.
        self.scale_factor = 0.0  # Factor for scaling.
        self.relative_migration = 0.0 # Relative migration value.
        self.speed = 0.01        # Speed of protein movement.
        self.mw = mw             # Molecular weight of the protein.
        self.charge = 0.0        # Charge on the protein.
        self.name = name         # Short name of the protein.
        self.full_name = full_name # Full name of the protein.
        self.abbr = abbr         # Abbreviation for the protein.
        self.selected = False    # Flag indicating if protein is selected.
        self.color = color       # Color representation (RGB) of the protein.
        # GUI related attributes for positioning and plotting.
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

    # Sets the starting position of the protein on the GUI.
    # @param x: The x-coordinate for the starting position.
    # @param y: The y-coordinate for the starting position.
    def set_start_position(self, x, y):
        self.x1 = x
        self.y1 = y
        self.start_y = self.y1
        self.y1_float = float(self.y1)

    # Resets the decision counter.
    def reset_decider(self):
        self.decider = 1
        self.counter = 1

    # Incrementally updates the position of the protein based on its speed.
    def incr_position(self):
        if self.counter == self.decider:
            self.y1_float += self.speed
            self.counter = 1
        else:
            self.counter += 1
        self.y1 = int(self.y1_float)

    # Checks if a point (x,y) matches with the protein's position.
    # @param x: x-coordinate of the point.
    # @param y: y-coordinate of the point.
    def match_position(self, x, y):
        x2 = self.x1 + self.width
        y2 = self.y1 + self.height
        range_val = 2
        return x >= self.x1 - range_val and x <= x2 + range_val and y >= self.y1 - range_val and y <= y2 + range_val

    # Sets the width of the protein representation in the GUI.
    # @param w: The desired width value.
    def set_width(self, w):
        self.width = w

    # Returns the current value of the decider.
    def get_decider(self):
        return self.decider

    # Sets the decider value.
    # @param i: The desired decider value.
    def set_decider(self, i):
        self.decider = i

    # Sets the scaling factor.
    # @param f: The scaling factor value.
    def set_host_scale_factor(self, f):
        self.scale_factor = f

    # Sets the maximum possible position for the protein.
    # @param i: The maximum position value.
    def set_max_position(self, i):
        self.max_position = i

    # Sets the concentration of the protein.
    # @param i: New concentration value to be set.
    def set_concentration(self, i):
        self.concentration = i

    # Checks if a given point (x,y) is close to the protein's plotting position.
    # The point is considered a match if it is within a range of 3 units from the protein's position.
    # @param x: x-coordinate of the point.
    # @param y: y-coordinate of the point.
    # @return: True if the point matches the protein's plotting position, False otherwise.
    def match_plot_position(self, x, y):
        range_val = 3
        return x >= self.plot_x_pos - range_val and x <= self.plot_x_pos + range_val and y >= self.plot_y_pos - range_val and y <= self.plot_y_pos + range_val

    # Calculates the distance traveled by the protein based on the scale factor.
    # The distance is determined as the scaled difference between the current and starting y-coordinates.
    # @return: Calculated distance traveled by the protein.
    def get_distance(self):
        self.distance = self.scale_factor * (self.y1 - self.start_y)
        return self.distance

    # Utilizes Biopython SeqIO library to parse through a fasta file given by the user and collect
    # information stored within the file
    # @return: Sequence identifier, amino acid sequence, length of amino acid sequence
    def parse_protein(self, file):
        seq_id = ""
        sequence = ""
        seq_len = 0
        seq_name = ""
        for seq_record in SeqIO.parse(file, "fasta"):
            seq_id = seq_record.id
            sequence = seq_record.seq
            seq_len = len(seq_record)
            seq_name = seq_record.description
        return seq_id, sequence, seq_len, seq_name

    # Utilizes the ProteinAnalysis object to get a sequence of amino acids and calculate the molecular weight
    # @return: molecular weight of the protein from fasta file given by user
    def get_mw(self, file):
        seq = ProteinAnalysis(self.parse_protein(file)[1])
        self.mw = seq.molecular_weight()
        return self.mw

    # Utilizes the ProteinAnalysis object to get a sequence of amino acids and finds the number of amino acids
    # @return: the number of amino acids from fasta file given by user
    def get_amino_acid_count(self, file):
        seq = ProteinAnalysis(self.parse_protein(file)[1])
        return seq.count_amino_acids()

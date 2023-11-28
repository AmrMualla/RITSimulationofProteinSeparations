"""
Class to hold information about Parameters for Python GUI, likely
not necessary since frontend will be handled by Javascript.
@author Bader Alharbi, Mack Leonard
"""


import tkinter as tk


class Protein:
    def __init__(self, name, full_name, abbr, mw, color):
        self.name = name
        self.full_name = full_name
        self.abbr = abbr
        self.mw = mw
        self.color = color
        self.speed = 0.0
        self.selected = False
        self.decider = False

    def set_decider(self, value):
        self.decider = value

    def reset_decider(self):
        self.decider = False

class Acrylamide:
    def __init__(self, percent_gel, suppressor):
        self.percent_gel = percent_gel
        self.suppressor = suppressor

class Electrophoresis:
    def __init__(self):
        self.selected_speed = Constants.medium
        self.selected_sample = None
        self.selected_gel = None
        self.std1_ref = 0

    def set_acrylamide(self, gel):
        self.selected_gel = gel

    def set_animation_speed(self, speed):
        self.selected_speed = speed

    def display_protein(self, protein):
        pass

    def add_standard(self):
        pass

    def add_sample(self):
        pass

    def start_run(self, std_protein_array, selected_sample, dye1, dye2):
        pass

    def stop_run(self):
        pass

    def set_plot_data(self, std_protein_array, selected_sample, dye1):
        pass

class Constants:
    slow = "Slow"
    moderate = "Moderate"
    fast = "Fast"
    low = 1.0
    medium = 1.5
    high = 2.0
    highX2 = 4.0
    gel1 = Acrylamide("6%", 12.0)
    gel2 = Acrylamide("8%", 10.0)
    gel3 = Acrylamide("10%", 7.5)
    gel4 = Acrylamide("12%", 5.0)

class Parameters(tk.Frame, Constants):
    def __init__(self, master):
        super().__init__(master)

        self.selected_sample = None
        self.selected_gel = None
        self.std1_ref = 0
        self.selected_speed = self.medium

        self.std_protein_array = [None] * 7
        self.unknown1 = Protein("Unknown #1", "Aconitase", "Acon", 0x14250, "black")
        self.unknown2 = Protein("Unknown #2", "Conconavalin A", "Con A", 25556, "black")
        self.unknown3 = Protein("Unknown #3", "Glucose Oxidase", "GO", 63058, "black")
        self.unknown4 = Protein("Unknown #4", "Neuraminidase", "Neur", 43505, "black")
        self.unknown5 = Protein("Unknown #5", "Phosphorylase b", "Phos b", 0x172f9, "black")
        self.unknown6 = Protein("Unknown #6", "Pyruvate Kinase", "Pyr Kin", 56773, "black")
        self.unknown7 = Protein("Unknown #7", "Ribonuclease A", "Ribo A", 13673, "black")
        self.unknown8 = Protein("Unknown #8", "Chymotrypsinogen", "Chymo", 23564, "black")
        self.unknown9 = Protein("Unknown #9", "p-Hydroxybenzoate", "Hydrox", 43939, "black")
        self.unknown10 = Protein("Unknown #10", "Ribonuclease H", "Ribo H", 16638, "black")

        samples = [self.unknown1.name, self.unknown2.name, self.unknown3.name,
                   self.unknown4.name, self.unknown5.name, self.unknown6.name, self.unknown7.name,
                   self.unknown8.name, self.unknown9.name, self.unknown10.name]
        gel_list = [self.gel1.percent_gel, self.gel2.percent_gel, self.gel3.percent_gel, self.gel4.percent_gel]

        self.acrylamide = tk.StringVar()
        self.sample = tk.StringVar()
        self.voltage = tk.IntVar()
        self.speed = tk.IntVar()
        self.std1_ref = 0

        self.dye_color = ""
        self.parent = master

        self.std_protein_array[self.std1_ref] = Protein("Standard #1", "beta-Galactosidase", "b-gal", 0x1c58b, "blue")
        self.std_protein_array[self.std1_ref + 1] = Protein("Standard #2", "Ovalbumin", "oval", 42734, "yellow")
        self.std_protein_array[self.std1_ref + 2] = Protein("Standard #3", "Carbonic Anhydrase", "carb anh", 29011, "gray")
        self.std_protein_array[self.std1_ref + 3] = Protein("Standard #4", "Triose Phosphate Isomerase", "TIM", 26527, "green")
        self.std_protein_array[self.std1_ref + 4] = Protein("Standard #5", "Myoglobin", "Myo", 17183, "magenta")
        self.std_protein_array[self.std1_ref + 5] = Protein("Standard #6", "Lysozyme", "Lyso", 14296, "white")
        self.std_protein_array[self.std1_ref + 6] = Protein("Standard #7", "MassSpec.Trypsin Inhibitor", "BPTI", 6500, "red")

        border = tk.Label(self, text="ELECTROPHORESIS PARAMETERS", relief=tk.RAISED)
        border1 = tk.Label(self, text="Animation Speed", relief=tk.RAISED)

        self.set_panels_colors()

        header_panel = tk.Frame(self)
        header_sub2 = tk.Frame(self)
        label_panel1 = tk.Frame(self)
        label_panel2 = tk.Frame(self)
        drop_panel = tk.Frame(self)
        selection_panel1 = tk.Frame(self)
        selection_panel2 = tk.Frame(self)
        standard_panel = tk.Frame(self)
        color_panel = tk.Frame(self)
        voltage_panel = tk.Frame(self)
        voltage_sub2_panel = tk.Frame(self)

        self.set_layout()

        # Create radio buttons for animation speed
        speed1_button = tk.Radiobutton(header_sub2, text=self.slow, value=self.low, variable=self.speed)
        speed2_button = tk.Radiobutton(header_sub2, text=self.moderate, value=self.medium, variable=self.speed)
        speed3_button = tk.Radiobutton(header_sub2, text=self.fast, value=self.high, variable=self.speed)

        # Create radio buttons for voltage
        volt1 = tk.Radiobutton(voltage_sub2_panel, text="50V", value=50, variable=self.voltage)
        volt2 = tk.Radiobutton(voltage_sub2_panel, text="100V", value=100, variable=self.voltage)
        volt3 = tk.Radiobutton(voltage_sub2_panel, text="150V", value=150, variable=self.voltage)
        volt4 = tk.Radiobutton(voltage_sub2_panel, text="200V", value=200, variable=self.voltage)

        # Create labels
        unknown_label = tk.Label(label_panel1, text="Unknown Proteins")
        percent_acrylamide_label = tk.Label(label_panel1, text="% Acrylamide")
        standards_label = tk.Label(label_panel2, text="Standards")

        unknown_label_tooltip = tk.Label(unknown_label, text="Set of unknown samples")
        percent_acrylamide_tooltip = tk.Label(percent_acrylamide_label, text="Affects the density of the gel")
        standards_label_tooltip = tk.Label(standards_label, text="Set of known values for comparison")

        self.speed.set(self.medium)
        speed2_button.select()
        self.voltage.set(150)
        volt3.select()

        # Add components to the frame
        unknown_label_tooltip.grid(row=0, column=0, padx=5)
        percent_acrylamide_tooltip.grid(row=0, column=1, padx=5)
        standards_label_tooltip.grid(row=0, column=0, padx=5)
        unknown_label.grid(row=1, column=0, padx=5)
        percent_acrylamide_label.grid(row=1, column=1, padx=5)
        standards_label.grid(row=1, column=0, padx=5)

        speed1_button.grid(row=0, column=0, padx=5)
        speed2_button.grid(row=0, column=1, padx=5)
        speed3_button.grid(row=0, column=2, padx=5)

        volt1.grid(row=0, column=0, padx=5)
        volt2.grid(row=0, column=1, padx=5)
        volt3.grid(row=0, column=2, padx=5)
        volt4.grid(row=0, column=3, padx=5)

        self.pack()

    def set_panels_colors(self):
        self.configure(bg="light gray")
        header_panel.configure(bg="light gray")
        selection_panel1.configure(bg="light gray")
        selection_panel2.configure(bg="light gray")
        standard_panel.configure(bg="light gray")
        voltage_panel.configure(bg="light gray")
        voltage_sub1_panel.configure(bg="light gray")
        voltage_sub2_panel.configure(bg="light gray")
        label_panel1.configure(bg="light gray")
        label_panel2.configure(bg="light gray")
        drop_panel.configure(bg="light gray")

    def set_layout(self):
        header_panel.grid(row=0, column=0)
        header_sub2.grid(row=1, column=0)
        label_panel1.grid(row=2, column=0)
        label_panel2.grid(row=3, column=0)
        drop_panel.grid(row=4, column=0)
        selection_panel1.grid(row=5, column=0)
        selection_panel2.grid(row=5, column=1)
        voltage_panel.grid(row=6, column=0)
        voltage_sub1_panel.grid(row=0, column=0)
        voltage_sub2_panel.grid(row=1, column=0)
        color_panel.grid(row=2, column=0)
        standard_panel.grid(row=2, column=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = Parameters(master=root)
    app.mainloop()

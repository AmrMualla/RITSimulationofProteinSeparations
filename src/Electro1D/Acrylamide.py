# Acrylamide class
#
# @author Chase Amador and Bader Alharbi
# class is responsible for holding the Acclaimed gel parameters (the percentage and the numerical factor that affect the bands speed on)
class Acrylamide:

    #default parametrized  constructor that take the percentage & numerical factor
    #
    # @param s the Acrylamide gel concentration percentage
    # @param d numerical factor
    def __init__(self, s, d):
        self.percent_gel = "0.0%"
        self.suppressor = 1
        self.percent_gel = s
        self.concentration = d
        self.set_suppressor(d)

    
    # getConc() get the Acrylamide gel concentration
    #
    # @return concentration
    def get_conc(self):
        return self.concentration

	# set the numerical factor (suppressor)
	#
	# @param d concentration
    def set_suppressor(self, d):
        self.suppressor = 6 if d > 12 else (3 if d > 10 else (2 if d > 7.5 else 1))


# Example usage:
# Create an Acrylamide object
acrylamide_obj = Acrylamide("10.0%", 11.0)

# Access properties and methods
print(f"Acrylamide concentration: {acrylamide_obj.get_conc()}")
print(f"Suppressor: {acrylamide_obj.suppressor}")
class Person:
    """Class container with properties of a person"""

    # --------- MAGIC METHODS ---------
    def __init__(self, name=""):
        """Constructor"""
        self.name = name
        self._height = 0
        self._weight = 0

    # --------- PROPERTIES ---------
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Height must be a number.")
        if not (0 < value < 2.4):
            raise ValueError("Height must between 0 < X < 2.4 m.")
        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Weight must be a number.")
        if not (0 < value < 200):
            raise ValueError("Weight must between 0 < X < 200 kg.")
        self._weight = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value.strip().title()

    # --------- NORMAL METHODS ---------
    def bmi(self):
        """Calculate the bmi of this person
        Returns:
            A floating point number as BMI
        Raises:
            ValueError: when divide by 0
        """
        if self.height == 0:
            raise ValueError("Height can't be zero")
        return self.weight / (self.height * self.height)

    def print_bmi_string(self):
        """Show a human readable text of the bmi."""
        bmi = self.bmi()
        bmi_str = f"{self.name} you have a BMI of {bmi:0.2f}.\n\n"
        if bmi < 18.5:
            bmi_str += "UNDERWEIGHT:\n Increase your weight."
        elif bmi < 25:
            bmi_str += "NORMAL WEIGHT:\n Keep your weight that way."
        elif bmi < 30:
            bmi_str += "OVERWEIGHT:\n Try to lose weight."
        else:
            bmi_str += "OBESITY:\n Let yourself be assisted by a specialist."
        return bmi_str


# --------- TEST ZONE ---------
if __name__ == '__main__':
    person1 = Person('StiJn tas')
    person1.weight = 98
    person1.height = 1.8
    print(person1.bmi(), person1.name)

"""
File: taxformwithgui.py
Project 8.1
A GUI-based tax calculator.

Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and a flat tax rate
of 20%.
"""

from breezypythongui import EasyFrame


class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Tax Calculator")

        # Label and field for the income
        self.addLabel(text="Gross Income", row=0, column=0)
        self.incomeField = self.addFloatField(0.0, 0, 1, 2, precision=2)

        # Label and field for the number of dependents
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(0, 1, 2)

        # The command button
        self.addButton("Compute", 2, 1, command=self.computeTax)

        # Label and field for the tax
        self.addLabel("Total Tax", 3, 0)
        self.taxField = self.addFloatField(0, 3, 1, 2, precision=2, state="readonly")

    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field."""
        gross_income = float(self.incomeField.getValue())
        dependents = int(self.depField.getValue())
        result = float(((gross_income - (dependents * 3000)) - 10000) * 0.2)
        self.taxField.setValue(result)


def main():
    TaxCalculator().mainloop()


if __name__ == "__main__":
    main()


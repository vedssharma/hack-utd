from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
content = ttk.Frame(root)

def handle_click():
    if is_valid() == False:
        error_message = ttk.Label(content, text="Please enter only numbers")
        error_message.grid(column=0, row=8)
    else:
        calculate_approval()

button = ttk.Button(content, text="Check Approval", command=handle_click)

error = False

# user variables for input
creditScore = StringVar()
monthlyIncome = StringVar()
monthlyCarPayment = StringVar()
monthlyCreditCardPayment = StringVar()
appraisedValue = StringVar()
downPayment = StringVar()
monthlyMortgagePayment = StringVar()

# labels for user input
creditScoreLabel = ttk.Label(content, text="Enter your credit score: ")
monthlyIncomeLabel = ttk.Label(content, text="Enter your monthly income: ")
monthlyCarPaymentLabel = ttk.Label(content, text="Enter your monthly car payment: ")
monthlyCreditCardPaymentLabel = ttk.Label(content, text="Enter your monthly credit card payment: ")
appraisedValueLabel = ttk.Label(content, text="Enter the appraised value of the home: ")
downPaymentLabel = ttk.Label(content, text="Enter the down payment: ")
monthlyMortgagePaymentLabel = ttk.Label(content, text="Enter the monthly mortgage payment: ")

# user input fields
creditScoreInput = ttk.Entry(content, width=7, textvariable=creditScore)
monthlyIncomeInput = ttk.Entry(content, width=7, textvariable=monthlyIncome)
monthlyCarPaymentInput = ttk.Entry(content, width=7, textvariable=monthlyCarPayment)
monthlyCreditCardPaymentInput = ttk.Entry(content, width=7, textvariable=monthlyCreditCardPayment)
appraisedValueInput = ttk.Entry(content, width=7, textvariable=appraisedValue)
downPaymentInput = ttk.Entry(content, width=7, textvariable=downPayment)
monthlyMortgagePaymentInput = ttk.Entry(content, width=7, textvariable=monthlyMortgagePayment)

def calculate_approval():
    pass

def is_valid():
    if not creditScoreInput.get().isnumeric() or not monthlyIncomeInput.get().isnumeric() or not monthlyCarPaymentInput.get().isnumeric() or not monthlyCreditCardPaymentInput.get().isnumeric() or not appraisedValueInput.get().isnumeric() or not downPaymentInput.get().isnumeric() or not monthlyMortgagePaymentInput.get().isnumeric():
        return False
    else:
        pass
    

creditScore = creditScoreInput.get()
monthlyIncome = monthlyIncomeInput.get()
monthlyCarPayment = monthlyCarPaymentInput.get()
monthlyCreditCardPayment = monthlyCreditCardPaymentInput.get()
appraisedValue = appraisedValueInput.get()
downPayment = downPaymentInput.get()
monthlyMortgagePayment = monthlyMortgagePaymentInput.get()

# grid layout
content.grid(column=0, row=0)
creditScoreLabel.grid(column=0, row=0)
monthlyIncomeLabel.grid(column=0, row=1)
monthlyCarPaymentLabel.grid(column=0, row=2)
monthlyCreditCardPaymentLabel.grid(column=0, row=3)
appraisedValueLabel.grid(column=0, row=4)
downPaymentLabel.grid(column=0, row=5)
monthlyMortgagePaymentLabel.grid(column=0, row=6)

creditScoreInput.grid(column=1, row=0)
monthlyIncomeInput.grid(column=1, row=1)
monthlyCarPaymentInput.grid(column=1, row=2)
monthlyCreditCardPaymentInput.grid(column=1, row=3)
appraisedValueInput.grid(column=1, row=4)
downPaymentInput.grid(column=1, row=5)
monthlyMortgagePaymentInput.grid(column=1, row=6)
button.grid(column=0, row=7)

# main loop
root.mainloop()

#LEVEL 1
#INPUT STATEMENTS
nameOfEmployee = input("Enter the name of the employee: ")
employeeId = input("Enter the employee ID: ")
basicMonthlySalary = float(input("Enter the basic monthly salary: "))
specialAllowances = float(input("Enter the special allowances: "))
bonusPercentage = float(input("Enter the bonus percentage(%): "))
#CALCULATIONS
grossMonthlySalary = basicMonthlySalary + specialAllowances
annualBonus = (bonusPercentage / 100) * (grossMonthlySalary * 12)
annualGrossSalary = (grossMonthlySalary * 12) + annualBonus
print()
#DISPLAYING RESULT 
print(f"Employee Name: {nameOfEmployee}")
print(f"Gross Monthly Salary: {grossMonthlySalary:.2f}")
print()

#LEVEL 2
#TO CALCULATE TAXABLE INCOME
standardDeduction = 50000
taxableIncome = annualGrossSalary - standardDeduction
#CHECKING IF TAXABLE INCOME IS NEGATIVE
if taxableIncome < 0:
    taxableIncome = 0
#DISPLAYING RESULT 
print(("---TAXABLE INCOME CALCULATION---"))
print(f"Annual Gross Salary: {annualGrossSalary:.2f}")
print(f"Standard Deduction: {standardDeduction:.2f}")
print(f"Taxable Income: {taxableIncome:.2f}")
print()

#LEVEL 3
taxP = 0 #tax percentage
taxSlab = 0 #tax slab
if taxableIncome <= 300000 :
    taxP = 0
    taxSlab = "Upto Rs 3 Lakhs"
elif taxableIncome <= 600000 :
    taxP = 5
    taxSlab = "From 3,00,001 to 6,00,000"
elif taxableIncome <= 900000 :
    taxP = 10
    taxSlab = "From 6,00,001 to 9,00,000"
elif taxableIncome <= 1200000 :
    taxP = 15
    taxSlab = "From 9,00,001 to 12,00,000"
elif taxableIncome <= 1500000 :
    taxP = 20
    taxSlab = "From 12,00,001 to 15,00,000"
else :
    taxP = 30
    taxSlab = "Above 15,00,000"

#APPLYING SECTION 87A REBATE
if taxableIncome <= 700000:
    taxP = 0
    taxSlab = "NO TAX SLAB"

#ADDING 4% HEALTH & EDUCATION CESS
taxP +=4 
#CALCULATING TAX PAYABLE
taxPayable = (taxP / 100) * taxableIncome

#RESULT
print("---TAX CALCULATION---")
print(f"TAX Slab : {taxSlab}")
print("ADDING 4% HEALTH & EDUCATION CESS")
print(f"Tax percentage is: {taxP}%")
print(f"Tax Payable: {taxPayable:.2f}")
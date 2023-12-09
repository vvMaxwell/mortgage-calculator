#inputs from user
clientName = input("Enter client name: ")
clientAddress = input("Enter address of property: ")
propertyPriceInput = float(input("Enter purchase: "))
#5 percent
if propertyPriceInput <= 499999:
    fivePercentTax = propertyPriceInput * 0.05
    percentTax = (fivePercentTax / propertyPriceInput) * 100
#5 & 10 percent
elif propertyPriceInput >= 500000:
    if propertyPriceInput < 1000000:
        fiveAndTenPercentTax = ((500000 * 0.05)) + (((propertyPriceInput - 500000) * 0.10))
        percentTax = (fiveAndTenPercentTax / propertyPriceInput) * 100
#20 percent
if propertyPriceInput >= 1000000:
    twentyPercentTax = propertyPriceInput * 0.2
    percentTax = (twentyPercentTax / propertyPriceInput) * 100
downPaymentPercent = int(input(f"Enter down payment percentage (minimum {percentTax:.3f}): "))

while True:
    if downPaymentPercent < percentTax:
        print("Please enter a value between the minimum and 100")
        downPaymentPercent = float(input(f"Enter down payment percentage (minimum {percentTax:.3f}): "))
    elif downPaymentPercent > 100:
        print("Please enter a value between the minumum and 100")
        downPaymentPercent = float(input(f"Enter down payment percentage (minimum {percentTax:.3f}): "))
    elif downPaymentPercent >= percentTax:
            break
    continue

downPayment = (downPaymentPercent / 100) * propertyPriceInput
print(f"Down payment amount is ${downPayment:.0f}")

#mortgage insurance & mortgage amount
if downPaymentPercent >= 5 and downPaymentPercent < 10:
    mortgageInsurancePremium = 4
    insuranceCost = (propertyPriceInput - downPayment) * mortgageInsurancePremium / 100
    principalAmount = propertyPriceInput - downPayment + insuranceCost
elif downPaymentPercent >= 10 and downPaymentPercent < 15:
    mortgageInsurancePremium = 3.1
    insuranceCost = (propertyPriceInput - downPayment) * mortgageInsurancePremium / 100
    principalAmount = propertyPriceInput - downPayment + insuranceCost
elif downPaymentPercent >= 10 and downPaymentPercent < 15:
    mortgageInsurancePremium = 2.8
    insuranceCost = (propertyPriceInput - downPayment) * mortgageInsurancePremium / 100
    principalAmount = propertyPriceInput - downPayment + insuranceCost
else:
    downPaymentPercent >= 20
    mortgageInsurancePremium = 0
    insuranceCost = (propertyPriceInput - downPayment) * mortgageInsurancePremium / 100
    principalAmount = propertyPriceInput - downPayment + insuranceCost

insuranceCost = (propertyPriceInput - downPayment) * mortgageInsurancePremium / 100
print(f"Mortgage insurance propertyPriceInput is ${insuranceCost:,.0f} ")
totalMortgageAmount = propertyPriceInput - downPayment + insuranceCost
print(f"Total mortgage amount is ${totalMortgageAmount:,.0f} ")

#mortgage terms
mortgageTerms = [1,2,3,5,10]
mortgageTerm = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))

#mortgage interest rates
if mortgageTerm == 1:
    interestRate = 0.0595
elif mortgageTerm == 2:
    interestRate = 0.059
elif mortgageTerm == 3:
    interestRate = 0.056
elif mortgageTerm == 5:
    interestRate = 0.0529
else: 
    mortgageTerm == 10
    interestRate = 0.06

#validations
while mortgageTerm not in [1, 2, 3, 5, 10]:
    print("Please enter the correct term")
    mortgageTerm = float(input("Enter Term (1, 2, 3, 5, 10): "))

mortgageAmortization = float(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
validationForMA = [5, 10, 15, 20, 25]
while mortgageAmortization not in validationForMA:
        print("Please enter a valid choice")
        mortgageAmortization = float(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))

#emr
emr = ((1 + interestRate / 2)**2)**(1 / 12) - 1
monthly_amort = 12 * mortgageAmortization
printInterestRate = interestRate * 100
print(f"Interest rate for the term is: {printInterestRate:.2f}%")

#monthly payment calculator
monthlyPayment = totalMortgageAmount * (emr) * (1 + (emr))**monthly_amort / (((1 + emr)**monthly_amort) - 1)
print(f"Montly payment amount is: ${monthlyPayment:.0f}")

#tables
table = input("Would you like to see the amorization table? (Y/N): ")
if table.upper() == "N":
    exit()
while table.upper() == "Y":
    print("                        Monthly Amortization Schedule                        \n"
        f"{'Month':<8}{'Open Bal':<15}{'Payment':<15}{'Principal':<15}{'Interest':<15}{'Closing Bal':<15}")

    monthlyTerm = mortgageTerm * 12
    totalInterest = 0
    totalPrincipal = 0

    for i in range(int(monthlyTerm)):
        initialPrice = principalAmount
        monthlyInterest = principalAmount * emr
        definedMonthlyInterest = monthlyInterest

        monthlyPrincipalAmount = monthlyPayment - definedMonthlyInterest
        definedPrincipalAmount = monthlyPrincipalAmount

        closingBalance = principalAmount - definedPrincipalAmount
        definedClosingBalance = closingBalance

        payment = monthlyPayment

        principalAmount -= definedPrincipalAmount

        totalInterest += definedMonthlyInterest
        totalPrincipal += definedPrincipalAmount

        print(f"{i + 1:<6}\t{initialPrice:.2f}{payment:.2f}{definedPrincipalAmount:.2f}{definedMonthlyInterest:.2f}{definedClosingBalance:.2f}")
    print(f"==================================================================================\nTotal                         {totalPrincipal:.2f}       {totalInterest:.2f}")
    break

salesMenCount = int(input("How many salesmen? "))
totalQuarters = 4
q1Total = 0
q2Total = 0
q3Total = 0
q4Total = 0

highestAnnualSales = 0
highestSalesMen = 0

# Salesmen Quarterly Sales
grandTotal = 0

for salesMen in range(1, salesMenCount + 1):
    currentTotalSales = 0

    print(f"Input quarterly sales for salesman {salesMen} :")

    for quarter in range(1, totalQuarters + 1):

        currentQuarter = float(input(f"\t\tQuarter {quarter} : "))
        currentTotalSales += currentQuarter

        match quarter:
            case 1:
                q1Total += currentQuarter
            case 2:
                q2Total += currentQuarter
            case 3:
                q3Total += currentQuarter
            case 4:
                q4Total += currentQuarter

    if currentTotalSales > highestAnnualSales:
        highestAnnualSales = currentTotalSales
        highestSalesMen += 1

    print(f"\tTotal Sales for Salesman {salesMen} : {currentTotalSales:,.2f}")
    grandTotal += currentTotalSales

print(f"Total Sales: {grandTotal:,.2f}")
print(f"Average Sales for Q1: {q1Total/salesMenCount:,.2f}")
print(f"Average Sales for Q2: {q2Total/salesMenCount:,.2f}")
print(f"Average Sales for Q3: {q3Total/salesMenCount:,.2f}")
print(f"Average Sales for Q4: {q4Total/salesMenCount:,.2f}")
print(f"Salesmen {highestSalesMen} has the highest annual sales of {highestAnnualSales:,.2f}")
print(f"Bonus: {highestAnnualSales * 0.15:,.2f}")

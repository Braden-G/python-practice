Sal = float(input("enter your annual salary\n"))
#percentsaving = float(input("what percent will be saved a year as a decimal?\n"))
totalCost = 1000000
semi_annual_raise = 0.07
downpayment = totalCost * 0.25
savedamount = 0
r = 0.04
tolerance = downpayment / 100
steps = 0
low = 0
high = 10000
guess = (high + low) // 2
month = 0

while abs(savedamount - downpayment) >= 100:
    savedamount = 0
    for_annual_salary = Sal
    rate = guess/10000
    for month in range(36):
        if month % 6 == 0 and month > 0:
            for_annual_salary += for_annual_salary*semi_annual_raise
        monthly_sal = for_annual_salary/12
        savedamount += monthly_sal*rate+savedamount*r/12
    if savedamount > downpayment:
            high = guess
    else:
            low = guess
    guess = (high + low)/2  
    steps += 1
    if steps > 13:
        break
if steps > 13:
    print("It is not possible to save enough for the down payment")
else:
    print("best savings rate ", rate)
    print(steps +1)
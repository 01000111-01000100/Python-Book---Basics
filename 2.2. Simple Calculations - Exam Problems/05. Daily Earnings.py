working_days = int(input())
profit_per_day = float(input())
currency_rate = float(input())

monthly_salary = working_days * profit_per_day
annual_earning = monthly_salary * 12 + monthly_salary * 2.5
taxes = annual_earning * 0.25
net_annual_earnings = (annual_earning - taxes)
salary_in_leva = net_annual_earnings * currency_rate
print("%.2f" % (salary_in_leva / 365))
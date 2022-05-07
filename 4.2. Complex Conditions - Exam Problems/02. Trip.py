budget = float(input())
season = input()

destination_result = ""
holiday_information = ""
money_spend = 0.00

if budget <= 100:
    destination_result = "Bulgaria"
    if season == "summer":
        money_spend = 0.30 * budget
        holiday_information = f"Camp - {money_spend:.2f}"
    else:
        money_spend = 0.70 * budget
        holiday_information = f"Hotel - {money_spend:.2f}"
elif budget <= 1000:
    destination_result = "Balkans"
    if season == "summer":
        money_spend = 0.40 * budget
        holiday_information = f"Camp - {money_spend:.2f}"
    else:
        money_spend = 0.80 * budget
        holiday_information = f"Hotel - {money_spend:.2f}"
else:
    destination_result = "Europe"
    money_spend = 0.90 * budget
    holiday_information = f"Hotel - {money_spend:.2f}"
print("Somewhere in " + destination_result)
print(holiday_information)
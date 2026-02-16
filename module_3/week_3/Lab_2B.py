total_income = float(input("Enter your total income this year: "))
owed_taxes = 0
if total_income > 609350:
    owed_taxes += (total_income - 609350) * 0.37 

if 243725 < total_income <= 609350:
    owed_taxes += 0.35 * (total_income - 243725)
elif total_income > 609350:
    owed_taxes += (609350 - 243725) * 0.35

if 191950 < total_income <= 243725:
    owed_taxes += 0.32 * (total_income - 191950)
elif total_income > 243725:
    owed_taxes += (243725 - 191950) * 0.32

if 100525 < total_income <= 191950:
    owed_taxes += (total_income - 100525)* 0.24
elif total_income > 191950:
    owed_taxes += (191950 - 100525) * 0.24

if 47150 < total_income <= 100525:
    owed_taxes += (total_income - 47150) * 0.22
elif total_income > 100525:
    owed_taxes += (100525 - 47150) * 0.22


if 11600 < total_income <= 47150:
    owed_taxes += (total_income - 11600) * 0.12
elif total_income > 47150:
    owed_taxes += (47150 - 11600) * 0.12

if total_income <= 11600:
    owed_taxes += total_income * 0.10
else:
    owed_taxes+= 11600 * 0.10

print(f"You owe ${owed_taxes:.2f} this year.")
has_good_credit = True
has_high_income = True
has_criminal_record = True
if has_good_credit and has_high_income:
    print("you are eligible for a loan in full")
elif has_high_income or has_good_credit:
    print("eligible for half the loan")
else:
    print("not eligible for a loan")
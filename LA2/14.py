tax_inc=int(input("Enter Taxable Income :"))
if tax_inc<=20000:
    tax=0.02*tax_inc
else:
    if tax_inc<=50000:
        tax=400+0.025*(tax_inc-20000)
    else:
        tax=1150+0.035*(tax_inc-50000)
print(tax)

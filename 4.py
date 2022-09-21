p=float(input("Enter the initial principal balance:"))
r=float(input("Enter the interest rate:"))
t=float(input("enter the no. of time periods elapsed:"))
print(f"The final amount with compound interest is:{p*(((1+r/(100))**(t)))}")
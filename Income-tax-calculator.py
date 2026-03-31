# Progressive tax calculator
salary = float(input("enter salary: "))

if salary <= 30000:
    total_tax = (salary * 0.05)
elif salary > 30000 and salary <= 70000:
    total_tax = ((30000 * 0.05) + ((salary - 30000) * 0.15))
elif salary > 70000:
    total_tax = ((30000 * 0.05) + (40000 * 0.15) + ((salary - 70000) * 0.25)) 

print(f"Total tax owed: {total_tax:,.2f}")
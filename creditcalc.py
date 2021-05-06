import math
import argparse
import sys

def annuity_payment(principal, periods, interest):
    payment = math.ceil(principal * interest * (1 + interest) ** periods / ((1 + interest) ** periods - 1))
    print(f"Your monthly payment = {payment}!")
    return payment

def annuity_periods(principal, payment, interest):
    periods = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
    if periods == 1:
        print(f"It will take 1 month to repay this loan!")
    elif periods < 12:
        print(f"It will take {periods} months to repay this loan!")
    elif periods == 12:
        print("It will take 1 year to repay this loan!")
    elif periods == 13:
        print("It will take 1 year and 1 month to repay this loan!")
    else:
        years = periods // 12
        if periods == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} year and {periods % 12} months to repay this loan!")
    return periods

def annuity_principal(periods, payment, interest):
    principal = math.floor(payment * ((1 + interest) ** periods - 1) / (interest * (1 + interest) ** periods))
    print(f"Your loan principal = {principal}!")
    return principal

def diff_payment(principal, periods, interest):
    payment = list()
    for i in range(periods):
        payment.append(math.ceil(principal / periods + interest * (principal - principal * i / periods)))
    for i in range(periods):
        print(f"Month {i + 1}: payment is {payment[i]}")
    return payment

def is_valid_arguments(args):
    if args.type == None:
        return False
    if args.interest == None:
        return False
    if args.type == "diff":
        if not (args.principal != None and args.periods != None and args.payment == None):
            return False 
    elif args.type == "annuity":
        if args.principal == None:
            if not (args.payment != None and args.periods != None):
                return False
        elif args.periods == None:
            if not (args.payment != None and args.principal != None):
                return False
        elif args.payment == None:
            if not (args.principal != None and args.periods != None):
                return False
    else:
        return False

    if float(args.interest) < 0:
        return False
    
    if args.principal != None:
        if int(args.principal) < 0:
            return False
    
    if args.periods != None:
        if int(args.periods) < 0:
            return False

    if args.payment != None:
        if float(args.payment) < 0:
            return False

    return True
    
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args = parser.parse_args()
if not is_valid_arguments(args):
    print("Incorrect parameters")
    sys.exit()

type = args.type
principal= args.principal
periods = args.periods
payment = args.payment
interest = float(args.interest) / (100 * 12)

if type == "annuity":
    if periods == None:
        periods = annuity_periods(int(principal), float(payment), interest)
    elif payment == None:
        payment = annuity_payment(int(principal), int(periods), interest)
    elif principal == None:
        principal = annuity_principal(int(periods), float(payment), interest)
    overpayment = int(payment) * int(periods) - int(principal)
elif type == "diff":
    payment = diff_payment(int(principal), int(periods), interest)
    print()
    overpayment = sum(payment) - int(principal)

print(f"Overpayment = {overpayment}")
import os

if not os.path.exists('ledger.txt'):
    with open('ledger.txt','w') as z:
        z.write('0')

def total_balance():
    with open('ledger.txt','r') as z:
        balance = float(z.read())
    print(f'Your current balance is: ${balance:.2f}')
    
def a_debit():
    value = input("How much is the debit (withdraw)?\n Use Format = ####.## no comma or $\n" )
    try:
        value = float(value)
        if value < 0:
            raise ValueError
    except ValueError:
        print('Please check your format and try again')
        a_debit()
        return
    with open('ledger.txt','r') as z:
        balance = float(z.read())
    if value > balance:
        print('You dont have that much $$$$, GO HOME!!')
        return
    balance -= value
    with open('ledger.txt','w') as z:
        z.write(str(balance))
        print(f'Withdraw successful, new balance is: ${balance:.2f}')

def a_credit():
    value = input("How much is the credit (deposit)?\n Format = ####.## no comma or $\n" )
    try:
        value = float(value)
        if value < 0:
            raise ValueError
    except ValueError:
        print('Please check format and try again')
        a_credit()
        return
    with open('ledger.txt','r') as z:
        balance = float(z.read())
    balance += value
    with open('ledger.txt','w') as z:
        z.write(str(balance))
        print(f'Deposit successful, new balance is: ${balance:.2f}')
    
def back_to_the_furture():
    print("Don't worry. As long as you hit that wire with the connecting hook at precisely 88 miles per hour, the instant the lightning strikes the tower... everything will be fine -- Dr. Emmett Brown")
def flux_capacitor():
    with open('ledger.txt','r') as z:
        balance = float(z.read())
    print("GREAT SCOTT!!! Time Travel at your own RISK!")
    print("Plutonium is required to properly operate the flux capacitor")
    print("Plutonium is used by the onboard nuclear reactor")
    print("which then powers the flux capacitor to provide the needed 1.21 gigawatts of electrical power.")
    print("Please contact your local plutonium supplier.")
    print(f"But, with a balance of ${balance:.2f}, I wouldn't waste your time")
while True:
    choice = input("   ---  Welcome to your terminal checkbook!  --- \n\nWhat would you like to do?\n\nMake a selection using 1-4\n  1) view current balance\n  2) record a debit (withdraw)\n  3) record a credit (deposit)\n  4) exit\nYour choice (1-4)?: ")
    if choice == '1':
        total_balance() 
    elif choice == '2':
        a_debit()
    elif choice == '3':
        a_credit()
    elif choice == '4':
        print("Have a good day!")
        quit()
    elif choice == '88':
        back_to_the_furture() 
    elif choice == '121':
        flux_capacitor()     
    else:
        print("Please try again, something is wrong with your input")

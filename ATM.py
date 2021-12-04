while True:
    balance=10000
    print("   ATM    ")
    print('''
    1)        Balance
    2)        withdraw
    3)        Deposit
    4)        Quit
    ''')
    try:
        Option=int(input("Enter Option:  "))
    except Expection as e:
        print("Error", e)
        print("Enter 1, 2, 3 or 4 only")
        continue
    if Option==1:
        print("Balance  Rs ",balance)
    if Option==2:
        print("Balance  Rs ",balance)
        withdraw=float(input('Enter withdraw amount  Rs '))
        if withdraw>0:
            TotalBalance=(balance-withdraw)
            print("Total Balance  Rs ",TotalBalance)
        elif withdraw>balance:
            print("NO FUNDS IN ACCOUNT")
        else:
            print("None Withdraw made")

    if Option==3:
        print("Balance  Rs ",balance)
        Deposit=float(input("Enter deposit amount   Rs "))
        if Deposit>0:
            TotalBalance=(balance+Deposit)
            print("Total Balance    Rs ",TotalBalance)
        else:
            print("None Deposit made")

    if Option==4:
        exit()
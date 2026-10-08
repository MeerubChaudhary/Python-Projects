'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Welcome to the Panera Bread Tipping Calculator!')
print('Enter your bill amount (listed on your sales check):')
check_amount = float(input("Amount here: "))
print('Suggested Gratuities')
print('--------------------')
fifteen_percent = check_amount*0.15
twenty_percent = check_amount*0.20
twentyfive_percent = check_amount*0.25
print('15%\t$', fifteen_percent)
print('20%\t$', twenty_percent)
print('25%\t$', twentyfive_percent)
tip_amount = float(input('Please enter your tip amount: $'))
GrandTotal = check_amount + tip_amount
print('You total is', GrandTotal)
print('Thank you for dining at Panera!')
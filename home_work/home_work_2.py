#-----Converte UAH to USD or USD to UAH by NBU exchange rate-----

#choice currency
choice = input('Choose currency (USD or UAH): ')
while choice != 'USD' and choice !='UAH':
    print('Wrong value! Try again.')
    choice = input('Choose currency (USD or UAH): ')
else:
    #in depending on choice used different convertation
    if choice =='UAH':
        money = input("Enter UAH: ")
        while type(money) != int or type(money) != float:
                
                try:
                    money = float(money)
                    break
                except Exception: 
                    money = input('It is not a number! Enter UAH: ')


        dollar = money / 40.5
        print(f'{money} UAH = {dollar} USD')

    elif choice =='USD' :
        money = input("Enter USD: ")
        while type(money) != int or type(money) != float:
                
                try:
                    money = float(money)
                    break
                except Exception: 
                    money = input('It is not a number! Enter USD: ')


        hryvnia = money * 36.57
        print(f'{money} USD = {hryvnia} UAH')

#Converte UAH to USD or USD to UAH by NBU exchange rate

choose = input('Choose currency (USD or UAH): ')
while choose != 'USD' and choose !='UAH':
    print('Wrong value! Try again.')
    choose = input('Choose currency (USD or UAH): ')
else:
    if choose =='UAH':
        money = input("Enter UAH: ")
        while type(money) != int or type(money) != float:
                
                try:
                    money = float(money)
                    break
                except Exception: 
                    money = input('It is not a number! Enter UAH: ')


        dollar = money / 40.5
        print(f'{money} UAH = {dollar} USD')

    elif choose =='USD' :
        money = input("Enter USD: ")
        while type(money) != int or type(money) != float:
                
                try:
                    money = float(money)
                    break
                except Exception: 
                    money = input('It is not a number! Enter USD: ')


        hryvnia = money * 36.57
        print(f'{money} USD = {hryvnia} UAH')

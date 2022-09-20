#----------- Converte UAH to USD or USD to UAH by NBU exchange rate; version 2.0 -----------#


#function for check and return currency
def currency_check():
    choice = input('Choose currency (USD or UAH): ')
    while choice != 'USD' and choice !='UAH' and choice != 'usd' and choice != 'uah':
        print('Wrong value! Try again.')
        choice = input('Choose currency (USD or UAH): ')
    return choice


#input and float/int check; after checking num will return
def return_float(currency):
    num = input(f'Enter {currency.upper()}: ')
    while type(num) != int or type(num) != float:
            
            try:
                num = float(num)
                return num
            except Exception: 
                num = input(f'It is not a number! Enter {currency.upper()}: ')
                
#main part
if __name__ == '__main__':
    #choice currency
    user_choise = currency_check()
    dollar = 40.5
    hryvnia = 36.57

    money = return_float(user_choise)

    if user_choise =='UAH':
        print(f'{money} UAH = {round(money / dollar, 3)} USD')
    else:
        print(f'{money} USD = {round(money * hryvnia, 3)} UAH')
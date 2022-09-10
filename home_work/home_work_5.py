#Print last number


num = input("Enter number: ")
while type(num) != int or type(num) != float:
        
        try:
            num = int(num)
            break
        except Exception: 
            num = input('It is not a number! Enter number: ')

num = str(num)

#check if num more two-digit
if len(num) > 1:
    num = num[len(num)-1]
    print('New value: ', num)
else:
    print('Only one-digit: ', num)


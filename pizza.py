import os
import time

Meat,Vegg = 'Meat Lover Pizza <@ Rp. 80000,->','Vegetarian Lover Pizza <@ Rp. 50000,->'
varInput,varOrder = 0,0
orderM,orderV = 0,0
userPay = 0
while varInput != '3':
    os.system('cls')
    print('Welcome to Yummy Delivery Pizza')
    print('================================')
    print('1. Order Pizza')
    print('2. Pay')
    print('3. Exit')
    varInput = input('\nChoose : ')
    if varInput == '1':
        os.system('cls')
        print('Choose an Order')
        print('================')
        print('1. '+Meat)
        print('2. '+Vegg)
        while varOrder != '1' or varOrder != '2':
            varOrder = input('\nWhich Pizza do u want to order[1-2]: ')
            if varOrder == '1':
                print('Thanks for ordering '+Meat)
                orderM+=1
                time.sleep(1.2)
                break
            elif varOrder == '2':
                print('Thanks for ordering '+Vegg)
                orderV+=1
                time.sleep(1.2)
                break
    elif varInput == '2':
        os.system('cls')
        print('You have ordered {} Meat Lover Pizza(s) and {} Vegetarian Pizza(s)'.format(orderM,orderV))
        totalPrice = orderM*80000+orderV*50000
        print('\nTotal Price : Rp. {}'.format(totalPrice))
        while userPay < totalPrice:
            userPay = int(input('Input Your Money [Minimum Rp. {}] : '.format(totalPrice)))
        else:
            print('Your Change : {}'.format(userPay-totalPrice)) 
            print('Thank You for Your Purchase')
            break
            varInput=3
    elif varInput == '3':
        break
    
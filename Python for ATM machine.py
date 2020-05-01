
#Khedr, Ahmed Mohamed
#
#POS program for MinMax
#compatable with Python 3.4 - 3.7
#

#if __name__ == "__main__":


itemList={'111111': 1 , '666666':5 , '242424':19}

totalPrice =[0,0,0]
indxItemRaw =0
indxItemTax=1
indxItemWithTax=2
condition = True

def round_to_five(indxItemWithTax):
    """
    (number) -> float
    Returns the price of the item(s) being purchased plus the price of tax,
    rounded to the nearest .05 (5 cents).

    >>>round_to_five(10.67)
    >>>10.70

    >>>round_to_five(217.33)
    >>>217.30
    """
    return round(0.05*round(indxItemWithTax/0.05), 2)

def welcomeMessage():
    """
    (None) -> None

    Displays a welcome message visible to the cashier and the customer.
    """

    print("Hello" " How are you?")

def getBarCode():
    """
    (None) -> int OR str
    
    Prompts the user (cashier) to input the UCP of each individual item being purchased.

    >>>getBarCode()
    Scan Item or Enter Q for Exit: 111111
    111111
    price before tax  1 tax amount  0.13 price after tax   1.15
    Total Bill   1.15 Total Price (Before Tax) 1 Total Tax 0.13
    Scan Item or Enter Q for Exit:

    >>>getBarCode()
    can Item or Enter Q for Exit: 111111
    123456
    That UCP isn't in our system. Please try again.
    Scan Item or Enter Q for Exit: 
    """

    item= input(" Scan Item or Enter Q for Exit: ").strip().capitalize()
    print(item)

    if item == 'Q':
        return -1

    if item in itemList:
        print ('price before tax ' , itemList[item] , 'tax amount ' , itemList[item]*.13 , \
        'price after tax ', '% .2f' % round_to_five(itemList[item]*1.13))  
        return item
    else:
        return -2



welcomeMessage()


while condition:
    item = getBarCode()
    
    if( item == -1):
        break
    if (item != -2):
        totalPrice[indxItemRaw]+=itemList[item]
        totalPrice[indxItemTax]+=itemList[item]*.13
        totalPrice[indxItemWithTax]+=itemList[item]*1.13
        
    

        print (('Subtotal price before tax', totalPrice[indxItemRaw]),\
        ('Subtotal tax',totalPrice[indxItemTax]),\
        ( "Subtotal Bill ", '% .2f' % round_to_five(totalPrice[indxItemWithTax])))
        
    else:
        print('That UCP isn\'t in our system. Please try again.')


      
amount_tendered=input("Please enter the amount of cash in dollars given by the client.")
print(amount_tendered)
amount_of_change = float(amount_tendered) - (totalPrice[indxItemWithTax])
print(amount_of_change)
if float(amount_tendered) > totalPrice[indxItemWithTax]:
    print("Thank you for shopping at MinMax! Here is your change.")
else:
    print("Insufficient funds. The transaction has been cancelled. Please talk to the cashier.") 
    
        
          
if __name__ == "__main__":
    welcomeMessage()
    getBarCode()
    amount_tendered()
    amount_of_change()
    calculate_total_bill()
    display_total_bill()
    calculate_subtotal()
    
        
    

'''
Functions do the following:
1. stores the data associated with your products read from an HTML file and creates /displays a Binary Search Tree.

2. Provide a menu that allows the following functionality:

    a. Print all items print the itemID, the item price and the number of items in stock. eg.  3235, $75.20, 25
    b. Get the number of items in stock that sell for under $50.00.
       That is, if an item sells for $2 each and there are 10 in stock, then you would count this as 10 items.
    c. Check a price given an item ID
    d. Increase Price – when the user selects this option, the prices are increased by 10% and all items are
       printed on the screen with the new prices. 

'''
import urllib.request

#menu display function
def menu(tree):
    print("1.Print all nodes \n2.Return the price of an item \n3. Count items cheaper than $50 \n4.Increase price of some items by 10%")
    choice = input("select a number from the menu")
    if choice == "1":
        printID(tree)
        menu(tree)
    if choice == "2":
        ID = int(input("enter item ID"))
        print(printPrice(tree, ID))
        menu(tree)
    if choice == "3":
        lessThan(tree)
        menu(tree)
    if choice == "4":
        priceUp(tree)
        menu(tree)
        
def readHtml():
    response = urllib.request.urlopen("http://www.cs.queensu.ca/home/cords2/data121.txt")
    html = response.read()
    data = html.decode('utf-8').split()
    return data


def changeToFloats(data):
    item_list = []
    i = 0
    size = len(data)
    while i < size:
        item_set = []
        j = 0
        while j < 3:
            item_set.append(float(data[i+j]))
            j += 1
        item_list.append(item_set)
        i += 3
    return item_list

def add(tree, value):
    if tree == None:
        return {'data':value, 'left':None, 'right':None}
    elif value < tree['data']:
        tree['left'] = add(tree['left'],value)
        return tree
    elif value > tree['data']:
        tree['right'] = add(tree['right'],value)
        return tree
    else: # value == tree['data']
        return tree # ignore duplicate
    return tree

def createTree(data, myTree):
    i = 0
    for i in range(0, len(data)):
        myTree = add(myTree, data[i])
    return myTree    

'''
 printID prints out all the nodes in the tree by smallest to largest ID on a
 new line including price and stock
'''
def printID(tree):
    if tree == None: # empty
        pass
    else:
        # right tree first (so it's on the right when you tilt your
        # head to the left to look at the display)
        printID(tree['left'])
        print(",".join(str(i) for i in (tree['data'])) )
        print()
        # now the left tree
        printID(tree['right'])

'''
printPrice takes an item ID and displays and returns the price.
'''

def printPrice(tree, ID):
    if tree == None:
        return False
    elif ID == int(tree['data'][0]):
        print("price: $",tree['data'][1])
        return True
    elif ID < int(tree['data'][0]):
        return printPrice(tree['left'],ID)
    else: # ID > tree['data']
        return printPrice(tree['right'],ID)

'''
lessThan counts (and return) the number of items that sell for
less than $50.00.

'''

def lessThan(tree):
    if tree == None:
        return 0
    price = float(tree['data'][1])
    stock = int(tree['data'][2])
    
    if price < 50:
        print(stock)
        return(stock + lessThan(tree['left']) + lessThan(tree['right']))
    else:
        return False


'''

priceUp increases the price of all items by 10% except for
items whose selling price ends in “.97”.

'''
#Checks if the price ends in '.97', if not returns False
#code source from CISC121 forum
def whatDoesitEndWith(number):
    number = str(number)
    if number[-3:] == '.97':
        return True
    else:
        return False
    
def priceUp(tree):
    if tree == None:
        return 0
    
    price = tree['data'][1]
    priceUp(tree['left'])
    
    if whatDoesitEndWith(price) == False:
        price +=(price * 0.10)
        tree['data'][1] = round(price,2)
        
    priceUp(tree['right'])
    price = tree['data']

def main():
    data = readHtml()
    data = changeToFloats(data)
    myTree = None #empty tree
    myTree = createTree(data, myTree)
    menu(myTree)
main()

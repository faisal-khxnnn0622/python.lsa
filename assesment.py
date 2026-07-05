# Assesment (Resturant bill)

#menu = "pizza"
#menu2 = "Burger"
#menu3 = "french fries"
#print(input("Enter the first food item ;"))
#print(input("Enter the second food item ;"))
#pizza = 250
#burger = 200
#print("pizza =" , pizza)
#print("burger =", burger)
#total = pizza + burger
#print(total)
#gst = total +18/100
#print("Your total bill is ;" , total + gst)



menu = ["pizza" , "burger" , "fries" , "nuggets" , "chicken65" , "sandwich"]
pricess = [260 , 200 , 120 , 140 , 130 , 110]

item1 = input("Enter first food item ;")
item2 = input("Enter your second food item ;")

price = pricess[menu.index(item1)]
price1 = pricess[menu.index(item2)]

final = price+price1
print("Sub total :" , final)
gst = final *18/100
print("GST(18%)" , gst)
print("Your total bill is ;" ,final+gst )

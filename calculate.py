# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
from re import I

broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

I = [broccoli, leek, potato, brussel_sprout]
sum_one_each = sum(I)
#print (sum_one_each)

avg_price = sum_one_each / len(I)
#print (avg_price)

num_broccolis = 5
num_leeks = 2
num_potatoes = 7
num_brussel_sprouts = 10

numb_broccolis = broccoli * num_broccolis
#print (numb_broccolis)
numb_leek = leek * num_leeks
numb_potato = potato * num_potatoes
numb_brussel_sprouts = brussel_sprout * num_brussel_sprouts

X = [numb_broccolis, numb_leek, numb_potato, numb_brussel_sprouts]
#print(X)
sum_total = sum(X)
#print (sum_total)

discount_percentage = float(30)
Y = float(sum_total) / 100
F = Y * discount_percentage
discounted_sum_total = float(sum_total) - F
print (discounted_sum_total)

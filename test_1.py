"""
You are given two salary options for 10 days of work. The first option is 100$ per day.
The second option is  1$ the first day doubling each day for 10 days.
There will be 2 functions. 
1st function will be 100 ($) x 10 (days)
2nd function will be loop 10x with each time doubling the amount 
and add that amount to the total.
check if Option1 and Option2 are = or output the greater Option
"""
"""
# option1
return 100x10

#option2
amount = 1
list1 = []
loop 10x
add amount to list1
amount *= 2
sum = add all items in loop
return sum

# main
if Option1 > Option2 
reutrn Option1 is better

if Options2 > Option1
reutrn Option2 is better

else 
return they are equal
"""
def option1():
    return 100 * 10


def option2():
    amount = 1
    list1 = []
    for i in range(0,10):
        list1.append(amount)
        amount *= 2
    total = sum(list1)
    return total

def main():
    pass

var1 = option1()
var2 = option2()
answer = ""
print("Option 1 is: ", var1)
print("Option 2 is: ", var2)

if var1 == var2:
    answer = "Option 1 and Option 2 pays the same."
if var1 > var2:
    answer = "Option 1 is better."
else: 
    answer = "Option 2 is better."
print(answer)



#1 Basics
for num in range(151):
    print(num)
#2 Multiples of Five
for num in range(5, 1001, 5):
    print(num)
#3 Counting, the Dojo Way 
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)
#4 Whoa. That Sucker's Huge            
sum_odd = 0
for num in range(1, 500001, 2):
    sum_odd += num
print(sum_odd)
#5 Countdown by Fours 
for num in range(2018, 0, -4):
    print(num)
#6 Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)
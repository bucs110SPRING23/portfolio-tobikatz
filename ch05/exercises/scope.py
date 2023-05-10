def multiply(num1, num2):
   times = 0
   for _ in range(num1):
       times = times + num2
   return times

def exponent(num1, num2):
   times = 1
   for _ in range(num1):
       times = times*num2
   return times

def square(num1):
   return exponent(2,num1)

def main():
    print (multiply(3,2))
    print(exponent(4,2))
    print(square(356))

main()
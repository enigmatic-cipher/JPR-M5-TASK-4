"""
Given a number n as input, for the numbers from 1 to n print print Fizz if it is divisible by 5, Buzz if it is divisible by 3, FizzBuzz if it is divisible by 15, otherwise print the number.
Input-> 20
Output-> 1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz, 
16,17,Fizz,19,Buzz
"""

def reo(n):
  for i in range(1,n+1):
    if (i%5==0):
      print("Fizz")
    elif (i%3==0):
      print("Buzz")
    elif (i%15==0):
      print("FizzBuzz")
    print(i)

num = 20
reo(num)
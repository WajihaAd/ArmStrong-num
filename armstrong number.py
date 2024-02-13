import math

count = 0


def count1(num):
  global count
  while (num != 0):
    count += 1
    num //= 10
  return count


def strong(count, num2):
  sum = 0
  original = num2
  while (num2 != 0):
    lastdigit = num2 % 10
    sum += pow(lastdigit, count)
    num2 //= 10
  final(sum, original)


def final(sum, original):
  if sum == original:
    print("The number is an armstrong number")
  else:
    print("The number is not an armstrong number")


num = int(input("Enter a number: "))
num2 = num
count1(num)
strong(count, num2)

#function definition
def cal_sum(a,b):   #parameter
    return a + b

sum = cal_sum(10,20)   #function call #argument
print("Sum:", sum)

#2nd example
def print_hello():
    print("hello")

output = print_hello()
print("Output:", output)

#find avarage of 3 numbers
def cal_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

cal_avg(30,60,90)

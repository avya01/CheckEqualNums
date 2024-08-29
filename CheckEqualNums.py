# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# def checkEquality(num1, num2):
#     equality = num1^num2
#     if(equality == 0):
#         return True
#     else:
#         return False
    
# print(checkEquality(num1, num2))

num_of_inputs = int(input("Enter the number of inputs you want to enter: "))
list_of_nums=[]

for i in range(0, num_of_inputs):
    num = int(input("Enter a number:"))
    list_of_nums.append(num)


def findNum(list_of_nums):
    ans = 0
    for element in list_of_nums:
        ans = ans^element
    return ans

print(findNum(list_of_nums))
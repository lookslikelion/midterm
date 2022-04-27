total_dic = {}
while True:
    fruit = input("Enter a fruit type (q to quit): ")
    if fruit == "q":
        break
    else:
        weight = input("Enter the weight in kg: ")
        total_dic[fruit] = weight
print(total_dic)
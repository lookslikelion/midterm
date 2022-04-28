
import random
import time
from tkinter import FALSE

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요. 동일한 메뉴는 안돼요!")

list = []
while True:
    menu = input("메뉴 추가 :")
        #추가되는 메뉴가 저장된 메뉴의 부분집합인지의 여부에 따라 다르게 출력하고 싶었으나 구현 못 함. 
    redundant = set(menu) <= set(list)
    if redundant == True:
            print("이미 있는 메뉴예요! 다른 메뉴를 입력해주세요.")
            print("현재 메뉴 수 =", len(list))
    if redundant == False:
            list.append(menu)
            print("현재 메뉴 수 =", len(list))

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(list)
print("과연 오늘의 메뉴는?")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

choice = random.choice(list)
#n번째메뉴 표현하는 법 구현 못 함
print("오늘의 메뉴는",list.index(choice)+1,"번째 메뉴", choice,"입니다.")


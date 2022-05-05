while 1:
    phone_number = input("Enter a phone number: ").split("-")
    if len(phone_number) != 3:
        print("Wrong format")
        continue
    
    if len(phone_number[0]) != 3 or len(phone_number[1]) != 4 or len(phone_number[2]) != 4:
        print("Wrong format")
        continue

    if not phone_number[0].isdigit() or not phone_number[1].isdigit() or not phone_number[2].isdigit():
        print("Wrong format")
        continue
        
    print("Correct format")
    break
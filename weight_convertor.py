weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    print(f"{weight / 0.45} pounds.")
elif unit.upper() == "K":
    print(f"{weight * 0.45} kilos.")
else:
    print("Please enter L for lbs and K for kg.")

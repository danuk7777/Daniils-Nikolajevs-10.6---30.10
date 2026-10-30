atzime = int(input("Ievadi atzīmi (1-10): "))

if atzime >= 9 and atzime <= 10:
    print("Izcili")
elif atzime >= 7 and atzime <= 8:
    print("Labi")
elif atzime >= 4 and atzime <= 6:
    print("Viduvēji")
elif atzime < 4 and atzime >= 1:
    print("Neieskaitīts")
else:
    print("Nepareiza atzīme")
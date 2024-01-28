a = int(input('Hoeveel pakjes heb je dit jaar al online besteld? : '))

try:
    if a > 50:
        with open('huiswerk9.txt', 'w+') as b:
            print('Dan heb je al veel geshopt.')
except Exception as e:
    print(f"Fout: {e}")

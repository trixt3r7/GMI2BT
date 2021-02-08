print('Skriv in två nummer, och jag kommer dividera dem.')
print('Skriv q för att avsluta')
while True:
    first_number = input('\nFörsta nummret: ')
    if first_number == 'q':
        break
    second_number = input('\nAndra nummret: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError as diverr:
        print('Det går inte att dela med 0')
        print(diverr)
    except ValueError as verr:
        print('Det går inte att omvandla strängen till ett tal')
        print(verr)
print('Tack för att du spelade...')

# minLikes = 500
# minShares = 100
# numLikes = 2469
numShares = 1247
if (numLikes >= 500) and (numShares >= 100):
    print('Obniżka o 10%')
else:
    print('Nie ma wystarczającej liczy like i share')

isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = True
if (isPizzaOrdered == True) or (isBigDrinkOrdered == False) or (not isWeekend == True):
    print('Dostałeś kupon na burgera!')
else:
    print('Zakup pizzę lub duży napój, aby otrzymać kupon na burgera!')

diskSize = 140
diskSizeUsed = 133
fileSize = 10
if (diskSize - diskSizeUsed) >= fileSize:
    print('Możesz pobrać plik')
else:
    print('Nie możesz pobrać pliku')
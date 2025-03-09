# Zadanie 1:
MIN_LIKES = 500
MIN_SHARES = 100
num_likes = 300
num_shares= 550
if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('GREAT! Today our prizes drop 10% !!!')
else:
    if num_likes <MIN_LIKES:
        print('We still need more likes to start the promotion')
    else:
        print('We still need more shares to start the promotion')

# druga opcja:
if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print('GREAT! Today our prizes drop 10% !!!')
elif num_likes <MIN_LIKES:
     print('We still need more likes to start the promotion')
else:
     print('We still need more shares to start the promotion')

# Zadanie 2:
isPizzaOrdered = True
isWeekend = True
isBigDrinkOrdered = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
else:
    if isWeekend:
        print('Come back on non-Weekend day')
    else:
        print('You need to order Pizza or Big drink to have a Burger coupon')

# druga opcja:
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Burger for FREE!!!')
elif isWeekend:
    print('Come back on non-Weekend day')
else:
    print('You need to order Pizza or Big drink to have a Burger coupon')
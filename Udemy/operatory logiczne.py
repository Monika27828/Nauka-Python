isAutomaticMode = False
print("Is Automatic Mode: ",isAutomaticMode)
is80PercentLight = True
print("Is the light good: ",is80PercentLight)
isDirectLight = False
print("Is sun low: ",isDirectLight)
isRainy = True
print("Is it Rainy: ",isRainy)
turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
print("Turn lights on: ",turnLightsOn)

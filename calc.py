
# konvertē datu mērvienības
def megabit_to_megabyte(megabit):
   result = megabit * 8
   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
   hundred = kilometers / 100
   result = litres / hundred
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = celsius * (9/5) + 32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail, x):
    result =   0
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
     if grams >= 1000000:
          result = int(grams / 1000000)
          return str(result) + "t"
     if grams >= 100000:
        result =  int(grams / 100000)
        return str(result) + "c"
     if grams >= 10000:
        result =  int(grams / 1000) 
        return str(result) + "kg"
     if grams >= 100:
        result = int(grams)
        return  str(result) + "g"
    
    
   

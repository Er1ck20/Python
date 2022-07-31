contador = 0

while contador <=15:
    contador += 1
    if contador % 3 == 0:
        print(f'{contador} - Fiiz')
    
    elif contador % 5 == 0:
        print(f'{contador} - Buzz')
    
    else:
        print(f'{contador} - FiizBuzz')
import random

while True:
    v=str(input('diga start para iniciar:'))
    s=random.randint(0,6)
    if s==6:
      print('\033[31musuário desconectado\033[0m')
      break
    else:
        n=input('você sobreviveu, gostaria de continuar?')    
        if n == 'sim':
            continue
        else:
            break

"""secuencia de Collatz

Original file is located at
    https://colab.research.google.com/drive/1zf0BIARKY5hJTsGDJduNq5lzRjmU7lGh
"""

def collatz(n:int)->list: 
  numeros=[]
  if n==1:
    return 1
  while n !=1:
    numeros.append(int(n))
    if n%2==0:
      n=n/2.0
    else:
      n=(3*n)+1
  numeros.append(1)
  return numeros
  
if __name__=="__main__":
  print('ingrese 4 números enteros')
  sumatoria=0
  for _ in range(4):
    sumatoria+=int(input('ingrese el número: '))
  n=int(sumatoria/4)
  print(f'la secuencia de secuencia de Collatz para el número {n} es : ',collatz(n))
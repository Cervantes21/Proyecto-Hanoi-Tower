def hanoi(N, inc='1', temp='2', fin='3'): #Este programa logico-matematico pertenece intelectualmente a Luis Luna IICBA luis.mireles@uaem.edu.mx

       if N > 0:
              hanoi(N-1, inc, fin, temp)
              print ('mover de torre', inc, 'a torre', fin)
              hanoi(N-1, temp, inc, fin)
             
             
n = int(input("coloca numero de discos de hanoi y nadie podra ganarme jaja:"))
hanoi(n)

def numerodemovimientos(n):
      if n == 1:
              count = 1
      else: count = (2 * numerodemovimientos(n-1) + 1)
      return count
def movimientos():
       print("{} los discos deben moverse: {} veces".format(n, numerodemovimientos(n)))
if __name__ == "__main__":
      movimientos()
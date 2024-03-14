import random
import matplotlib.pyplot as plt


class Main:
   def __init__(self, number , numertwo):
      self.generateRandomNumber(number, numertwo)

   def generateRandomNumber(self, min, max):
      return random.randint(min, max)
   


def main():
   main = Main(5, 100)

   print(main.generateRandomNumber(5, 100))
   listHolder = [random.randint(1, 100) for _ in range(80)]
   print("even numbers")
   evenHoldr = filter(lambda x: x % 2 == 0, listHolder)
   print(sorted(list(evenHoldr)))

   print("\n\n")

   
   print("odd numbers")
   oddHolder = filter(lambda x: x % 2 != 0, listHolder)
   print(sorted(list(oddHolder)))

   plt.plot(sorted(list(evenHoldr)), sorted(list(oddHolder)), marker='o')
   plt.xlabel('Even Numbers')
   plt.ylabel('Odd Numbers')
   plt.title('Even vs Odd Numbers')
   plt.grid(True)
   plt.show()
if __name__ == "__main__":
   main()
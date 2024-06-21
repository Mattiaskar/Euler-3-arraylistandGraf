import random
import matplotlib.pyplot as plt
random.seed()


def leur():
  people = []
  for i in range(0, 50):
    people.append(100, )
  
  #print(people)
  print("   \t\n")
  
  for beshkan in range (0, 10000):
    for person1 in range(0, 50):
      person2 = random.randrange(0, 50)
      #print (person1, person2)
      while people[person2] == 0:
         person2 = random.randrange(0, 50)
          
      if people[person1] !=0:
         people[person1] = people[person1] - 1
         people[person2] = people[person2] + 1
  
  
  print(people)
  plt.bar(range(0, 50), sorted(people, reverse=True))
  plt.show()
  people.sort()
  
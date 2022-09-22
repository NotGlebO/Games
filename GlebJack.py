import random 
print('Добро пожаловать в BalckJack 1.0\nДля начало игры введите "Start"')
Start = input("Введите команду: ")
start = Start.lower()
print('Цель набрать 21 очко. Если больше - поражение. Меньше чем у диллера - поражение')

if start == "start":
  diller = random.randrange(1,11)
  diller_2 = random.randrange(1,11)
  while diller == diller_2:
    diller_2 = random.randrange(1,11)
  diller_all = diller+ diller_2
  diller_3 = 0
  diller_4 = 0
  card1 = random.randrange(1,11)
  card2 = random.randrange(1,11)
  card3 = 0
  card4 = 0
  while card1 == diller or card1 == diller_2:
    card1 = random.randrange(1,11)
  while card1 == card2 or diller == card2 or diller_2 == card2:
    card2 = random.randrange(1,11)
  while diller == diller_2:
    diller_2 = random.randrange(1,11)

print("Карты диллера: " + str(diller) + " и ?")

print("Ваши карты: " + str(card1) + " и " +str(card2))
  
check= input("Выберите действие(out или more): ")
  
  
if check == "more":
  card3 = random.randrange(1,11)
  while card3 == diller or card3 == diller_2 or card3 == card1 or card3 == card2:
    card3 = random.randrange(1,11)

    
  print("Игрок взял 3 карту")
    
  print("Ваши карты: "+ str(card1)+", "+str(card2) + ", "+ str(card3))
  check = input("Выберите действие(out или more): ")


if check == "more":
  card4 = random.randrange(1,11)
  while card4 == diller or card4 == diller_2 or card4 == card1 or card4 == card2 or card4 == card3:
    card4 = random.randrange(1,11)
  print("Игрок взял 4 карту")

print("Ваши карты: "+ str(card1)+", "+str(card2) +", " +str(card3) +", "+ str(card4))



cardall = card1 + card2 + card3 + card4

if diller_all <= 18:
       diller_3 = random.randrange(1,11)
       while diller_3 == diller or diller_3 == diller_2 or diller_3 == card1 or diller_3 == card2 or diller_3 == card3:
         diller_3 = random.randrange(1,11)
       print("Диллер взял 3 карту")
       print("Карты диллера: " +str(diller) + ", ?, " + str(diller_3))
       diller_all = diller_all + diller_3 
       if diller_all<= 18:
          diller_4 = random.randrange(1, 11)
          print("Диллер взял 4 карту")
          print("Карты диллера: " +str(diller) + ", ?, " + str(diller_3) + " " + str(diller_4))
          diller_all = diller_all + diller_4


print("Карты диллера" +str(diller) + ", "+ str(diller_2) +", "+str(diller_3) + ", " + str(diller_4))
  
if cardall > diller_all:
  if cardall > 21:
    print("Сумма диллера: " + str(diller_all))
    print("Ваша сумма: " + str(cardall))
    print("Вы проиграли")
  if cardall < 21:
    print("Сумма диллера: " + str(diller_all))
    print("Ваша сумма: " + str(cardall))
    print("Вы выиграли")

if cardall < diller_all:
  if cardall >= 21:
    print("Сумма диллера: " + str(diller_all))
    print("Ваша сумма: " + str(cardall))
    print("Вы проиграли!")
  if diller_all <= 21:
    print("Сумма диллера: " + str(diller_all))
    print("Ваша сумма: " + str(cardall))
    print("Вы  проиграли!")
  if diller_all > 21: 
    print("Сумма диллера: " + str(diller_all))
    print("Ваша сумма: " + str(cardall))
    print("Вы выиграли!")

if cardall == diller_all:
  if cardall <= 21:
    print("Сумма диллера: " + str(diller_all))
    print("Ваша сумма: " + str(cardall))
    print("Ничья")



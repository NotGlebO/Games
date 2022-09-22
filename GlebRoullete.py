import random
print("Добро пожаловать в GlebRoullet 1.0 Beta")
balance = 5000

while balance != 0:
  print("Ваш баланс: " + str(balance))
  try:
    print("Возможные ставки 250, 500, 1000, 2000, 5000, 10000, allin")
    stavka = int(input("Введите число ставки(целое): "))
  except:
    print("Неверная ставка")
    continue
  else:
    pass
    
  if stavka > balance:
    print("Недостаточно средств")
    continue
  voz = [250, 500, 1000, 2000, 5000, 10000]
  if voz.count(stavka) or stavka == balance:
    pass
  else: 
    g = 1
    while g == 1:
      print("Неверная ставка")
      print("Возможные ставки 250, 500, 1000, 2000, 5000, 10000, allin")
      stavka = int(input("Введите число ставки(целое): "))
      if voz.count(stavka) or stavka == balance:
        g -= 1
      else:
        continue
  balance -= stavka
  error1 = 1
  
  vivs = input("Выберите вид ставки(color, number, eo(even or odd)):")
  
  if vivs.count("color") or vivs.count("number") or vivs.count("eo"):
    pass 
     
  else:
    while error1 == 1:
        print("Неверный выбор ставки")
        vivs = input("Выберите вид ставки(color, number, eo(even or odd)):")
        
        if vivs.count("color") or vivs.count("number") or vivs.count("eo"):
          pass
          error1 -= 1
        else:
          continue
        
         
  if vivs == "color":
    color = input("Выберите цвет(red/black): ")
      
    if color.count("red") or color.count("black"):
        pass
    else:
      error = 1
      while error == 1:
        print("Ошибка синтаксиса, напишите еще раз!")
        color = input("Выберите цвет(red/black): ")
        if color.count("red") or color.count("black"): 
          error -= 1
      
  roullet = random.randrange(0, 36)
  red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]    
  
  if vivs == "number":
    o = 1
    while o == 1:
      try:
        check = int(input("Выберите номер на который хотите поставить, от 0 - 36: "))
      except:
        print("Некорректное число") 
      else:
        if check > 36 or check < 0:
          print("Слишком маленькое/большое число")
          continue
        else:
          o -= 1
      
  if vivs == "eo":
    e = 1
    while e == 1:
      ch = input("Выберите четное или нечетное(even/odd)")
      if ch.count("even") or ch.count('odd'):
        e -= 1
      else: 
        print('Неверный выбор')
        continue

  if red.count(roullet):
    print("Выпало " + str(roullet) + " красное")  
  if roullet == 0:
    print("Выпало " + str(roullet) + " зелёное") 
  if not red.count(roullet):
    print("Выпало " + str(roullet) + " черное")

  
  if vivs.count("color"):
    if red.count(roullet):
      if color == "red":
          pobeda = stavka * 1.5
          print("Ваш выигрыш составляет " + str(pobeda) + "(x1.5)")
          balance += pobeda
      if color != "red":
        print("Вы проиграли: " + str(stavka))
    else:
        if color == "black":
          pobeda = stavka * 1.5
          print("Ваш выигры составляет " + str(pobeda) + "(x3)")
          balance += pobeda
        if color != "black":
          print("Вы проиграл: " + str(stavka))

    
  
  
  if vivs.count("number"):
    pobedan = stavka * 3
    podeba0 = stavka * 5
    if check == roullet:
      if roullet == 0:
        print("Ваш выигрыш составляет " + str(pobeda0) + "(x5)")
      else:
        print("Ваш выигрыш составляет " + str(pobedan) + "(x3)")   
        balance += pobedan
    if check != roullet:
      print("Вы проиграли: " + str(stavka))
  
  if vivs.count('eo'):
    eeo = stavka * 1.5
    chetnoe = roullet % 2
    if chetnoe == 0:
      if ch == "even":
        print("Ваш выигрыш составляет " + str(eeo) + "(x1.5)")
        balance += eeo
      if ch != "even":
        print("Вы проиграли: " + str(stavka))
    if chetnoe == 1: 
      if ch == "odd":
        print("Ваш выигрыш составляет " + str(eeo) + "(x1.5)")
        balance += eeo
      if ch != "odd":
        print("Вы проиграли: " + str(stavka))

def get_integer(prompt):
  money = int(input(prompt))
  return money

def exchange(money):
  n500 = money // 500
  money %= 500
  n100 = money // 100
  money %= 100
  n50 = money // 50
  money %= 50 
  n10 = money // 10

  print ('500원 동전의 개수: ',n500)
  print ('100원 동전의 개수: ',n100)
  print ('50원 동전의 개수: ',n50)
  print ('10원 동전의 개수: ',n10)

money = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(money)

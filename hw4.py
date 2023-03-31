def eng_name(name):
  name = str(input(name))
  return name
  
def rep_char(num):
  print('-'*num)

name = eng_name('Input his/her name: ')
msg1 = 'Hello '+str(name)+','
msg2 = ('Welcome to Seoul.')
nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
rep_char(nstr)
print(msg1)
print(msg2)
rep_char(nstr)

import pickle

filename = 'score.bin'

def save(score, filepath) as file:
    with open(filepath, 'wb', encoding = 'utf8') as file :
        for score in score :
            n.write(f'{n}\n')

def load(filepath) as file:
    with open(filepath, 'rb', encoding = 'utf8') as file :
        num = pickle.load(file)
        
        
scores = []
avg = 0
i = 1
t = 0

if pickle.path.exists(filename) :
    print('[파일 읽기]')
    shopping_bag = load(filename)
    show(shopping_bag)

print('[점수 입력]')
while True :
    print(f'#{i}', end = '')
    n = int(input('? '))
    
    if n < 0 :
        break
    
    scores.append(n)
    save(n, filename)
    avg += n
    i += 1
    
avg /= (i-1)
print()
print('[점수 출력]')
print('개인 점수 : ', end = '')
for k in range(len(scores)) :
    print(f'{scores[k]} ', end = '')
print()
print(f'평균 :  {avg:.1f}')

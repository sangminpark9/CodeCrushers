n = input()
m = n.split('-')

answer = 0

x = sum(map(int, (m[0].split('+'))))
if n[0] == '-':
    answer -= x
else:
    answer += x
for ele in range(1,len(m)):
    answer -= sum(map(int, m[ele].split('+')))
    
print(answer)

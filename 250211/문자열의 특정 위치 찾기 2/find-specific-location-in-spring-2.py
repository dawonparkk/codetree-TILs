list_v = ['apple', 'banana', 'grape', 'blueberry','orange']
word = str(input())
cnt =0
for i in range(len(list_v)):
    if word == list_v[i][2] or word == list_v[i][3]:
        print(list_v[i])
        cnt+=1
      
print(cnt)
    
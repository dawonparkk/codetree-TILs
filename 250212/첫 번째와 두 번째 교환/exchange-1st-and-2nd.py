s = list(input())
fir = s[0]
sec = s[1]
for i in range(0,len(s)):
    if s[i]==fir :
        s[i] = sec 
    elif s[i]==sec :
        s[i] = fir
        
        
print(''.join(s))
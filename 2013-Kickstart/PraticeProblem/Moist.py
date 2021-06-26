t = int(input())

for test in range(1, t + 1):
    
    n = int(input())
    ans = 0
    
    cards = [input() for i in range(n)]
    
    previous = cards[0]
    
    for i in range(1, len(cards)):
    	
    	if cards[i] < previous:
    		ans += 1
    	else:
    		previous = cards[i]
    
    
    print("Case #"+str(test)+": "+str(ans))

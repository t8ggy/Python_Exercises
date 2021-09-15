def challenge_5(integers):
    all_factors = []
    
    for i in integers:
        i_factors=[]
        for j in range (1, i-1):
            
            if i % j == 0:
                
                i_factors.append(str(j))
        comma_space = ', '.join(i_factors)
        all_factors.append(comma_space)
     
    #with open('factors.csv', 'a') as f:
    #    for factorsList in all_factors:
    #        f.write(factorsList + '\n')
    print(all_factors)

challenge_5([64,19,98,14,18])

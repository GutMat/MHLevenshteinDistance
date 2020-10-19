import sys
import numpy as np
word1 = sys.argv[1]
word2 = sys.argv[2]

word1_len, word2_len = len(word1), len(word2)

memo = [[0 for word1 in range(word2_len + 1)] for word2 in range(word1_len + 1)]

print("Tablica startowa {0} na {1} ".format(word1_len+1, word2_len+1))
print(np.array(memo))

for i in range(word1_len +1):
    for j in range(word2_len + 1):
        
        if i == 0: 
            memo[i][j] = j
        
        elif j == 0: 
            memo[i][j] = i

        elif word1[i-1] == word2[j-1]: 
            memo[i][j] = memo[i-1][j-1] 

        else: 
            memo[i][j] = 1 + min(memo[i][j-1],    
                                memo[i-1][j],       
                                memo[i-1][j-1])      
print("Tablica końcowa z wynikiem znajdującym się w prawym dolnym rogu memo[{0}][{1}]".format(word1_len, word2_len))         
print(np.array(memo))

print("Minimalna liczba operacji potrzebna do uzyskania jednakowego wyrazu wynosi :", memo[word1_len][word2_len])
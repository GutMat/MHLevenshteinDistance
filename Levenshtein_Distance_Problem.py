# -*- coding: utf-8 -*-

# Funkcja obliczająca dystans Levenshteina
# Przyjmuje 4 argumenty
# Wyraz oryginalny oraz wyraz, który chcemy przeksztalcić
# wraz ich długosciami
# Taka implementacja tego problemu osiąga złożonosć czasową O(3^word2_len)
def distance(word1, word1_len, word2, word2_len):
    
    # Przypadek pierwszy
    # Sprawdzamy czy 1 wyraz jest pusty
    # Jesli jest pusty wymagana jest liczba operacji równa długosci drugiego wyrazu
    if word1_len == 0:
        return word2_len
    
    # Sprawdzamy czy 2 wyraz jest pusty
    # Jesli jest pusty wymagana jest liczba operacji równa długosci pierwszego wyrazu
    if word2_len == 0:
        return word1_len
    
	# Przypadek drugi
    # Sprawdzamy czy ostatnie znaki wyrazu są takie same
    # Jesli tak możemy pominąć ostatnie znaki i obliczyć dystans
    # dla pozostałych liter
    if word1[word1_len - 1] == word2[word2_len - 1]:
        return distance(word1, word1_len - 1, word2, word2_len - 1)

    # Zwracamy minimalną wartosć dystansu pomiedzy wyrazami
    # (liczby operacji potrzebnych do uzyskania identycznego wyrazu)
    # Rozpatrujemy tutaj 3 przypadki
    # a) gdy usuwamy litere z pierwszego wyrazu ('ABC', 'ABD') => ('AB', 'ABD')
    # b) gdy dodajemy litere do pierwszego wyrazu ('ABC', 'ABD') => ('ABCD', 'ABD') == ('ABC', 'AB')
    # c) gdy zamieniamy ('ABC', 'ABD') => ('AB', 'AB')
    return min(distance(word1, word1_len - 1, word2, word2_len) + 1,			
    			   distance(word1, word1_len, word2, word2_len - 1) + 1,			
    			   distance(word1, word1_len - 1, word2, word2_len - 1) + 1)

# Funkcja obliczająca dystans Levenshteina wykorzystująca
# technikę programowania dynamicznego i przechowywania rozwiązań podproblemów
# Taka implementacja tego problemu w taki sposób osiąga złożonosć czasowa O(word1_len*word2_len)
def distanceDP(word1, word2):

    # Obliczanie długosci poszczególnych wyrazów
    word1_len, word2_len = len(word1), len(word2)

    # Poniższa tablica przechowuje wszystkie możliwe wartosci odległosci pomiędzy
    # poszczególnymi znakami wyrazu pierwszego i wyrazu drugiego
    # Tablica posiada (word1_len +1)*(word2_len+1) wartosci
    memo = [[0 for word1 in range(word2_len + 1)] for word2 in range(word1_len + 1)]

    # Następnie iterujemy po poszczególnych literach wyrazów porównując je
    for i in range(word1_len +1):
        for j in range(word2_len + 1):
            
            # Przypadek pierwszy
            # Sprawdzamy czy 1 wyraz jest pusty
            # Jesli jest pusty wymagana jest liczba operacji równa długosci drugiego wyrazu
            if i == 0: 
                memo[i][j] = j
            
            # Sprawdzamy czy 2 wyraz jest pusty
            # Jesli jest pusty wymagana jest liczba operacji równa długosci drugiego wyrazu 
            elif j == 0: 
                memo[i][j] = i
  
            # Przypadek drugi
            # Sprawdzamy czy ostatnie znaki wyrazu są takie same
            # Jesli tak możemy pominąć ostatnie znaki i obliczyć dystans
            # dla pozostałych liter
            elif word1[i-1] == word2[j-1]: 
                memo[i][j] = memo[i-1][j-1] 
  
            # Jeśli ostatnie znaki się różnią, sprawdzamy wszystkie
            # możliwości i wyciągamy wartość minimalną
            else: 
                memo[i][j] = 1 + min(memo[i][j-1],      # Dodawanie
                                   memo[i-1][j],        # Usuwanie
                                   memo[i-1][j-1])      # Zamiana 
  
    return memo[word1_len][word2_len]


word_A = ""
word_B = "wino"

print(distance(word_A,len(word_A),word_B, len(word_B)))
print(distanceDP(word_A, word_B))

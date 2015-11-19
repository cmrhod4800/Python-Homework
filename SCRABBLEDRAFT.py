### I WILL REFERENCE EVERYTHING I HAVE FOUND ONLINE
### my funtions are running together the parameters need to match through
###out the game inorder for the board to correspond to players input
board =[]

board = [4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4, 5,
    0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0, 5,
    0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0, 5,
    1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1, 5,
    0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 5,
    0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 5,
    0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 5,
    4, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 4, 5,
    0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 5,
    0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 5,
    0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 5,
    1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1, 5,
    0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0, 5,
    0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0, 5,
    4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4] ### This is the exact board(Found online)


import sys

for k in board:
    if k == 5:
        print'\n\n',
    elif k == 4:
        print(' TW', 'attrs=[]', 'end = ' '')
    #print 'TW',
    elif k == 3:
        print(' DW', 'attrs=[]', 'end = ' '')
    #print 'DW',
    elif k == 2:
        print(' TL', 'attrs=[]', 'end = ' '')
    #print 'TL',
    elif k == 1:
        print(' DL', 'attrs=[]', 'end = ' '')
    #print 'DL',
    elif k == 0:
        print '___', ####WHY IS IT NOT PRINTING ON SCALE(Also found online)


def count_letters(word):
  count = {} 
  for letter in word:
    if letter not in count: count[letter] = 0
    count[letter] += 1 
  return count 
  

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 5, "i": 1, "h": 4, "k": 5, "j": 8, "m": 2, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 4, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 5, "v": 4, "y": 5, 
         "x": 10, "z": 10} ### scored according to common or uncommon
def scrabble_score(word):
    total = []
    for letter in word:
        total.append(score[letter.lower()])
    return sum(total)
print scrabble_score("max")###ADD THE DESIRED WORD FOR SCRABBLE PLAY HERE

def spellable_word(word, rack):
    valid_words = []
    words = word_reader('/usr/share/dict/words')
    scored =  ((score_word(word), word) for word in words if set(word).issubset(set(rack)) and len(word) > 1 and spellable(word, rack))
    word_count = count_letters(word)
    rack_count  = count_letters(rack)
    return all( [word_count[letter] <= rack_count[letter] for letter in word] )
for item in spellable_word(word, rack):
    candidate = True
    rack_letters = list(rack)
for letter in word:
        if letter not in rack_letters:
            candidate = False
            break # No need to keep checking letters.
        else:
            rack_letters.remove(letter)
        if candidate == True:
        # Get the Scrabble scores for each word.
            total = 0
        for letter in word:
            total = total + scores[letter]
        valid_words.append([total, word])
               

def word_reader(filename):
  ### returns an iterator
  return (word.strip() for word in  open(filename)) 

if __name__ == "__main__":
  import sys
  if len(sys.argv) == 2: 
    rack = sys.argv[1].strip()
  else:
    print 
    exit()
  
  for score, word in sorted(scored):
    print str(score), '\t', word
        

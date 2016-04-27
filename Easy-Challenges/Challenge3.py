"""Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest
word in the string. If there are two or more words that are the same length, return the first word from the string with that
length. Ignore punctuation and assume sen will not be empty."""

def LongestWord(sen):
  words = sen.split(" ") # splits the words in "sen" at each space
  greatest_word = words[0] # assigned greatest_word to the first split word
  
  for word in words:
    if len(word) > len(greatest_word): # check the length of each word in the sentence to that of greatest_word
      greatest_word = word # if the word was bigger than the current word, it is assigned to the variable
    elif len(word) == len(greatest_word):
      greatest_word == greatest_word # keeping it the same (I'm a newbie and don't know how to do this cleaner)
  return greatest_word

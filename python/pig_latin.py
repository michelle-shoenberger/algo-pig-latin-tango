def translate(word_or_phrase):
  if not isinstance(word_or_phrase,str):
    print("Not a string")
  vowels = "aeiou"
  ans = []
  for word in word_or_phrase.split(" "):
    word = list(word)
    consonants = []
    end = []
    if not word[-1].isalpha():
      # for punctuation at the end of the word
      end.append(word[-1])
      word = word[:-1]
    for char in word:
      if char == "u" and consonants[-1] == "q":
        consonants.append(char.lower())
        break
      elif char in vowels:
        break
      consonants.append(char.lower())
    if word[0].upper() == word[0]:
      ans.append(word[len(consonants)].upper() + "".join(word[len(consonants)+1:]) + "".join(consonants) + "ay" + "".join(end))
    else:
      ans.append("".join(word[len(consonants):]) + "".join(consonants) + "ay" + "".join(end))
  return " ".join(ans)
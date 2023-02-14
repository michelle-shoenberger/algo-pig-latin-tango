exports.translate = function(words) {
  let ans = [];
  let vowels = "aeiou"
  for (let word of  words.split(" ")) {
    let consonants ="";
    let end ="";
    if (!(/[a-zA-Z]/).test(word[word.length-1])) {
      end += word[word.length-1];
      word = word.slice(0,word.length-1)
    }
    for (let char of word) {
      if (char == "u" && consonants[-1] == "q") {
        consonants += char.toLowerCase()
        break
      } else if (vowels.includes(char)) {
        break
      }else{
        consonants += char.toLowerCase()
      }
    }
    if (word[0].toUpperCase() == word[0]) {
      ans.push(word[consonants.length].toUpperCase() +word.slice(consonants.length) + consonants + "ay" + end)
    }else{
      ans.push(word.slice(consonants.length) + consonants + "ay" + end)
    }
  }
  return ans.join(" ")
};
function wordCount(arrayOfStrings) {
  let group = {};
  for (let i = 0; i < arrayOfStrings.length; i++) {
    let word = arrayOfStrings[i]
    if (!group[word]) {
      group[word] = 1;
    } else {
      group[word]++
    }
  }

  return group; 

}

module.exports = wordCount;

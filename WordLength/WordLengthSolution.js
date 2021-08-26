function wordLength(arr) {
  let output = [];
  for (let i = 0; i < arr.length; i++) {
    let strLen = arr[i].length;
    let strValue = arr[i].toLowerCase()
    let newArr = [strValue, strLen];
    output.push(newArr);
  }

  let mapped = new Map(output)

  return mapped
}

module.exports = wordLength;
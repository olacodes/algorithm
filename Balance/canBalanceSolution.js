//canBalance function takes an array of numbers and returns true or false based on the following conditions
//It returns true if the array can be split at any point with the sum of the numbers on one side equal to the sum of the numbers at the other side
// For example, given the array [1, 2, 3, 4, 5, 5], it will return true as the array can be split into [1, 2, 3, 4] and [5, 5] giving a sum of 10 on each side.


function canBalance(array) {
  // Type your solutions here
  let leftElement = 0;
  let leftArr = [];
  for (let i = 0; i < array.length; i++) {
    leftElement += array[i];
    leftArr.push(array[i])

    let rightElement = 0;
    let rightArr = [];
    for (let j = i + 1; j < array.length; j++ ) {
      rightElement += array[j];
      rightArr.push(array[j])
    }

    if (rightElement <= 0) return -1;
    if (leftElement === rightElement) return [leftArr.length, rightArr.length];
    
  }
  return -1;


  // let Element = 0;
  // let Arr = [];
  // for (let i = 0; i < array.length; i++) {
  //   Element += array[i];
  //   Arr.push(array[i])

  //   let removed = Arr.pop();
  //   let rightElement = Element - removed;
  //   let rightArr = [];
  //   rightArr.push(removed)

  //   if (rightElement <= 0) return -1;
  //   if (Element === rightElement) return [Arr.length, rightArr.length];
  // }

  // let sum = array.reduce((a,b) => a + b)
  // let el = 0;
  // let elem = 0;
  // let newArr = [...array];
  // let newArr2 = [...array];
  // let rightArr = [];

  // for (let i = 0; i < newArr.length; i++) {
  //   let leftRemoved = newArr.shift();
  //   el += leftRemoved;

  //   let rightRemoved = newArr2.pop()
  //   elem += rightRemoved
  //  // rightArr.push(rightRemoved);
  //   // let rightSum = sum - elem;

  //   if (el === elem) {
  //     return [newArr.length, newArr2.length];
  //   } else {
  //     return -1;
  //   }
  //  // if (rightSum <= 0) return -1;
  // }
}

module.exports = canBalance;

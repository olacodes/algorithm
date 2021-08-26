function almostIncreasingSequence(sequence){
  let sorted_sequence = sequence
  let count = 0;
  let i;
  for(i=0;  i < sorted_sequence.length; i++){
    let leftDiff = sorted_sequence[i] - sorted_sequence[i + 1] > 1
    let rightDiff = sorted_sequence[i+1] <= sorted_sequence[i]

    let left = sorted_sequence[i]
    let right = sorted_sequence[i+1]


    if(rightDiff) {
      count += 1
      sorted_sequence.splice(i+1, 1)
      i -= 1
    }

    else if (leftDiff) {
      count += 1
      sorted_sequence.splice(i, 1)
      i -= 1
    }
    
    if (count > 1){
      return false
    }
  }
  return true
  
}
let arr = [1,2,1,2]
let arrr = [10,1,2,3,4,5]
let arr1 = [1, 2, 3, 4, 5, 3, 5, 6]
console.log(almostIncreasingSequence(arr1))
console.log(arr);
arrr.splice(0,1)
console.log(arrr);
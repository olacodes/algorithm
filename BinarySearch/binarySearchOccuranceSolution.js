//Given an array of numbers
//Given a number
//This program uses the binary search algorithm to check if the number is in the array

function binarySearchOccurance(array, number) {
  //Type your solutions here
  let startIndex = 0;
  let endIndex = array.length - 1;
  let search = {};
  let counter = 0;
  
    if (array.length === 0) {
      search.occurance =  -1;
      search.count =  0;
    } else {
      for (let i = 0; i < array.length; i++){
        let middleIndex = Math.floor((startIndex + endIndex) / 2);
        if(array[i] === number || array[array[endIndex]] === number) {
          search.occurance = counter + 1;
          search.count = array.indexOf(number) + 1;
          counter++;
      }
      if(array[array[endIndex]] === number) {  //ask question
        for (let i = endIndex; i > array[startIndex]; i--) {
          let counter = 0;
          search.occurance = counter + 1;
          search.count = 1;
          counter++;
        }
      }
      // if(array[middleIndex] === number) {
      //   for (let i = array.length; i > array[0]; i++)
      //   search.occurance = counter + 1;
      //   search.count = array.indexOf(number) + 1;
      //   counter++;
      // }
      if(number > array[middleIndex]) {
        for (let i = middleIndex; i < array[endIndex]; i++)
        middleIndex + 1;
        let counter = 0;
        search.occurance = counter + 1;
        search.count = array.indexOf(number) + 1;
        counter++;
      }
      // if(number < array[middleIndex]) {
      //   for (let i = startIndex; i < array[middleIndex]; i--)
      //   middleIndex - 1;
      //   let counter = 0;
      //   search.occurance = counter + 1;
      //   search.count = array.indexOf(number) + 1;
      //   counter++;
      // }
      else if (!(array.includes(number)) ){
        search.occurance = -1;
        search.count = 0;
      }
    }

  }
  // return search;
  console.log(search)
  
}
binarySearchOccurance([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9], 9)

module.exports = binarySearchOccurance;


// function binarySearch(array, number) {
//   //Type your solutions here
// ​
// ​
// ​
//   let first = 0;    //left endpoint
//     let last = array.length - 1;   //right endpoint
//     let position = -1;
//     let found = false;
//     let middle;
//     let count=0;
// ​
//     while (found === false && first <= last) {
//         middle = Math.floor((first + last)/2);
//         if (array[middle] === number) {
//             found = true;
//             position = middle;
//         } else if (array[middle] > number) {  //if in lower half
//             last = middle - 1;
//         } else {  //in in upper half
//             first = middle + 1;
//         }
//         count=count+1;
        
// ​
//     }
    
//     return {
//       "index":position,
//       "count" :count
//     };
// }
// ​
// module.exports = binarySearch;

//Given an array of numbers
//Given a number
//This program uses the binary search algorithm to check if the number is in the array
// it returns true if the number is in the array and false if otherwise

function binarySearch(array, number) {
  //Type your solutions here
    let search = {};
    if (array.length === 0) {
      search.index =  -1;
      search.count =  0;
    } else {
      for (let i = 0; i < array.length; i++){
       if(array[i] === number){
          search.index = array.indexOf(number);
          search.count = i + 1;
      }
      else if (!(array.includes(number)) ){
        search.index = -1;
        search.count = (array.indexOf(array[i]) + 1);
        }
    }

  }
  return search;

  
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
}


module.exports = binarySearch;

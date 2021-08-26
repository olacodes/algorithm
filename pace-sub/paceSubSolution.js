function paceSub(S, W, T) {
  // code goes here ...
  // let temp = '';
  // for (let i = 0; i < W.length; i++) {
  //   for (let j = 0; j < S.length; j++) {
  //     if (W[i] === S[j]) {
  //       let index = j + T;
  //       let count;
  //       temp += S[index];
  //     }
  //   }
  // }
  // console.log(temp)

  var concat = ""
  var counter = 0;
  while (counter < W.length) {
    var shiftIndex = S.indexOf(W[counter]) + T
    if (shiftIndex >= S.length) {
      shiftIndex = S.indexOf(W[counter]) + T - 1
    }
    concat += S[shiftIndex]
    counter++
  }
  return concat;
}

// paceSub("abcdefgh","hfh", 6);

module.exports = paceSub;

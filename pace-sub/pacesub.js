const paceSub = (S, W, T) => {

  // var store = [];

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
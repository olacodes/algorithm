

function solution(P, C) {
    //Provide Your solution here 
    let pairPlayers = parseInt(P / 2);
    if (pairPlayers < C) return parseInt(pairPlayers);
    if (pairPlayers === 1 && C === 0) return 0;
    if (pairPlayers >= C) return parseInt(C);

}

module.exports = solution;
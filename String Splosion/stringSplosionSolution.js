function stringSplosion(str) {
    let p = '';
    let q = []
    for(let i = 0; i < str.length; i++) {
        p+= str[i];
        q.push(p);
    }
    return q.join('')
}


module.exports = stringSplosion;
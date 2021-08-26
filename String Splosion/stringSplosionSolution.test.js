const stringSplosion = require("./stringSplosionSolution")

test('String splosion of Code', () => {
    expect(stringSplosion('Code')).toEqual('CCoCodCode');
})

test('String splosion of abc', () => {
    expect(stringSplosion('abc')).toEqual('aababc');
})

test('String splosion of ab', () => {
    expect(stringSplosion('ab')).toEqual('aab');
})

test('String splosion of father', () => {
    expect(stringSplosion('father')).toEqual('ffafatfathfathefather');
})

test('String splosion of gamble', () => {
    expect(stringSplosion('gamble')).toEqual('ggagamgambgamblgamble');
})
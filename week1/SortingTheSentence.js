/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    var sentence=[]
    var jumbled= s.split(' ')
    for(var i=0; i<jumbled.length;i++){
        sentence[Number(jumbled[i].slice(-1))]=jumbled[i].slice(0,-1)
    }
    return(sentence.join(" ").substring(1))
};

/**
 * @param {number[]} piles
 * @return {number}
 */
 var maxCoins = function(piles) {
    var result=0
    piles.sort((x, y)=> x-y)
    console.log(piles)
    for(var i=piles.length-2; i >= piles.length/3;i-=2){
        result+= piles[i]
    }
    return(result)
};
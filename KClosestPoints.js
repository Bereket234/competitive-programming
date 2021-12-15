/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    var pt1, pt2, min, temp
    var result=[]
    for(var i=0; i< points.length; i++){
        min= i
        for(var j=i; j<points.length; j++){
            
            pt1= points[min][0]**2 + points[min][1]**2
            pt2= points[j][0]**2 + points[j][1]**2
            if(pt1 > pt2){
                min= j
            }
        }
        temp= points[min]
        points[min]= points[i]
        points[i]= temp 
    }
    for(var i=0; i<k; i++){
        result.push(points[i])
    }
    return(result)
};

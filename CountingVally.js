'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */

function countingValleys(steps, path) {
    // Write your code here
    var stack=[]
    var count=0
    path.toUpperCase()
    
    for(var i=0;i<steps;i++){
        if((stack.length==0) && (path[i]=='D')){
            stack.push('D')
            count++
        }else if(stack.length==0 && path[i]=='U'){
            stack.push('U')
        }else if(((stack[stack.length-1]=='U') && (path[i]=='D')) || ((stack        [stack.length-1]=='D')&& (path[i]=='U'))){
            stack.pop()
        }else{
            stack.push(path[i])
        }
    }
    return count
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const steps = parseInt(readLine().trim(), 10);

    const path = readLine();

    const result = countingValleys(steps, path);

    ws.write(result + '\n');

    ws.end();
}

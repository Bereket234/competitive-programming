/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    var arr=[]
    var i=0
    while(head !=null){
        arr[i]= head
        head= head.next
        i++
    }
    var mid=Math.floor(i/2)
    return(arr[mid])
};
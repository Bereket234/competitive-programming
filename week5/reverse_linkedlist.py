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

function ListNode(val, next){
    this.val= val
    this.next= (next=== undefined? null: next)
}
var reverseList = function(head) {
    var temp=null
    if(!head){
        return(null)
    }else{
        let result=new ListNode()
        while(head){
            result= new ListNode(head.val, temp)
            temp=result
            head=head.next
        }
        return result
    }
};
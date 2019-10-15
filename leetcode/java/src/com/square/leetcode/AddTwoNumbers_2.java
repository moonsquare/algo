package com.square.leetcode;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
}
class AddTwoNumbers{
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int flag=0;
        ListNode head = l1;
        while (l1!=null || l2!=null){
            int val1=0;
            int val2=0;
            if(l1!=null) val1= l1.val;
            if(l2!=null) val2 = l2.val; 
            int sum = val1 + val2+flag;
            int val = sum%10;
            flag = sum/10;
            l1.val=val;
            if(flag > 0 && l1.next==null) l1.next = new ListNode(0);
            if(l2!=null && l2.next!=null && l1.next==null){
                l1.next = new ListNode(0);
            }
            l1=l1.next;
            if(l2!=null)l2=l2.next;
        }
        return head;
    }

    public static void main(String[] args) {
        System.out.println(10/10);
    }
}


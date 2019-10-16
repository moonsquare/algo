package com.square.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LongestPalindrome_5 {
    public String longestPalindrome(String s) {

        if(s.length()==0||s.length()==1){
            return s;
        }
        int maxL=1;
        String maxS=s.substring(0,1);
        for(int i =0;i<s.length();i++){
            for(int j=i+maxL+1;j<=s.length();j++){
                String subs = s.substring(i,j);
                if(isPalindrome(subs)){
                    maxL=subs.length();
                    maxS=subs;
                }
            }
        }
        return maxS;

    }
    public boolean isPalindrome(String s){
        char[] chars = s.toCharArray();
        for(int i=0;i<chars.length/2;i++){
            if(chars[i]!=chars[chars.length-1-i]){
                return false;
            }
        }
        return true;
    }
    public void test(String s){
        s="lixiuping";
    }
    public void test(int s){
        s=6;
    }
    public void test(Integer s){

    }

    public static void main(String[] args) {
        LongestPalindrome_5 l5 = new LongestPalindrome_5();
//        l5.longestPalindrome("bb");
        String s = "zhangjizong";
        int i = 5;
        Integer j = 5;
        l5.test(s);
        l5.test(i);
        l5.test(j);
        System.out.println(s);
        System.out.println(i);
        System.out.println(j);

    }
}

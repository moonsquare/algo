package com.square.leetcode;
import java.util.HashMap;
import java.util.Map;
class LengthOfLongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        char[] chars = s.toCharArray();
        int maxLength=0;
        int flag=0;
        int length=0;

        Map<Character,Integer> map = new HashMap();
        for(int i =0;i<chars.length;i++){
            if(map.get(chars[i])!=null){
                length=i-flag;
                if(length>maxLength) maxLength=length;
                if(map.get(chars[i])+1>flag)flag=map.get(chars[i])+1;
            }
            map.put(chars[i],i);
        }
        length = chars.length-flag;
        if(length>maxLength) maxLength=length;
        return maxLength;
    }

    public static void main(String[] args) {
        LengthOfLongestSubstring lols = new LengthOfLongestSubstring();
        System.out.println(lols.lengthOfLongestSubstring("abba"));
    }
}

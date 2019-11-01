package com.square.leetcode;

public class Atoi_8 {
    public static int myAtoi(String str) {
        int res = 0;
        if(str == null) return res;
        str= str.trim();
        int i = 0;
        int len = str.length();
        boolean flag = true;
        int limit = Integer.MAX_VALUE;
        if(len <=0) {
            return res;
        }else{
            char firstChar = str.charAt(i);
            if(firstChar == '-'){
                flag = false;
                i++;
                if(len ==1) return res;
            }else if(firstChar == '+'){
                i++;
                if(len ==1) return res;
            }else if (!Character.isDigit(firstChar)){
                return res;
            }
        }
        for(int j=i;j<len&&Character.isDigit(str.charAt(j));j++){
            int digit = Character.digit(str.charAt(j),10);
            if(flag){
                if(res>(Integer.MAX_VALUE-digit)/10)return Integer.MAX_VALUE;
            }else{
                if(res>(Integer.MAX_VALUE-digit+1)/10)return Integer.MIN_VALUE;
            }
            res=res*10+digit;
        }
        return flag ? res : -res;
    }

    public static void main(String[] args) {
        System.out.println(Atoi_8.myAtoi("-00000000000000001  sfsdf"));
//        System.out.println(Integer.parseInt("-0000000000000000000000001"));
    }
}

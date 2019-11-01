package com.square.leetcode;

public class IsPalindrome_9 {
    public static int reverse(int x) {
        int result = 0;
        while (x != 0) {
            if (result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && x % 10 > 7)) return 0;
            if (result < Integer.MIN_VALUE / 10 || (result == Integer.MIN_VALUE / 10 && x % 10 < -8)) return 0;
            result = result * 10 + x % 10;
            x = x / 10;
        }
        return result;
    }
    public static boolean isPalindrome(int x) {
        boolean res = false;
        if(x==reverse(x))res = true;
        return res;
    }

    public static void main(String[] args) {
        System.out.println(IsPalindrome_9.isPalindrome(1221));
    }
}

package com.square.leetcode;

import java.util.Arrays;

public class ZigZag_6 {
    public static String zigZag(String s, int numRows) {

        char[] chars = s.toCharArray();
        int row = Math.min(numRows, chars.length);
        if(row==1) return s;
        StringBuffer[] bufferArray = new StringBuffer[row];
        int nowRow = 0;
        //0 向下，1 向上
        int direction = 0;
        for(char c : chars){
            if (bufferArray[nowRow] == null) {
                bufferArray[nowRow] = new StringBuffer();
            }
            bufferArray[nowRow]
                    .append(c);
            //确定下一行
            if (nowRow == numRows - 1) {
                direction = 1;
            } else if (nowRow == 0) {
                direction = 0;
            }
            if (direction == 0) {
                nowRow++;
            } else {
                nowRow--;
            }
        }
        String result = Arrays.stream(bufferArray).reduce(new StringBuffer(""), (x, y) -> x.append(y)).toString();
        return result;
    }

    public static void main(String[] args) {
        String s = "AB";
        System.out.println(ZigZag_6.zigZag("AB", 1));

    }
}

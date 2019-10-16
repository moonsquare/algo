package com.square.leetcode;

import java.util.HashMap;
import java.util.Map;

public class TwoSum_1 {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map=new HashMap();
        int[] result=new int[2];
        for(int i=0;i<nums.length;i++){
            int s = target-nums[i];
            if(map.get(s)!=null){
                result[0]=map.get(s);
                result[1]=i;
                return result;
            }else{
                map.put(nums[i],i);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        TwoSum_1 ts = new TwoSum_1();
        System.out.println(ts.twoSum(nums,target));

    }
}

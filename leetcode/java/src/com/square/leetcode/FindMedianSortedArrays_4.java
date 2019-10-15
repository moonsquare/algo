package com.square.leetcode;

public class FindMedianSortedArrays_4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        double result;
        int[] nums3 = new int[nums1.length+nums2.length];
        int i=0;
        int j=0;
        int k=0;

        while( i< nums1.length || j <nums2.length){
            if(i==nums1.length){
                nums3[k]=nums2[j];
                j++;
                k++;
                continue;
            }
            if(j==nums2.length){
                nums3[k]=nums1[i];
                i++;
                k++;
                continue;
            }
            if(nums1[i] > nums2[j]){
                nums3[k]=nums2[j];
                j++;
            }else{
                nums3[k]=nums1[i];
                i++;
            }
            k++;
        }
        if(nums3.length%2==1){
            result=nums3[nums3.length/2];
        }else{
            result=(nums3[nums3.length/2]+nums3[nums3.length/2-1])/2.0;
        }
        return result;
    }

    public static void main(String[] args) {
        int[] a = {1,3};
        int[] b = {2,4};
        FindMedianSortedArrays_4  f = new FindMedianSortedArrays_4();
        System.out.println(f.findMedianSortedArrays(a,b));
    }
}

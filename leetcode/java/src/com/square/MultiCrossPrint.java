package com.square;

public class MultiCrossPrint {
    //static volatile int num = 1;
    static Object o = new Object();

    public static void main(String[] args) {

//        new Thread(() -> {
//            while(num < 100){
//                synchronized (o){
//                    if(num%2==1){
//                        System.out.println(num);
//                        num++;
//                        o.notifyAll();
//                    }else{
//                        try {
//                            o.wait();
//                        } catch (InterruptedException e) {
//                            e.printStackTrace();
//                        }
//                    }
//                }
//
//            }
//
//        }).start();
        new Thread(new Runnable() {
            @Override
            public void run() {
                int num= 1;
                while(num < 100){
                    synchronized (o) {
                        o.notifyAll();
                        System.out.println(num);
                        num=num+2;
                        try {
                            o.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }

                }
            }
        } ).start();

        new Thread(() -> {
            int num= 2;
            while(num < 100){
                synchronized (o) {
                    o.notifyAll();
                    System.out.println(num);
                    num=num+2;
                    try {
                        o.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

            }

        }).start();
    }

}

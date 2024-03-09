package programmingjam9.q3;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n=scanner.nextInt();
        int[][] arr=new int[n][2];

        ArrayList<Integer> rejects=new ArrayList<>();
        rejects.add(2);
        ArrayList<Integer> members=new ArrayList<>();
        for (int i=0;i<n;i++){
            arr[i][0]=scanner.nextInt();
            arr[i][1]=scanner.nextInt();
        }
        for (int i=0;i<n;i++){
            if (arr[i][0]==1&&arr[i][1]!=2){
                members.add(arr[i][1]);
            }
            else if (arr[i][1]==1&&arr[i][0]!=2){
                members.add(arr[i][0]);
            }
        }
        for (int i=0;i<n;i++){
            if (arr[i][0]==2&&arr[i][1]!=1){
                rejects.add(arr[i][1]);
            }
            else if (arr[i][1]==2&&arr[i][0]!=1){
                rejects.add(arr[i][0]);
            }
        }
//        Iterator<Integer> rejIterator=rejects.iterator();
//        while (rejIterator.hasNext()){
//            Integer reject=rejIterator.next();
//            for (int i=0;i<n;i++){
//                if (arr[i][0]==reject&&arr[i][1]!=1){
//                    rejects.add(arr[i][1]);
//                }
//                else if (arr[i][1]==reject&&arr[i][0]!=1){
//                    rejects.add(arr[i][0]);
//                }
//            }
//        }
        Integer[] rejectsArr=rejects.toArray(new Integer[0]);
        Iterator<Integer> iterator = members.iterator();

        while (iterator.hasNext()){
            Integer element = iterator.next();
            for (int i=0;i<n;i++){
                for (int j=0;j<rejectsArr.length;j++){
                    if (arr[i][0]==element&&arr[i][1]==rejectsArr[j]){
                        iterator.remove();
                    }
                    else if (arr[i][1]==element&&arr[i][0]==rejectsArr[j]){
                        iterator.remove();
                    }
                }
            }
        }
        Integer[] memberArr=members.toArray(new Integer[0]);
        Arrays.sort(memberArr);
        if (memberArr.length>0){
            for (int elem: memberArr){
                System.out.print(elem+" ");
            }
        }
        else System.out.print("nobody");

    }
}
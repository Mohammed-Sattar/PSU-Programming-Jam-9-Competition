package programmingjam9.q10;

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        int R = 0;
        int C = 0;
        int A = 0;
        int B = 0;
        int [][] arr = new int[T][4];
        
        for (int i = 0; i < T; i++) {
            R = scanner.nextInt();
            C = scanner.nextInt();
            A = scanner.nextInt();
            B = scanner.nextInt();
            arr[i][0] = R;
            arr[i][1] = C;
            arr[i][2] = A;
            arr[i][3] = B;
        }

        for (int i = 0; i < T; i++) {
            R = arr[i][0];
            C = arr[i][1];
            A = arr[i][2];
            B = arr[i][3];

            System.out.print("Case #"+ i + ":");            
            String result = hasWinningStrategy(R, C, A, B);
            System.out.println(result);
        }
        
        scanner.close();
    }
    
    public static String hasWinningStrategy(int R, int C, int A, int B) {
        // Check if the target coordinates are (1, 1)
        if (R == 1 && C == 1) {
            return "YES";
        }
        
        // Check if the target coordinates are on the same row or column as (1, 1)
        if (R == 1 || C == 1) {
            return "NO";
        }
        
        // Check if A divides R or B divides C
        if (R % A == 0 || C % B == 0) {
            return "YES";
        }
        
        // Check if A is even and B is odd, or A is odd and B is even
        if ((A % 2 == 0 && B % 2 != 0) || (A % 2 != 0 && B % 2 == 0)) {
            return "YES";
        }
        
        return "NO";
    }
}

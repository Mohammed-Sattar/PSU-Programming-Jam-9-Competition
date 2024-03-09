package programmingjam9.q5;

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read input values
        int levels = scanner.nextInt(); // Number of levels
        int officesPerLevel = scanner.nextInt(); // Number of offices on each level
        int serversToTurnOff = scanner.nextInt(); // Number of servers to turn off
        int serversRemainging = serversToTurnOff;

        // Read online offices for each level
        int[] onlineOffices = new int[levels];
        for (int i = 0; i < levels; i++) {
            onlineOffices[i] = scanner.nextInt();
        }

        // Calculate initial total online offices
        int initialTotal = 0;
        for (int offices : onlineOffices) {
            initialTotal += offices;
        }

        int[][] floorArr = new int[levels][officesPerLevel];
        for (int i = 0; i < levels; i++) {
            for (int j = 0; j < officesPerLevel; j++) {
                if (j < onlineOffices[i]) {
                    floorArr[i][j] = 1;
                } else {
                    floorArr[i][j] = 0;
                }
            }
        }
        
        while (serversRemainging > 0) {
            int minVal = Arrays.stream(onlineOffices).min().orElse(0);
            int newValue = officesPerLevel - minVal;
    
            // Update the array with the new value
            for (int j = 0; j < onlineOffices.length; j++) {
                if (onlineOffices[j] == minVal) {
                    onlineOffices[j] = newValue;
                    serversRemainging--;
                    break; // Assuming there's only one minimum value
                }
            }
        }

        int sum = 0;
        for (int office : onlineOffices) {
            sum += office;
        }
        System.out.println(sum);
    }
}

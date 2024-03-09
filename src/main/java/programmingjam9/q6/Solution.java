package programmingjam9.q6;

import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int solarPanels_N = sc.nextInt();
        int numOfOperations_Q = sc.nextInt();

        // try {
        //     solarPanels_N = sc.nextInt();
        //     numOfOperations_Q = sc.nextInt();
        //     if (solarPanels_N < 0 || numOfOperations_Q > 100000) {
        //         System.exit(0);
        //     }
        // } catch (Exception e) {
        //     System.exit(0);
        // }
        

        double[] solarPanelsEfficiency = new double[solarPanels_N];
        double[][] rowValues = new double[numOfOperations_Q][3];
        double[][] tempRows = Arrays.copyOf(rowValues, rowValues.length);

        for (int i = 0; i < solarPanels_N; i++) {
            solarPanelsEfficiency[i] = sc.nextDouble();
        }

        for (int i = 0; i < numOfOperations_Q; i++) {
            for (int j = 0; j < 3; j++) {
                rowValues[i][j] = sc.nextDouble();
            }
        }

        for (double[] ds : tempRows) {
            int operation = (int) ds[0];
            double[] row = Arrays.copyOf(ds, ds.length);
            operation(operation, row, solarPanelsEfficiency, solarPanels_N);
        }
    }

    public static void operation (int operation, double[] row, double[] solarPanelsEfficiency, int solarPanels_N) {
        int solarPanel_L = 0;
        int solarPanel_R = 0;

        if (operation != 1 && operation!= 2 && operation!= 3) {
            System.exit(0);
        }

        switch (operation) {
            case 1:
                int solarPanel_index = (int) row[1];

                double[] updatedEfficiency = Arrays.copyOf(solarPanelsEfficiency, solarPanelsEfficiency.length);
                updatedEfficiency[solarPanel_index] = row[2];         
                break;

            case 2:
                solarPanel_L = (int) row[1];
                solarPanel_R = (int) row[2];
                double maxEfficiency = 0;
                int maxEfficiencyIndex = solarPanel_L - 1; // Initialize the index to the leftmost solar panel
                for (int i = solarPanel_L-1; i < solarPanel_R; i++) {
                    if (solarPanelsEfficiency[i] > solarPanelsEfficiency[maxEfficiencyIndex]) {
                        maxEfficiencyIndex = i; // Update the index if a larger value is found
                    }
                }
                maxEfficiency = solarPanelsEfficiency[maxEfficiencyIndex];
                System.out.println(maxEfficiency);
                break;

            case 3:
                solarPanel_L = (int) row[1];
                solarPanel_R = (int) row[2];

                float sum = 0;
                float avgEfficiency = 0;

                for (int i = solarPanel_L-1; i < solarPanel_R; i++) {
                    // System.out.println(solarPanelsEfficiency[i]);
                    sum += solarPanelsEfficiency[i];
                }
                avgEfficiency = sum / (solarPanel_R - solarPanel_L + 1);
                double roundedValue = Math.round(avgEfficiency * 10.0) / 10.0;
                // System.out.println(avgEfficiency);
                System.out.println(roundedValue);
                break;
            
            default:
                break;
        }
    }
}

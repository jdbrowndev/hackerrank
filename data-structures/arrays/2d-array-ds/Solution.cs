using System;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 7-23-16</para>
/// <para>
/// Solves the 2D array DS problem by finding the max hourglass sum.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/2d-array
/// </para>
/// </summary>
public class Solution
{
    public static void Main()
    {
        int[,] arr = new int[6, 6];

        // Populate arr.
        for (int r = 0; r < arr.GetLength(0); r++)
        {
            string[] input = Console.ReadLine().Split(' ');
            for (int c = 0; c < arr.GetLength(1); c++)
            {
                arr[r, c] = Convert.ToInt32(input[c]);
            }
        }

        // Find max hourglass sum.
        int max = int.MinValue;
        for (int r = 0; r <= 3; r++)
        {
            for (int c = 0; c <= 3; c++)
            {
                int sum = arr[r, c] + arr[r, c + 1] + arr[r, c + 2] // Hourglass top.
                          + arr[r + 1, c + 1] // Middle.
                          + arr[r + 2, c] + arr[r + 2, c + 1] + arr[r + 2, c + 2]; // Bottom.
                if (sum > max)
                    max = sum;
            }
        }

        // Output max.
        Console.WriteLine(max);
    }
}
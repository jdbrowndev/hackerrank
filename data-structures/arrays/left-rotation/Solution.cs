using System;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 8-3-16</para>
/// <para>
/// Solves the array left rotation problem.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/array-left-rotation
/// </para>
/// </summary>
public class Solution
{
    public static void Main()
    {
        // Read d (don't need n).
        string[] args = Console.ReadLine().Split(' ');
        int d = Convert.ToInt32(args[1]);

        // Print state of array after d rotations.
        string[] arr = Console.ReadLine().Split(' ');
        for (int i = d; i < arr.Length; i++)
        {
            Console.Write($"{arr[i]} ");
        }
        for (int i = 0; i < d; i++)
        {
            Console.Write($"{arr[i]} ");
        }
    }
}
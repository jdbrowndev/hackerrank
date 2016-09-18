using System;
using System.Linq;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 9-17-16</para>
/// <para>
/// Solves the maximum subarray problem.
/// Kadane's algorithm is used to find the maximum contiguous subarray.
/// A similar technique is used to find the maximum non-contiguous subarray.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/maxsubarray
/// </para>
/// </summary>
public class Solution
{
    public static void Main()
    {
        int t = Convert.ToInt32(Console.ReadLine());
        for (int i = 1; i <= t; i++)
        {
            Console.ReadLine(); // Don't need n.
            int[] arr = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
            Console.WriteLine("{0} {1}", GetMaxContiguousSubArray(arr), GetMaxNonContiguousSubArray(arr));
        }
    }

    private static int GetMaxContiguousSubArray(int[] arr)
    {
        int currentMax = arr[0],
            overallMax = arr[0];

        for (int i = 1; i < arr.Length; i++)
        {
            currentMax = Math.Max(arr[i], currentMax + arr[i]);
            overallMax = Math.Max(currentMax, overallMax);
        }

        return overallMax;
    }

    private static int GetMaxNonContiguousSubArray(int[] arr)
    {
        int max = int.MinValue;
        int? sum = null;

        foreach (int i in arr)
        {
            if (i > max)
                max = i;
            if (i > 0)
            {
                if (sum == null)
                    sum = i;
                else
                    sum += i;
            }
        }

        return Math.Max(max, sum ?? int.MinValue);
    }
}

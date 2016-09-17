using System;
using System.Collections.Generic;
using System.Linq;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 9-17-16</para>
/// <para>
/// Solves the maximum subarray problem. This is a custom solution that is not as
/// efficient as Kadane's algorithm but works nonetheless.
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

    public static int GetMaxContiguousSubArray(int[] arr)
    {
        // First, traverse the array and sum adjacent positive integers and adjacent negative integers.

        int maxElement = arr[0];
        List<int> sums = new List<int>();
        bool previousPositive = false;
        
        foreach (int i in arr)
        {
            // Find the array's maximum element.
            // If all integers are negative, the array's maximum element is the solution.
            if (i > maxElement)
                maxElement = i;

            // Find sums.
            if (i > 0)
            {
                if (previousPositive)
                    sums[sums.Count - 1] += i;
                else
                    sums.Add(i);
                previousPositive = true;
            }
            else
            {
                if (previousPositive || !sums.Any())
                    sums.Add(i);
                else
                    sums[sums.Count - 1] += i;
                previousPositive = false;
            }
        }

        // Second, find the maximum sum within the sums list.

        // If the first sum is a negative integer, remove it since it cannot
        // contribute to the maximum sum.
        if (sums[0] <= 0)
            sums.RemoveAt(0);

        int maxAggregate;
        if (sums.Count == 0)
        {
            // This is the case where all integers in the array are negative.
            maxAggregate = int.MinValue;
        }
        else if (sums.Count <= 2)
        {
            // Choose max between first sum and second sum (if it exists).
            maxAggregate = Math.Max(sums[0], sums.Count == 2 ? sums[1] : int.MinValue);
        }
        else
        {
            // Else, integers are arranged in positive-negative-positive groups.
            // Combine each group when the first two elements have a sum > 0.
            for (int i = 0; i + 2 < sums.Count; i += 2)
            {
                int combined = sums[i] + sums[i + 1];
                if (combined > 0)
                    sums[i + 2] += combined;
            }
            maxAggregate = sums.Max();
        }

        return Math.Max(maxElement, maxAggregate);
    }

    private static int GetMaxNonContiguousSubArray(int[] arr)
    {
        // Solution is:
        //  - The max element if all integers in the array are negative
        //  OR
        //  - The sum of all positive integers.

        int max = arr[0];
        List<int> positiveInts = new List<int>();

        foreach (int i in arr)
        {
            if (i > max)
                max = i;
            if (i > 0)
                positiveInts.Add(i);
        }

        return positiveInts.Any() ? positiveInts.Sum() : max;
    }
}

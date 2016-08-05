using System;
using System.Linq;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 8-4-16</para>
/// <para>
/// Solves the sherlock and array problem.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/sherlock-and-array
/// </para>
/// </summary>
public class Solution
{
    public static void Main()
    {
        // Loop through all test cases.
        int t = Convert.ToInt32(Console.ReadLine());
        for (int i = 1; i <= t; i++)
        {
            Console.ReadLine(); // Don't need n.

            // For each test case, determine if there is an index in input such that the sum of the
            // left equals the sum of the right.
            int[] input = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
            Console.WriteLine(GetLeftSumEqualsRightSumIndex(input) == -1 ? "NO" : "YES");
        }
    }

    private static int GetLeftSumEqualsRightSumIndex(int[] array)
    {
        // Create an array that, at each index i, contains the sum of all elements before i.
        int[] beforeIndex = new int[array.Length];
        for (int i = 1; i < beforeIndex.Length; i++)
        {
            beforeIndex[i] = beforeIndex[i - 1] + array[i - 1];
        }

        // Create an array that, at each index i, contains the sum of all elements after i.
        // For better speed, create this array as the problem is being solved.
        int[] afterIndex = new int[array.Length];
        for (int i = array.Length - 1; i >= 0; i--)
        {
            if (i == array.Length - 1)
            {
                if (beforeIndex[i] == 0)
                    return i;
            }
            else if (i == 0)
            {
                afterIndex[i] = afterIndex[i + 1] + array[i + 1];
                if (afterIndex[i] == 0)
                    return i;
            }
            else
            {                
                afterIndex[i] = afterIndex[i + 1] + array[i + 1];
                if (beforeIndex[i] == afterIndex[i])
                    return i;
            }
        }

        // Return -1 if no index found.
        return -1;
    }
}

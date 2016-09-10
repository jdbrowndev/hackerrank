using System;
using System.Linq;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 9-9-16</para>
/// <para>
/// Uses a greedy algorithm to solve the greedy florist problem.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/greedy-florist
/// </para>
/// </summary>
public class Solution
{
    public static void Main()
    {
        // Read inputs.
        int[] args = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).ToArray();
        int n = args[0], k = args[1];

        int[] flowers = Console.ReadLine().Split(' ').Select(x => Convert.ToInt32(x)).OrderByDescending(x => x).ToArray();

        // Get minimum cost.
        Console.WriteLine(GetMinimumPurchaseCost(k, flowers));
    }

    private static int GetMinimumPurchaseCost(int k, int[] flowers)
    {
        int cost = 0, costMultiplier = 1;
        for (int i = 0; i < flowers.Length; i++)
        {
            cost += costMultiplier*flowers[i];

            // After every k flowers bought, increase the cost multiplier by 1.
            if ((i + 1)%k == 0)
                costMultiplier++;
        }
        return cost;
    }
}

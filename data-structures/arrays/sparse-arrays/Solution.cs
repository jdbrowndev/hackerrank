using System;
using System.Collections.Generic;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 8-3-16</para>
/// <para>
/// Uses a dictionary to solve the sparse arrays problem.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/sparse-arrays
/// </para>
/// </summary>
public class Solution
{
    private static Dictionary<string, int> _occurrences = new Dictionary<string, int>();

    public static void Main()
    {
        // Map strings to number of occurrences.
        int n = Convert.ToInt32(Console.ReadLine());
        for (int i = 1; i <= n; i++)
        {
            string str = Console.ReadLine();
            if (_occurrences.ContainsKey(str))
            {
                _occurrences[str]++;
            }
            else
            {
                _occurrences[str] = 1;
            }
        }

        // Respond to queries.
        int q = Convert.ToInt32(Console.ReadLine());
        for (int i = 1; i <= q; i++)
        {
            string query = Console.ReadLine();
            Console.WriteLine(_occurrences.ContainsKey(query) ? _occurrences[query] : 0);
        }
    }
}

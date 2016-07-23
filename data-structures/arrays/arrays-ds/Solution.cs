using System;
using System.Linq;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 7-23-16</para>
/// <para>
/// Solves the arrays DS problem by printing elements in reverse order.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/arrays-ds
/// </para>
/// </summary>
public class Solution
{
    public static void Main()
    {
        Console.ReadLine(); // Don't need n.
        Console.ReadLine().Split(' ').Reverse().ToList().ForEach(x => Console.Write($"{x} "));
    }
}
using System;
using System.Collections.Generic;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 7-23-16</para>
/// <para>
/// Solves the dynamic array problem via the DynamicArray class.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/dynamic-array
/// </para>
/// </summary>
public class Solution
{
    public static void Main()
    {
        string[] args = Console.ReadLine().Split(' ');
        int n = Convert.ToInt32(args[0]), q = Convert.ToInt32(args[1]);
        var dynamicArray = new DynamicArray(n);

        for (int i = 1; i <= q; i++)
        {
            string[] query = Console.ReadLine().Split(' ');
            if (query[0] == "1")
            {
                dynamicArray.Add(Convert.ToInt32(query[1]), Convert.ToInt32(query[2]));
            }
            else if (query[0] == "2")
            {
                int lastAns = dynamicArray.Get(Convert.ToInt32(query[1]), Convert.ToInt32(query[2]));
                Console.WriteLine(lastAns);
            }
        }
    }
}

public class DynamicArray
{
    private readonly int _size;
    private readonly List<int>[] _sequences;

    private int _lastAns;

    public DynamicArray(int size)
    {
        _size = size;
        _sequences = new List<int>[size];
        _lastAns = 0;

        for (int i = 0; i < size; i++)
        {
            _sequences[i] = new List<int>();
        }
    }

    public void Add(int x, int y)
    {
        var seq = _sequences[(x ^ _lastAns)%_size];
        seq.Add(y);
    }

    public int Get(int x, int y)
    {
        var seq = _sequences[(x ^ _lastAns)%_size];
        _lastAns = seq[y%seq.Count]; 
        return _lastAns;
    }
}

using System;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 7-17-16</para>
/// <para>
/// Solves the merging communities problem via a DisjointSet class.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/merging-communities
/// </para>
/// </summary>
public class Solution
{
    public static void Main()
    {
        string[] args = Console.ReadLine().Split(' ');
        int n = Int32.Parse(args[0]);
        int q = Int32.Parse(args[1]);

        DisjointSet set = new DisjointSet(n);

        for (int i = 1; i <= q; i++)
        {
            string[] query = Console.ReadLine().Split(' ');

            if (query[0] == "Q")
            {
                Console.WriteLine(set.GetSetSize(Int32.Parse(query[1])));
            }
            else if (query[0] == "M")
            {
                set.MergeSets(Int32.Parse(query[1]), Int32.Parse(query[2]));
            }
        }
    }
}

public class DisjointSet
{
    private readonly int[] _sets;
    private readonly int[] _ranks;

    public DisjointSet(int size)
    {
        _sets = new int[size + 1];
        _ranks = new int[size + 1];

        for (int i = 1; i < size + 1; i++)
        {
            _sets[i] = i;
            _ranks[i] = 1;
        }
    }

    public int GetSetSize(int element)
    {
        int tail = FindTail(element);
        return _ranks[tail];
    }

    public void MergeSets(int elementOne, int elementTwo)
    {
        int tailOne = FindTail(elementOne), tailTwo = FindTail(elementTwo);

        if (tailOne != tailTwo)
        {
            _ranks[tailTwo] += _ranks[tailOne];
            _sets[tailOne] = tailTwo;
        }
    }

    private int FindTail(int element)
    {
        if (_sets[element] == element)
        {
            return element;
        }

        int tail = FindTail(_sets[element]);
        _sets[element] = tail; // Optimizes path to tail in the future.
        return tail;
    }
}
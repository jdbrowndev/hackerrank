using System;
using System.Collections.Generic;

/// <summary>
/// My original attempt at the problem using a Dictionary of HashSets.
/// </summary>
public class OldDictionarySolution
{
    private static Dictionary<int, HashSet<int>> Communities;

    public static void RunOldDictionarySolution()
    {
        string[] args = Console.ReadLine().Split(' ');
        int n = Int32.Parse(args[0]);
        int q = Int32.Parse(args[1]);

        Communities = new Dictionary<int, HashSet<int>>(n);

        for (int i = 1; i <= n; i++)
        {
            var community = new HashSet<int>();
            community.Add(i);
            Communities[i] = community;
        }

        for (int i = 1; i <= q; i++)
        {
            string[] query = Console.ReadLine().Split(' ');

            if (query[0] == "Q")
            {
                Console.WriteLine(QueryCommunity(Int32.Parse(query[1])));
            }
            else if (query[0] == "M")
            {
                MergeCommunities(Int32.Parse(query[1]), Int32.Parse(query[2]));
            }
        }
    }

    private static int QueryCommunity(int person)
    {
        return Communities[person].Count;
    }

    private static bool MergeCommunities(int personOne, int personTwo)
    {
        var communityOne = Communities[personOne];
        var communityTwo = Communities[personTwo];

        if (communityOne != null && communityTwo != null)
        {
            communityOne.UnionWith(communityTwo);
            foreach (int person in communityTwo)
            {
                Communities[person] = communityOne;
            }
            return true;
        }

        return false;
    }
}

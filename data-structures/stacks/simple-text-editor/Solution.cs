using System;
using System.Collections.Generic;
using System.Text;

/// <summary>
/// <para>Author: Jordan Brown</para>
/// <para>Date: 8-27-16</para>
/// <para>
/// Solves the simple text editor problem using .NET's StringBuilder and Stack classes.
/// </para>
/// <para>
/// Link to problem: https://www.hackerrank.com/challenges/simple-text-editor
/// </para>
/// </summary>
public class Solution
{
    private static readonly StringBuilder Text = new StringBuilder();
    private static readonly Stack<Operation> Operations = new Stack<Operation>();

    private struct Operation
    {
        public int Type { get; set; }
        public string Characters { get; set; }
    }

    public static void Main()
    {
        int q = Convert.ToInt32(Console.ReadLine());

        for (int i = 1; i <= q; i++)
        {
            string[] input = Console.ReadLine().Split(' ');
            int operation = Convert.ToInt32(input[0]);
            switch (operation)
            {
                case 1:
                    AppendCharacters(input[1]);
                    break;
                case 2:
                    RemoveCharacters(Convert.ToInt32(input[1]));
                    break;
                case 3:
                    PrintCharacter(Convert.ToInt32(input[1]) - 1);
                    break;
                case 4:
                    UndoOperation();
                    break;
            }
        }
    }

    private static void AppendCharacters(string str)
    {
        Text.Append(str);
        Operations.Push(new Operation { Type = 1, Characters = str });
    }

    private static void RemoveCharacters(int k)
    {
        string removedChars = Text.ToString(Text.Length - k, k);
        Text.Remove(Text.Length - k, k);
        Operations.Push(new Operation { Type = 2, Characters = removedChars });
    }

    private static void PrintCharacter(int k)
    {
        Console.WriteLine(Text[k]);
    }

    private static void UndoOperation()
    {
        var prevOperation = Operations.Pop();
        switch (prevOperation.Type)
        {
            case 1:
                Text.Remove(Text.Length - prevOperation.Characters.Length, prevOperation.Characters.Length);
                break;
            case 2:
                Text.Append(prevOperation.Characters);
                break;
        }
    }
}
internal class NewBaseType
{
    public void Main(string[] arg)
    {
        Console.WriteLine("\n >>>> 	To find palindrome");
        int num = Convert.ToInt32(Console.Readline());
        temp = num;
        while (num > 0)
        {
            rem = num % 10;
            num = num / 10;
            sum = sum * 10 + rem;
        }
        if (temp == sum)
        {
            Console.WriteLine("Number is palindrome");
        }
        else
        {
            Console.Writeline("Number is not palindrome");
        }
    }
}

internal class NewBaseType : NewBaseType
{
}

class program : NewBaseType
{
}
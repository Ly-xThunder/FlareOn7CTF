using System;
using System.Text;

namespace FlareOn7
{
    class Program
    {
        public static byte[] Password = new byte[]
        {
            62, 38, 63, 63, 54, 39, 59, 50, 39
        };

        public static string Decode(byte[] e)
        {
            string text = "";
            foreach (byte b in e)
            {
                text += Convert.ToChar((int)(b ^ 83)).ToString();
            }
            return text;
        }

        static void Main(string[] args)
        {
            Console.WriteLine(Decode(Password));
        }
    }
}
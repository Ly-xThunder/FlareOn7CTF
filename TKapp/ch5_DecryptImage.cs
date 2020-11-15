using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Security.Cryptography;
using ExifLib;

namespace FlareOn7
{
    class Program
    {
        static string rootPath = "";

        static string readImageDesc()
        {
            string fullPath = rootPath + @"\res\gallery\05.jpg";
            using (ExifReader exifReader = new ExifReader(fullPath))
            {
                string desc;
                if (exifReader.GetTagValue<string>(ExifTags.ImageDescription, out desc))
                {
                    return desc;
                }
                return "";
            }
        }

        static string getFinalNote(bool isHome)
        {
            List<Todo> list = new List<Todo>();
            if (!isHome)
            {
                list.Add(new Todo("go home", "and enable GPS", false));
            }
            else
            {
                Todo[] collection = new Todo[]
                {
                    new Todo("hang out in tiger cage", "and survive", true),
                    new Todo("unload Walmart truck", "keep steaks for dinner", false),
                    new Todo("yell at staff", "maybe fire someone", false),
                    new Todo("say no to drugs", "unless it's a drinking day", false),
                    new Todo("listen to some tunes", "https://youtu.be/kTmZnQOfAF8", true)
                };
                list.AddRange(collection);
            }
            List<Todo> list2 = new List<Todo>();
            foreach (Todo todo in list)
            {
                if (!todo.Done)
                {
                    list2.Add(todo);
                }
            }
            //this.mylist.ItemsSource = list2;
            //App.Note = list2[0].Note;
            return list2[0].Note;
        }

        public static string GetString(byte[] cipherText, byte[] Key, byte[] IV)
        {
            string result = null;
            using (RijndaelManaged rijndaelManaged = new RijndaelManaged())
            {
                rijndaelManaged.Key = Key;
                rijndaelManaged.IV = IV;
                ICryptoTransform cryptoTransform = rijndaelManaged.CreateDecryptor(rijndaelManaged.Key, rijndaelManaged.IV);
                using (MemoryStream memoryStream = new MemoryStream(cipherText))
                {
                    using (CryptoStream cryptoStream = new CryptoStream(memoryStream, cryptoTransform, 0))
                    {
                        using (StreamReader streamReader = new StreamReader(cryptoStream))
                        {
                            result = streamReader.ReadToEnd();
                        }
                    }
                }
            }
            return result;
        }

        static void Main(string[] args)
        {
            rootPath = args[0];
            string runtimeDll = rootPath + "Runtime.dll";
            byte[] cipherText = File.ReadAllBytes(runtimeDll);
            string Password = "mullethat";
            string Step = "magic";
            string Desc = readImageDesc();
            string Note = getFinalNote(true);
            string text = new string(new char[]
            {
                Desc[2], Password[6], Password[4], Note[4], Note[0], Note[17], Note[18], Note[16], Note[11], Note[13], Note[12], Note[15], Step[4], Password[6], Desc[1], Password[2], Password[2], Password[4], Note[18], Step[2], Password[4], Note[5], Note[4], Desc[0], Desc[3], Note[15], Note[8], Desc[4], Desc[3], Note[4], Step[2], Note[13], Note[18], Note[18], Note[8], Note[4], Password[0], Password[7], Note[0], Password[4], Note[11], Password[6], Password[4], Desc[4], Desc[3]
            });
            byte[] key = SHA256.Create().ComputeHash(Encoding.ASCII.GetBytes(text));
            byte[] bytes = Encoding.ASCII.GetBytes("NoSaltOfTheEarth");
            byte[] decrypted = Convert.FromBase64String(GetString(cipherText, key, bytes));
            File.WriteAllBytes(rootPath + "decrypted.jpg", decrypted);
            Console.WriteLine("Done");
            Console.ReadKey();
        }
    }

    public class Todo
    {
        public string Name { get; set; }

        public string Note { get; set; }

        public bool Done { get; set; }

        public Todo(string Name, string Note, bool Done)
        {
            this.Name = Name;
            this.Note = Note;
            this.Done = Done;
        }
    }
}

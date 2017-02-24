using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace algoritma_kuvvetalma
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(power(3, 5));
            Console.ReadKey();
        }

        public static int power(int a, int b)
        {
            int result = 1;
            for(int i=0;i<b;i++)
            {
                result = result * a;
            }
            return result;
        }
    }
}

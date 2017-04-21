using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace algoritma21nisan
{
    public class Program
    {
        public static void Main(string[] args)
        {
            int[] array = {1,2,3,4,5,6,7,8,9 };
            Console.WriteLine("Min:" + FindMin(array));
            Console.WriteLine("Max:" + FindMax(array));
            Console.WriteLine("Average:" + FindAverage(array));
            
        }

        public static double FindAverage(int[] array)
        {
            double sum = 0;
            foreach(int i in array)
            {
                sum += i;
            }
            return sum / array.Length;
        }

        public static int FindMin(int[] array)
        {
            int min = array[0];
            foreach(int i in array)
            {
                if(i<min)
                {
                    min = i;
                }
            }
            return min;
        }

        public static int FindMax(int[] array)
        {
            int max = array[0];
            foreach(int i in array)
            {
                if(i>max)
                {
                    max = i;

                }
            }
            return max;
        }

        public static double StdDeviation(int[] array)
        {
            double stdDev = 0;
            double mean = 0;
            foreach(int i in array)
            {
                mean += i;
            }
            mean /= array.Length;

            foreach(int i in array)
            {
                stdDev += (i - mean) * (i - mean);
            }

            stdDev /= array.Length;
            stdDev = Math.Sqrt(stdDev);
            return stdDev;
        }

        public static double Variance(int[] array)
        {
            double stdDev = StdDeviation(array);
            return Math.Pow(stdDev, 2);
        }

        public static double NormalDistrubition(int[] array)
        {
            return 1.0 / ((Math.Sqrt(2 * Math.PI * Math.Pow(Variance(array), 2))) * (Math.Pow(Math.E, 2)));
        }
    }
}

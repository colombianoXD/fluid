using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Primes_DigitSumiAlsoPrime
    {
        public static void Main2(String[] Args)
        {
            int cant = 0;

            for (int i = 1000000; i > 0; i++)
            {
                if (EsPrimo(i))
                {
                    Char[] StrI = i.ToString().ToCharArray();
                    int intSuma = 0;
                    foreach (char ch in StrI)
                    {
                        int digit = int.Parse(ch.ToString());
                        intSuma += digit;

                    }
                    if (EsPrimo(intSuma))
                    {
                        System.Console.WriteLine(i.ToString());
                        cant++;
                    }

                }
                if (cant > 2)
                {
                    break;
                }
            }
            System.Console.Read();
        }

        static Boolean EsPrimo(int numero)
        {
            int a = 0, i;
            for (i = 1; i <= numero; i++)
            {
                if (numero % i == 0)
                {
                    a++;
                }
            }
            if (a != 2)
            {
                return false;
            }
            else
            {
                return true;
            }

        }
    }
}

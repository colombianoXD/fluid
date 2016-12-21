using System.IO;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text.RegularExpressions;

class PackageProblem
{
    //
    static Dictionary<int, double> weight = new Dictionary<int, double>();
    static Dictionary<int, double> price = new Dictionary<int, double>();
    static ArrayList answer = new ArrayList();
    static string temp = "";
    static double max_weight = 0.0;
    static double curr_weight = 0.0;

    static void Main(string[] args)
    {
        using (StreamReader reader = File.OpenText(args[0]))
        while (!reader.EndOfStream)
        {

            string line = reader.ReadLine();
            if (line.Contains("-"))
            {
                Console.WriteLine(line);
                continue;
            }

                Regex pattern = new Regex("[$()]");
                line = pattern.Replace(line, "");

                double max_Price = 0.0;
                string res = "-";
                string[] parts = line.Split(' ');
                max_weight = Convert.ToDouble(parts[0]);
                int lenPaks = parts.Length -2;

                parsePaks(parts, max_weight);
                recurPaks(1,lenPaks);

                answer.Remove(null);


                foreach(string id in answer)
                {
                    if (id == " ") continue;

                    double curr_Price = 0.0;
                    string item = id.Remove(id.Length - 1);
                    //Console.WriteLine(id);
                    foreach (string c in item.Split(','))
                    {
                        //Console.WriteLine(c);
                        curr_Price += price[Int32.Parse(c)];
                    }

                   if (curr_Price == max_Price)
                    {
                        double item_Weight = 9999999.0;
                        double res_Weight = 9999999.0;

                        foreach (string c in item.Split(','))
                        {
                            item_Weight += weight[Int32.Parse(c)];
                        }

                        foreach (string c in item.Split(','))
                        {
                            res_Weight += weight[Int32.Parse(c)];
                        }

                        if (item_Weight < res_Weight) res = item;
                    }

                    if (curr_Price > max_Price)
                    {
                        max_Price = curr_Price;
                        res = item;
                    }

                }

                //res = res.Trim();
                Console.WriteLine(res);

            //Console.WriteLine(line);
            temp = "";
            weight.Clear();
            price.Clear();
            answer.Clear();
            max_weight = 0.0;
            curr_weight = 0.0;

        }
    }

    static void recurPaks(int k, int len){


        if (k > len) return;

        for (int i = k; k <= len; i++){

             //Console.WriteLine("antes: "+i);
             if (i > len) return;
             if (weight.ContainsKey(i)) curr_weight += weight[i];
             else continue;

            // Console.WriteLine("despues:"+i);
            // Console.WriteLine("curr_weight antes = "+curr_weight);

             if (curr_weight < max_weight)
             {
                //temp += ",";
                temp += i.ToString()+ ",";
               // Console.WriteLine(temp);
                if (!answer.Contains(temp)) answer.Add(temp.Trim());
                //Console.WriteLine("Recursion a continuacion");
                recurPaks(++i,len);
                //continue;


             }else{
                curr_weight -= weight[i];
                //Console.WriteLine("curr_weight despues = "+curr_weight);
                continue;
             }
             //Console.WriteLine("llego hastaaaaaaaaaa acaaaaaaa");
             i--;
             //temp = temp.Remove(temp.Length - 1);

             temp = temp.Remove(temp.Length - i.ToString().Length - 1);
             curr_weight -= weight[i];

        }
        return;
    }

    static void parsePaks(string[] paks, double max_w)
    {
        for (int i = 2; i < paks.Length; i++)
        {
            if (getW(paks[i]) < max_w)
            {
                weight.Add(getIdx(paks[i]),getW(paks[i]));
                price.Add(getIdx(paks[i]),getP(paks[i]));
            }
        }
    }

    static int getIdx(string pak){ return Int32.Parse(pak.Split(',')[0]); }
    static double getW(string pak){ return Convert.ToDouble(pak.Split(',')[1]);}
    static double getP(string pak){ return Convert.ToDouble(pak.Split(',')[2]);}

}

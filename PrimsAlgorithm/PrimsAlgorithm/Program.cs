using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Markup;

namespace Algorithm_Prim
{
    class Program
    {
        static void Main(string[] args)
        {
            Initialization();
            Prim();
            Output();
            Console.ReadLine();
        }

        struct Edge
        {
            public int u, v;
        };

        static int[,] graph; // 
        static List<int> MST; // Minimum spanning tree или минимален път
        static List<Edge> EDGE;
        static List<int> Values;
       
        static void Prim()
        {
            int u = -1, ///съществуващ възел
                v = -1; ///нов възел
            int min;
            int n = graph.GetLength(0);

            int x = 0; //стартов възел
            MST.Add(x);
 
            while (MST.Count != n)
            {
                min = int.MaxValue;
                
                foreach (int i in MST)
                {
                    for (int j = 0; j < n; j++)
                    {
                        if (MST.Contains(j)) continue;
                        if (graph[i, j] != 0 && graph[i, j] < min)
                        {
                            min = graph[i, j];
                            u = i; v = j;
                        }
                    }
                }
                MST.Add(v);
                Values.Add(min);
                Edge e = new Edge();
                e.u = u; e.v = v;
                EDGE.Add(e);
            }
        }

        static void Initialization()
        {

            graph = new int[,]
            {
                {0,17,0,26,0,0,0},
                {17,0,5,10,0,0,0},
                {0,5,0,3,2,20,0},
                {26,10,3,0,8,0,0},
                {0,0,2,8,0,8,0},
                {0,0,20,0,8,0,9},
                {0,0,0,0,0,9,0}
            };
            MST = new List<int>();
            EDGE = new List<Edge>();
            Values = new List<int>();
        }

        static void Output()
        {
            Console.Write("Minimum path: ");
            foreach (int i in MST)
            {
                Console.Write("{0} ", i + 1);
            }
            Console.WriteLine();
            Console.Write("Edges: ");
            foreach (Edge e in EDGE)
            {
                Console.Write("({0}, {1}) ", e.u+1, e.v+1);
            }
            Console.WriteLine();
            int F = 0;
            foreach (var item in Values)
            {
                F += item;
            }
            Console.WriteLine("Fmin= {0}", F);
        }
    }
}

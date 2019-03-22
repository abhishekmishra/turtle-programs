using System;
using picoturtle;

namespace cspico
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            // Create the turtle before using
            Turtle t = picoturtle.Turtle.CreateTurtle(args);
            
            if (t != null) {
                // Your code goes here

                t.pendown();
                t.pencolour(255, 0, 0);
                var r = new Random();
                for(int i = 0; i < 100; i++) {
                    t.forward(r.Next(0, 10));
                    t.right(r.Next(-90, 90));
                }

                // Your code ends here

                // Always stop the turtle
                t.stop();
            }
            else {
                Console.Error.WriteLine("Error: Unable to create a turtle.");
                Environment.Exit(-1);
            }
        }
    }
}

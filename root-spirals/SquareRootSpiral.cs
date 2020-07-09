using System;
using picoturtle;

namespace cspico
{
    class SquareRootSpiral
    {
        private static double DegreeToRadian(double angle)
        {
            return Math.PI * angle / 180.0;
        }

        private static double RadianToDegree(double angle)
        {
            return angle * (180.0 / Math.PI);
        }

        public static void Main(string[] args)
        {
            // Create the turtle before using
            Turtle t = picoturtle.Turtle.CreateTurtle(args);
            
            if (t != null) {
                // Your code goes here
                
                t.canvas_size(1000, 1000);
                t.setpos(500, 500);
                int x = 50;
                t.pendown();
                t.pencolour(150, 50, 50);
                t.penwidth(3);
                t.right(90);
                t.forward(x);

                for (int i = 0; i < 30; i++) {
                    var angle = 90 - RadianToDegree(Math.Acos(1/Math.Sqrt(i+1)));
                    Console.WriteLine(angle);
                    t.left(angle);
                    t.forward(x);
                    t.pencolour(300 - 10 * i, 300 - 10 * i, 150);
                    var loc = t.state().location;
                    t.setpos(500, 500);
                    t.setpos(loc.x, loc.y);
                    t.pencolour(150, 50, 50);
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

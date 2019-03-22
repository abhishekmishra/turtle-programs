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

                t.penup();
                t.pencolour(0, 255, 255);
                t.sety(0);
                t.setx(0);
                t.right(90);
                t.font("12pt Courier");
                t.filltext("random turtle");
                
                t.home();
                t.pendown();
                t.penwidth(4);

                var r = new Random();
                for(int i = 0; i < 100; i++) {
                    t.pencolour(r.Next(0, 255), 
                                r.Next(0, 255), 
                                r.Next(0, 255));
                    t.forward(r.Next(0, 20));
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

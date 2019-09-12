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

                t.canvas_size(100, 400);
                t.penup();
                t.setpos(50, 200);
                t.pencolour(128, 255, 255);
                t.pendown();
                t.forward(150);
                t.export_img("d:\\testimg.png");
                
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

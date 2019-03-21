using System;
using picoturtle;

namespace cspico
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            // Create the turtle before using
            Turtle t = new picoturtle.Turtle(name: args[0], port: Int32.Parse(args[1]));

            // Your code goes here

            t.pendown();
            t.pencolour(128, 128, 0);
            t.forward(100);

            // Your code ends here

            // Always stop the turtle
            t.stop();
        }
    }
}

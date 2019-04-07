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
                t.setx(0);
                t.sety(250);

                for(double i = 0; i < 500; i+=0.25) {
                    t.setx(i);
                    double sin = Math.Sin(i/15);
                    double y = sin * 100;
                    t.forward(y);
                    t.pendown();
                    int col = Math.Abs((int)(sin * 255));
                    t.pencolour(
                        128 + col/3, 
                        col,
                        255 - col/2
                    );
                    double pw = 40 * sin;
                    if (pw > 0) {
                        pw += 5;
                     } else { 
                        pw -= 5;
                     }
                    t.forward(pw);
                    t.penup();
                    t.back(y + pw);
                }

                t.penup();
                t.setx(0);
                t.sety(250);
                for(double i = 0; i < 500; i+=0.25) {
                    t.setx(i);
                    double sin = -Math.Sin(i/15);
                    double y = sin * 100;
                    t.forward(y);
                    t.pendown();
                    int col = Math.Abs((int)(sin * 255));
                    t.pencolour(
                        128 + col/3, 
                        col,
                        255 - col/2
                    );
                    double pw = 40 * sin;
                    if (pw > 0) {
                        pw += 5;
                     } else { 
                        pw -= 5;
                     }
                    t.forward(pw);
                    t.penup();
                    t.back(y + pw);
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

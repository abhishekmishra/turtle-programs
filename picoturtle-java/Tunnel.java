import in.abhishekmishra.picoturtle.Turtle;
import in.abhishekmishra.picoturtle.TurtleState;

public class Tunnel
{
    public static void cuboid(Turtle t, double b, double w, double h) {
        t.forward(b);

        t.right(-45);
        t.forward(h);
        t.back(h);
        t.left(-45);

        t.left(90);
        t.forward(w);

        t.left(-45);
        t.forward(h);
        t.back(h);
        t.right(-45);

        t.left(90);
        t.forward(b);

        t.left(-135);
        t.forward(h);
        t.back(h);
        t.right(-135);

        t.left(90);
        t.forward(w);

        t.right(-135);
        t.forward(h);
        t.left(-135);

        t.left(90);
        t.forward(b);
        t.left(90);
        t.forward(w);
        t.left(90);
        t.forward(b);
        t.left(90);
        t.forward(w);
        t.pendown();
    }

    public static void main(String[] args)
    {
        // Create the turtle before using
        Turtle t = Turtle.CreateTurtle(args);
        
        if (t != null) {
            // Your code goes here

            t.penup();
            t.setx(300);
            t.sety(200);
            t.heading(100);
            TurtleState ts = t.state();

            for (double i = 1; i < 50; i+=1.5) {
                double b = i*8, w = i*8, h = i/2;
                t.right(90);
                t.back(b/2);

                t.left(90);
                t.back(w/2);

                t.heading(i*0.7);
                t.pendown();
                t.penwidth(1);
                t.pencolour((int)(4*i), (int)(255 - 3*i), (int)(5*i));
                cuboid(t, b, w, h);

                t.penup();
                t.heading(ts.angle);
                t.setx(ts.location.x);
                t.sety(ts.location.y);
            }

            // Your code ends here

            // Always stop the turtle
            t.stop();
        }
        else {
            System.out.println("Error: Unable to create a turtle.");
            System.exit(-1);
        }
    }
}

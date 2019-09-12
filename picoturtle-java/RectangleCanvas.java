import in.abhishekmishra.picoturtle.Turtle;
import in.abhishekmishra.picoturtle.TurtleState;

public class RectangleCanvas //change this to match the file name
{
    public static void main(String[] args)
    {
        // Create the turtle before using
        Turtle t = Turtle.CreateTurtle(args);
        
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
            System.out.println("Error: Unable to create a turtle.");
            System.exit(-1);
        }
    }
}

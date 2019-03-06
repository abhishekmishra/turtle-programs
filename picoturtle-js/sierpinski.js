const { create_turtle, penup, pendown, penwidth, clear, stop, pencolour, forward, right, left, print } = require('@picoturtle/picoturtle-nodejs-client');

let main = async () => {
    await create_turtle();
    /* Your code goes here */

    function draw_sierpinski(length, depth) {
        if(depth == 0) {
            pendown();
            for(var i = 0; i < 3; i++) {
                forward(length);
                left(120);
            }
            penup();
        }
        else {
            let half = length/2.0;
            draw_sierpinski(half, depth - 1);
            forward(half);
            draw_sierpinski(half, depth - 1);
            forward(-half);
            left(60);
            forward(half);
            right(60);
            draw_sierpinski(half, depth - 1);
            left(60);
            forward(-half);
            right(60);
        }
    }

    left(90);
    forward(200);
    right(90);
    forward(-200);
    pencolour(255, 69, 0);
    penwidth(2);
    pendown();
    right(90);
    draw_sierpinski(400, 5);

    /* Your code ends here */

    /* Always stop the turtle */
    await stop();
};
main();
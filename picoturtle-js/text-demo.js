const { create_turtle, penup, pendown, penwidth, clear, stop, pencolour, forward, right, left, print, back, font, filltext, stroketext } = require('@picoturtle/picoturtle-nodejs-client');

let main = async () => {
    await create_turtle();
    /* Your code goes here */

    await penup();
    await back(250);
    await right(90);
    await forward(200);
    await left(90);
    
    await pendown();
    await right(90);

    for(var i = 0; i < 40; i++) {
        await font('' + i + 'pt Arial');
        if(i%2 == 0) {
            await pencolour(255, 128, 128);
            await filltext('पीको टर्टल');
        } else {
            await pencolour(255, 128, 255);
            await filltext('PicoTurtle');
        }
        await penup();
        // await back(10);
        await left(90 + 2);
        await forward(i * 1.3);
        await right(90);
        await pendown();
    }

    /* Your code ends here */

    /* Always stop the turtle */
    await stop();
};
main();
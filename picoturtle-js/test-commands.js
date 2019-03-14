const { create_turtle, home, clear, stop, print, state } = require('@picoturtle/picoturtle-nodejs-client');
const { font, filltext, stroketext } = require('@picoturtle/picoturtle-nodejs-client');
const { penup, pendown, penwidth, pencolour } = require('@picoturtle/picoturtle-nodejs-client');
const { left, right, forward, back } = require('@picoturtle/picoturtle-nodejs-client');
const { setpos, setx, sety, heading } = require('@picoturtle/picoturtle-nodejs-client');

let main = async () => {
    await create_turtle();
    /* Your code goes here */

    async function poly(side, angle, incs, inca) {
        for (var i = 0; i < 100; i++) {
            await forward(side);
            await right(angle);
            side += incs;
            angle += inca;
        }
    }
    await penup();
    await back(50);
    await pencolour(255, 0, 0);
    await pendown();
    await poly(5, 120, 3, 0);
    await penup();
    await forward(100);
    await font('bold 30pt Arial');
    await left(30);
    await pencolour(0, 255, 0);
    await filltext('नमस्ते');
    await penup();
    await forward(100);
    await pendown();
    await penwidth(1);
    await pencolour(255, 0, 255);
    await stroketext('दुनिया');
    await penup();
    await forward(120);
    await home();
    await setpos(10, 10);
    await pendown();
    await pencolour(255, 128, 0);
    await penwidth(5);
    await forward(150);
    await setx(40);
    await sety(100);
    await heading(0);
    let s = await state();
    console.log(s);

    /* Your code ends here */

    /* Always stop the turtle */
    await stop();
};

main()
    .catch((err) => {
        console.error(err);
        process.exit(1);
    });
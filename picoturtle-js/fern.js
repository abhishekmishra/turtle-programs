const { create_turtle, penup, pendown, penwidth, clear, stop, pencolour, forward, right, left, print } = require('@picoturtle/picoturtle-nodejs-client');

let main = async () => {
    await create_turtle();
    /* Your code goes here */

    async function fern(size, sign) {
        if (size < 2) {
            return;
        }
        await forward(size);

        await right(70 * sign);
        await fern(size/2, sign*-1);
        await left(70 * sign);

        await forward(size);

        await left(70 * sign);
        await fern(size/2, sign);
        await right(70 * sign);

        await right(7 * sign);
        await fern(size - 2, sign);
        await left(7 * sign);

        await forward(-size);
        await forward(-size);
    }

    await pencolour(0, 128, 0);
    await penup();
    await forward(-150);
    await pendown();
    await fern(20, 1);

    /* Your code ends here */

    /* Always stop the turtle */
    await stop();
};
main();
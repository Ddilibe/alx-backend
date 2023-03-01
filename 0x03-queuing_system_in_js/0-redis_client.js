import {createClient} from "redis";


function redisConnect() {

    const client = createClient();

    client.on('connect', () => {
        process.stdout.write("Redis client connected to the server");
    }).on('error', (err) => {
        process.stdout.write(`Redis client not connected to the server: ${err}`);
    });
}

redisConnect();

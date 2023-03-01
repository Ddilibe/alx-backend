import {createClient} from "redis";


const client = createClient();

client.on('connect', () => {
    process.stdout.write("Redis client connected to the server\n");
}).on('error', (err) => {
    process.stdout.write(`Redis client not connected to the server: ${err.message}\n`);
});

const channel = "holberton school channel";
client.subscribe(channel);
client.on('message', (channel, message) => {
    process.stdout.write(`${message}\n`);
    if (message === "KILL_SERVER") {
        client.unsubscribe(channel);
        client.quit();
    };
});

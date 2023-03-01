import {createClient} from "redis";


const client = createClient();

client.on('connect', () => {
    process.stdout.write("Redis client connected to the server\n");
}).on('error', (err) => {
    process.stdout.write(`Redis client not connected to the server: ${err.message}\n`);
});

async function publishMessage(message, time) {
    setTimeout(() => {
        process.stdout.write(`About to send ${message}\n`);
        client.publish("holberton school channel", message);
    }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

import {createClient, print} from "redis";
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
    process.stdout.write("Redis client connected to the server\n");
});
client.on('error', (err) => {
    process.stdout.write(`Redis client not connected to the server: ${err}\n`);
});

const keys = ["Portland", "Seattle", "New York", "Bogota", "Cali", "Paris"]
const value = ["50", "80", "20", "20", "40","2"]
const schoolName = "HolbertonSchools"

for (var i = 0; i < keys.length; i++) {
    client.hset("HolbertonSchools", keys[i], value[i], print);
};
client.hgetall("HolbertonSchools", (err, data) => {
    if (err) {
        process.stdout.write(`${err}\n`);
        throw err;
    }
    process.stdout.write(`${data}\n`);
});

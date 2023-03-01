import {createClient, print} from "redis";
import { promisify } from "util";

const client = createClient();

client.on('connect', () => {
    process.stdout.write("Redis client connected to the server\n");
});
client.on('error', (err) => {
    process.stdout.write(`Redis client not connected to the server: ${err}\n`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
};

function displaySchoolValue(schoolName) {
    const get = promisify(client.get).bind(client);
    get(schoolName).then((data) => {
        process.stdout.write(`${data}\n`);
    }).catch(err => {
        process.stdout.write(`${err}\n`);
            throw err;
    });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
// this

import {createClient, print} from "redis";

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
    client.get(schoolName, (err, data) => {
        if (err){
            process.stdout.write(`${err}\n`);
            throw err;
        }
        process.stdout.write(`${data}\n`);
    });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
// this

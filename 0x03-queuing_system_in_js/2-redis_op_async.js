import { createClient } from "redis";
const { promisify } = require('util');

const client = createClient({ url: 'redis://localhost:6379' });

client.on('error', err => {
  console.log('Redis client not connected to the server: ' + err);
});

client.on_connect(console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) throw err;
    console.log('Reply: ' + reply);
  });
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  console.log(await getAsync(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

import { createClient } from "redis";

const client = createClient({url: 'redis://localhost:6379'});

client.on('error', err => {
  console.log('Redis client not connected to the server: ' + err);
});

client.on_connect(console.log('Redis client connected to the server'));

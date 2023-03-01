import {createQueue} from 'kue';

const queue = createQueue();

function sendNotification(phoneNumber, message) {
    process.stdout.write(`Sending notification to ${phoneNumber}, with message: ${message}\n`);
};

queue.process("push_notification_code", (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});

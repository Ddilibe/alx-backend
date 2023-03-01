import {createQueue} from 'kue';

const queue = createQueue();

const notification = {
  phoneNumber: "4153518780",
  message: "This is the code to verify your account",
}

const job = queue.create(
    "push_notification_code",
    notification
).save((err) => {
    if (!err) {
        process.stdout.write(`Notification job created: ${job.id}\n`);
    }
});

job.on('complete', () => {
    process.stdout.write("Notification job complete\n");
});
job.on('failed', () => {
    process.stdout.write("Notification job failed\n");
});

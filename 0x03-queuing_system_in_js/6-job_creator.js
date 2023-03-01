import {createQueue} from 'kue';

const queue = createQueue();

const notification = {
  phoneNumber: "123456789",
  message: "Learn to take care of your confessions",
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

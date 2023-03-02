import {createQueue} from 'kue';

const queue = createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

for (var i = 0; i < jobs.length; i++) {
  const job = queue.create(
    "push_notification_code_2",
    jobs[i]
  ).save((err) => {
    if (!err) {
      process.stdout.write(`Notification job created: ${job.id}\n`);
    }
  });
  job.on('complete', () => {
      process.stdout.write(`Notification job ${job.id} completed\n`);
  });
  job.on('failed', (err) => {
      process.stdout.write(`Notification job ${job.id} failed: ${err}\n`);
  });
  job.on('progress', (progress, data) => {
    process.stdout.write(`Notification job ${job.id} ${progress}% complete\n`)
  });
}


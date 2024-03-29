// Creates a queue with Kue, creates a job object
const kue = require('kue');
const queue = kue.createQueue();

const job = queue
	.create('push_notification_code', {
		phoneNumber: '4153518780',
		message: 'This is the code to verify your account',
	}).save();

job
	.on('enqueue', () => {
		console.log(`Notification job created: ${job.id}`);
	})
	.on('complete', () => {
		console.log('Notification job completed');
	})
	.on('failed', () => {
		console.log('Notification job failed');
	})
  
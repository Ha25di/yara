require('dotenv').config();
const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors({ origin: '*' })); // Configure as needed for your environment
// app.use(bodyParser.json());
app.use(express.json());
// Define the transporter using the environment variables
const transporter = nodemailer.createTransport({
  service: 'hotmail',
  auth: {
    user: process.env.HOTMAIL_USERNAME,
    pass: process.env.HOTMAIL_PASSWORD,
  },
});

//Define the POST route for sending emails
app.post('/send', async (req, res) => {
  try {
    console.log('Attempting to send email with data:', req.body);
    const { email, subject, message } = req.body;

    let info = await transporter.sendMail({
      from: process.env.HOTMAIL_USERNAME, // The email account you're using to send the email
      replyTo: email, // User's email who filled out the form
      to: process.env.HOTMAIL_USERNAME, // YOUR email where you want to receive messages
      subject: subject,
      text: message,
      html: `<p>Message from: <b>${email}</b></p><p>${message}</p>`, // Including user's email in the body
    
    });
    
    console.log('Message sent: %s', info.messageId);
    res.status(200).send({ message: 'Email sent: ' + info.response });
  } catch (error) {
    console.error('Error sending email: ', error);
    res.status(500).send({ message: 'Error sending email: ' + error.message });
  }
});

// Start the server and listen on port 3001
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Add a root route for simple server check
app.get('/', (req, res) => {
  res.send('Server is running');
});





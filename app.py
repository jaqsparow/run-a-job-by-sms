from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def command():
    number = request.form['From']
    message_body = request.form['Body']
    action = message_body.split()[0]

    response = 'command ' + action + ' executed'

   if action.lower()== 'job1':
        command = "/usr/bin/python3 ~/scripts/job1.py"
        os.popen(command)

   elif action.lower()== 'job2':
        command = "/usr/bin/python3 ~/scripts/job2.py"
        os.popen(command)
   else:
        response = "Invalid request

    resp = MessagingResponse()
    resp.message(response)
    return str(resp)

if __name__ == '__main__':
    app.run()

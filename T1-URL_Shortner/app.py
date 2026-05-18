# URL Shortener - Main Server File
# A complete, runnable URL shortener using Flask and SQLite

from flask import Flask, request, jsonify, redirect, render_template
import sqlite3
import random
import string

# Create the Flask application
app = Flask(__name__)

# ==================== DATABASE SETUP ====================

def setup_database():
    """Create the database and table if they don't exist"""
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    
    # Create table with short_code as primary key and long_url column
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (short_code TEXT PRIMARY KEY, 
                  long_url TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    conn.commit()
    conn.close()
    print("✅ Database ready!")

# Call this once when the program starts
setup_database()

# ==================== HELPER FUNCTIONS ====================

def generate_short_code(length=6):
    """Generate a random short code like 'Xk9mQp'"""
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code

def is_code_unique(short_code):
    """Check if a short code is already used"""
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT short_code FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()
    conn.close()
    return result is None  # True if unique, False if already exists

def get_unique_short_code():
    """Keep generating codes until we find a unique one"""
    while True:
        code = generate_short_code()
        if is_code_unique(code):
            return code

# ==================== API ENDPOINTS ====================

@app.route('/')
def home():
    """Show the main web page"""
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """
    Receive a long URL and return a short code
    Expected JSON: {"long_url": "https://example.com/very/long/url"}
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        long_url = data.get('long_url')
        
        # Validate that URL was provided
        if not long_url:
            return jsonify({"error": "No URL provided. Please send {'long_url': 'your-url'}"}), 400
        
        # Add http:// if the URL doesn't have a protocol
        if not long_url.startswith(('http://', 'https://')):
            long_url = 'https://' + long_url
        
        # Generate a unique short code
        short_code = get_unique_short_code()
        
        # Save to database
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        c.execute("INSERT INTO urls (short_code, long_url) VALUES (?, ?)", 
                  (short_code, long_url))
        conn.commit()
        conn.close()
        
        # Return the result
        short_url = f"http://127.0.0.1:8548/{short_code}"
        
        return jsonify({
            "success": True,
            "short_code": short_code,
            "short_url": short_url,
            "long_url": long_url
        })
        
    except Exception as e:
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500

@app.route('/<short_code>')
def redirect_to_long(short_code):
    """
    When someone visits a short link like /abc123,
    look up the original URL and redirect them
    """
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    result = c.fetchone()
    conn.close()
    
    if result:
        long_url = result[0]
        print(f"✅ Redirecting {short_code} → {long_url}")  # This shows in terminal
        return redirect(long_url)
    else:
        # Show a friendly error page
        return f"""
        <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>🔗 Link Not Found</h1>
            <p>The short code '{short_code}' doesn't exist in our system.</p>
            <a href="/">Go back to homepage</a>
        </body>
        </html>
        """, 404

# ==================== EXTRA: VIEW ALL LINKS (for debugging) ====================

@app.route('/admin/links')
def view_all_links():
    """See all shortened links (handy for testing)"""
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT short_code, long_url, created_at FROM urls ORDER BY created_at DESC")
    all_links = c.fetchall()
    conn.close()
    
    if not all_links:
        return "<h3>No links yet! Create your first one using the homepage.</h3>"
    
    html = "<h1>📊 All Shortened Links</h1><ul>"
    for link in all_links:
        html += f"<li><b>{link[0]}</b> → {link[1]} <i>(created: {link[2]})</i></li>"
    html += "</ul><a href='/'>Back to homepage</a>"
    return html

# ==================== RUN THE SERVER ====================

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 URL Shortener is starting...")
    print("📱 Open your browser and go to: http://127.0.0.1:8548")
    print("🔧 Press Ctrl+C to stop the server")
    print("=" * 50)
    app.run(debug=True, host='127.0.0.1', port=8548)
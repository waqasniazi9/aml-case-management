# 🌐 Deploy AML System Online - Complete Guide

## **OPTION 1: Instant Public Access with ngrok (2 minutes)**

Perfect for quick testing and demos.

### Steps

```powershell
# Install ngrok (one-time)
choco install ngrok

# Make sure server is running on localhost:5000
python start_server.py

# In another terminal, expose to internet
ngrok http 5000
```

**Result:** You get a public URL like `https://abc123.ngrok.io`

- Share this URL with anyone
- They can access your system from anywhere
- Valid for 2 hours (free tier)

---

## **OPTION 2: PythonAnywhere Free Hosting (10 minutes) ⭐ RECOMMENDED**

Best for permanent free hosting without credit card.

### Steps

1. **Sign up** at <https://www.pythonanywhere.com/> (free account)

2. **Upload your files:**
   - Go to Files → Upload a file
   - Upload these files:
     - `aml_system.py`
     - `dashboard_enhanced.html`
     - `aml_multi_user.db`
     - `requirements.txt`
     - `config.py`

3. **Create a Flask web app:**
   - Go to Web → Add a new web app
   - Choose "Flask"
   - Choose Python 3.10
   - Set source code to your uploaded directory

4. **Edit WSGI config:**
   - Go to Web → Edit WSGI configuration file
   - Replace with this:

```python
import sys
import os

path = '/home/yourusername/mysite'  # Update with your path
if path not in sys.path:
    sys.path.append(path)

from aml_system import create_app
application = create_app()
```

1. **Reload your web app** and visit the URL

**Result:** Get URL like `yourusername.pythonanywhere.com`

---

## **OPTION 3: Railway.app (5 minutes)**

Simple one-click deployment.

### Steps

1. **Sign up** at <https://railway.app/>
2. **Connect GitHub** (or upload manually)
3. **Deploy** - It auto-deploys Flask apps
4. **Get URL** - Railway assigns a public domain

---

## **OPTION 4: Render.com (5 minutes)**

Free with easy setup.

### Steps

1. **Sign up** at <https://render.com/>
2. **New Web Service** → Select GitHub or upload files
3. **Configure:**
   - Build command: `pip install -r requirements.txt`
   - Start command: `python wsgi.py`
4. **Deploy** → Get public URL

---

## **OPTION 5: Heroku (Advanced)**

Requires credit card (free tier ended but still available with payment method).

```bash
# Install Heroku CLI
choco install heroku-cli

# Login
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main

# View
heroku open
```

---

## **Files Ready for Deployment** ✅

Your system is now configured for cloud deployment:

- ✅ `aml_system.py` - Main application
- ✅ `dashboard_enhanced.html` - UI with all features
- ✅ `aml_multi_user.db` - SQLite database (portable)
- ✅ `requirements.txt` - Dependencies
- ✅ `config.py` - Production config ⭐ NEW
- ✅ `wsgi.py` - WSGI entry point ⭐ NEW

---

## **Important: Before Deploying**

### Set Environment Variables

On your deployment platform, set these environment variables:

```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here-make-it-long-and-random
PORT=5000
HOST=0.0.0.0
DB_PATH=aml_multi_user.db
```

### Database Persistence

**SQLite won't work well** on platforms like Heroku (ephemeral filesystem).

For permanent hosting, consider:

- **Free option:** Use PythonAnywhere (persistent storage)
- **Better option:** Upgrade to PostgreSQL (most platforms offer free tier)

To use PostgreSQL, install:

```bash
pip install psycopg2-binary
```

---

## **Quick Commands Reference**

### **Test locally:**

```powershell
python wsgi.py
# Then visit http://127.0.0.1:5000
```

### **Production mode locally:**

```powershell
pip install waitress
$env:FLASK_ENV='production'
python wsgi.py
```

### **Check dependencies:**

```powershell
pip install -r requirements.txt
```

---

## **Security Checklist Before Going Live** ⚠️

- [ ] Change `SECRET_KEY` to a random string (40+ characters)
- [ ] Set strong password for admin account
- [ ] Enable HTTPS (all platforms do this automatically)
- [ ] Set `DEBUG = False` in production (done in config.py)
- [ ] Use environment variables for sensitive data
- [ ] Regular database backups
- [ ] Monitor for errors in platform logs

---

## **My Recommendation:**

**For immediate use:** Use **ngrok** (test with anyone in 2 minutes)

**For permanent hosting:** Use **PythonAnywhere** (free, no credit card, easiest setup)

**For scalability:** Use **Railway** or **Render** (can upgrade later)

---

## **Need Help?**

I can help you with:

1. Setting up ngrok for instant access
2. Deploying to any specific platform
3. Configuring environment variables
4. Migrating to PostgreSQL database
5. Setting up custom domain names

Just let me know which option you prefer!

# 🚀 PythonAnywhere Setup - Complete Step-by-Step Guide

## Your Account: waqasniazi9

---

## **STEP 1: Upload Your Files to PythonAnywhere**

1. Go to: <https://www.pythonanywhere.com/user/waqasniazi9/files/>
2. Click **"Upload a file"** (or drag & drop)
3. **Upload these 6 files** from your computer:
   - `aml_system.py` ⭐
   - `dashboard_enhanced.html` ⭐
   - `aml_multi_user.db` ⭐
   - `requirements.txt`
   - `config.py`
   - `wsgi.py`

**Expected folder after upload:** `/home/waqasniazi9/`

---

## **STEP 2: Create New Web App**

1. Go to: <https://www.pythonanywhere.com/user/waqasniazi9/webapps/>
2. Click **"Add a new web app"** (+ icon)
3. Choose **"Flask"**
4. Choose **"Python 3.10"** (or latest)
5. Choose **"Manual configuration"** (NOT bottle or Django)
6. Click **"Next"**

---

## **STEP 3: Configure WSGI File (IMPORTANT!)**

1. Go to: <https://www.pythonanywhere.com/user/waqasniazi9/webapps/>
2. Find your web app → Click it
3. Scroll down to **"Code"** section
4. Click **"WSGI configuration file"** to edit it
5. **Replace ALL content** with this code:

```python
# ============================================
# PythonAnywhere WSGI Configuration
# AML Case Management System
# ============================================

import sys
import os

# Add your home directory to the path
path = '/home/waqasniazi9'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variables
os.environ['FLASK_ENV'] = 'production'
os.environ['DB_PATH'] = '/home/waqasniazi9/aml_multi_user.db'

# Import and create the Flask app
from aml_system import create_app

application = create_app()
```

1. Click **"Save"**

---

## **STEP 4: Configure Virtual Environment**

1. Go to: <https://www.pythonanywhere.com/user/waqasniazi9/webapps/>
2. Find your web app → Click it
3. Scroll to **"Virtualenv"** section
4. Click **"Create a new virtual environment"**
5. Choose **"Python 3.10"**
6. **Wait for it to complete** (takes 1-2 minutes)

---

## **STEP 5: Install Python Dependencies**

1. Open **Bash console**: <https://www.pythonanywhere.com/user/waqasniazi9/bash/>
2. Paste this command:

```bash
cd /home/waqasniazi9
/home/waqasniazi9/.virtualenvs/*/bin/pip install --upgrade pip
/home/waqasniazi9/.virtualenvs/*/bin/pip install -r requirements.txt
```

1. Press **Enter**
2. **Wait for installation** (takes 2-3 minutes)
3. You should see: **"Successfully installed ..."**

---

## **STEP 6: Reload Web App**

1. Go to: <https://www.pythonanywhere.com/user/waqasniazi9/webapps/>
2. Find your web app
3. Click **"Reload"** button (green button on right)
4. **Wait 10 seconds** for reload to complete

---

## **STEP 7: Test Your App**

1. Go to: <https://www.pythonanywhere.com/user/waqasniazi9/webapps/>
2. Find your web app
3. Click the **URL** at the top (looks like `waqasniazi9.pythonanywhere.com`)
4. You should see the **Login Page** ✅

**If you see errors:**

- Click **"Error logs"** tab to see what went wrong
- Take a screenshot and send me the error

---

## **STEP 8: Login and Test**

Your account is already set up! Login with:

- **Username:** `admin`
- **Password:** `admin123`

---

## **Troubleshooting**

### **"No module named 'aml_system'"**

→ Make sure all `.py` files are in `/home/waqasniazi9/` (not in a subfolder)

### **"No such file: aml_multi_user.db"**

→ Upload the database file to the same folder

### **"Import error"**

→ Go to Bash console and run:

```bash
/home/waqasniazi9/.virtualenvs/*/bin/pip install -r requirements.txt
```

### **Still not working?**

→ Click **"Error logs"** and copy the error message for me

---

## **Your Public URL**

Once working, your app will be at:

**<https://waqasniazi9.pythonanywhere.com>**

Share this URL with anyone and they can use your AML system!

---

## **Quick Reference**

| Step | Action | Link |
|------|--------|------|
| 1 | Upload files | <https://www.pythonanywhere.com/user/waqasniazi9/files/> |
| 2 | Create web app | <https://www.pythonanywhere.com/user/waqasniazi9/webapps/> |
| 3 | Edit WSGI | Edit in web app settings |
| 4 | Virtual env | Create in web app settings |
| 5 | Install packages | Bash console |
| 6 | Reload | Web app settings |
| 7 | Test | Visit your URL |

---

## **Still Need Help?**

If you get stuck on any step, tell me which step number and the error message!

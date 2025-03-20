## Deployment Steps

To deploy your Django project on **Vercel**, follow these steps:  

---

## ✅ **Prerequisites**  
Ensure you have the following:  
- Vercel account ([Sign up here](https://vercel.com/signup) if not already registered)  
- Vercel CLI installed (`npm install -g vercel`)  
- Python 3.8 or higher installed  
- Project up and running locally  

---

## 🛠 **Step 1: Install Required Packages**  

Install **gunicorn** and **whitenoise** for production:  
```bash
pip install gunicorn whitenoise
```

---

## ⚙️ **Step 2: Configure Project for Vercel**  

1. **Create a `vercel.json` file** in your root directory:  
```json
{
  "version": 2,
  "builds": [
    {
      "src": "support_system/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "support_system/wsgi.py"
    }
  ]
}
```

2. **Add a Vercel Entry Point**  
Ensure `support_system/wsgi.py` is correctly set up to run your app.

---

## 📦 **Step 3: Configure Static Files**  

1. In `settings.py`:  
    - Add `whitenoise.middleware.WhiteNoiseMiddleware` to `MIDDLEWARE` after `SecurityMiddleware`.  
    - Configure static files:  
      ```python
      STATIC_URL = '/static/'
      STATIC_ROOT = BASE_DIR / 'staticfiles'
      ```
2. Run the command to collect static files:  
    ```bash
    python manage.py collectstatic
    ```

---

## 🔐 **Step 4: Set Environment Variables**  

On Vercel, set environment variables like your Gmail credentials securely:  
- Go to your Vercel dashboard.  
- Select the project → **Settings** → **Environment Variables**.  
- Add your `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, and other necessary variables.  

---

## 🚀 **Step 5: Deploy to Vercel**  

1. Login to Vercel using:  
    ```bash
    vercel login
    ```
2. Deploy the project:  
    ```bash
    vercel
    ```
3. Follow the prompts to select your project and confirm deployment.

---

## 🧪 **Step 6: Test the Deployment**  

- After deployment is complete, Vercel will provide a live URL.  
- Access it using the URL (e.g., `https://your-project-name.vercel.app/submit`).  
- Submit a ticket to ensure everything works as expected.  

---

## 🚦 **Troubleshooting Tips**  
- Ensure all necessary environment variables are set on Vercel.  
- Check logs using:  
  ```bash
  vercel logs your-project-name
  ```
- If static files are not loading, verify the `collectstatic` command was run successfully.  

---

That’s it! Your Django customer support system should now be live on Vercel. 😊
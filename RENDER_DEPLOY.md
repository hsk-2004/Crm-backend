# Deploying Django + PostgreSQL to Render 🚀

Your Django backend is now configured for deployment on Render with PostgreSQL.

## 1. Prerequisites (Done ✅)
The project structure is updated:
- `requirements.txt` includes `gunicorn`, `psycopg2-binary`, `dj-database-url`, `whitenoise`
- `Procfile` is created (tells Render how to run the app)
- `render-build.sh` handles setup & migrations
- `settings.py` is configured for database URL + static files
- `.env.example` shows required environment variables

---

## 2. Push to GitHub
Make sure your latest code (including the new files) is pushed to GitHub:

```bash
git add .
git commit -m "Configure for Render deployment"
git push origin main
```

---

## 3. Create Render Service
1.  Go to [Render Dashboard](https://dashboard.render.com).
2.  Click **New +** -> **Web Service**.
3.  Connect your GitHub repository.
4.  Configure the service:
    *   **Name**: `crm-backend` (or similar)
    *   **Runtime**: `Python 3`
    *   **Build Command**: `./render-build.sh`
    *   **Start Command**: `gunicorn crm.wsgi:application`

---

## 4. Add Environment Variables
In the Render dashboard for your service, go to **Environment** and add the following keys using the values from `.env.example` as a guide, but change them for production:

| Key | Value |
|---|---|
| `PYTHON_VERSION` | `3.10.12` (or your Python version) |
| `SECRET_KEY` | (Generate a strong random key) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*` (or your specific render domain) |

---

## 5. Add PostgreSQL Database
1.  Click **New +** -> **PostgreSQL**.
2.  **Name**: `crm-db`
3.  **Region**: Same as your Web Service.
4.  Click **Create Database**.
5.  Copy the **Internal Database URL**.
6.  Go back to your Web Service -> **Environment**.
7.  Add a new variable: `DATABASE_URL` with the value you just copied.

---

## 6. Deploy & Finish
Render will automatically start building.
- Check the **Logs** tab.
- Once it says "Your service is live", open the URL.
- Test your API endpoints!

---

## Troubleshooting
- **Build fails?** Check `requirements.txt` versions.
- **502 Bad Gateway?** Check logs; ensure Gunicorn is starting.
- **Database error?** Verify `DATABASE_URL` is correct.

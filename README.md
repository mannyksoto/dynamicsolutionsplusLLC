# Dynamic Solutions Plus LLC — Website

Landscaping & irrigation company site built with Streamlit.

## Structure
```
app.py                 # entry point + top navigation
site_config.py         # ALL business text (phone, services, about) — edit here
ui.py                  # shared CSS, footer, call-to-action
pages/                 # home, services, gallery, about, contact
assets/gallery/        # drop job photos here (file name = caption)
.streamlit/config.toml # theme colors
```

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Push to GitHub
```bash
git init
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/<you>/dynamic-solutions-site.git
git push -u origin main
```

## Deploy (Streamlit Community Cloud)
1. share.streamlit.io → **Create app** → pick the repo, branch `main`, file `app.py`.
2. Set a custom subdomain, e.g. `dynamicsolutionsplus.streamlit.app`.
3. App settings → **Secrets** → paste contents of `secrets.toml.example` with real values
   so the estimate form emails the owner.

Every `git push` to `main` redeploys automatically.

## Before launch checklist
- [ ] Replace every `[BRACKETED]` placeholder in `site_config.py`
- [ ] Add logo + job photos
- [ ] Configure email secrets and send a test estimate
- [ ] Decide on custom domain approach (see notes)

## Keep the app awake
Free Community Cloud apps sleep after inactivity. `.github/workflows/keepalive.yml`
opens the site in a headless browser every 6 hours and clicks "wake up" if needed.

1. Repo → Settings → Secrets and variables → Actions → **Variables** tab →
   New variable `APP_URL` = `https://<your-subdomain>.streamlit.app`
2. Actions tab → "Keep Streamlit app awake" → **Run workflow** to test.

Note: GitHub pauses scheduled workflows after 60 days with no repo activity —
re-enable it from the Actions tab if that happens.

Run it from a Raspberry Pi instead (cron, every 6 h):
```
pip install playwright && playwright install --with-deps chromium
crontab -e
17 */6 * * * /usr/bin/python3 /home/pi/dynamic-solutions-site/scripts/keepalive.py https://<your-subdomain>.streamlit.app >> /home/pi/keepalive.log 2>&1
```

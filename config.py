# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "jcorio@gmail.com"  # Your Gmail address (e.g., "your.email@gmail.com")
SENDER_PASSWORD = "ckkuildgeysvmbsf"  # Your 16-character App Password from Google (no spaces)
RECIPIENT_EMAIL = "orders@turano.com"
ORDER_SUBJECT = "5389510"

# Order Items
ORDER_ITEMS = {
    "Burger Bun pack 13241": "",
    "Focaccia pack 16201": "",
    "Panini Sourdough 32162": "",
    "Kid Burger 19128": ""
}

# Instructions for Gmail setup:
# 1. Enable 2-Step Verification in your Google Account
# 2. Generate an App Password:
#    - Go to Google Account > Security > App passwords
#    - Select "Mail" and "Windows Computer"
#    - Copy the 16-character password
# 3. Paste your Gmail address in SENDER_EMAIL
# 4. Paste the App Password in SENDER_PASSWORD 
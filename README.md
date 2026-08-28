# MSP Outreach Automator

A simple Python script built to automate job outreach to local IT companies and MSPs without doing the repetitive manual work every morning.

---

## Why I Built This
Applying on massive job portals often feels like sending resumes into a void. Directly emailing hiring managers at local IT companies gets much better results, but manually typing out emails, attaching specific CV variants, and hitting send one-by-one gets tedious fast. 

I built this tool to automate the boring parts: it pulls recipient details from a simple spreadsheet, pairs the company with the right resume version (e.g., **IT Support** vs. **Networking**), and safely sends everything through Gmail.

---

## What It Does
* **CSV-Driven Campaigns:** Load all target contacts, email addresses, and personalized message templates into a single `targets.csv` file.
* **Smart Resume Matching:** Automatically attaches the correct PDF resume based on the role type you specify.
* **Safety Dry-Run Mode:** Includes a `DRY_RUN = True` toggle so you can preview everything in the terminal before firing off real emails.
* **Secure Auth:** Uses `.env` environment variables and Google App Passwords to keep credentials 100% hidden from GitHub.

---

## Tech & Requirements
* **Language:** Python 3.10+
* **Standard Libraries:** `smtplib`, `email.message`, `csv`, `ssl`, `pathlib`
* **External Library:** `python-dotenv`

---

## How to Run It

### 1. Clone the Repo
```bash
git clone [https://github.com/Ctrl-Yam/msp-outreach-automator.git](https://github.com/Ctrl-Yam/msp-outreach-automator.git)
cd msp-outreach-automator
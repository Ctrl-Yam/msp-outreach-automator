Copy and paste this markdown directly into your `README.md` file:

```markdown
# Dynamic Role-Based Email Automation Engine (CLI V1.0)

A high-performance, memory-optimized Python CLI tool designed for automated, role-targeted email outreach via Gmail SMTP. 

Unlike standard mail-merge software, this engine pre-loads all binary attachments and message templates into RAM before executing, eliminating disk I/O bottlenecks during sending. It features dynamic template parsing, custom PDF routing based on recipient classification, and randomized dispatch pacing to protect domain reputation.

---

## Key Features

* **RAM-Buffered File Operations:** Reads all `.txt` templates and `.pdf` attachments into memory up-front for maximum execution speed.
* **Dynamic Template & Attachment Routing:** Reads recipient metadata from a CSV and automatically pairs target roles (`N` vs `S`) with custom subjects, bodies, and matching attachments.
* **Header Line Subject Extraction:** Automatically parses Line 1 of template files as the email subject line while dynamically formatting the remaining text as the body.
* **Anti-Spam Delay Pacing:** Implements a randomized delay (5–10 seconds) between outgoing dispatches to simulate human typing/sending patterns and reduce spam triggers.
* **Deterministic Fallback:** Defaults unclassified or malformed recipient data to standard fallback configurations to prevent mid-batch execution crashes.

---

## Prerequisites

* **Python 3.8+** installed on your system.
* A **Gmail Account** with **2-Step Verification** enabled.
* A Gmail **App Password** (standard Gmail account passwords will not work with SMTP).

---

## Installation & Environment Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name

```

2. **Install required dependencies:**
This project relies on `python-dotenv` to securely manage credentials:
```bash
pip install python-dotenv

```


3. **Configure Environment Variables:**
Duplicate `.env.example` and rename it to `.env`:
```bash
cp .env.example .env

```


Open `.env` and insert your Gmail address and 16-character App Password:
```env
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_16_character_app_password

```



---

## File & Folder Configuration

To run the script successfully, you must populate the root directory with your own target data, templates, and resume attachments.

### 1. Resumes / PDF Attachments - REQUIRED

Place your PDF files in the root folder. By default, the script looks for two specific filenames:

* `N_resume.pdf` (Attachment for Category N targets)
* `S_resume.pdf` (Attachment for Category S targets)

> **Note:** If your PDF files have different names (e.g., `John_Doe_CV.pdf`), you can either rename your PDF files to match `N_resume.pdf` / `S_resume.pdf`, or open `main.py` and update lines 29 & 33 to point to your exact file names:
> ```python
> with open("YOUR_FILENAME_HERE.pdf", "rb") as f:
> 
> ```
> 
> 

### 2. Message Templates (`N_message.txt` & `S_message.txt`)

Create text files for each recipient category following this exact structural format:

* **Line 1:** Email Subject Line
* **Line 2:** Empty Line (used as a spacer)
* **Line 3+:** Email Body Text

**Example `N_message.txt`:**

```text
Application for Network Administration Role

Hi 
Please find attached my resume for the Network Administrator position...

```

### 3. Target Recipients (`targets.csv`)

Create or update `targets.csv` (you can copy `targets.example.csv`). The engine parses rows assuming the following column indexes:

* `Column 1` (Index 1): Recipient Email Address
* `Column 3` (Index 3): Recipient Name
* `Column 4` (Index 4): Position Type Indicator (`N` or `S`)

---

## Usage

Once all configuration steps, templates, CSV rows, and PDF attachments are set up in the project root, launch the engine:

```bash
python main.py

```

The script will log progress directly to the console, showing outgoing email delivery and randomized delay intervals between messages.

---

## Roadmap (V2.0)

This V1 release represents the core CLI automation backend. Planned updates for V2.0 include:

* [ ] **PyQt Desktop Interface:** A full GUI wrapper built around `QThread` for non-technical users.
* [ ] **Terminal Dashboard:** Interactive progress bars using `rich`.
* [ ] **Dynamic CSV Mapping:** Configurable GUI dropdowns to map custom CSV column headers.

---

## Contributing

Contributions are welcome! If you want to assist with building the PyQt GUI or expanding CLI features:

1. Fork the project repository.
2. Create a feature branch (`git checkout -b feature/gui-layout`).
3. Commit your changes and open a Pull Request against `main`.

```

```
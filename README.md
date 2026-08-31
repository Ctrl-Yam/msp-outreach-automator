# msp-outreach-automator (v2.0-dev)

A high-performance Python application and custom UI designed for role-targeted email outreach via Gmail SMTP. 

Originally built as a memory-optimized CLI engine, **`msp-outreach-automator`** pre-loads binary attachments and message templates into RAM to eliminate disk I/O bottlenecks during sending. Version 2 updates the platform with a modern dark-mode GUI, non-blocking multithreaded dispatch, and real-time console logging.

---

##  Author

**Yamkelo Vilakazi**
* GitHub: [@Ctrl-Yam](https://github.com/Ctrl-Yam)
* Portfolio: [ctrl-yam.github.io](https://ctrl-yam.github.io)

---

## Key Features

* **CustomTkinter Dark Mode UI:** Modern desktop interface with dynamic file configuration and campaign controls.
* **RAM-Buffered Execution:** Reads all `.txt` templates and `.pdf` attachments into memory up-front for maximum execution speed.
* **Dynamic Template & Attachment Routing:** Reads recipient metadata from CSVs to automatically pair target categories (`N` vs `S`) with matching subjects, bodies, and resume attachments.
* **Header Line Subject Parsing:** Automatically treats Line 1 of template text files as the subject line and formats the remaining lines into the email body.
* **Anti-Spam Delay Pacing:** Implements randomized delays (5–10 seconds) between outgoing dispatches to simulate human typing patterns and protect domain reputation.
* **Multithreaded Execution Engine:** Runs outreach dispatches on background threads to keep the user interface responsive during batch sends.

---

## Prerequisites

* **Python 3.8+** installed on your system.
* A **Gmail Account** with **2-Step Verification** enabled.
* A Gmail **App Password** (standard Gmail passwords will not work with SMTP).

---

## Quick Start & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ctrl-Yam/msp-outreach-automator.git](https://github.com/Ctrl-Yam/msp-outreach-automator.git)
   cd msp-outreach-automator
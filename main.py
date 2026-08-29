import argparse
import csv
import os
import random
import smtplib
import time
from email.message import EmailMessage

from dotenv import load_dotenv
from rich.console import Console
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.table import Table

load_dotenv()

emailAddress = os.environ.get("GMAIL_USER")
emailPass = os.environ.get("GMAIL_PASSWORD")

N_message_file_path = "N_message.txt"
S_message_file_path = "S_message.txt"
recipients_file_path = "targets.csv"

console = Console()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Role-based email outreach via Gmail SMTP."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip SMTP login and sending; still show progress, delays, and summary.",
    )
    return parser.parse_args()


def wait_with_countdown(progress, delay_task, seconds):
    progress.update(
        delay_task,
        visible=True,
        completed=0,
        total=seconds,
        description=f"Waiting {seconds}s",
    )
    for remaining in range(seconds, 0, -1):
        progress.update(delay_task, description=f"Waiting {remaining}s")
        time.sleep(1)
        progress.advance(delay_task)
    progress.update(delay_task, visible=False)


def print_summary(total, sent, failed):
    table = Table(title="Outreach Summary")
    table.add_column("Metric", style="bold")
    table.add_column("Count", justify="right")
    table.add_row("Total", str(total))
    table.add_row("Sent", str(sent), style="green")
    table.add_row("Failed", str(failed), style="red" if failed else None)
    console.print()
    console.print(table)


def main():
    args = parse_args()

    try:
        with open(N_message_file_path, "r") as N_message:
            N_text = N_message.readlines()

        with open(S_message_file_path, "r") as S_message:
            S_text = S_message.readlines()

        with open(recipients_file_path, "r") as file:
            content = csv.reader(file)
            rows = list(content)

        with open("N_resume.pdf", "rb") as f:
            N_resume_data = f.read()
            N_resume_name = f.name

        with open("S_resume.pdf", "rb") as f:
            S_resume_data = f.read()
            S_resume_name = f.name

        targets = rows[1:]
        total = len(targets)
        sent = 0
        failed = 0

        if args.dry_run:
            console.print("[yellow]Dry-run mode — no emails will be sent.[/]")
            smtp = None
        else:
            smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            smtp.login(emailAddress, emailPass)

        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                MofNCompleteColumn(),
                TimeElapsedColumn(),
                console=console,
            ) as progress:
                send_task = progress.add_task("Sending emails", total=total)
                delay_task = progress.add_task("Waiting", total=1, visible=False)

                for index, row in enumerate(targets):
                    try:
                        recipient_name = row[3]
                        recipient_email = row[1]
                        position_type = row[4].strip().upper()

                        if position_type == "S":
                            subject = S_text[0].strip()
                            text = "".join(S_text[2:])
                            resume_data = S_resume_data
                            resume_name = S_resume_name
                        else:
                            subject = N_text[0].strip()
                            text = "".join(N_text[2:])
                            resume_data = N_resume_data
                            resume_name = N_resume_name

                        msg = EmailMessage()
                        msg["Subject"] = subject
                        msg["From"] = emailAddress
                        msg["To"] = recipient_email
                        msg.set_content(f"Hi {recipient_name}\n{text}")
                        msg.add_attachment(
                            resume_data,
                            maintype="application",
                            subtype="pdf",
                            filename=resume_name,
                        )

                        if smtp is not None:
                            smtp.send_message(msg)

                        sent += 1
                        label = "Dry-run" if args.dry_run else "Sent"
                        color = "yellow" if args.dry_run else "green"
                        progress.console.print(
                            f"[{color}]{label}[/] to {recipient_name} <{recipient_email}>"
                        )
                    except Exception as exc:
                        failed += 1
                        name = row[3] if len(row) > 3 else f"row {index + 2}"
                        progress.console.print(f"[red]Failed[/] {name}: {exc}")

                    progress.advance(send_task)

                    if index < total - 1:
                        delay_time = int(random.uniform(5, 10))
                        wait_with_countdown(progress, delay_task, delay_time)
        finally:
            if smtp is not None:
                smtp.quit()

        print_summary(total, sent, failed)

    except FileNotFoundError:
        console.print("[red]The file was not found![/]")


if __name__ == "__main__":
    main()

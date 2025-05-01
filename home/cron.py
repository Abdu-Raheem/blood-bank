from django.core.management import call_command
from django.core.management.base import CommandError

def perform_database_backup():
    try:
        call_command('dbbackup')
        print("Database backup completed successfully.")
    except CommandError as e:
        print(f"Error during database backup: {e}")

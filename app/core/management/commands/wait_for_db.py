"""
Django command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Django command to wait for database.
    """

    def handle(self, *args, **options) -> None:
        self.stdout.write("Waiting for database...")

        database_up: bool = False
        while database_up is False:
            try:
                self.check(databases=["default"])
                database_up = True
            except (Psycopg2OperationalError, OperationalError):
                self.stdout.write(
                    "Database is unavailable, waiting 1 seccond..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available."))

from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model
from decimal import Decimal

User = get_user_model()

class Command(BaseCommand):
    help = "Populates the database with sample listings"

    def handle(self, *args, **options):
        try:
            # Grab an existing user to be host (make sure at least one exists)
            host = User.objects.first()
            if not host:
                self.stdout.write(self.style.WARNING("No users found. Create a user first."))
                return

            # Sample listings data
            sample_listings = [
                Listing(
                    host=host,
                    title="Cozy Apartment in Downtown",
                    description="A comfortable apartment close to everything.",
                    location="New York",
                    price_per_night=Decimal("120.00")
                ),
                Listing(
                    host=host,
                    title="Beach House",
                    description="Relaxing house near the beach.",
                    location="Miami",
                    price_per_night=Decimal("250.00")
                ),
                Listing(
                    host=host,
                    title="Mountain Cabin",
                    description="Secluded cabin in the mountains.",
                    location="Denver",
                    price_per_night=Decimal("180.00")
                ),
            ]

            # Bulk create listings
            Listing.objects.bulk_create(sample_listings)

            self.stdout.write(self.style.SUCCESS("Listing table successfully populated!"))

        except Exception as e:
            self.stderr.write(f"Listing population error: {e}")

        

        

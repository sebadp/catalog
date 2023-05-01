import os

from botocore.exceptions import ClientError
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product
from django.core.mail import send_mail

User = get_user_model()


@receiver(post_save, sender=Product)
def product_change_notification(sender, instance, **kwargs):
    """
    Send a notification to all other admins when a product is changed.
    """

    # Construct the email message
    message = f"Product {instance.name} has been updated."
    subject = f"Product update: {instance.name}"
    # Get the email addresses of all admin users
    admin_emails = User.objects.filter(is_superuser=True).values_list('email', flat=True)
    to_addresses = list(admin_emails)
    # Try to send the email up to 3 times if it fails
    for i in range(3):
        try:
            # Send the email
            send_mail(
                subject,
                message,
                os.environ.get('EMAIL_USER'),
                admin_emails,
                fail_silently=False)

            # If the email was sent successfully, exit the loop
            break

        except ClientError as e:
            # If the email failed to send, retry up to 3 times
            if i < 2 and e.response['Error']['Code'] in ['Throttling', 'Timeout']:
                continue

            # Otherwise, log the error and exit the loop
            else:
                print(f"Failed to send email: {e}")
                break

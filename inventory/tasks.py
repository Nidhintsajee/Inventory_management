from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import ItemStock

@shared_task
def send_low_stock_alerts():
    low_stock_items = ItemStock.objects.filter(stock_in_hand__lte=5) 

    for item_stock in low_stock_items:
        subject = f"Low Stock Alert for {item_stock.item.name}"
        message = f"The stock for item {item_stock.item.name} is low (Stock in Hand: {item_stock.stock_in_hand}). Please replenish the stock."
        recipient_list = ['admin@example.com'] 

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )

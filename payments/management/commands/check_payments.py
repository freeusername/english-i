import datetime
from django.core.management.base import NoArgsCommand
from payments.models import PaymentOrder, Payment, BACKEND_ADMIN
from liqpay.integration import LiqPayIntegration
from accounts.models import User
from django.db.models import Q
from django.utils import timezone

class Command(NoArgsCommand):
    """
    Check is_premium flags for users

    Usage::

        $ python manage.py check_payments
        Check is_premium flags for users

    """
    help = "Check is_premium flags for users"

    def handle_noargs(self, **options):
        # payments = Payment.objects.all()
        # excluded = [int(p.order) for p in payments]
        curr_datetime = timezone.now()

        # delete unused orders
        workdate = curr_datetime - datetime.timedelta(hours=5)
        orders = PaymentOrder.objects.filter(created_at__lt=workdate).exclude(transaction_id__isnull=False).exclude(backend=BACKEND_ADMIN)
        orders.delete()

        # filter valid users
        lp = LiqPayIntegration()
        valid_statuses = lp.get_valid_statuses()
        valid_payments = Payment.objects.filter(status__in=valid_statuses)
        payments_ids = [p.pk for p in valid_payments]
        curr_date = curr_datetime.date()
        valid_users =  User.objects.filter(Q(payment_orders__date_begin__lte=curr_date), Q(payment_orders__date_end__gte=curr_date), Q(Q(payment_orders__transaction_id__in=payments_ids) | Q (payment_orders__backend=BACKEND_ADMIN)))

        # mark validity completed users
        excluded = []
        for u in valid_users:
            if u.pk in excluded:
                pass
            else:
                excluded.append(u.pk)

        User.objects.filter(is_premium=True).exclude(pk__in=excluded).update(is_premium=False)

        # mark valid users
        valid_users.filter(is_premium=False).update(is_premium=True)



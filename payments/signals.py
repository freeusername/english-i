
def update_order(transaction):
    import datetime
    import logging
    from payments.utils import get_order, order2json, FraudAttemptError
    from liqpay.integration import LiqPayIntegration
    logger = logging.getLogger('app')
    try:
        order, order_json = get_order(transaction.order_id)
    except FraudAttemptError as e:
        logger.error(u'update_order: Have error: %s' % e.message)
    if order:
        local_json = order2json(order)
        if local_json == order_json:
            if order.transaction_id == transaction.pk:
                pass
            else:
                order.transaction = transaction
                date_begin = order.created_at.date()
                date_end = datetime.date(date_begin.year+1, date_begin.month, date_begin.day)
                order.date_begin = date_begin
                order.date_end = date_end
                order.save()
            lp = LiqPayIntegration()
            valid_statuses = lp.get_valid_statuses()
            if transaction.status in valid_statuses:
                # enable PRO
                user = order.user
                user.is_premium = True
                user.save()
        else:
            logger.error("update_order: Order properties is not identical:")
            logger.error("update_order:   Local: %s" % local_json)
            logger.error("update_order:  Remote: %s" % order_json)
    return None


def liqpay_transaction_successfull(sender, type, response, **kwargs):
    from liqpay import get_liqpay_transaction_model
    TransactionModel = get_liqpay_transaction_model()
    transaction_id = response.get('local_trans_id', None)
    if transaction_id:
        transaction = TransactionModel.objects.get(pk=transaction_id)
        update_order(transaction)

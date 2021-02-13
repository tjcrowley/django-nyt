import logging
# removed group call and imported async-to-sync for message
from asgiref.sync import async_to_sync

from . import models, settings

logger = logging.getLogger(__name__)


def notify_subscribers(notifications, key):
    """
    Notify all open channels about new notifications
    """

    logger.debug("Broadcasting to subscribers")

    notification_type_ids = models.NotificationType.objects.values('key').filter(key=key)

    for notification_type in notification_type_ids:

    #
    # use async to sync to send message instead of deprecated group class.

        async_to_sync(settings.NOTIFICATION_CHANNEL.group_send)(notification_type['key'], {"text": "new-notification"})

   #     g = Group(
   #         settings.NOTIFICATION_CHANNEL.format(
   #             notification_key=notification_type['key']
   #         )
   #     )
   #     g.send(
   #         {'text': 'new-notification'}
   #     )

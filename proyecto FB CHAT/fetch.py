# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

client = Client("juancrlsmarcano@hotmail.com", "westinghouse12")

print("Own id: {}".format(client.uid))

client.send(Message(text="Hi me!"), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()
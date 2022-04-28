import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
  def connect(self):
    self.room_group_name = 'test'

    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name
    )

    self.accept()

    self.send(text_data = json.dumps({
      'type': 'connection_stablished',
      'message': 'you are now connected!',
    }))

  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message = text_data_json['message']
    username = text_data_json['username']

    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'chat_message', #defines the function that uses the message?
        'username': username,
        'message': message
      }
    )

  def chat_message(self, event):
    message = event['message']
    username = event['username']
    print("message: ", event)


    self.send(text_data=json.dumps({
      'type': 'chat',
      'username': username,
      'message': message
    }))


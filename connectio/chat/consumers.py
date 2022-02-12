import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Message, Group
from users.models import NewUser


class Consumer(AsyncConsumer):
    async def websocket_connect(self, event):
        self.room_name = self.scope['url_route']['kwargs']['chat']
        print(f'{self.room_name = }')
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        info = event.get('text', None)
        if info:
            data = json.loads(info)
            group = data['group']
            author = data['author']
            content = data['content']
            return_data = await self.save_message(group, author, content)
            await self.channel_layer.group_send(self.room_name, {
                'type': 'chat.message',
                'text': json.dumps(return_data),
            })

    async def chat_message(self, event):
        message = event['text']
        await self.send({
            'type': 'websocket.send',
            'text': message,
        })

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)
        await self.send({
            'type': 'websocket.close',
        })

    @database_sync_to_async
    def save_message(self, group, author, content):
        db_group = Group.objects.get(group_name=group)
        db_author = NewUser.objects.get(username=author)
        new_msg = Message.objects.create(group=db_group, author=db_author, msg_content=content)
        new_msg.save()
        return {
            'author': new_msg.author.username,
            'name': new_msg.author.profile.name,
            'content': new_msg.msg_content,
            'time': str(new_msg.time),
            'pk': new_msg.pk,
        }

import magic
import mimetypes

import json
from channels.generic.websocket import AsyncWebsocketConsumer

from django.conf import settings


class FileExtensionConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data=None, bytes_data=None):
        # Set a maximum allowed size for the file data (in bytes)
        max_allowed_size = settings.MAX_ALLOWED_SIZE * 1024 * 1024

        if len(bytes_data) > max_allowed_size:
            # If the file data exceeds the maximum allowed size, send a validation error message
            await self.send(
                text_data=json.dumps(
                    {"error": "File size exceeds the maximum allowed size."}
                )
            )
        else:
            # Get the file extension
            extension = self.get_file_extension(bytes_data)

            # Send extension back to the client
            await self.send(text_data=json.dumps({"extension": extension}))

    def get_file_extension(self, file_data):
        # Create a magic object
        magic_instance = magic.Magic(mime=True)

        # Get the MIME type of the file
        mime_type = magic_instance.from_buffer(file_data)

        return mimetypes.guess_extension(mime_type, strict=True)

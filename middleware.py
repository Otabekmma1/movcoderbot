import time
from aiogram import types
from aiogram import BaseMiddleware

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: int, cooldown: int):
        super().__init__()
        self.limit = limit  # Max allowed commands within the time frame
        self.cooldown = cooldown  # Time frame in seconds
        self.user_data = {}  # Store command usage data for each user

    async def on_process_message(self, message: types.Message, data: dict):
        user_id = message.from_user.id
        current_time = time.time()

        # Initialize user data if it doesn't exist
        if user_id not in self.user_data:
            self.user_data[user_id] = []

        # Clean up old timestamps
        self.user_data[user_id] = [timestamp for timestamp in self.user_data[user_id] if current_time - timestamp < self.cooldown]

        # Check if the user exceeds the limit
        if len(self.user_data[user_id]) >= self.limit:
            await message.answer("Siz juda ko'p buyruq yuboryapsiz. Iltimos, bir oz kuting.")
            return  # Block the command

        # Register the current command timestamp
        self.user_data[user_id].append(current_time)

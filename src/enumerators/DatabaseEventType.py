from enum import Enum

class DatabaseEventType(Enum):
    guild_joined = 1
    guild_left = 2
    voice_channel_joined = 3
    voice_channel_left = 4
    received_private_message = 5
    sent_private_message = 6
    received_text_channel_command = 7
    responded_to_text_channel_command = 8
    enabled_logging_in_guild = 9
    bot_started = 10
    message_received = 11
    message_sent = 12
    message_deleted = 13
    message_edited = 14
    guild_updated = 15
    channel_updated = 16
    member_joined = 17
    member_left = 18
    member_updated = 19
    member_banned = 20

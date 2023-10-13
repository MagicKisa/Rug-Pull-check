import asyncio
from telegram import Bot

async def check_chat_existence():
    # Вставьте ваш токен бота здесь
    bot_token = '6466406464:AAGnHNnHM3v4bVm0NbpLWnOV--Ie53NseOk'
    
    # Создайте объект бота
    bot = Bot(token=bot_token)
    
    # ID чата или username чата, который вы хотите проверить
    chat_identifier = '@rabbitkingX'
    
    try:
        chat = await bot.get_chat(chat_identifier)
        print(f'Чат существует: {chat.title} ({chat.id})')
    except Exception as e:
        if "Chat not found" in str(e):
            print(f'Чат с идентификатором {chat_identifier} не существует.')
        else:
            print(f'Произошла ошибка при проверке чата: {e}')

if __name__ == "__main__":
    asyncio.run(check_chat_existence())

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
import asyncio
import random
import json
import logging
import threading
import time
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='threading')

# Глобальное состояние бота
bot_state = {
    'running': False,
    'stats': {'sent': 0, 'success': 0, 'failed': 0},
    'last_error': None,
    'logs': []
}

class TelegramBot:
    def __init__(self):
        self.client = None
        self.task = None
        self.config = {
            'api_id': 000000,#your
            'api_hash': 'your',
            'phone': '+7your',
            'session_name': 'web_controlled_bot',
            'target': 'your',
            'messages': ["Тестовое сообщение"],
            'delay': 30
        }

    async def send_message(self):
        try:
            target = await self.client.get_input_entity(self.config['target'])
            message = random.choice(self.config['messages'])
            
            await self.client.send_message(target, message)
            return True
        except Exception as e:
            return str(e)

    async def run(self):
        self.client = TelegramClient(
            self.config['session_name'],
            self.config['api_id'],
            self.config['api_hash']
        )
        
        await self.client.start(self.config['phone'])
        
        while bot_state['running']:
            result = await self.send_message()
            
            if result is True:
                bot_state['stats']['sent'] += 1
                bot_state['stats']['success'] += 1
                log = f"{datetime.now()}: Сообщение отправлено"
            else:
                bot_state['stats']['sent'] += 1
                bot_state['stats']['failed'] += 1
                bot_state['last_error'] = result
                log = f"{datetime.now()}: Ошибка: {result}"
            
            bot_state['logs'].append(log)
            socketio.emit('update', bot_state)
            
            await asyncio.sleep(self.config['delay'])

        await self.client.disconnect()

bot = TelegramBot()

def run_bot_in_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(bot.run())

@app.route('/')
def index():
    return render_template('index.html', state=bot_state)

@app.route('/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        new_config = request.json
        bot.config.update(new_config)
        return jsonify(success=True)
    return jsonify(bot.config)

@app.route('/control', methods=['POST'])
def control():
    action = request.json.get('action')
    
    if action == 'start' and not bot_state['running']:
        bot_state['running'] = True
        bot_state['logs'].append(f"{datetime.now()}: Бот запущен")
        threading.Thread(target=run_bot_in_thread).start()
        
    elif action == 'stop' and bot_state['running']:
        bot_state['running'] = False
        bot_state['logs'].append(f"{datetime.now()}: Бот остановлен")
    
    socketio.emit('update', bot_state)
    return jsonify(success=True)

@app.route('/logs')
def logs():
    return jsonify(logs=bot_state['logs'])

if __name__ == '__main__':
    socketio.run(app, debug=True)

@app.route('/control', methods=['POST'])
def control():
    action = request.json.get('action')
    if action == 'start':
        bot_state['running'] = True
        threading.Thread(target=run_bot_in_thread).start()
    elif action == 'stop':
        bot_state['running'] = False
    return jsonify(success=True)
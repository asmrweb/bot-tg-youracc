<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        ul, ol {
            padding-left: 20px;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .note {
            background-color: #fff3cd;
            border: 1px solid #ffeeba;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .important {
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .section {
            margin-bottom: 40px;
        }
        .code-block {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

    <h1>Telegram Bot Control Application / Управление Telegram-ботом</h1>

    <div class="section">
        <h2>Overview / Обзор</h2>
        <p>This application allows you to control a Telegram bot via a web interface. You can configure the bot settings, start and stop its operation, and monitor its activity in real-time.</p>
        <p>Приложение позволяет управлять Telegram-ботом через веб-интерфейс. Вы можете настроить параметры бота, запускать и останавливать его работу, а также отслеживать активность в реальном времени.</p>
    </div>

    <div class="section">
        <h2>Features / Возможности</h2>
        <ul>
            <li>Start/Stop bot functionality / Запуск/остановка работы бота</li>
            <li>Configure phone number, target recipient, messages, and delay between messages / Настройка номера телефона, получателя, сообщений и задержки между отправками</li>
            <li>Real-time monitoring of sent messages, successes, and failures / Мониторинг отправленных сообщений, успешных попыток и ошибок в реальном времени</li>
            <li>Live logs and statistics chart / Логи и статистика в реальном времени</li>
        </ul>
    </div>

    <div class="section">
        <h2>Installation / Установка</h2>

        <h3>Step 1: Obtain <code>api_id</code> and <code>api_hash</code> / Получение <code>api_id</code> и <code>api_hash</code></h3>
        <ol>
            <li>Go to <a href="https://my.telegram.org/">https://my.telegram.org/</a> and log in with your Telegram account.  
                Перейдите на <a href="https://my.telegram.org/">https://my.telegram.org/</a> и войдите в свой аккаунт Telegram.</li>
            <li>Create a new application (App) to obtain <strong><code>api_id</code></strong> and <strong><code>api_hash</code></strong>.  
                Создайте новое приложение (App), чтобы получить <strong><code>api_id</code></strong> и <strong><code>api_hash</code></strong>.</li>
            <li>Copy these values and paste them into the Python code. Replace the following lines:  
                Скопируйте эти значения и вставьте их в код Python. Замените следующие строки:</li>
        </ol>
        <pre class="code-block">
self.config = {
    'api_id': YOUR_API_ID,  # Replace with your api_id / Замените на ваш api_id
    'api_hash': 'YOUR_API_HASH',  # Replace with your api_hash / Замените на ваш api_hash
    ...
}
        </pre>

        <h3>Step 2: Install Dependencies / Установка зависимостей</h3>
        <p>Ensure that you have the required Python libraries installed. Run the command:  
           Убедитесь, что установлены необходимые библиотеки Python. Выполните команду:</p>
        <pre class="code-block">pip install flask telethon flask-socketio chart.js</pre>

        <h3>Step 3: Run the Application / Запуск приложения</h3>
        <p>Start the script by running:  
           Запустите скрипт, выполнив команду:</p>
        <pre class="code-block">python filename.py</pre>
        <p>After launching, open your browser and navigate to:  
           После запуска откройте браузер и перейдите по адресу:</p>
        <pre class="code-block">http://127.0.0.1:5000</pre>
    </div>

    <div class="section">
        <h2>Usage / Использование</h2>

        <h3>Step 1: Authorization / Авторизация</h3>
        <p>On the first launch, the program will request an <strong>authorization code</strong>, which will be sent to you via Telegram. Enter this code in the console.  
           При первом запуске программа запросит <strong>код авторизации</strong>, который будет отправлен вам через Telegram. Введите этот код в консоль.</p>

        <h3>Web Interface Components / Компоненты веб-интерфейса</h3>

        <h4>1. Status Panel / Панель состояния</h4>
        <ul>
            <li><strong>Status</strong>: Shows whether the bot is active or inactive.  
                <strong>Статус</strong>: Показывает, активен ли бот.</li>
            <li><strong>Control Buttons</strong>:  
                <strong>Кнопки управления</strong>:
                <ul>
                    <li><strong>Start</strong>: Activates the bot.  
                        <strong>Запустить</strong>: Активирует бота.</li>
                    <li><strong>Stop</strong>: Stops the bot's tasks.  
                        <strong>Остановить</strong>: Останавливает выполнение задач бота.</li>
                    <li><strong>Run Program</strong>: Duplicates the functionality of the "Start" button.  
                        <strong>Запустить программу</strong>: Дублирует функционал кнопки "Запустить".</li>
                </ul>
            </li>
        </ul>

        <h4>2. Configuration Settings / Настройка конфигурации</h4>
        <p>Configure the bot parameters:  
           Настройте параметры бота:</p>
        <ul>
            <li><strong>Phone Number</strong>: Enter the phone number linked to your Telegram account.  
                <strong>Номер телефона</strong>: Укажите номер, привязанный к вашему аккаунту Telegram.</li>
            <li><strong>Recipient</strong>: Specify the username or ID of the message recipient.  
                <strong>Получатель</strong>: Укажите имя пользователя или ID получателя сообщений.</li>
            <li><strong>Messages</strong>: Enter message texts separated by commas (e.g., "Hello, How are you, Bye").  
                <strong>Сообщения</strong>: Введите тексты сообщений через запятую (например: "Привет, Как дела, Пока").</li>
            <li><strong>Delay (sec)</strong>: Set the interval between message sends in seconds.  
                <strong>Задержка (сек)</strong>: Установите интервал между отправками сообщений в секундах.</li>
            <li>Click <strong>Save</strong> to apply changes.  
                Нажмите <strong>Сохранить</strong>, чтобы применить изменения.</li>
        </ul>

        <h4>3. Monitoring Statistics / Мониторинг статистики</h4>
        <p>The page displays:  
           На странице отображается:</p>
        <ul>
            <li><strong>Sent</strong>: Total number of messages sent.  
                <strong>Отправлено</strong>: Общее количество отправленных сообщений.</li>
            <li><strong>Success</strong>: Number of successfully delivered messages.  
                <strong>Успешно</strong>: Количество успешно доставленных сообщений.</li>
            <li><strong>Errors</strong>: Number of failed attempts.  
                <strong>Ошибки</strong>: Количество неудачных попыток.</li>
            <li>A chart visually represents the statistics.  
                График наглядно демонстрирует статистику.</li>
        </ul>

        <h4>4. Logs / Логи</h4>
        <p>The "Logs" section shows all events, including errors and successful deliveries.  
           В разделе "Логи" отображаются все события, включая ошибки и успешные отправки.</p>
    </div>

    <div class="section">
        <h2>Example Usage / Пример использования</h2>
        <ol>
            <li>Enter your data in the configuration form.  
                Введите ваши данные в форму конфигурации.</li>
            <li>Click <strong>Save</strong>.  
                Нажмите <strong>Сохранить</strong>.</li>
            <li>Click <strong>Start</strong> to activate the bot.  
                Нажмите <strong>Запустить</strong>, чтобы активировать бота.</li>
            <li>The bot will begin sending random messages from the list at the specified interval.  
                Бот начнет отправлять случайные сообщения из списка с указанной задержкой.</li>
            <li>To stop, click <strong>Stop</strong>.  
                Для остановки нажмите <strong>Остановить</strong>.</li>
        </ol>
    </div>

    <div class="section important">
        <h2>Important Notes / Важные примечания</h2>
        <ul>
            <li>On the first launch, the program creates a Telegram session file. Do not delete it to avoid re-authorization.  
                При первом запуске программа создаст файл сессии Telegram. Не удаляйте его, чтобы избежать повторной авторизации.</li>
            <li>If you change <code>api_id</code>, <code>api_hash</code>, or the phone number, delete the old session file and restart the application.  
                Если вы измените <code>api_id</code>, <code>api_hash</code> или номер телефона, удалите старый файл сессии и перезапустите приложение.</li>
            <li>Ensure that your IP address is not blocked by Telegram, as this may cause connection issues.  
                Убедитесь, что ваш IP-адрес не заблокирован Telegram, так как это может вызвать проблемы с подключением.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Contributing / Вклад</h2>
        <p>If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.  
           Если вы хотите внести вклад, создайте форк репозитория и используйте отдельную ветку. Pull-запросы приветствуются.</p>
    </div>

    <div class="section">
        <h2>License / Лицензия</h2>
        <p>MIT License  
           Лицензия MIT</p>
    </div>

</body>
</html>

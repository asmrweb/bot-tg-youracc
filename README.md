

```markdown
# Telegram Bot Control Application / Управление Telegram-ботом

## Overview / Обзор

This application allows you to control a Telegram bot via a web interface. You can configure the bot settings, start and stop its operation, and monitor its activity in real-time.

Приложение позволяет управлять Telegram-ботом через веб-интерфейс. Вы можете настроить параметры бота, запускать и останавливать его работу, а также отслеживать активность в реальном времени.

## Features / Возможности

- Start/Stop bot functionality / Запуск/остановка работы бота
- Configure phone number, target recipient, messages, and delay between messages / Настройка номера телефона, получателя, сообщений и задержки между отправками
- Real-time monitoring of sent messages, successes, and failures / Мониторинг отправленных сообщений, успешных попыток и ошибок в реальном времени
- Live logs and statistics chart / Логи и статистика в реальном времени

## Installation / Установка

### Step 1: Obtain `api_id` and `api_hash` / Получение `api_id` и `api_hash`

1. Go to [https://my.telegram.org/](https://my.telegram.org/) and log in with your Telegram account.
   Перейдите на [https://my.telegram.org/](https://my.telegram.org/) и войдите в свой аккаунт Telegram.
2. Create a new application (App) to obtain **`api_id`** and **`api_hash`**.
   Создайте новое приложение (App), чтобы получить **`api_id`** и **`api_hash`**.
3. Copy these values and paste them into the Python code. Replace the following lines:
   Скопируйте эти значения и вставьте их в код Python. Замените следующие строки:

```python
self.config = {
    'api_id': YOUR_API_ID,  # Replace with your api_id / Замените на ваш api_id
    'api_hash': 'YOUR_API_HASH',  # Replace with your api_hash / Замените на ваш api_hash
    ...
}
```

### Step 2: Install Dependencies / Установка зависимостей

Ensure that you have the required Python libraries installed. Run the command:
Убедитесь, что установлены необходимые библиотеки Python. Выполните команду:

```bash
pip install flask telethon flask-socketio chart.js
```

### Step 3: Run the Application / Запуск приложения

Start the script by running:
Запустите скрипт, выполнив команду:

```bash
python filename.py
```

After launching, open your browser and navigate to:
После запуска откройте браузер и перейдите по адресу:

```
http://127.0.0.1:5000
```

## Usage / Использование

### Step 1: Authorization / Авторизация

On the first launch, the program will request an **authorization code**, which will be sent to you via Telegram. Enter this code in the console.
При первом запуске программа запросит **код авторизации**, который будет отправлен вам через Telegram. Введите этот код в консоль.

### Web Interface Components / Компоненты веб-интерфейса

#### 1. Status Panel / Панель состояния

- **Status**: Shows whether the bot is active or inactive.
  **Статус**: Показывает, активен ли бот.
- **Control Buttons**:
  **Кнопки управления**:
  - **Start**: Activates the bot.
    **Запустить**: Активирует бота.
  - **Stop**: Stops the bot's tasks.
    **Остановить**: Останавливает выполнение задач бота.
  - **Run Program**: Duplicates the functionality of the "Start" button.
    **Запустить программу**: Дублирует функционал кнопки "Запустить".

#### 2. Configuration Settings / Настройка конфигурации

Configure the bot parameters:
Настройте параметры бота:

- **Phone Number**: Enter the phone number linked to your Telegram account.
  **Номер телефона**: Укажите номер, привязанный к вашему аккаунту Telegram.
- **Recipient**: Specify the username or ID of the message recipient.
  **Получатель**: Укажите имя пользователя или ID получателя сообщений.
- **Messages**: Enter message texts separated by commas (e.g., "Hello, How are you, Bye").
  **Сообщения**: Введите тексты сообщений через запятую (например: "Привет, Как дела, Пока").
- **Delay (sec)**: Set the interval between message sends in seconds.
  **Задержка (сек)**: Установите интервал между отправками сообщений в секундах.
- Click **Save** to apply changes.
  Нажмите **Сохранить**, чтобы применить изменения.

#### 3. Monitoring Statistics / Мониторинг статистики

The page displays:
На странице отображается:

- **Sent**: Total number of messages sent.
  **Отправлено**: Общее количество отправленных сообщений.
- **Success**: Number of successfully delivered messages.
  **Успешно**: Количество успешно доставленных сообщений.
- **Errors**: Number of failed attempts.
  **Ошибки**: Количество неудачных попыток.
- A chart visually represents the statistics.
  График наглядно демонстрирует статистику.

#### 4. Logs / Логи

The "Logs" section shows all events, including errors and successful deliveries.
В разделе "Логи" отображаются все события, включая ошибки и успешные отправки.

## Example Usage / Пример использования

1. Enter your data in the configuration form.
   Введите ваши данные в форму конфигурации.
2. Click **Save**.
   Нажмите **Сохранить**.
3. Click **Start** to activate the bot.
   Нажмите **Запустить**, чтобы активировать бота.
4. The bot will begin sending random messages from the list at the specified interval.
   Бот начнет отправлять случайные сообщения из списка с указанной задержкой.
5. To stop, click **Stop**.
   Для остановки нажмите **Остановить**.

## Important Notes / Важные примечания

- On the first launch, the program creates a Telegram session file. Do not delete it to avoid re-authorization.
  При первом запуске программа создаст файл сессии Telegram. Не удаляйте его, чтобы избежать повторной авторизации.
- If you change `api_id`, `api_hash`, or the phone number, delete the old session file and restart the application.
  Если вы измените `api_id`, `api_hash` или номер телефона, удалите старый файл сессии и перезапустите приложение.
- Ensure that your IP address is not blocked by Telegram, as this may cause connection issues.
  Убедитесь, что ваш IP-адрес не заблокирован Telegram, так как это может вызвать проблемы с подключением.

## Contributing / Вклад

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.
Если вы хотите внести вклад, создайте форк репозитория и используйте отдельную ветку. Pull-запросы приветствуются.

## License / Лицензия

MIT License  
Лицензия MIT
```


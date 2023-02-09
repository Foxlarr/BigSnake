from telegram.ext import Updater, ConversationHandler, CommandHandler, Filters, MessageHandler
from logg import logging

CHOICE, NUMBER_ONE, NUMBER_TWO, OPERATIONS_NUMBERS = range(4)


def start(update, _):
    update.message.reply_text(f"Привет, {update.effective_user.first_name}, это - калькулятор.\n"
                              f"Выберите пожалуйста команду.\n" "Команда /cancel, чтобы прекратить разговор.\n\n")
    update.message.reply_text('1 - Начать работать;\n2 - Выйти из калькулятора \n')
    return CHOICE


def choice(update, _):
    user = update.message.from_user
    logging.info("Start of the program: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice in '12':
        if user_choice == '1':
            user = update.message.from_user
            logging.info("The user has started work: %s: %s", user.first_name, update.message.text)
            update.message.reply_text('Введите число. \n Первое число - это: ')
            return NUMBER_ONE
        if user_choice == '2':
            user = update.message.from_user
            logging.info("The user has completed the work: %s: %s", user.first_name, update.message.text)
            update.message.reply_text('До свидания!')
            return ConversationHandler.END
    else:
        update.message.reply_text('Ошибка ввода. Введите цифру операции: \n 1 - для начала работы;\n2 - для выхода \n')


def number_one(update, context):
    user = update.message.from_user
    logging.info("The user entered a number: %s: %s", user.first_name, update.message.text)
    get_number = update.message.text
    if get_number.isdigit():
        get_number = float(get_number)
        context.user_data['number_one'] = get_number
        update.message.reply_text('Введите второе число')
        return NUMBER_TWO

    else:
        update.message.reply_text('Нужно ввести число')


def number_two(update, context):
    user = update.message.from_user
    logging.info("The user entered a number: %s: %s", user.first_name, update.message.text)
    get_number = update.message.text
    if get_number.isdigit():
        get_number = float(get_number)
        context.user_data['number_two'] = get_number
        update.message.reply_text(
            'Выберите действие: \n\n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n')
        return OPERATIONS_NUMBERS
    else:
        update.message.reply_text('Нужно ввести число')


def operations_numbers(update, context):
    user = update.message.from_user
    logging.info("The user has selected an operation %s: %s", user.first_name, update.message.text)
    num_one = context.user_data.get('number_one')
    num_two = context.user_data.get('number_two')
    user_choice = update.message.text
    result = 0
    if user_choice in '+-/*':
        if user_choice == '+':
            result = num_one + num_two
        if user_choice == '-':
            result = num_one - num_two
        if user_choice == '*':
            result = num_one * num_two
        if user_choice == '/':
            try:
                result = num_one / num_two
            except ZeroDivisionError:
                update.message.reply_text('Деление на ноль запрещено')
                exit()
        logging.info(f"result -{result} %s: %s", user.first_name, update.message.text)
        update.message.reply_text(f'Результат: {num_one} + {num_two} = {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text(
            'Ошибка ввода. Выберите действие: \n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для '
            'деления. \n')


def cancel(update, _):
    user = update.message.from_user
    logging.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Спасибо, до свидания!')
    return ConversationHandler.END


TOKEN = '5898958780:AAFvE8vqNefRWEvo5c_e3hHhPJWetzbPWwM'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
conversation_handler = ConversationHandler(

    entry_points=[CommandHandler('start', start)],

    states={
        CHOICE: [MessageHandler(Filters.text, choice)],
        NUMBER_ONE: [MessageHandler(Filters.text, number_one)],
        NUMBER_TWO: [MessageHandler(Filters.text, number_two)],
        OPERATIONS_NUMBERS: [MessageHandler(Filters.text, operations_numbers)],
    },

    fallbacks=[CommandHandler('cancel', cancel)],
)

dispatcher.add_handler(conversation_handler)
print('server start')
updater.start_polling()
updater.idle()
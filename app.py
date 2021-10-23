import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update, ReplyKeyboardRemove, ForceReply
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

from flask import Flask
import asyncio

loop = asyncio.get_event_loop()
app = Flask(__name__)

@app.route('/')
def index():
    # keyboard
    signal_key = [
        [
        InlineKeyboardButton("➡️ WizScalp", url='https://t.me/WizScalp'),
        InlineKeyboardButton("➡️ Other", url='https://dgpbot.com')
            ]
        ]

    binance_key = [
        [InlineKeyboardButton("➡️ Create Binance Account", url='https://accounts.binance.com/en/register')]
    ]

    registerdgpbot_key = [
        [InlineKeyboardButton("➡️ Join DGPBot", url='https://dgpbot.com/register')]
    ]

    tutorial_key = [
        [InlineKeyboardButton("➡️ Solve API not Valid or Permission", url='https://www.youtube.com/watch?v=g7hxyyS8kgs'),
        InlineKeyboardButton("➡️ Insuficience Fund or Balance", url='https://www.youtube.com/watch?v=8Pq3ohFwaPE')],

        [InlineKeyboardButton("➡️ Problem solving No Main Menu", url='https://www.youtube.com/watch?v=8Pq3ohFwaPE'),
        InlineKeyboardButton("➡️ DGPBOT Promotion", url='https://www.youtube.com/watch?v=SfJDpKkZqhU')],

        [InlineKeyboardButton("➡️ DGPBOT Tutorial", url='https://www.youtube.com/watch?v=LEyQs_baRhY'),
        InlineKeyboardButton("➡️ Connect Binance API with DGPBOT", url='https://www.youtube.com/watch?v=VMkxFnice_Y')],

        [InlineKeyboardButton("➡️ Activation Tutorial of DGPBOT", url='https://www.youtube.com/watch?v=Ubdvg2163tI')]
    ]

    settingdgpbot_key = [
        [InlineKeyboardButton("➡️ Change Language Preference", callback_data="change_language_preference"),
        InlineKeyboardButton("➡️ Set BTC per buy", callback_data="set_btc_per_buy")],

        [InlineKeyboardButton("➡️ Configuration", callback_data="configured_correctly"),
        InlineKeyboardButton("➡️ Generate Report", callback_data="generate_report")],

        [InlineKeyboardButton("➡️ DCA Set Re-buy", callback_data="dca_set_re_buy"),
        InlineKeyboardButton("➡️ Set Re-buy Percentage", callback_data="percentage")],

        [InlineKeyboardButton("➡️ Set/Deactivate SL", callback_data="deactivate_sl"),
        InlineKeyboardButton("➡️ Set Maximum Signal", callback_data="maximum_signal")],

        [InlineKeyboardButton("➡️ Set Cancel Order Time", callback_data="cancel_order"),
        InlineKeyboardButton("➡️ Set Trail Stop", callback_data="trail_stop")],

        [InlineKeyboardButton("➡️ Activate/Deactivate an Algorithm", callback_data="algorithm")]
    ]

    faq_key = [
        [InlineKeyboardButton("⚠️ I see sign in front of my open position. What does that mean?", callback_data="faq_one")],
        [InlineKeyboardButton("⚠️ Can I set different re-buy %, stop loss, BTC per buy etc. for different algorithms?", callback_data="faq_two")],
        [InlineKeyboardButton("⚠️ Can I trade signals based on USDT?", callback_data="faq_three")],
        [InlineKeyboardButton("⚠️ I don’t want to get any new signal but I want my open signals to becompleted. Can I do this?", callback_data="faq_four")]
    ]

    def start(update: Update, context: CallbackContext) -> None:
        """Sends a message with three inline buttons attached."""
        query = update.callback_query

        def openKeyboard():
            rkeyboard = [
                [KeyboardButton('ℹ️ About DGPBOT')],
                [KeyboardButton('📶 Signal DGPBOT'), KeyboardButton('🛠 Setting DGPBOT')],
                [KeyboardButton('♻️ Create Binance Account')],
                [KeyboardButton('♻️ Join DGPBot'), KeyboardButton('💬 FAQ')],
                [KeyboardButton('🔍 Tutorial')],
                [KeyboardButton('🎯 Thoughts and Advices')]
            ]

            reply_kmarkup = ReplyKeyboardMarkup(rkeyboard)
            update.message.reply_text(text='🌟 *Welcome to our Service* 🌟', reply_markup=reply_kmarkup, parse_mode=telegram.ParseMode.MARKDOWN)
        
        if '/start' == update.message.text:
            openKeyboard()

        # reply_markup = InlineKeyboardMarkup(keyboard)
        # update.message.reply_text('Main Menu', reply_markup=reply_markup)

    def button(update: Update, context: CallbackContext) -> None:
        """Parses the CallbackQuery and updates the message text."""

        query = update.callback_query
        query.answer()

        if 'change_language_preference' == query.data:
            query.message.reply_text(text="<b>How to Change Language Preference</b>\n\nThis bot is offered in 6 different languages. You can switch between English,Turkish, French, Russian, Indonesian, and Persian. Unfortunately, there are some untranslated parts in each language. Those remaining parts offered in English will be fully translated in near future.", parse_mode=telegram.ParseMode.HTML)
            query.message.reply_photo(photo='https://blogger.googleusercontent.com/img/a/AVvXsEg4neIpMbL2FEM7FAby9N8C7zab7SK3Ln9Vp-gGcRrF6R7ypl_vjOH1srQ2toHMNl0JP6GLtAbaz5NPNegot43uqqhGC2lGWl2-yBn1Lb-sR8ExDszuiGj0oiQMUOpNubYtoN60jI3pNm3j6EpjKjwsnfSJB5Lisskdy9rV-Yy2n_b2vyIW9RJW4SXiwQ=s381')
            query.message.reply_text(text="<b>→ Information → Language → Choose whichever language you want to use.</b>", parse_mode=telegram.ParseMode.HTML)

        elif 'set_btc_per_buy' == query.data:
            query.message.reply_text(text="<b>How to Set BTC per buy</b>\n\nYou need to set a BTC per buy value for the bot to place order when in signal. This value is very important and depends on the risk appetite of the users. It is recommended to set 1/20 of your total balance as the optimal value.\n\n<b>To set BTC per buy, simply write <b>setBuy</b> 0.003</b>\n<b>This will set your BTC per buy = 0.003</b>", parse_mode=telegram.ParseMode.HTML)
        
        elif 'configured_correctly' == query.data:
            query.message.reply_text(text="<b>How to Make Sure the Bot Is Configured Correctly</b>\n\nAfter setting your API Key and Secret information, click the <b>Start bot</b> button from the main menu. Then open your Binance account and place any buy or sell orders. If the bot detects your order, it will send you a message.\n\nIf the message does not come, either you haven't started the bot or your API Key and Secret values are incorrect. Do this process again until you get a message that the order has been placed.", parse_mode=telegram.ParseMode.HTML)
            query.message.reply_photo(photo="https://blogger.googleusercontent.com/img/a/AVvXsEiaAViMGSLhZcDeZguoUnJeXPe6c1TgxRLHG0Ta3lssVjACZ3O-cmXgRV2SA7hIE2dUb3yL7r_taDDyeC_Z6U8MXBt03GFhxC2JN3XPFemhFbr7hONMb8BteuIAo3f_as5zSRiaGX0yQLS6Z9lkQIsVPMknWFNFB_KlPZsM4lzTBwC-VEpxC1vYDdaLbQ=s338")

        elif 'generate_report' == query.data:
            query.message.reply_text(text="<b>How to Generate Report for Finished Trades</b>\n\nYou can create an Excel file to see the transaction history, profitability rate of the signals traded by the bot.\n\n<b>→ Report → Export to Excel.</b>\n\n<b>Note:</b> If an old report is sent, or nothing is returned, click Export to Excel button again.", parse_mode=telegram.ParseMode.HTML)
            query.message.reply_photo(photo="https://blogger.googleusercontent.com/img/a/AVvXsEiL46bR5Aaialp6qZbrEr3-W1KvNUVDqg1G3G9KSSkJ_oBqVjkCXqsJnkAtY1oSWPSZn8ATXMxYFN4QQ0hh8EXLFw2K8wX1wEczowqNYR0hXTUs3aHxedDk-SS8nG9dFNX2WHXviqCLDq2Ak-DBASymB-7lAPICqmh43p3dRSlvWNrhTSpARaqlt2fNlQ=s387")

        elif 'dca_set_re_buy' == query.data:
            query.message.reply_text(text="<b>How to Dollar-Cost Averaging (DCA), Set Re-buy</b>\n\nThis means that if you are in a signal and price drops, bot will automatically rebuy the coin to lower your average buy price. Dollar-Cost averaging is a really helpful method to exit the signal as early as possible. However, it should be noted that this might also get you in a position with huge loss. Decide carefully how many times to buyback again.\n\n<b>→ Settings → Re-buy → Click how many times you want to re-buy.</b>", parse_mode=telegram.ParseMode.HTML)

        elif 'percentage' == query.data:
            query.message.reply_text(text="<b>How to Set Re-buy Percentage</b>\n\nTo apply Dollar-Cost Averaging, you must define a distance to have the bot buy again for you.\n\n<b>Let’s examine this situation:</b>\nYour re-buy % = 3%\nYou bought a signal when it is 10000 satoshi, it means that your first re-buy will be when price is 9700 satoshi.\nYour second re-buy will be when price is 9700*0.97=9409 satoshi\nYour third re-buy will be when price is 9409*0.97=9127 satoshi\n\n<b>→ Settings → Stop Loss → Click what percentage do you want to set.</b>", parse_mode=telegram.ParseMode.HTML)

        elif 'deactivate_sl' == query.data:
            query.message.reply_text(text="<b>How to Set/Deactivate Stop-loss</b>\n\nStop-loss can be defined as an advance order to sell an asset when it reaches a particular price point. It is used to limit loss or gain in a trade. By placing a stop-loss order, the investor instructs the broker/agent to sell a security when it reaches a pre-set price limit\n\n<b>→ Settings → Stop Loss → Click what percentage do you want to set.</b>\n\n<b>Note:</b> If you don't want to set stop-loss, click Don't use stop loss", parse_mode=telegram.ParseMode.HTML)

        elif 'maximum_signal' == query.data:
            query.message.reply_text(text="<b>How to Set Maximum Signal</b>\n\nIn order to use your budget effectively and apply dollar-cost averaging, you should adjust the maximum number of signals you will be trading at the same time.\n\n<b>→ Settings → Max Signal → Click how many signals you want to trade at the same time.</b>", parse_mode=telegram.ParseMode.HTML)

        elif 'cancel_order' == query.data:
            query.message.reply_text(text="<b>How to Set Cancel Order Time</b>\n\nIn some cases, the signal may be completed before the orders we placed are filled, and the order may remain open for no reason. Therefore, it would be in our best interest to cancel our orders automatically after a certain period of time.\n\n<b>→ Settings → Cancel Order → Click how many minutes you want to wait before canceling the order.</b>", parse_mode=telegram.ParseMode.HTML)

        elif 'trail_stop' == query.data:
            query.message.reply_text(text="<b>How to Set Trail Stop</b>\n\nThis feature is under construction currently. It will be documented later.", parse_mode=telegram.ParseMode.HTML)

        elif 'algorithm' == query.data:
            query.message.reply_text(text="<b>How to Activate/Deactivate an Algorithm</b>\n\nSimply click on the algorithm you want to activate/deactivate.", parse_mode=telegram.ParseMode.HTML)
            query.message.reply_photo(photo="https://blogger.googleusercontent.com/img/a/AVvXsEieRAKrJ-7k8K2PlE7Lp3f83EBujIGtCAKdl6fwHwRpa831jCdNviissyL0hjNN0OVQnfYphX7DqPO-kG_z2-iYs9qRRYq-SkLdSx3oShEc5H_NXJMgYEGKusjdoA-2iVVs83GxjuKKLaNMaMKl1VjRTvvNsi7onQZfEJfMaRTb-g1qdmRhG8JKWE6tIg=s339")

        # FAQ 

        elif 'faq_one' == query.data:
            query.message.reply_text(text="<b>I see sign in front of my open position. What does that mean</b> ❓\n\nThis sign is placed under conditions where:\n\n✔️ <b>You manually interfered the position and sold what the bot bought:</b> You should not interfere with the transactions opened by the bot. If you sell 20 of them while the bot has bought 100, the bot will get an error when trying to sell 100 purchased, because now you have 80. When the bot encounters such a situation, it stops intervening in that process. If you encounter such a situation, you should open your position and click the <b>Delete position</b> button. If you don't click it, it will continue to appear open.\n\n✔️ <b>When the bot tries to buy again, there is not enough BTC in your account:</b> The bot repurchases according to the criteria you have previously set. If the necessary BTC is not exist in your account when the bot makes a repurchase, it will not be able to make the purchase. In this case, all you have to do is click on your position and click on the <b>Start Trading</b> button when you have enough BTC in your account again.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_two' == query.data:
            query.message.reply_text(text="<b>Can I set different re-buy %, stop loss, BTC per buy etc. for different algorithms</b> ❓\n\nNo, unfortunately you cannot do that currently. On later versions, it is planned to have different trading settings for each algorithm.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_three' == query.data:
            query.message.reply_text(text="<b>Can I trade signals based on USDT</b> ❓\n\nNo, unfortunately there isn’t any signal provider in our ecosystem that provides USDT based signals. In the future, it is planned to gather different algorithm provider to the system and increase the signal number and diversity.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_four' == query.data:
            query.message.reply_text(text="<b>I don’t want to get any new signal but I want my open signals to be completed. Can I do this</b> ❓\n\nYes, you can do that. All you need to do deactivate all algorithms you followed, and not to close bot’s connection to your account. In this condition bot will not get any new signal for your account, however it will continue trading your open signals.", parse_mode=telegram.ParseMode.HTML)

    def mainButton(update: Update, context: CallbackContext) -> None:

        if 'Main Menu' == update.message.text:
            # update.message.delete(10)
            rem_kmarkup = ReplyKeyboardRemove(True)
            update.message.reply_text('Main Menu', reply_markup=rem_kmarkup)

            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text('Main Menu', reply_markup=reply_markup)

        elif 'ℹ️ About DGPBOT' == update.message.text:
            # update.message.delete(10)
            update.message.reply_text('❇️ DGPbot is an automated trading bot that combines AI technology with our trading analysis software. DGPbot will auto-execute based on Telegram signal groups and TradingView alerts. We have built a platform with features that minimize risk, whether you are trading manually or automatically ❇️\n\n➡️ https://dgpbot.com/')
        
        elif '📶 Signal DGPBOT' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(signal_key)
            update.message.reply_text('♻️ Signal DGPBOT ♻️', reply_markup=reply_markup)
        
        elif '♻️ Create Binance Account' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(binance_key)
            update.message.reply_text('♻️ Create Binance Account ♻️', reply_markup=reply_markup)

        elif '♻️ Join DGPBot' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(registerdgpbot_key)
            update.message.reply_text('♻️ Join DGPBot ♻️', reply_markup=reply_markup)

        elif '🔍 Tutorial' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(tutorial_key)
            update.message.reply_text('♻️ <b>Tutorial</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

        elif '🛠 Setting DGPBOT' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(settingdgpbot_key)
            update.message.reply_text('♻️ Setting DGPBOT ♻️', reply_markup=reply_markup)

        elif '🎯 Thoughts and Advices' == update.message.text:
            # update.message.delete(10)
            update.message.reply_text(f'♻️ <b>Some Thoughts and Advices</b> ♻️\n\nIn this section, I would like to tell you, as the developer of the bot, how you can achieve the highest efficiency while using the bot actively. I think that the logic that I will explain here will be very useful for you when doing day-trading as well. Please keep in mind that when using DGPBot or similar systems, the operations will not be done by you. While a normal trader can follow several positions at the same time, a bot can follow multiple positions and trade according to pre-determined rules. Therefore, when asking the bot to enter a transaction, do not set it to enter with the balance you enter at the regular time.\n\nThe logic we have to apply here should be like this, we should set the balance that the bot will use when entering a transaction very low compared to our total balance so that the bot can be involved in many signals at the same time. Because, while some signals do not reach the target for a long time, some signals can reach the target in a very short time. We wouldn’t want to have to wait as we put most of our budget on one signal, while other signals are completing quickly. In addition, when we apply this approach, when we come across an unsuccessful signal, we minimize the amount of loss since we do not allocate most of our balance to that signal.\n\nIf we take a look at the statistics of WizScalp channel, which is currently used most actively on DGPBot, the rate of reaching the target in 96 hours seems to be around 91.5%. This rate can be increased to around 95% on average with repeat purchases with the use of bots. In the past time, I have observed that some users using the bot can increase this rate up to 98%. When I looked closely at how this success was achieved, I saw the following.\n\n✅ The balance of these users was high.\n✅ These users had set the BTC value per purchase very accurately.\n\nWhen these users went in an unsuccessful signal, they were able to repurchase up to 8-9 times and wait, because their balances were high and their btc values per purchase were low compared to their balance. This is not a very viable method for users with lower balances (less than 0.5 BTC), I agree.However, the main approach here is that dividing our money as much as possible will provide us with more positive returns in the long run. How smartly we distribute our money will be the main factor that will determine the benefit we will get from the bot. In the rest of this document, I will talk about how to set up your customizable options such as btc per buy, re-buy(dca) amount, stop-loss etc.', parse_mode=telegram.ParseMode.HTML)

        elif '💬 FAQ' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(faq_key)
            update.message.reply_text('♻️ Frequently Asked Questions ♻️', reply_markup=reply_markup)


    async def main():
        updater = Updater("1987254247:AAENZxY0HRzWcqrYvjRWtXjJMkPRQJNQMkM", request_kwargs={'read_timeout': 6, 'connect_timeout': 7})
        
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CallbackQueryHandler(button))
        updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), mainButton))
        
        updater.start_polling()

    loop.run_until_complete(main())

    return "success.."

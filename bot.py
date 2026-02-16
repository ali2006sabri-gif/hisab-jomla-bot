from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN="ضع_التوكن_الجديد_هنا"
products={"ماء":35,"كوكا":120,"حمود":85}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا 👋\nاكتب المنتج والكمية\nمثال: كوكا 10")

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        name,q=update.message.text.split()
        q=int(q)
        if name in products:
            total=products[name]*q
            await update.message.reply_text(f"{q}×{products[name]}={total} دج")
        else: await update.message.reply_text("❌ المنتج غير موجود")
    except: await update.message.reply_text("اكتب هكذا: كوكا 10")

app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT&~filters.COMMAND,calc))
app.run_polling()

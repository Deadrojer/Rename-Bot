from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client , filters




@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
    text = """Free Plan User
Daily  Upload limit 5GB
Price 0

🪙 Basic
Daily  Upload  limit 20GB
Price Rs 39  ind /🌎 0.49$  per Month

⚡ Standard
Daily Upload limit 50GB
Price Rs 80  ind /🌎 1$  per Month

💎 Pro
Daily Upload limit 100GB
Price Rs 150  ind /🌎 2$  per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>narutoprit@fam</code>

After Payment Send Screenshots Of Payment To Admin @NARUTO_UZUMAKI07th""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://telegram.me/NARUTO_UZUMAKI07th"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await update.message.edit(text = text,reply_markup = keybord, disable_web_page_preview=True)
    
    

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
    text = """Free Plan User
Daily  Upload limit 5GB
Price 0

🪙 Basic
Daily  Upload  limit 20GB
Price Rs 39  ind /🌎 0.49$  per Month

⚡ Standard
Daily Upload limit 50GB
Price Rs 80  ind /🌎 1$  per Month

💎 Pro
Daily Upload limit 100GB
Price Rs 150  ind /🌎 2$  per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>Narutoprit@fam</code>

After Payment Send Screenshots Of Payment To Admin @NARUTO_UZUMAKI07th"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "T.me/NARUTO_UZUMAKI07th"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await message.reply_text(text=text, reply_markup=keybord, quote=True, disable_web_page_preview=True)

from aiogram import Bot, Dispatcher, types, executor
import pyqrcode as pq

bot = Bot('5945311394:AAH-M16d_elD133SYQqJwVMn2H5X2GbMhaM')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def starter(msg: types.Message):
    await msg.answer(
        "Salom, sizni botda ko'rib turganimdan mamnunman\n Istalgan so'z, gap, havola kabilarni yuboring va men sizga QR code holatini yaratib beraman")

@dp.message_handler()
async def send_text_based_qr(msg: types.Message):
    await msg.answer("Qabul qilindi. \nIltimos kuting!...")

    qr_code = pq.create(msg.text)
    qr_code.png('code.png', scale=16)

    with open('code.png', 'rb') as photo:
        await bot.send_photo(msg.chat.id, photo)
        await bot.send_message(msg.chat.id, 'QR kodingiz tayyor! \nYana boshqa xabar yuborishingiz mumkin')
executor.start_polling(dp)
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random, os

import compres
import write
from moviepy.editor import *
import numpy
from PIL import Image

bot = Bot(token = "5291799706:AAF-1ctQif_rSTCmdg6qJvChHCZeZHsaTmA")
dp = Dispatcher(bot)

extension = ['jpg', 'png']
photo_delivered: set[int] = set()

def collage(folder):
	try:
		print(5)
		h, hs = {}, 0
		k , k1, s = 0, 0, 0
		o = 2
		if k1 <= 6:
			for i in os.listdir(folder):
				s += 1
				k1 += 1
				if s == 2:
					s = 0
					hs += 1
					n = numpy.array(Image.open(f'{folder}/{i}'))
					h[hs] = numpy.hstack((n,k))
				else:
					k = numpy.array(Image.open(f'{folder}/{i}'))
	
		st = []
		for j in range(1, hs+1):  st.append(h[j])
		arrayImageFinal=numpy.vstack(tuple(st))
		finalImage=Image.fromarray(arrayImageFinal)
		filename = f'collage{str(random.randint(1,9999))}.png'
		finalImage.save(filename)
		return filename
	except Exception as e:
		print(e)
		return False
	

async def photovid(id, folder):
	if os.path.isdir(folder):
		clips = []
		for i in os.listdir(folder):
			clip1 =  ImageClip(f"{folder}/{i}").set_duration(3)
			clips.append(clip1)
			video_clip = concatenate_videoclips(clips, method='compose')
			video_clip.write_videofile(f"{folder}/video-output.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")
			await bot.send_video(id, open(f"{folder}/video-output.mp4", 'rb'))
		os.system(f"rm -rf {folder}")
	else:
		bot.send_message(id, "Hozircha fotolar yo'q")
    	
    	
async def say_thanks(user: types.User):
    folder = f"download/{str(user.id)}/"
    if user.id in photo_delivered:
        return
    photo_delivered.add(user.id)
    if os.path.isdir(folder) == False:
    	os.mkdir(folder)
    
    await bot.send_message(user.id, "Saqlandi")

async def photo_handler(message: types.Message):
	folder = f"download/{str(message.from_user.id)}"
	await say_thanks(message.from_user)
	photo = message.photo.pop()
	await photo.download(f'{folder}/{str(random.randint(1,9999))}.jpg')


async def video_handler(message: types.Message):
	folder = f"download/vid{str(message.from_user.id)}"
	if not (os.path.isdir(folder)):
		os.mkdir(folder)
	video = message.video
	await message.reply("YUKLANMOQDA...")
	file_name = f'{folder}/{str(random.randint(1,9999))}.mp4'
	await video.download(file_name)
	keyboard = types.InlineKeyboardMarkup()
	b1 = types.InlineKeyboardButton(text='↖️', callback_data=f"k//{file_name}//left,top//{video.file_size}")
	b2 = types.InlineKeyboardButton(text='⬆️️', callback_data=f"k//{file_name}//top//{video.file_size}")
	b3 = types.InlineKeyboardButton(text='↗️', callback_data=f"k//{file_name}//right,top//{video.file_size}")
	b4 = types.InlineKeyboardButton(text='⬅️️', callback_data=f"k//{file_name}//left//{video.file_size}")
	b5 = types.InlineKeyboardButton(text='⏺', callback_data=f"k//{file_name}//center//{video.file_size}")
	b6 = types.InlineKeyboardButton(text='➡️', callback_data=f"k//{file_name}//right//{video.file_size}")
	b7 = types.InlineKeyboardButton(text='↙️', callback_data=f"k//{file_name}//left,bottom//{video.file_size}")
	b8 = types.InlineKeyboardButton(text='⬇️', callback_data=f"k//{file_name}//bottom//{video.file_size}")
	b9 = types.InlineKeyboardButton(text='↘️', callback_data=f"k//{file_name}//right,bottom//{video.file_size}")
	await message.reply("YUKLANDI LOGO QAYSI TOMONDA CHIQSIN", reply_markup=keyboard.add(b1,b2,b3).add(b4,b5,b6).add(b7,b8,b9))

@dp.callback_query_handler()
async def menu(call: types.CallbackQuery):
	b = call.data.split("//")
	if b[0] == "k":
		keyboard = types.InlineKeyboardMarkup()
		b1 = types.InlineKeyboardButton(text='↖️', callback_data=f"k={file_name}//left,top")
		b2 = types.InlineKeyboardButton(text='⬆️️', callback_data=f"k={file_name}//top")
		b3 = types.InlineKeyboardButton(text='↗️', callback_data=f"k={file_name}//right,top")
		b4 = types.InlineKeyboardButton(text='⬅️️', callback_data=f"k={file_name}//left")
		b5 = types.InlineKeyboardButton(text='⏺', callback_data=f"k={file_name}//center")
		b6 = types.InlineKeyboardButton(text='➡️', callback_data=f"k={file_name}//right")
		b7 = types.InlineKeyboardButton(text='↙️', callback_data=f"k={file_name}//left,bottom")
		b8 = types.InlineKeyboardButton(text='⬇️', callback_data=f"k={file_name}//bottom")
		b9 = types.InlineKeyboardButton(text='↘️', callback_data=f"k={file_name}//right,bottom")
		await bot.edit_message_text("EDIT BOSHLANDI",call.message.chat.id, call.message.message_id)

	elif b[0] == "m":
		folder = f"download/vid{str(call.from_user.id)}"

		print(b)
		filename = b[1]
		pos = tuple(map(str, b[2].split(',')))
		if len(pos) == 1:
			pos = b[1]
		print(pos)
		down_name = f'{folder}/{str(random.randint(1, 9999))}.mp4'
		await bot.edit_message_text("EDIT BOSHLANDI",call.message.chat.id, call.message.message_id)
		await compres.compress_video(b[])
		await bot.send_video(call.from_user.id, open(write.tologo(filename, pos, down_name), 'rb'))
		os.remove(filename)
		os.remove(down_name)


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Hush kelibsiz\n\nFotolar yuboring men uni saqlab olaman\nCollage qilish uchn /collage buyrug'ini\nVideo qilish uchun /vid buyrug'ini yuboring\nTozalash uchun /clean dan foydalaning")


async def coll(message: types.Message):
	await bot.send_message(message.from_user.id, "Tayyorlanmoqda...")
	try:
		photo_delivered.remove(message.from_user.id)
	except:
		pass
	await bot.send_message(message.from_user.id, "Tayyorlanmoqda")
	filename = collage(f"download/{message.from_user.id}")
	if filename == False:
		await bot.send_message(message.from_user.id, "Fotolar mos kelmadi")
	else:
		await bot.send_photo(message.from_user.id, open(filename, "rb"))
		os.remove(filename)

async def vid(message: types.Message):
    folder = f"download/{str(message.from_user.id)}"
    await bot.send_message(message.from_user.id, "Tayyorlanmoqda...")
    await photovid(message.from_user.id, folder)



async def clean(message: types.Message):
    await bot.send_message(message.from_user.id, "Tarix tozalandi")
    os.system(f"rm -rf download/{message.from_user.id}/")
dp.register_message_handler(photo_handler, content_types=['photo'])
dp.register_message_handler(video_handler, content_types=['video'])
dp.register_message_handler(start, commands=['start'])
dp.register_message_handler(coll, commands=['collage'])
dp.register_message_handler(vid, commands=['vid'])
dp.register_message_handler(clean, commands=['clean'])
executor.start_polling(dp, skip_updates=True)



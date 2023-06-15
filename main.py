
from time import sleep
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random, write, os, compres, collage
from moviepy.editor import *

bot = Bot(token = "5529772988:AAEn2oRhxWfE80yKwf_Y_LH40ES8iaZCdJM")

dp = Dispatcher(bot)
mess = {}
img = {}
step = {}

extension = ['jpg', 'png']
photo_delivered: set[int] = set()


async def photovid(id, folder):
	if os.path.isdir(folder):
		clips = []
		for i in os.listdir(folder):
			clip1 = ImageClip(f"{folder}/{i}").set_duration(3)
			clips.append(clip1)
		video_clip = concatenate_videoclips(clips, method='compose')
		clip = video_clip.subclip(0, 5)
		x, y = clip.size
		logo = (ImageClip('logo.png')
				.set_duration(video_clip.duration)
				.resize(height=(x + y) / 14)
				.margin(right=10, top=10, left=10, bottom=10, opacity=0)
				.set_pos(('right', 'top')))
		final = CompositeVideoClip([video_clip, logo])
		final.write_videofile(f"{folder}/video-output.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")
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
	r = await bot.send_message(user.id, "Yuklanmoqda...")
	sleep(1)
	await bot.edit_message_text("Yuklanmoqda 🔆",user.id, r.message_id)
	sleep(1)
	await bot.edit_message_text("Yuklab olindi!\nYana photo yuborishingiz mumkin!\nVideo tayyorlash /vid\nCollage tayyorlash /collage\nO'chirib tashlash /clean", user.id, r.message_id)


async def start(message: types.Message):
    step[message.from_user.id] = None
    img[message.from_user.id] = 1000
    open("logosize.txt", 'w+').write("15")
    await bot.send_message(message.from_user.id, "Botimizga Hush kelibsiz\n\nBotimiz nima qila oladi? \n1. Video yuborsangiz uni audio qilishingiz\n2. Siz yuborgan Videoni xajmini kichrayritib logo bosishi \n3. Audioni(.ogg) Musicga (.mp3) convert qilishi yoki aksincha \n4. Ko'pgina fotolar yuborilsa unicollage qilib berishi mumkin\n\n\nEslatib o'tadigan commandlar\n/start - Qayta ishga tushirish \n/quality - Sifatni tanlash imkoniyati\n/logosize - Videoga qo'yiladigan logoni xajmini o'zgartirish\n/logo - Logoni o'zgartirish (Video va Collagega tegishli)")

async def coll(message: types.Message):
	folder = f"./download/{message.from_user.id}"
	if os.path.isdir(folder):
		try:
			photo_delivered.remove(message.from_user.id)
		except:
			pass
		await bot.send_message(message.from_user.id, "Tayyorlanmoqda...")
		filename = collage.imgcollage(folder)
		print(filename)
		try: await bot.send_photo(message.from_user.id, open(filename, "rb"), caption="✅ Tayyor")
		except Exception as e: await message.reply(str(e))
		os.system(f"rm -rf {folder}")
		try: del photo_delivered[message.from_user.id]
		except: pass
	else:
		await bot.send_message(message.from_user.id, "❌ HOZIRDA PHOTOLAR MAVJUD EMAS")



async def vid(message: types.Message):
	folder = f"download/{str(message.from_user.id)}"
	if os.path.isdir(folder):
		try:
			photo_delivered.remove(message.from_user.id)
		except:
			pass
		await bot.send_message(message.from_user.id, "Tayyorlanmoqda...")
		await photovid(message.from_user.id, folder)
	else:
		await bot.send_message(message.from_user.id, "❌ HOZIRDA PHOTOLAR MAVJUD EMAS")

async def clean(message: types.Message):
	await bot.send_message(message.from_user.id, "Tarix tozalandi")
	os.system(f"rm -rf download/{message.from_user.id}/")
	try: del photo_delivered[mess.from_user.id]
	except: pass

async def audio_handler(message: types.Message):
	mess[message.from_user.id] = message
	folder = f"download/vid{str(message.from_user.id)}"
	await message.reply("Tayyorlanmoqda...")
	if message.audio:
		file_name = f'{folder}/{str(random.randint(1,9999))}.mp3'
		file_id = message.audio.file_id
		file = await bot.get_file(file_id)
		file_path = file.file_path
		await bot.download_file(file_path, file_name)
		await bot.send_voice(message.from_user.id, open(file_name, 'rb'), "✅ Tayyor")
		os.remove(file_name)

async def voice_handler(message: types.Message):
	mess[message.from_user.id] = message
	folder = f"download/vid{str(message.from_user.id)}"
	await message.reply("Tayyorlanmoqda...")
	if message.voice:
		file_name = f'{folder}/{str(random.randint(1,9999))}.mp3'
		file_id = message.voice.file_id
		file = await bot.get_file(file_id)
		file_path = file.file_path
		await bot.download_file(file_path, file_name)
		await bot.send_audio(message.from_user.id, open(file_name, 'rb'), "✅ Tayyor", performer="UzbProMax", title="Media Tools")
		os.remove(file_name)

async def photo_handler(message: types.Message):
	folder = f"download/{str(message.from_user.id)}"
	await say_thanks(message.from_user)
	photo = message.photo.pop()
	try: img[message.from_user.id] += 1
	except: img[message.from_user.id] = 1000
	filename = f'{folder}/{str(img[message.from_user.id])}.jpg'
	await photo.download(filename)


async def video_handler(message: types.Message):
	mess[message.from_user.id] = message
	keyboard = types.InlineKeyboardMarkup()
	b1 = types.InlineKeyboardButton(text='Audio Qilish', callback_data=f"toaudio")
	b2 = types.InlineKeyboardButton(text='Text va Compress qilish', callback_data=f"totext")
	b3 = types.InlineKeyboardButton(text='Logo va Compress qilish', callback_data=f"tologo")
	await message.reply("Videoni nima qilmoqchisiz", reply_markup=keyboard.add(b1,b2).add(b3))

async def audio_(message: types.Message):
	folder = f"download/vid{str(message.from_user.id)}"
	await message.reply("YUKLANMOQDA...")
	video = message.video
	file_name = f'{folder}/{video.file_unique_id}.mp4'
	output = f'{folder}/{video.file_unique_id}.mp3'
	await video.download(file_name)
	await bot.send_message(message.from_user.id, "Tayyorlanmoqda...")
	await bot.send_audio(message.from_user.id, open(write.toaudio(file_name, output), 'rb'), "✅ Tayyor", performer = "UzbProMax", title = "Media Tools")
	os.remove(file_name)
	os.remove(output)

async def text_(message: types.Message, call):
    try:
        folder = f"download/vid{str(message.from_user.id)}"
        file_name = f'{folder}/{str(random.randint(1,9999))}.mp4'
        down_name = f'{folder}/{str(random.randint(1, 9999))}.mp4'
        dow_name = f'{folder}/{str(random.randint(1, 9999))}.mp4'
        video = message.video
        await video.download(file_name)
        await write.totext(file_name, "@VodiyBozor", 100,  dow_name)
        await bot.send_video(message.from_user.id, open(dow_name, 'rb'))
        await compres.compress_video(dow_name, down_name, int(video.file_size)//1024//3)
        await bot.send_video(message.from_user.id, open(down_name, 'rb'))
        os.remove(file_name)
        os.remove(down_name)
        os.remove(dow_name)
    except:
        await bot.answer_callback_query(call.id, "Bu bo'lim tamirda...", True)
      

async def video_(message: types.Message):
	folder = f"download/vid{str(message.from_user.id)}"
	if not (os.path.isdir(folder)):
		os.mkdir(folder)
	video = message.video
	await message.reply("YUKLANMOQDA...")
	file_name = f'{folder}/{str(random.randint(1,9999))}.mp4'
	await video.download(file_name)
	keyboard = types.InlineKeyboardMarkup()
	b1 = types.InlineKeyboardButton(text='↖️', callback_data=f"k//{file_name}//left,top//{str(video.file_size)}")
	b2 = types.InlineKeyboardButton(text='⬆️️', callback_data=f"k//{file_name}//top//{str(video.file_size)}")
	b3 = types.InlineKeyboardButton(text='↗️', callback_data=f"k//{file_name}//right,top//{str(video.file_size)}")
	b4 = types.InlineKeyboardButton(text='⬅️️', callback_data=f"k//{file_name}//left//{str(video.file_size)}")
	b5 = types.InlineKeyboardButton(text='⏺', callback_data=f"k//{file_name}//center//{str(video.file_size)}")
	b6 = types.InlineKeyboardButton(text='➡️', callback_data=f"k//{file_name}//right//{str(video.file_size)}")
	b7 = types.InlineKeyboardButton(text='↙️', callback_data=f"k//{file_name}//left,bottom//{str(video.file_size)}")
	b8 = types.InlineKeyboardButton(text='⬇️', callback_data=f"k//{file_name}//bottom//{str(video.file_size)}")
	b9 = types.InlineKeyboardButton(text='↘️', callback_data=f"k//{file_name}//right,bottom//{str(video.file_size)}")
	await message.reply("YUKLANDI LOGO QAYSI TOMONDA CHIQSIN", reply_markup=keyboard.add(b1,b2,b3).add(b4,b5,b6).add(b7,b8,b9))

@dp.callback_query_handler()
async def menu(call: types.CallbackQuery):
	print(call.data)
	if call.data == "toaudio":
		await audio_(mess[call.from_user.id])
	elif call.data == "tologo":
		await video_(mess[call.from_user.id])
	elif call.data == "totext":
		await text_(mess[call.from_user.id], call)
	b = call.data.split("//")
	if b[0] == "k":
		keyboard = types.InlineKeyboardMarkup()
		b1 = types.InlineKeyboardButton(text=f'{compres.convert_size(int(b[3]))}️', callback_data=f"m//{b[1]}//{b[2]}//{int(b[3])}")
		b2 = types.InlineKeyboardButton(text=f'{compres.convert_size(int(b[3]) // 1.5)}', callback_data=f"m//{b[1]}//{b[2]}//{int(int(b[3]) // 1.5)}")
		b3 = types.InlineKeyboardButton(text=f'{compres.convert_size(int(b[3]) // 2)}️', callback_data=f"m//{b[1]}//{b[2]}//{int(int(b[3]) // 2)}")
		b4 = types.InlineKeyboardButton(text=f'{compres.convert_size(int(b[3]) // 2.5)}', callback_data=f"m//{b[1]}//{b[2]}//{int(int(b[3]) // 2.5)}")
		b5 = types.InlineKeyboardButton(text=f'{compres.convert_size(int(b[3]) // 3)}', callback_data=f"m//{b[1]}//{b[2]}//{int(int(b[3]) // 3)}")
		b6 = types.InlineKeyboardButton(text=f'{compres.convert_size(int(b[3]) // 3.5)}', callback_data=f"m//{b[1]}//{b[2]}//{int(int(b[3]) // 3.5)}")
		b7 = types.InlineKeyboardButton(text=f'{compres.convert_size(int(b[3]) // 4)}', callback_data=f"m//{b[1]}//{b[2]}//{int(int(b[3]) // 4)}")
		b8 = types.InlineKeyboardButton(text=f'{compres.convert_size(int(b[3]) // 4.5)}', callback_data=f"m//{b[1]}//{b[2]}//{int(int(b[3]) // 4.5)}")
		b9 = types.InlineKeyboardButton(text=f'{compres.convert_size(int(b[3]) // 5)}', callback_data=f"m//{b[1]}//{b[2]}//{int(int(b[3]) // 5)}")
		await bot.edit_message_text("Hajm tanlang",call.message.chat.id, call.message.message_id, reply_markup=keyboard.add(b1,b2,b3).add(b4,b5,b6).add(b7,b8,b9))

	elif b[0] == "m":
		await bot.edit_message_text("...", call.message.chat.id, call.message.message_id)
		folder = f"download/vid{str(call.from_user.id)}"

		filename = b[1]
		pos = tuple(map(str, b[2].split(',')))
		if len(pos) == 1:
			pos = b[2]

		down_name = f'{folder}/{str(random.randint(1, 9999))}.mp4'
		dow_name = f'{folder}/{str(random.randint(1, 9999))}.mp4'
		print(int(b[3]))
		print(int(b[3])//1024)
		await bot.edit_message_text("EDIT BOSHLANDI",call.message.chat.id, call.message.message_id)
		await write.tologo(b[1], pos, dow_name)
		await bot.send_video(call.from_user.id, open(dow_name, 'rb'), caption="ORGINAL !!! FAQAT LOGO QO'YILDI \nCOMPRES HOZIR TAYYORLANMOQDA...")
		try:
			fn = await compres.compress_video(dow_name, int(b[3])//1024, int(open("quality.txt", "r").read()))
			await bot.send_message(call.from_user.id, fn)
			await bot.send_video(call.from_user.id, open(fn, 'rb'),caption="✅ Tayyor")
			os.system(f"rm -rf {folder}")
		except:
			await bot.send_message(call.from_user.id, "Video sifati juda pas bo'lib ketdi! Qayta urinib yuqoriroq hajm tanlang!")

async def logo(message: types.Message):
    await message.reply("Logo uchun logo rasmini document korinishida yuboring")
    step[message.from_user.id] = "logo"

async def doc_handler(message: types.Message):
	if step[message.from_user.id] == "logo":
		await message.document.download("logo.png")
		await message.reply("✅ Yuklandi")
		step[message.from_user.id] = None
    
async def logosize(message: types.Message):
    await message.reply("Logo videoni necha bo'lagida chiqsin! Video o'lchamini siz kiritgan songa bo'lib shu o'lcham logoga beriladi\nO'rtacha: 15\nKichrayib boradi (son) > 15 < (son) Kattalashib boradi")
    step[message.from_user.id] = "logo"
    
async def quality(message: types.Message):
	await message.reply("Video sifatini tanlang\n\n0 - Yuqori sifat lekin xajm avtomatik beriladi yana xajmni ozaytirish uchun videoni qayta yuboring\n1 - Past sifat lekin xajm tanlanadi\n\nHozir tanlangan: {}".format(open("quality.txt", "r").read()))
	step[message.from_user.id] = "quality"

async def stepp(message: types.Message):
	tx = message.text
	if not message.from_user.id in step: step[message.from_user.id] = None

	if step[message.from_user.id] == 'logo':
		if tx.isdigit():
			await message.reply("✅ Kiritildi")
			open("logosize.txt", "w+").write(tx)
			step[message.from_user.id] = None
	elif step[message.from_user.id] == 'quality':
		if tx.isdigit() and (tx == '0' or tx == '1'):
			await message.reply("✅ Kiritildi")
			open("quality.txt", "w+").write(tx)
			step[message.from_user.id] = None
    

dp.register_message_handler(photo_handler, content_types=['photo'])
dp.register_message_handler(video_handler, content_types=['video'])
dp.register_message_handler(voice_handler, content_types=['voice'])
dp.register_message_handler(audio_handler, content_types=['audio'])
dp.register_message_handler(doc_handler, content_types=['document'])
dp.register_message_handler(start, commands=['start'])
dp.register_message_handler(coll, commands=['collage'])
dp.register_message_handler(vid, commands=['vid'])
dp.register_message_handler(clean, commands=['clean'])
dp.register_message_handler(logo, commands=['logo'])
dp.register_message_handler(logosize, commands=['logosize'])
dp.register_message_handler(quality, commands=['quality'])
dp.register_message_handler(stepp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

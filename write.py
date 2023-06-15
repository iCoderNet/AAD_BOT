from moviepy.editor import *

async def tologo(video, pos, adress):
        video=VideoFileClip(video)
        clip = video
        x, y = clip.size
        if x < 200:
                d = 1
        elif x < 300:
                d = 0.9
        elif x < 400:
                d = 0.8
        elif x < 600:
                d = 0.7
        elif x < 800:
                d = 0.6
        elif x < 1000:
                d = 0.5
        elif x < 1600:
                d = 0.4
        else:
                d = 0.3
        print(x, y , d)
        logosize = int(open("logosize.txt", 'r+').read())
        logo=(ImageClip('logo.png')
                .set_duration(video.duration)
                .resize(height=(x+y)/logosize)
                .margin(right=10, top=10, left=10, bottom=10, opacity=0)
                .set_pos(pos))
        final=CompositeVideoClip([video.resize(d), logo])
        final.write_videofile(adress)
        return adress

async def totext(video, tx, size, adress):
        clip = VideoFileClip(video)
        clip = clip.subclip(0, 5)
        clip = clip.volumex(0.5)
        txt_clip = TextClip(tx, fontsize=size, color='grey')
        txt_clip = txt_clip.set_pos('center').set_duration(5)
        video = CompositeVideoClip([clip, txt_clip])
        video.subclip(0).resize(0.5).write_videofile(adress)
        return True

def toaudio(input, output):
    clip = VideoFileClip(input)
    clip.audio.write_audiofile(output)
    return output
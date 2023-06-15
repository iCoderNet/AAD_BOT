import math
import os, ffmpeg

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
   
# async def compress_video(video_full_path, output_file_name, target_size):
#     # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
#     min_audio_bitrate = 32000
#     max_audio_bitrate = 256000
#     probe = ffmpeg.probe(video_full_path)
#     # Video duration, in s.
#     duration = float(probe['format']['duration'])
#     # Audio bitrate, in bps.
#     audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
#     print(audio_bitrate)
#     # Target total bitrate, in bps.
#     target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)
#     # Target audio bitrate, in bps
#     if 10 * audio_bitrate > target_total_bitrate:
#         audio_bitrate = target_total_bitrate / 10
#         if audio_bitrate < min_audio_bitrate < target_total_bitrate:
#             audio_bitrate = min_audio_bitrate
#         elif audio_bitrate > max_audio_bitrate:
#             audio_bitrate = max_audio_bitrate
#     # Target video bitrate, in bps.
#     video_bitrate = target_total_bitrate - audio_bitrate
#     print(audio_bitrate)
#     i = ffmpeg.input(video_full_path)
#     ffmpeg.output(i, os.devnull,
#                   **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
#                   ).overwrite_output().run()
#     ffmpeg.output(i, output_file_name,
#                   **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}
#                   ).overwrite_output().run()


def sized(w, h, basewidth):
    basewidth = int(basewidth)
    wsize = int(basewidth/w*h)
    return (basewidth,wsize)

async def compress_video(video_full_path, size_upper_bound, sc=0, two_pass=True, filename_suffix='VBMEDIA'):
    """
    Compress video file to max-supported size.
    :param video_full_path: the video you want to compress.
    :param size_upper_bound: Max video size in KB.
    :param two_pass: Set to True to enable two-pass calculation.
    :param filename_suffix: Add a suffix for new video.
    :return: out_put_name or error
    """
    sc += 1
    filename, extension = os.path.splitext(video_full_path)
    extension = '.mp4'
    output_file_name = filename + filename_suffix + extension

    total_bitrate_lower_bound = 11000
    min_audio_bitrate = 50000
    max_audio_bitrate = 300000
    min_video_bitrate = 100000

    try:
        # Bitrate reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
        probe = ffmpeg.probe(video_full_path)
        # Video duration, in s.
        duration = float(probe['format']['duration'])
        # Audio bitrate, in bps.
        audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
        
        # Target total bitrate, in bps.
        target_total_bitrate = (size_upper_bound * 1024 * 8) / (1.073741824 * duration)
        if target_total_bitrate < total_bitrate_lower_bound:
            return ('Bitrate is extremely low! Stop compress!')
            # return False

        # Best min size, in kB.
        best_min_size = (min_audio_bitrate + min_video_bitrate) * (1.073741824 * duration) / (8 * 1024)
        if size_upper_bound < best_min_size:
            return ('Quality not good! Recommended minimum size:', '{:,}'.format(int(best_min_size)), 'KB.')
            # return False

        # Target audio bitrate, in bps.
        audio_bitrate = audio_bitrate

        # target audio bitrate, in bps
        if 10 * audio_bitrate > target_total_bitrate:
            audio_bitrate = target_total_bitrate / 10
            if audio_bitrate < min_audio_bitrate < target_total_bitrate:
                audio_bitrate = min_audio_bitrate
            elif audio_bitrate > max_audio_bitrate:
                audio_bitrate = max_audio_bitrate

        # Target video bitrate, in bps.
        if sc == 2:
            video_bitrate = target_total_bitrate - audio_bitrate
        else:
            video_bitrate = float(next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)['bit_rate'])
        if video_bitrate < 1000:
            return ('Bitrate {} is extremely low! Stop compress.'.format(video_bitrate))
            # return False


        i = ffmpeg.input(video_full_path)
        if two_pass:
            ffmpeg.output(i, os.devnull,
                          **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
                          ).overwrite_output().run()
            ffmpeg.output(i, output_file_name,
                          **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}
                          ).overwrite_output().run()
        else:
            ffmpeg.output(i, output_file_name,
                          **{'c:v': 'libx264', 'b:v': video_bitrate, 'c:a': 'aac', 'b:a': audio_bitrate}
                          ).overwrite_output().run()

        if os.path.getsize(output_file_name) <= size_upper_bound * 1024:
            return output_file_name
        elif os.path.getsize(output_file_name) < os.path.getsize(video_full_path):  # Do it again
            if sc >= 3:
                return output_file_name
            return await compress_video(output_file_name, size_upper_bound, sc)
        else:
            return output_file_name
    except FileNotFoundError as e:
        print('You do not have ffmpeg installed!', e)
        print('You can install ffmpeg by reading https://github.com/kkroening/ffmpeg-python/issues/251')
        return False

if __name__ == "__main__":
    from write import tologo
    a = tologo("/home/uzbpromax/Downloads/yt1s.com - User Profile With One To One Relationship  Django 30 Crash Course Tutorials pt 16_1080p.mp4", ('left','top'), '/home/uzbpromax/Downloads/90-600000.mp4')
    compress_video(a, int(input('>')))
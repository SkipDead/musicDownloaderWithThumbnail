import eyed3
from eyed3.id3.frames import ImageFrame
import youtube_dl
from croppingimage import getYtThumbnail
import logging
eyed3.log.setLevel(logging.DEBUG)


def download_ytvid_as_mp3():
    video_url = input("enter url of youtube video:")
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))
    return filename, video_url


def addpicture(mp3filename, imgfilename):
    audiofile = eyed3.load(mp3filename)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(imgfilename,'rb').read(), 'image/jpeg')
    audiofile.tag.title = title[:-4]
    audiofile.tag.album = title[:-4]
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
    print(audiofile.tag.title)

def main():
    mp3filename, video_url = download_ytvid_as_mp3()
    print(f'finished downloaded{mp3filename}. Getting the thumbnail...')
    imgfilename = getYtThumbnail(video_url)
    addpicture(mp3filename,imgfilename)

if __name__ == "__main__":
    main()
from pytube import YouTube
from random import randint
import os, shutil
from log import log
from requests import get
import pyAesCrypt
from os import stat, remove, rename
from urllib.parse import urlparse

class utils:
    def youtube_video(url):
        folder = str(os.getcwd() + "\\aero-data\\file-sandbox\\")
        yt = YouTube(
            str(url)
            ).streams.first()
        yt.download(
            output_path=str(
                folder
                )
            )
        found_file = str()
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)

            if yt.title.split()[0] in filename:
                found_file = file_path
                
        if len(found_file) < 1:
            found_file = None
        return found_file   


    def youtube_to_mp3(url):
        folder = str(os.getcwd() + "\\aero-data\\file-sandbox\\")
        yt = YouTube(str(url))
        this = yt.streams.filter(
            only_audio=True
            ).all()
        this[0].download(
            output_path=str(
                folder
                )
            )
        found_file = str()
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            
            if yt.title.split()[0] in filename:
                found_file = file_path
                
        if len(found_file) < 1:
            found_file = None
        return found_file                   

    def download_image(url):
#        check_blob = url.split('.')
#        if "png" in check_blob:
#            ext = '.png'
#        if "jpg" in check_blob:
#            ext = '.jpg'
#        if "jpeg" in check_blob:
#            ext = '.jpeg'
#        if "jfiff" in check_blob:
#            ext = '.jfiff'
#        if "webp" in check_blob:
#            ext = '.jpeg'
#        if "tiff" in check_blob:
#            ext = '.tiff'
#        if "exif" in check_blob:
#            ext = '.exif'         
        fname = str("aero-data/img/"+str(randint(1111, 9999))+".png")
        with open(fname, 'wb') as handle:
            response = get(url, stream=True)
            if not response.ok:
                log.log("Failed To Download Image\nResponse:"+str(response))
                fname = None
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        return fname
    
    def download_file(url):
        a = urlparse(url)
        original = str(os.path.basename(a.path))   
        with open(original, 'wb') as handle:
            
            response = get(url, stream=True, allow_redirects = True)
            
            if not response.ok:
                print("[x] - Failed To Download File\nResponse:"+str(response))
                fname = None
                
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
            fname = original    
                
        return fname

    def encrypt_file(url, password):
     
        cont = True
        try:
            original = utils.download_file(url)
        except Exception as error:
            print(error)
            cont = False
            this = None
            
        if cont == True:
            encFileName = f"{original}.aes"
            NonencFileSize = stat(original).st_size
            with open(original, "rb") as fIn:
                with open(encFileName, "wb") as fOut:
                    pyAesCrypt.encryptStream(fIn, fOut, str(password), 64 * 1024)

            encFileSize = stat(encFileName).st_size
            this = {}
            this['fname'] = encFileName
            this['non_encrypted_size'] = NonencFileSize
            this['encrypted_size'] = encFileSize
            this['password'] = str(password)
        return this    
            
    def decrypt_file(url, password):
        cont = True
        original = utils.download_file(url)
        original_fsize = stat(original).st_size
        with open(original, "rb") as fIn:
            try:
                decrypted = original.replace(".aes","")
                with open(decrypted, "wb") as fOut:
                    pyAesCrypt.decryptStream(fIn, fOut, str(password), 64 * 1024, stat(original).st_size)    
                
            except Exception as error:
                print(error)
                decrypted = None
                cont = False
        if cont == True:
            this = {}
            this['fname'] = decrypted
            this['non_encrypted_size'] = stat(decrypted).st_size
            this['encrypted_size'] = original_fsize
            this['password'] = str(password)
        remove(original)
        return this
            
def get_file_info(url):
    fname = utils.download_file(url)
    file = stat(fname)
    remove(fname)
    return file
    #(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
    


# decrypt

            
            
                

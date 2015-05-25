import bs4

#--Steps--
#seach for "#autobackup"
#scroll down to very end of page (keep pressed end key untill no more loading pics/vids)
#save the page
#open saved html page with line below:

html = open("Photos - Google+.htm","r").read()
soup = bs4.BeautifulSoup(html)

#finding tags like:
#<img src="./Photos%20-%20Google+_files/IMG_20141004_183253.jpg" class="Bea VLb"
tags = soup.find_all("img","Bea VLb")
print("mined results from google+")
googleplus_media = []
for tag in tags:
    googleplus_media.append(tag["src"].split("/")[-1])

#print(len(media))

from subprocess import check_output,call
files_android = str(check_output(["adb", "shell","ls","/sdcard/DCIM/Camera"])).split("\\r\\r\\n")
#print(files_android)

for file in files_android:
    if(file in googleplus_media):
        #print(file)
        call(["adb", "shell","mv","/sdcard/DCIM/Camera/"+file,"/sdcard/SAFE-DELETE"])
       
        


"""
photos that can be deleted:
    exist on both lists

"""
print("DOPE! you can now delete the folder on yo sdcard called SAFE-DELTE to free up the phone of the backuped media")
print("If you have broken gallery thumbnails, deleting /data/data/com.androids.providers.media/databases/external.db may solve the problem (not internal.db)")

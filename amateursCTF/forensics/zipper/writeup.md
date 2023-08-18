We are given a zip file with a lot of txt files. First, using exiftool and we can see the first part and the third part of the flag:

<img src= https://github.com/dxisdh/CTF-WU/blob/main/amateursCTF/forensics/zipper/1.png>

Part 1: amateursCTF{z1PP3d_

Part 3: laY3r_0f

Next, we will check the info of the zip by using the zipinfo command: 

<img src= https://github.com/dxisdh/CTF-WU/blob/main/amateursCTF/forensics/zipper/2.png>

So, there are two directories with the same name, and the second one has 17 bytes in it. If we unzip it manually, one of the directories will be overwritten, to avoid it, we will write a Python program to extract it:

````
import zipfile
zfile = zipfile.ZipFile('flag.zip', 'r')

namelist = zfile.namelist()
for name in namelist:
    info = zfile.getinfo(name)
    if info.comment:
        print(name, zfile.read(name))
````

Run it and we will get the second part of the flag: 

<img src= https://github.com/dxisdh/CTF-WU/blob/main/amateursCTF/forensics/zipper/3.png>

And for the last part, open the zip file, we will find that two files with the same name:

<img src= https://github.com/dxisdh/CTF-WU/blob/main/amateursCTF/forensics/zipper/4.png>

Don't overwrite it and we will find the last part:

<img src= https://github.com/dxisdh/CTF-WU/blob/main/amateursCTF/forensics/zipper/5.png>

Flag: `amateursCTF{z1PP3d_in5id3_4_laY3r_0f_Zips}`

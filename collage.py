# # import numpy
# # from PIL import Image

# # image1=Image.open('image.jpg')
# # image2=Image.open('image1.jpg')
# # image3=Image.open('image2.jpg')
# # image4=Image.open('image3.jpg')

# # arrayimage1=numpy.array(image1)
# # arrayimage2=numpy.array(image2)
# # arrayimage3=numpy.array(image3)
# # arrayimage4=numpy.array(image4)

# # h1=numpy.hstack((arrayimage1,arrayimage2))
# # h2=numpy.hstack((arrayimage3,arrayimage4))

# # arrayImageFinal=numpy.vstack((h1,h2))

# # finalImage=Image.fromarray(arrayImageFinal)

# # finalImage.save(file_name)

# from PIL import Image, ImageEnhance
# import os, numpy

# def centersize(i , o, p, l):
#     if i > p:
#         i = (i - p) 
#     else:
#         i = 0
#     if o > l:
#         o = (o - l)
#     else:
#         o = 0

#     return (i, o, p, l)

# def Average(lst):
#     return sum(lst) / len(lst)

# def di(mydict, findex):
#     for index, key in enumerate(mydict.keys()):
#         print(index, key)
#         if index == findex-1:
#             return key
#     return None  # the key doesn't exist

# def dl(mydict):
#     h = []
#     for i in mydict:
#         h.append(i)
#     return h

# def imgcollage(folder):
#     imgs = {}
#     images = os.listdir(folder)
#     simg = len(images)
#     for f in images:
#         imgs[f] = Image.open(f"{folder}/{f}", 'r').size
#     print(imgs)
#     kk = {k: v for k, v in sorted(imgs.items(), key=lambda item: item[1])}
#     print(kk)
#     r, t ={}, {}
#     if simg == 2:
#         wort, hort, i, p, s  = [], [], 0, 0, 0
#         wort = int(min([ kk[di(kk, qq)][0] for qq in range(1, 3)]))
#         for j in images:
#             i+=1
#             ht = int(min([kk[di(kk, 1)][1], kk[di(kk, 2)][1]]))
#             if i == 2:
#                 p += 1
#                 s += 1
#                 print()
#                 # wt = int(Average([kk[di(kk, i)][0], kk[di(kk, i-1)][0]]))
#                 # ht = int(Average([kk[di(kk, i)][1], kk[di(kk, i-1)][1]]))
#                 # print(wt, wort)
#                 # print(ht, hort)
#                 im = Image.open(f'{folder}/{j}')
#                 w, h = im.size
#                 f = (0, 0, wort, ht)
#                 nn=numpy.array(im.crop(f))
#                 t[p]=numpy.hstack((nn,r[1]))
#                 # print(t)
#                 i = 0
#             else:
#                 im = Image.open(f'{folder}/{j}')
#                 f = (0, 0, wort, ht)
#                 r[i]=numpy.array(im.crop(f) )
#         print()
#         finalImage=Image.fromarray(t[1])
#         finalImage.save(file_name)
#     elif simg == 4:
#         wort, hort, i, p, s, ja  = [], [], 0, 0, 0, 0
#         wort = int(min([ kk[di(kk, qq)][0] for qq in range(1, 5)]))
#         for j in images:
#             i+=1
#             if ja < 2:
#                 ht = int(min([kk[di(kk, 1)][1], kk[di(kk, 2)][1]]))
#             elif ja < 4:
#                 ht = int(min([kk[di(kk, 3)][1], kk[di(kk, 4)][1]]))
#             if i == 2:
#                 p += 1
#                 s += 1
#                 print()
#                 # wt = int(Average([kk[di(kk, s)][0], kk[di(kk, s)][0]]))
#                 # ht = int(Average([kk[di(kk, s)][1], kk[di(kk, s)][1]]))
#                 # print(wt, wort)
#                 # print(ht, hort)
#                 f = (0, 0, wort, ht)
#                 nn=numpy.array(Image.open(f'{folder}/{j}').crop(f))
#                 t[p]=numpy.hstack((nn,r[1]))
#                 # print(t)
#                 i = 0
#             else:
#                 f = (0, 0, wort, ht)
#                 r[i]=numpy.array(Image.open(f'{folder}/{j}').crop(f) )
#         print()
#         arrayImageFinal=numpy.vstack((t[1],t[2]))
#         finalImage=Image.fromarray(arrayImageFinal)
#         finalImage.save(file_name)
#     elif simg == 6:
#         wort, hort, i, p, s, ja  = [], [], 0, 0, 0, 0
#         wort = int(min([ kk[di(kk, qq)][0] for qq in range(1, 7)]))
#         for j in images:
#             i+=1
#             ja += 1
#             if ja < 3:
#                 ht = int(min([kk[di(kk, 1)][1], kk[di(kk, 2)][1], kk[di(kk, 3)][1]]))
#             elif ja < 6:
#                 ht = int(min([kk[di(kk, 4)][1], kk[di(kk, 5)][1], kk[di(kk, 6)][1]]))
#             if i == 3:
#                 p += 1
#                 s += 1
#                 print()
#                 # wt = int(Average([kk[di(kk, s)][0], kk[di(kk, s)][0]]))
#                 # ht = int(Average([kk[di(kk, s)][1], kk[di(kk, s)][1]]))
#                 # print(wt, wort)
#                 # print(ht, hort)
#                 f = (0, 0, wort, ht)
#                 nn=numpy.array(Image.open(f'{folder}/{j}').crop(f))
#                 t[p]=numpy.hstack((nn,r[2],r[1]))
#                 # print(t)
#                 i = 0
#             else:
#                 f = (0, 0, wort, ht)
#                 r[i]=numpy.array(Image.open(f'{folder}/{j}').crop(f) )
#         print(p)
#         arrayImageFinal=numpy.vstack((t[1],t[2]))
#         finalImage=Image.fromarray(arrayImageFinal)
#         finalImage.save(file_name)
#     elif simg == 8:
#         wort, hort, i, p, s, ja  = [], [], 0, 0, 0, 0
#         wort = int(min([ kk[di(kk, qq)][0] for qq in range(1, 9)]))
#         for j in images:
#             i+=1
#             ja += 1
#             print(i)
#             if ja < 4:
#                 ht = int(min([kk[di(kk, 1)][1], kk[di(kk, 2)][1], kk[di(kk, 3)][1], kk[di(kk, 4)][1]]))
#             elif ja < 8:
#                 ht = int(min([kk[di(kk, 5)][1], kk[di(kk, 6)][1], kk[di(kk, 7)][1], kk[di(kk, 8)][1]]))
#             if i == 4:
#                 p += 1
#                 s += 1
#                 print()
#                 f = (0, 0, wort, ht)
#                 nn=numpy.array(Image.open(f'{folder}/{j}').crop(f))
#                 t[p]=numpy.hstack((nn,r[3],r[2],r[1]))
#                 # print(t)
#                 i = 0
#             else:
#                 f = (0, 0, wort, ht)
#                 r[i]=numpy.array(Image.open(f'{folder}/{j}').crop(f) )
#         print(p)
#         arrayImageFinal=numpy.vstack((t[1],t[2]))
#         finalImage=Image.fromarray(arrayImageFinal)
#         finalImage.save(file_name)
#     elif simg == 9:
#         wort, hort, i, p, s, ja, uu  = [], [], 0, 0, 0, 0, None
#         wort = int(min([ kk[di(kk, qq)][0] for qq in range(1, 10)]))
#         for j in images:
#             i+=1
#             ja += 1
#             print(i)
#             if ja < 3:
#                 ht = int(min([kk[di(kk, 1)][1], kk[di(kk, 2)][1], kk[di(kk, 3)][1]]))
#             elif ja < 6:
#                 ht = int(min([kk[di(kk, 4)][1], kk[di(kk, 5)][1], kk[di(kk, 6)][1]]))
#             elif ja < 9:
#                 ht = int(min([kk[di(kk, 7)][1], kk[di(kk, 8)][1], kk[di(kk, 9)][1]]))
#             if i == 3:
#                 p += 1
#                 s += 1
#                 print()
#                 # wt = int(Average([kk[di(kk, s)][0], kk[di(kk, s)][0]]))
#                 # print(wt, wort)
#                 # print(ht, hort)
#                 im = Image.open(f'{folder}/{j}')
#                 f = (0, 0, im.size[0], ht)
#                 nn=numpy.array(im.crop(f))
#                 if uu == None:
#                     t[p]=Image.fromarray(numpy.hstack((nn,r[2],r[1])))
#                     uu = t[p].size
#                 else:
#                     t[p]=Image.fromarray(numpy.hstack((nn,r[2],r[1]))).crop((0,0,uu[0], uu[1]))
#                 i = 0
#             else:
#                 im = Image.open(f'{folder}/{j}')
#                 f = (0, 0, im.size[0], ht)
#                 r[i]=numpy.array(im.crop(f))
                
#         print(p)
#         arrayImageFinal=numpy.vstack((t[1],t[2],t[3]))
#         finalImage=Image.fromarray(arrayImageFinal)
#         finalImage.save(file_name)


# imgcollage("./download/2125481502/")

from PIL import Image
import os, numpy, random

def hsized(img, basewidth):
    wsize = int(basewidth/img.size[1]*img.size[0])
    img = img.resize((wsize, basewidth), Image.ANTIALIAS)
    return img

def wsized(img, basewidth):
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    return img

def corner(img):
    line = Image.new("RGB", (img.size[0],10), (255,255,255))
    image = numpy.vstack((line,img,line))
    img = Image.fromarray(image)
    lineh = Image.new("RGB", (10,img.size[1]), (255,255,255))
    image = numpy.hstack((lineh,img,lineh))
    finalImage=Image.fromarray(image)
    return finalImage

def imgcollage(folder, size=1024):
    file_name = f'{folder}/{str(random.randint(5000,9999))}.jpg'
    images = os.listdir(folder)
    print(images)
    ipp = [int(e.split('.')[0]) for e in images]
    print(ipp)
    images = [f"{e}.jpg" for e in sorted(ipp)]
    print(images)
    simg = len(images)
    i, s,p, r, t = 0, 0,0, {}, {}
    if simg == 1:
        for image in images:
            img = Image.open(f'{folder}/{image}')
            width, height = img.size
            sLogo = hsized(Image.open("logo.png"), int((width+height)/12))
            sLogoWidth, sLogoHeight = sLogo.size
            img.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
            img.save(file_name)
        
    elif simg == 2:
        for image in images:
            i += 1
            s += 1
            if s == 2:
                p+=1
                img = corner(Image.open(f'{folder}/{image}'))
                img1 = Image.fromarray(r[1])
                print(img.size)
                if int(img.size[0]) < int(img.size[1]) or int(img1.size[0]) < int(img1.size[1]):
                    img = hsized(img, size)
                    img1 = hsized(Image.fromarray(r[1]), size)
                    t[p] = Image.fromarray(numpy.hstack((img1, img)))
                else:
                    img = wsized(img, size)
                    img1 = wsized(img1, size)
                    t[p] = Image.fromarray(numpy.vstack((img,img1)))
                s = 0
            else:
                img = corner(Image.open(f'{folder}/{image}'))
                r[s] = numpy.array(img)
        width, height = t[1].size
        sLogo = hsized(Image.open("logo.png"), int((width+height)/15))
        sLogoWidth, sLogoHeight = sLogo.size
        t[1].paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
        t[1].save(file_name)

    elif simg == 3:
        for image in images:
            i += 1
            s += 1
            print(i)
            if s == 2:
                p+=1
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                t[p] = Image.fromarray(numpy.hstack((r[1], img)))
                s = 0
            else:
                if i == 3:
                    p += 1
                    img = corner(Image.open(f'{folder}/{image}'))
                    t[p] = hsized(img, size)
                else:
                    img = corner(Image.open(f'{folder}/{image}'))
                    img = hsized(img, size)
                    r[s] = numpy.array(img)
        wmax = max( [t[qq].size[0] for qq in range(1,3)] )
        print(wmax)
        arrayImageFinal=numpy.vstack(( wsized(t[1], wmax), wsized(t[2], wmax) ))
        finalImage=Image.fromarray(arrayImageFinal)
        width, height = finalImage.size
        sLogo = hsized(Image.open("logo.png"), int((width+height)/16))
        width, height = finalImage.size
        sLogoWidth, sLogoHeight = sLogo.size
        finalImage.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
        finalImage.save(file_name)

    elif simg == 4:
        for image in images:
            i += 1
            s += 1
            print(image)
            if s == 2:
                p+=1
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                t[p] = Image.fromarray(numpy.hstack((r[1], img)))
                s = 0
            else:
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                r[s] = numpy.array(img)
        wmax = max( [t[qq].size[0] for qq in range(1,3)] )
        print(wmax)
        arrayImageFinal=numpy.vstack(( wsized(t[1], wmax), wsized(t[2], wmax) ))
        finalImage=Image.fromarray(arrayImageFinal)
        width, height = finalImage.size
        sLogo = hsized(Image.open("logo.png"), int((width+height)/16))
        width, height = finalImage.size
        sLogoWidth, sLogoHeight = sLogo.size
        finalImage.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
        finalImage.save(file_name)

    elif simg == 5:
        for image in images:
            i += 1
            s += 1
            print(i)
            if s == 2:
                p+=1
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                t[p] = Image.fromarray(numpy.hstack((r[1], img)))
                s = 0
            else:
                if i == 5:
                    p += 1
                    img = corner(Image.open(f'{folder}/{image}'))
                    t[p] = hsized(img, size)
                else:
                    img = corner(Image.open(f'{folder}/{image}'))
                    img = hsized(img, size)
                    r[s] = numpy.array(img)
        wmax = max( [t[qq].size[0] for qq in range(1,3)] )
        print(wmax)
        arrayImageFinal=numpy.vstack(( wsized(t[1], wmax), wsized(t[2], wmax) ))
        arrayImageFinal=numpy.hstack((arrayImageFinal, hsized(t[3], Image.fromarray(arrayImageFinal).size[1])))
        finalImage=Image.fromarray(arrayImageFinal)
        width, height = finalImage.size
        sLogo = hsized(Image.open("logo.png"), int((width+height)/16))
        width, height = finalImage.size
        sLogoWidth, sLogoHeight = sLogo.size
        finalImage.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
        finalImage.save(file_name)

    elif simg == 6:
        for image in images:
            i += 1
            s += 1
            print(i)
            if s == 2:
                p+=1
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                t[p] = Image.fromarray(numpy.hstack((r[1], img)))
                s = 0
            else:
                if s == 3 and s == 6:
                    p+=1
                    t[p] = corner(Image.open(f'{folder}/{image}'))
                else:
                    img = corner(Image.open(f'{folder}/{image}'))
                    img = hsized(img, size)
                    r[s] = numpy.array(img)
        wmax = max( [t[qq].size[0] for qq in range(1,3)] )
        print(p)
        arrayImageFinal=numpy.vstack(( wsized(t[1], wmax), wsized(t[2], wmax), wsized(t[3], wmax) ))
        finalImage=Image.fromarray(arrayImageFinal)
        width, height = finalImage.size
        sLogo = hsized(Image.open("logo.png"), int((width+height)/16))
        width, height = finalImage.size
        sLogoWidth, sLogoHeight = sLogo.size
        finalImage.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
        finalImage.save(file_name)

    elif simg == 7:
        for image in images:
            i += 1
            s += 1
            print(i)
            if s == 3:
                p+=1
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                t[p] = Image.fromarray(numpy.hstack((r[2], r[1], img)))
                s = 0
            else:
                if i == 7:
                    p += 1
                    img = corner(Image.open(f'{folder}/{image}'))
                    t[p] = hsized(img, size)
                else:
                    img = corner(Image.open(f'{folder}/{image}'))
                    img = hsized(img, size)
                    r[s] = numpy.array(img)
        wmax = max( [t[qq].size[0] for qq in range(1,3)] )
        print(wmax)
        arrayImageFinal=numpy.vstack(( wsized(t[1], wmax), wsized(t[2], wmax)))
        arrayImageFinal=numpy.hstack((arrayImageFinal, hsized(t[3], Image.fromarray(arrayImageFinal).size[1])))
        finalImage=Image.fromarray(arrayImageFinal)
        width, height = finalImage.size
        sLogo = hsized(Image.open("logo.png"), int((width+height)/16))
        width, height = finalImage.size
        sLogoWidth, sLogoHeight = sLogo.size
        finalImage.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
        finalImage.save(file_name)


    elif simg == 8:
        for image in images:
            i += 1
            s += 1
            print(i)
            if s == 3:
                p+=1
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                t[p] = Image.fromarray(numpy.hstack((r[2],r[1], img)))
                s = 0
            else:
                if i == 8:
                    p += 1
                    img = corner(Image.open(f'{folder}/{image}'))
                    img = hsized(img, size)
                    t[p] = Image.fromarray(numpy.hstack((r[1], img)))
                else:
                    img = corner(Image.open(f'{folder}/{image}'))
                    img = hsized(img, size)
                    r[s] = numpy.array(img)
        wmax = max( [t[qq].size[0] for qq in range(1,4)] )
        print(wmax)
        arrayImageFinal=numpy.vstack(( wsized(t[1], wmax), wsized(t[2], wmax), wsized(t[3], wmax) ))
        finalImage=Image.fromarray(arrayImageFinal)
        width, height = finalImage.size
        sLogo = hsized(Image.open("logo.png"), int((width+height)/16))
        width, height = finalImage.size
        sLogoWidth, sLogoHeight = sLogo.size
        finalImage.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
        finalImage.save(file_name)

    elif simg == 9:
        for image in images:
            i += 1
            s += 1
            print(i)
            if s == 3:
                p+=1
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                t[p] = Image.fromarray(numpy.hstack((r[2],r[1],img)))
                s = 0
            else:
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                r[s] = numpy.array(img)
        wmax = max( [t[qq].size[0] for qq in range(1,4)] )
        print(wmax)
        arrayImageFinal=numpy.vstack(( wsized(t[1], wmax), wsized(t[2], wmax), wsized(t[3], wmax) ))
        finalImage=Image.fromarray(arrayImageFinal)
        width, height = finalImage.size
        sLogo = hsized(Image.open("logo.png"), int((width+height)/16))
        sLogoWidth, sLogoHeight = sLogo.size
        finalImage.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
        finalImage.save(file_name)

    elif simg >= 10:
        for image in images:
            i += 1
            s += 1
            print(i)
            if s == 4:
                p+=1
                img = corner(Image.open(f'{folder}/{image}'))
                img = hsized(img, size)
                t[p] = Image.fromarray(numpy.hstack((r[3],r[2],r[1], img)))
                s = 0
            else:
                if i == 10:
                    p += 1
                    img = corner(Image.open(f'{folder}/{image}'))
                    img = hsized(img, size)
                    t[p] = Image.fromarray(numpy.hstack((r[1], img)))
                else:
                    img = corner(Image.open(f'{folder}/{image}'))
                    img = hsized(img, size)
                    r[s] = numpy.array(img)
        wmax = max( [t[qq].size[0] for qq in range(1,3)] )
        print(wmax)
        arrayImageFinal=numpy.vstack(( wsized(t[1], wmax), wsized(t[2], wmax), wsized(t[3], wmax) ))
        finalImage=Image.fromarray(arrayImageFinal)
        width, height = finalImage.size
        sLogo = hsized(Image.open("logo.png"), int((width+height)/16))
        sLogoWidth, sLogoHeight = sLogo.size
        finalImage.paste(sLogo, (width - sLogoWidth, height - sLogoHeight), sLogo)
        finalImage.save(file_name)

    return file_name


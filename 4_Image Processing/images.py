from PIL import Image, ImageFilter

img=Image.open('Image Processing\Pokedex\pikachu.jpg')

#basic Operations
# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)


filtered_img=img.filter(ImageFilter.BLUR)
smooth_img=img.filter(ImageFilter.SMOOTH)
sharpen_img=img.filter(ImageFilter.SHARPEN)
gray_img=img.convert('L')
rotated_img=img.rotate(180)    
resize_img  =  img.resize((300,300))
box=(100,100,400,400)
crop_img=img.crop(box)

filtered_img.save("blur.png", 'png')
smooth_img.save("smooth.png",'png')
sharpen_img.save("Sharp.png",'png')
gray_img.save("gray.png",'png')
rotated_img.save("rotated.png",'png')
resize_img.save("recise.png",'png')
crop_img.save("crop.png",'png')
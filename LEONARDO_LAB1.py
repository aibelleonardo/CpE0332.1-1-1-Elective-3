from PIL import Image, ImageOps

img = Image.open('flower.jpg')

rotImg = img.rotate(45, expand = True)

flipImg = ImageOps.mirror(rotImg)

totWidth = img.width + rotImg.width + flipImg.width
totHeight = max(img.height, rotImg.height, flipImg.height)

newImg = Image.new('RGB', (totWidth, totHeight))

newImg.paste(img, (0, 0))
newImg.paste(rotImg, (img.width, 0))
newImg.paste(flipImg, (img.width + rotImg.width, 0))

newImg.show()
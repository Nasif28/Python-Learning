from PIL import Image
from PIL import ImageFilter

img = Image.open('_DSC0074-001.JPG')
print(img.size)
print(img.format)
img.show()

area = (200,300,600,1000)
cropped_img = img.crop(area)
cropped_img.show()

# img1 = Image.open('Love.jpg')
# area = (50, 50, 100, 100)
# img.paste(img1, area)
# img.show()

print(img.mode)
r, g, b = img.split()
r.show()
g.show()
b.show()

img2 = Image.merge('RGB', (r, g, b))
img2.show()

imgr = img2.resize((500, 500))
imgr.show()

imgr1 = img2.transpose(Image.FLIP_LEFT_RIGHT)
imgr2 = img2.transpose(Image.ROTATE_90)
imgr1.show()
imgr2.show()

img3 = Image.open('P_20170402_151303.jpg')
imgc = img3.convert('L')
imgc1 = img3.filter(ImageFilter.BLUR)
imgc2 = img3.filter(ImageFilter.DETAIL)
imgc3 = img3.filter(ImageFilter.FIND_EDGES)

img3.show()
imgc.show()
imgc1.show()
imgc2.show()
imgc3.show()


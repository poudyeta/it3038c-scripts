from PIL import Image, ImageEnhance

im = Image.open('car.png')

width = im.width
height = im.height

im1 = im.rotate(180, expand=True)


im2 = ImageEnhance.Color(im)
im2 = im2.enhance(0)

im3 = ImageEnhance.Sharpness(im)
im3 = im3.enhance(3)

im4 = im.transpose(Image.FLIP_LEFT_RIGHT)

combined_im = Image.new('RGB', (width * 2, height * 2))

# Paste the images onto the combined image
combined_im.paste(im1, (0, 0))
combined_im.paste(im2, (width, 0))
combined_im.paste(im3, (0, height))
combined_im.paste(im4, (width, height))
combined_im.show()
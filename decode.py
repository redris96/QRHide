from PIL import Image

im = Image.open('encoded.png')
pix = im.load()

for x in range(im.size[0]):
	for y in range(im.size[1]):
		if sum(pix[x,y])%2:
			pix[x,y] = (255, 255, 255)
		else:
			pix[x,y] = (0, 0, 0)

im.save('decoded.png')

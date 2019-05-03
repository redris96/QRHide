from PIL import Image

im = Image.open('toss.jpeg')
pix = im.load()
qr = Image.open('code.png')
qrp = qr.load()

for x in range(qr.size[0]):
	for y in range(qr.size[1]):
		pi = pix[x,y]
		change = False
		if qrp[x,y][0]:
			if sum(pi)%2:
				continue
			else:
				change = True
		else:
			if sum(pi)%2:
				change = True
			else:
				continue
		if change:
			pix[x,y] = (pi[0]-1, pi[1], pi[2])

im.save('encoded.png')

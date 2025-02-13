from rembg import remove
from PIL import Image

inp_p = 'cat.jpg'
out_p = 'outcat.png'
input = Image.open(inp_p)
output = remove(input)
output.save(out_p)
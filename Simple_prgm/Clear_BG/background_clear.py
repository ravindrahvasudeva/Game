<<<<<<< HEAD
from rembg import remove
from PIL import Image
input_path = 'bird.jpg'
output_path = 'output2.png'
input = Image.open(input_path)
output =remove(input)
=======
from rembg import remove
from PIL import Image
input_path = 'bird.jpg'
output_path = 'output2.png'
input = Image.open(input_path)
output =remove(input)
>>>>>>> a15de333f5cb5d803fb18660f02ece1595789616
output.save(output_path)
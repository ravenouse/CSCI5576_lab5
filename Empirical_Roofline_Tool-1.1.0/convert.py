import sys
import os
import os
from PIL import Image

def convert_to_png(input_path, output_path):
    img = Image.open(input_path)
    img.save(os.path.join(output_path,"roofline.png"), quality=95, subsampling=0)
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 convert.py input_path output_path")
        sys.exit(1)
    convert_to_png(sys.argv[1], sys.argv[2])

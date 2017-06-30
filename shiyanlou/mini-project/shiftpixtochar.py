from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def parse_char(r,g,b,alpha=256):
    """
        get dark value from r g b value
    """
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    index = int((gray/256)*(len(ascii_char)-1))
    return ascii_char[index]

if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('file')
    parse.add_argument('-o','--outfile',default='out.txt')
    parse.add_argument('--height',type=int,default=60)
    parse.add_argument('--width',type=int,default=80)
    args = parse.parse_args()
    filepath = args.file
    outfile = args.outfile
    height = args.height
    width = args.width
    file = Image.open(filepath)
    file = file.resize((width,height), Image.NEAREST)
    
    txt = ""
    for i in range(height):
        for j in range(width):
            char = parse_char(*file.getpixel((j,i)))
            txt += char 
        txt +=" \n"
        
    print(txt)
    
    if outfile:
        with open(outfile,'w') as out:
            out.write(txt)
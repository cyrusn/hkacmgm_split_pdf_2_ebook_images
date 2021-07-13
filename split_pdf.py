from pdf2image import convert_from_path
from os import mkdir, rmdir, path
import sys
import argparse


# Required argument for the path of the pdf file
# Create the parser
my_parser = argparse.ArgumentParser(
    description='Split PDF to jpgs for HKACMGM ebook')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to pdf')

# Execute the parse_args() method
args = my_parser.parse_args()

file_path = args.Path
if not path.isfile(file_path):
    print('The path specified does not exist')
    sys.exit()

dirname = path.dirname(file_path)
basename = path.basename(file_path)
filename, ext = path.splitext(basename)
output_folder = f"./{dirname}/{filename}"
mkdir(output_folder)
print(dirname, output_folder)

# split the pdf in to 3 different size as follow.
specs = [
    {'size': 71, 'dpi': 200, 'prefix': 'thumb'},
    {'size': 571, 'dpi': 300, 'prefix': ''},
    {'size': 2479, 'dpi': 300, 'prefix': 'large'},
]

for spec in specs:
    size = spec['size']
    prefix = spec['prefix']
    dpi = spec['dpi']
    images = convert_from_path(f'{file_path}', dpi, fmt="jpeg", size=(size, None))
    for (n, image) in enumerate(images):
        image.save(f'{output_folder}/{n+1}{ "" if prefix == "" else "-"}{prefix}.jpg')

print(f"{basename} is converted.")

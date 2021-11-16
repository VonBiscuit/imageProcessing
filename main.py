from PIL import Image
import sys
import os

def convert_png_to_jpg():
    folder_to_convert = sys.argv[1]
    folder_to_save =  sys.argv[2]

    if not os.path.exists(folder_to_save):
        os.mkdir(folder_to_save)
    for f in os.listdir(folder_to_convert):
        path_to_pokemon = folder_to_convert + "\\" + f
        img = Image.open(path_to_pokemon)
        pokemon_name = f[:-4]
        path_to_save = folder_to_save +'\\' + pokemon_name + '.png'
        img.save(path_to_save)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_png_to_jpg()

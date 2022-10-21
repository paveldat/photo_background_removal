"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░

▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""
from rembg import remove
from PIL import Image
from pathlib import Path
from art import tprint
from progress.bar import Bar


def remove_background():
    list_of_extensions = ['*.jpg', '*.png']
    all_images = []

    print('Getting list of all files')
    for ext in list_of_extensions:
        all_images.extend(Path('images/input/').glob(ext))

    with Bar('Removing background...', max=len(all_images)) as bar:
        for image_path in all_images:
            input_path = Path(image_path)
            image = input_path.stem

            output_path = f'images/output/{image}.png'

            input_img = Image.open(input_path)
            output_img = remove(input_img)
            output_img.save(output_path)
            bar.next()


def main():
    tprint('Remove background')
    remove_background()


if __name__ == '__main__':
    main()

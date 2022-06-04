"""
'White Shell' theme generator
"""
from argparse import ArgumentParser

from colour import Color


def invert_hex_rgb(hex_code: str) -> str:
    """
    Inverts the hex rgb color in telegram way

    :param hex_code: Input hex color to be inverted
    :return: HEX color in format '#rrggbbaa'
    """
    hex_alpha = ''
    hex_code = hex_code.replace('#', '')

    if len(hex_code) > 6:
        # Cut the alpha part
        hex_alpha = hex_code[6:]
        hex_code = hex_code[:6]

    color = Color('#' + hex_code)
    color.set_red(1.0 - color.get_red())
    color.set_green(1.0 - color.get_green())
    color.set_blue(1.0 - color.get_blue())

    return color.get_hex_l() + hex_alpha


# Invert desktop theme test
theme_plaintext_list = []

with open('../TDesktop/DarkShell.tdesktop-palette', 'rt') as theme_text_file, \
     open('result.tdesktop-palette', 'wt') as theme_output_file:  # TODO: Replace hardcoded with consts. Adapt to cli usage this shitpost code
    for line in theme_text_file:
        line_split = line.split(': ')

        if len(line_split) == 2:
            color_raw = line_split[1].rstrip().replace(';', '')
            if color_raw.startswith('#'):
                inverted_color = invert_hex_rgb(color_raw)
                line = '{}: {};\n'.format(line_split[0], inverted_color)

        theme_output_file.write(line)


""" if __name__ == '__main__':
    argparser = ArgumentParser(
        description='Inverted theme generator for Dark Shell'
    )
    argparser.add_argument('') """

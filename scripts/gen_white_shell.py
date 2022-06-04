"""
'White Shell' theme generator
"""
from pathlib import Path
from argparse import ArgumentParser

from colour import Color


PATH_PROJECT = Path(__file__).parent.parent
PATH_TDESKTOP = PATH_PROJECT / Path('TDesktop/DarkShell.tdesktop-palette')
PATH_MACOS = PATH_PROJECT / Path('macOS/DarkShell.palette')
PATH_ANDROID = PATH_PROJECT / Path('Android/DarkShell.attheme')
PATH_IOS = PATH_PROJECT / Path('iOS/DarkShell.tgios-theme')


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


def invert_desktop_theme():
    path_for_result = PATH_TDESKTOP.parent / 'WhiteShell.tdesktop-palette'

    with open(PATH_TDESKTOP, 'rt') as theme_text_file, \
         open(path_for_result, 'wt') as theme_output_file:
        for line in theme_text_file:
            line_split = line.split(': ')

            if len(line_split) == 2:
                color_raw = line_split[1].rstrip().replace(';', '')
                if color_raw.startswith('#'):
                    inverted_color = invert_hex_rgb(color_raw)
                    line = '{}: {};\n'.format(line_split[0], inverted_color)

            theme_output_file.write(line)

    print('⌂ Successfully generated theme for TDesktop client, saved to "{}"'
          .format(path_for_result))


if __name__ == '__main__':
    argparser = ArgumentParser(description='White Shell theme generator for Dark Shell')
    argparser.add_argument('client_variant', choices=['tdesktop', 'android', 'ios', 'macos'],
                           help='Select the client for which the theme is intended')

    args = argparser.parse_args()

    if args.client_variant == 'tdesktop':
        invert_desktop_theme()
    else:
        print('⌂ Not yet supported 😿')

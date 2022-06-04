from colour import Color


theme_plaintext_list = []

with open('../TDesktop/DarkShell.tdesktop-palette', 'rt') as theme_text_file, \
     open('result.tdesktop-palette', 'wt') as theme_output_file:
    for line in theme_text_file:
        line_split = line.split(': ')

        if len(line_split) == 2:
            color_raw = line_split[1]
            if color_raw.startswith('#'):
                color = Color(color_raw[-2])
                color.


        #theme_output_file.write(line)

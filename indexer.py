import re
import json
from urllib.parse import quote
from urllib.request import urlopen


DEVELOPMENT = True
FLUENT_UI_MASTER_BRANCH ='https://github.com/microsoft/fluentui-system-icons/raw/master'
FLUENT_UI_RAW_MASTER_BRANCH = 'https://raw.githubusercontent.com/microsoft/fluentui-system-icons/master' # 2x faster


def parse_data(lines, decode=False):
    is_table_reached = False
    icons_dict = dict()
    icons_library = ''

    for line in lines:
        if decode:
            line = line.decode("utf8")

        if is_table_reached:
            line_split = line.strip('|').split('|')
            name_split = line_split[0].split(' (')
            entry = dict()

            entry['name'] = name_split[0]
            entry['style'] = name_split[1].strip(')')
            entry['link'] = "{}/{}".format(FLUENT_UI_RAW_MASTER_BRANCH, line_split[1].split("\"")[1].replace(' ', '%20'))
            entry['sizes'] = [re.sub(r'_[rf]', '', size) for size in re.findall(r"\d\d_[rf]", line_split[3])]

            icons_dict[line_split[0]] = entry
            for size in entry['sizes']:
                name = "{}_{}_{}".format(entry['name'].lower().replace(' ', '_'), size, entry['style'].lower())
                icons_library += "export const {} = require('@fluentui/svg-icons/icons/{}.svg');\n".format(name, name)
        elif '|---|---|---|---|' in line:
            is_table_reached = True
    
    return icons_dict, icons_library


def store_data(dictionary, library):
    if dictionary is not None:
        with open('docs\\assets\\icon_list.json', 'w') as out:
            json_data = json.dumps(dictionary) 
            out.write(json_data)

        with open('projects\\fluent-ui-icons-web\\src\\assets\\icon_list.json', 'w') as out:
            json_data = json.dumps(dictionary) 
            out.write(json_data)

    if library is not None:
        with open('projects\\fluent-ui-icons\\library\\icons.library.ts', 'w') as out:
            out.write(library)


if __name__ == "__main__":
    dictionary = None
    library = None

    if (DEVELOPMENT):
        with open('test\\icon_list.md', 'r') as f:
            dictionary, library = parse_data(f)
    else:
        with urlopen('https://raw.githubusercontent.com/microsoft/fluentui-system-icons/master/icons.md') as html:
            lines = html.readlines()
            dictionary, library = parse_data(lines, decode=True)

    if dictionary is not None or library is not None:
        store_data(dictionary, library)

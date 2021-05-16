import re
import os
import json
import glob
from urllib.parse import quote
from urllib.request import urlopen
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--production', action='store_true')
parsed_args = parser.parse_args()

DEVELOPMENT = parsed_args.production
FLUENT_UI_MASTER_BRANCH ='https://github.com/microsoft/fluentui-system-icons/raw/master'
FLUENT_UI_RAW_MASTER_BRANCH = 'https://raw.githubusercontent.com/microsoft/fluentui-system-icons/master' # 2x faster

SOURCE = '.\\node_modules\\@fluentui\\svg-icons\\icons';
DESTINATION = '.\\projects\\fluent-ui-icons\\library\\svg';
indexFile = '.\\projects\\fluent-ui-icons\\library\\index.ts';
allFile = '.\\projects\\fluent-ui-icons\\library\\all.ts';

def generate_importable_svg_assets():
    icon_paths = glob.glob(os.path.join(SOURCE, '*.svg'))
    generated_assets_names = []

    for path in icon_paths:
        with open(path) as f:
            icon_name, icon_ext = os.path.splitext(os.path.basename(path))
            markup = f.read()

            with open(os.path.join(DESTINATION, '{}.ts'.format(icon_name)), "w+") as f:
                f.write("export const {} = '{}';".format(icon_name, markup))
                generated_assets_names.append(icon_name)

    return generated_assets_names


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
            entry['sizes'] = {re.sub(r'_[rf]', '', size): '' for size in re.findall(r"\d\d_[rf]", line_split[3])}

            icons_dict[line_split[0]] = entry
            for size in entry['sizes'].keys():
                name = "{}_{}_{}".format(entry['name'].lower().replace(' ', '_').replace('__', '_'), size, entry['style'].lower())
                icons_library += "export {{ {} }} from './svg/{}';\n".format(name, name)
        elif '|---|---|---|---|' in line:
            is_table_reached = True
    
    return icons_dict, icons_library


def load_data():
    dictionary = None
    library = None
    code_map = None

    if (DEVELOPMENT):
        with open('test/icon_list.md', 'r') as f:
            dictionary, library = parse_data(f)
    else:
        with urlopen('https://raw.githubusercontent.com/microsoft/fluentui-system-icons/master/icons.md') as html:
            lines = html.readlines()
            dictionary, library = parse_data(lines, decode=True)

    with urlopen('https://raw.githubusercontent.com/microsoft/fluentui-system-icons/master/fonts/FluentSystemIcons-Filled.json') as url:
        code_map = json.loads(url.read().decode())

    with urlopen('https://raw.githubusercontent.com/microsoft/fluentui-system-icons/master/fonts/FluentSystemIcons-Regular.json') as url:
        code_map.update(json.loads(url.read().decode()))

    if (dictionary is not None and code_map is not None):
        for icon_data in dictionary.values():
            for size, code in icon_data['sizes'].items():
                key = "ic_fluent_{}_{}_{}".format(icon_data['name'].lower().replace(' ', '_').replace('__', '_'), size, icon_data['style'].lower())
                if key in code_map:
                    icon_data['sizes'][size] = code_map[key]

    return dictionary, library

def store_data(dictionary, library):
    if dictionary is not None:
        with open('docs/assets/icon_list.json', 'w+') as out:
            json_data = json.dumps(dictionary) 
            out.write(json_data)

        with open('projects/fluent-ui-icons-web/src/assets/icon_list.json', 'w+') as out:
            json_data = json.dumps(dictionary) 
            out.write(json_data)

    if library is not None:
        with open('projects/fluent-ui-icons/library/icons.library.ts', 'w+') as out:
            out.write(library)


if __name__ == "__main__":
    library = None
    local_library = None
    online_dictionary, online_library = load_data()

    local_library = generate_importable_svg_assets()

    if local_library is not None:
        for name in local_library:
            library += "export {{ {} }} from './svg/{}';\n".format(name, name)
    else:
        library = online_library

    if online_dictionary is not None or library is not None:
        store_data(online_dictionary, library)

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
            entry['sizes'] = re.findall(r"\d\d", line_split[2])
            icons_dict[line_split[0]] = entry
        elif '|---|---|---|---|' in line:
            is_table_reached = True
    
    return icons_dict


def store_data(data):
    with open('docs\\assets\\icon_list.json', 'w') as out:
        json_data = json.dumps(data) 
        out.write(json_data)

    with open('projects\\fluent-ui-icons-web\\src\\assets\\icon_list.json', 'w') as out:
        json_data = json.dumps(data) 
        out.write(json_data)


if __name__ == "__main__":
    data = None

    if (DEVELOPMENT):
        with open('test\\icon_list.md', 'r') as f:
            parse_data(f)
    else:
        with urlopen('https://raw.githubusercontent.com/microsoft/fluentui-system-icons/master/icons.md') as html:
            lines = html.readlines()
            parse_data(lines, decode=True)

    if data is not None:
        store_data(data)
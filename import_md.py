import json
import sys
import re
import string

file_path = sys.argv[1]
f = open(file_path)

md = f.read()
f.close()

counter = 0
for slide in md.split('\n#'):
    if counter > 0:
        slide = '#%s' % slide

    slide_dict = {
      "slide_title": slide[slide.rfind('#') + 1:slide.find('\n')].strip(),
      "slide_content": slide,
      "slide_x": 1000 * counter,
      "slide_y": -1500,
      "slide_number": counter + 1
    }

    pattern = re.compile('[\W_]+')

    slide_id = slide_dict["slide_title"].replace(' ', '').lower()
    slide_id = pattern.sub('', slide_id)
    slide_dict['_id'] = slide_id

    json.dump(slide_dict, open('%s.json' % slide_id, 'w'))
    counter += 1


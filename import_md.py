import json
import sys
import re
import string

file_path = sys.argv[1]
f = open(file_path)

md = f.read()
f.close()
width = 5
counter = 0
for slide in md.split('\n#'):
    if counter > 0:
        slide = '#%s' % slide
    y, x = divmod(counter, width)
    slide_dict = {
      "slide_title": slide[slide.rfind('#', 0, 6) + 1:slide.find('\n')].strip(),
      "slide_content": slide,
      "slide_x": 1000 * x,
      "slide_y": -1500 + (800 * y),
      "slide_number": counter + 1
    }

    pattern = re.compile('[\W_]+')

    slide_id = slide_dict["slide_title"].replace(' ', '').lower()
    slide_id = pattern.sub('', slide_id)
    slide_dict['_id'] = slide_id

    json.dump(slide_dict, open('%s.json' % slide_id, 'w'))
    counter += 1


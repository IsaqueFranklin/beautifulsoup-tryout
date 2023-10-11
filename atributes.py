#With tag objects, a Python list of attributes can be automatically accessed by calling this:
#=> myTag.attrs => this literally returns a Python dictionary object
#Source for the location of the image => myImgTag.attrs['src']

#Lambda functions in bs4 => bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')

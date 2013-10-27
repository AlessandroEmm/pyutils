# -*- coding: UTF-8 -*-
from string import Template

class tmplt(object):

    def __init__(self, filename):
        self.filename = open(filename)
        #Load the template
        try:
            self.template = Template(self.filename.read())
        except IOError:
            raise IOError("No file at that location")

    def render(self, **args):
        self.filename.close()
        return  self.template.substitute(args)

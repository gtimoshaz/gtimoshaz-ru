from markdown.treeprocessors import Treeprocessor

class ResponsiveImg(Treeprocessor):
    def run(self, root):
        for child in root:
            if "img" == child.tag:
                child.set('class', 'img-fluid')


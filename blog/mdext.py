from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

class ResponsiveImgTree(Treeprocessor):
    def run(self, root):
        for child in root:
            if "img" == child.tag:
                child.set('class', 'img-fluid')

class ResponsiveImgExt(Extension):
    
    TreeProcessorClass = ResponsiveImgTree

    def extendMarkdown(self, md):
        md.registerExtension(self)
        self.md = md
        ext = self.TreeProcessorClass(md)
        md.treeprocessors.register(ext, 'responsiveImg', -8)


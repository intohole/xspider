#coding=utf-8



from selector import Selector





class XpathSelector(Selector):



    def __init__(self , **kw ):
        super(XpathSelector , self).__init__("xpath" , **kw) 
        self.path = kw.get("path" , None)

    
    def find(self , page):
        tree = page.get_tree() 
        nodes = tree.xpath(self.path)
        if len(nodes) > 0 :
            return nodes[0]
        return None


    def finds(self , page):
        tree = page.get_tree()
        return tree.xpath(self.path)

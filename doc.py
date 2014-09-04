#coding=utf-8
#!/usr/bin/env python


import time



class Doc(object):


    def __init__(self , title , content , author ,  category ,tags  =  []  ,summary = None , head_date = None):
        if head_date == None:
            self.head_date = time.strftime('%Y-%m-%d %H:%M:%S')
        self.title = title 
        self.content = content 
        self.author = author 
        self.tags = ' ,'.join(tags)
        self.category = category
        self.file_name = title
        self.summary = summary 


    def __str__(self):
        msg = []
        msg.append('Date:%s  \n' % self.head_date)
        msg.append('Title:%s  \n' % self.title )
        msg.append('Author:%s  \n' % self.author)
        msg.append('Category:%s  \n' % self.category)
        msg.append('Tags:%s  \n' % self.tags)
        if self.summary:
            msg.append('Summary:%s  \n' % self.summary)
            msg.append('<div class="msummary">&nbsp&nbsp<h3>摘要<h3>: %s</div>  \n' %self.summary)
        msg.append('  %s' % self.content)
        return ''.join(msg)




if __name__ == '__main__':
    doc = Doc('test' , 'cool' , 'li'  , 'jiji' ,  ['1' , '2'] , '摘要')
    print doc



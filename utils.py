#coding=utf-8
#!/usr/bin/env python





from subprocess import call




def make_html(content_path):
    command = ['make' , 'html' , '-C' , content_path]
    call(command)


def make_server(content_path):
    command = ['make' , 'serve' , '-C' , content_path]



if __name__ == '__main__':
    make_server('/home/lixuze/github/test/')





from reader import Reader as rd
from integrater import convert ,wrap
from Function import Function as function
from Loop import For as loop
from out import export
from select_language import select_language
from Block import Block
language=select_language('cpp')
Block.language=language
read=language.read
read_array=language.read_array
declare = language.declare

# m=function('main','int',[
#     # declare('T','int'),
#     read('T','int'),
#     # declare('N','int'),
#     read('N','int'),
#     # declare('points','int','array'),
#     read_array('points','N','int'),
#     # declare('height','int','array'),
#     read_array('heights','N','int'),
#     # declare('M','int'),
#     function('inside','int',[
#         read('T','int'),
#     ]),
#     read('M','int'),
#     loop('0','N','1',[
#         # declare('M','int'),
#         read('M','int'),
#         loop('2','5','1',[
#             # declare('j','int'),
#         ]),
#         # declare('arr','int','array'),
#         read_array('arr','M','int'),
#     ]),
#     # declare('index','int','array'),
#     read_array('index','N','int'),
#     # declare('minheight','int','array'),
#     read_array('minheight','N','int'),
# ])
# def compile_method(method,lang):
#     code=method.inner_code
#     m=[compile_method(i,lang) if type(i)==Function else i  for i in code]
#     method.inner_code=convert(lang,m)
#     m=method.create_method()
#     return m
# def compile_loop(method,lang):
#     code=method.inner_code
#     m=[compile_loop(i,lang) if type(i)==loop else i  for i in code]
#     method.inner_code=convert(lang,m)
#     m=method.create_loop()
#     return m

l=loop('0','N','1',[
        declare('M','int'),
        read('M','int'),
        loop('2','5','1',[
            declare('j','int'),
        ]),
        declare('arr','int','array'),
        function('main','int',[
            declare('T','int'),
            read('T','int'),
            declare('N','int'),
            read('N','int'),]),
        read_array('arr','M','int'),
    ])






print(l)




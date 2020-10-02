from select_language import select_language
from abc import ABC, abstractmethod


class Block(ABC):
    language=select_language('python3')
    def __repr__(self):
        return self.compile(self,self)

    @staticmethod
    def compile(self,code_block):
        statements=""
        for statement in code_block.inner_code:
            if statement=="not_supported" :
                continue
            elif isinstance(statement,Block):
                statements=statements+'\n'+self.compile(self,statement)
            else:
                statements=statements+'\n'+statement
        code_block.inner_code=statements
        return code_block.create()

    @abstractmethod
    def create(self):
        pass
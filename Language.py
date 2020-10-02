from abc import ABC, abstractmethod

class Language(ABC):

    '''Abstract Methods'''

    @abstractmethod
    def loop(self):
        pass
    @abstractmethod
    def function(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def read_array(self):
        pass
    @abstractmethod
    def call(self):
        pass
    @abstractmethod
    def print_out(self):
        pass


    ''' Methods for Static Languages '''

    def declare(self,name,vartype,container='var'):
        return "not_supported"
    def declare_array(self,name,vartype,container='var'):
        return "not_supported"
    def headers(self,code):
        return code
    def create_class(self,name,inner_code,access_specifier):
        return "not_supported"












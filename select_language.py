import Languages as lang

def select_language(language):
    store={
        'python3':lang.Python3(),
        'php':lang.PHP(),
        'cpp':lang.CPP(),
        'python2':lang.Python2(),
    }
    return store[language]
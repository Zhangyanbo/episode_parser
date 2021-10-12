from .baidu import baidu_reader


class reader:
    def __init__(self):
        pass

    def search(self, key):
        pass
    
    def series(self):
        pass

    def save(self):
        pass

    def load(self):
        pass


class baidu(reader):
    def __init__(self, url):
        super(baidu, self).__init__()
        self.core = baidu_reader(url)
    
    def search(self, key):
        return self.core.search(key)
    
    def series(self):
        return self.core.series
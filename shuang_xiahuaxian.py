#关于双下划线的应用
class Test:

    def __init__(self,name,job):
        self.name=name
        self.job=job

    def __str__(self):
        return '姓名:'+ self.name+'工作是'+self.job

instance=Test('xiaoming','Teacher')
print(instance)





# def test(*args, **kwargs):
#     print(args)
#     print(kwargs)


# test(1,2,3,4, a = 112, b = 13, c=14 )


# l = [1,2,3,4]

# c = list(map(lambda x: x==2, l))
# print(c)


class People:

    name = None
    
    

    # def __init__(self) -> None:
    #     self.name = 1212
    
    @classmethod
    def get_name(cls):
        return cls.name

    @staticmethod
    def get_test():
        return "132343"




People.name = 1212
print(People.get_name())
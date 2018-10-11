def test(x,y):
    a= x + y
    print(a)


def func1(z,d):
    a = test(z,d)
    if z < d:
        return a

func1(5,4)

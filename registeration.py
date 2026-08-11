def register(func):
    u=[]
    def inner():
        nonlocal us
        if u  in us:
            us=input("enter user name:")
            psd=input("enter password:")
            age=int(input("enter ur age" ))
            sp=['@','&','*','+']
        if len(psd)>=8:
            us=list(filter(lambda x: x.isupper(),psd))
            sc=list(filter(lambda x: x in sp,psd))
            dg=list(filter(lambda x: x.isdigit(),psd))
            if age>=18 :
                if us and sc and dg:
                    print("valid")
            else:
                print("age should be greater thn 18")
        else:
            print("pasd must be 8 dgits")
        func()
    return inner
@register
def password():
    print("registration done success")
password()
password()






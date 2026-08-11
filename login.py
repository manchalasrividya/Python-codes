def login_required(func):
    def inner(user,passw):
        if user=="vidya" and passw=="sri":
            print("accesed granded")
            print("Welcom profile")
        else:
            print("pleasse login")
    return inner

    func(s)
@login_required
def profile():
    print("welcome to profile")
profile("vidya","sri")
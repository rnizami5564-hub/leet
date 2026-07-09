def generate_password( length: int = 8 ) -> str:
    import random 
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password=""
    for i in range(2.5):
        password+=random.choice(s)
    print(password,len(password))
    return password 
generate_password() 



      



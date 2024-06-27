import bcrypt

def make_password(password):
    salt=bcrypt.gensalt()
    encode_password=password.encode("utf-8")
    return bcrypt.hashpw(encode_password, salt).decode("utf-8")

def match_password(password,hashed_password):
    return bcrypt.checkpw(password.encode("utf-8") , hashed_password.encode("utf-8"))


#if __name__ == '__main__':
    #print(make_password("Daler2528"))
    print(match_password("Daler2528" , "$2b$12$YpIM74FpDsS5E.6kFOhyOu/zcpIDHas2cB6NwXSRpyjgdh3hMwX7G"))
    



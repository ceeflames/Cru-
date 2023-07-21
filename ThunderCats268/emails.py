from file_handle import File_man

class Main(object):
    def __init__(self, *args):
        super(Main, self).__init__(*args)
        self.FM = File_man()

    # RETURNS THE NEXT AVAILABLE USER_ID_#    
    def get_user_count(self):
        try:
            user_s = self.FM.read_file("dataBase/USER.txt", "$")
            if len(user_s) > 0:
                for i, user in enumerate(user_s):
                    print("USER: ", str(user), "\nUSER_COUNT: ", str(i))
            return i+1
        except Exception as e:
            print("[ERROR]:[CHECK_USERS]:", str(e))



class Register(object):
    def __init__(self, *args):
        super(Register, self).__init__(*args)
        self.FM = File_man()
        self.M = Main()

    def set_lst_str(self, data_list):
        try:
            ret_str = ""
            for i in data_list:
                ret_str+= str(i)
            return ret_str
        except Exception as e:
            print("[ERROR]:[list_to_STR]: ", str(e))

    def new_user(self, user_data):
        try:
            # CONVERT DATA TO WRITABLE STR
            print("NEW_USER: ", str(user_data))
            u_id = self.M.get_user_count()
            name_= ''
            email_= ''
            pswd_ = ''
            str_to_w = []
            for key, val in user_data.items():
                print("ITEMS: [key]", str(key), "[val]:", str(val))
                if str(key) == "uName":
                    name_ = val
                if str(key) == "eMail":
                    email_ = val
                if str(key) == "pSwD":
                    pswd_ = val
            str_to_w = ["$", str(u_id), "*", name_,"*", email_,"*", pswd_,"*"]
            ready_str = self.set_lst_str(str_to_w)
            self.FM.write_file("dataBase/USER.txt", ready_str, "%", "a")
            return "USER_REGISTER:[ "+str(name_)+" ]"
        except Exception as e:
            print("[ERROR]:[REGISTERATION] : ", str(e))



class Login(object):
    def __init__(self, *args):
        super(Login, self).__init__(*args)
        self.FM = File_man()
        self.M = Main()

    def check_users(self, name_, pswd_):
        try:
            print("NAME_ : ", name_)
            print("PSWD__: ", pswd_)
            user_s = self.FM.read_file("dataBase/USER.txt", "$")
            if len(user_s) > 0:
                for i, user in enumerate(user_s):
                    if i == 0:
                        continue
                    else:
                        set_U = str(user).split("*")
                        print("SET_U:0: ", str(set_U[0]))
                        print("SET_U:1: ", str(set_U[1]))
                        print("SET_U:2: ", str(set_U[2]))
                        print("SET_U:3: ", str(set_U[3]))
                        if str(name_) in str(set_U[1]):
                            print("FOUND_USER_NAME:: ", str(name_), "::", str(user))
                            C_name = True
                            print("PSWD_::? ", str(pswd_))
                            print("LENS::: ", str(len(str(set_U[3]))), "::", str(len(pswd_)))
                            if str(pswd_) == str(set_U[3]):
                                C_pswd = True
                                return set_U
                            else:
                                return "WRONG_PASSWORD"
                        else:
                            continue
        except Exception as e:
            print("[ERROR]:[CHECK_USERS]:", str(e))

    def attempt_login(self, name_, pswd_):
        try:
            # LIST vs LIST
            c_user = self.check_users(name_, pswd_)
            print("C_USER:: ", str(c_user), "::", str(name_), ":", str(pswd_))
            return True
        except Exception as e:
            print("[ERROR]:[ATTEMPT_LOGIN]:", str(e))



class Forgot(object):
    def __init__(self, *args):
        super(Forgot, self).__init__(*args)
        self.FM = File_man()
        self.M = Main()
        pass

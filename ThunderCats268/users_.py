import re
from file_handle import File_man

class User_Set(object):
    def __init__(self, *args):
        super(User_Set, self).__init__(*args)
        self.FM = File_man()
    # DATA_BASE USER INFO

    def write_users(self, UserList):
        try:
            data_ = ""
            print("--line-break--")
            for us_ in UserList:
                #print("[USER_TO_WRITE]: ", str(us_))
                data_ += str(us_)


            #print(f'TEXT_TO_WRITE: \n {data_}')
            with open("dataBase/USER_DATA.txt", "w") as wf:
                wf.write(data_)
                wf.close()
            return
        except Exception as e:
            print("[ERROR]:[TURNICATE_USERS]", str(e))
    def add_user(self, user_data):
        #print("[ADDING_USER_]:",str(user_data))
        try:
            exists = False
            catch_ = ""
            current_users = self.get_all_users()
            try:
                #print("[CHECKING_USERS]")
                if current_users != False:
                    for user in current_users:
                        user_ = self.split_data(user)
                        #print("[CURRENT_USER]: ",str(user))
                        if str(user_data[1]) == str(user_[1]):
                            print("USER_EMAIL_EXSIST")
                            catch_ = user
                            exists = True

                if exists == False:
                    current_users.append(str("@"+str(user_data)+"&\n"))
                    #print("NEW_USER_EMAIL")
                        # TURNICATE
                    self.write_users(current_users)
                    return [False, user_data]
                if exists == True:
                    return [True, catch_]
            except Exception as e:
                print("[ERROR]:[ADD_USER]:", str(e))

        except Exception as e:
            print("[ERROR]:[ADD_USER]:", str(e))
        pass
    def remove_user(self, user_data):
        pass
    def get_all_users(self):
        try:
            print("GETTING_USERS")
            try:
                with open("dataBase/USER_DATA.txt", "r") as rf:
                    data = rf.readlines()
                    rf.close()
                    return (data)
            except Exception as e:
                print("ERROR_READING_FILE", str(e))
                return False

        except Exception as e:
            print("[ERROR]:[GET_ALL_USERS]:", str(e))
            return False
    def get_set_users(self):
        try:
            user_list = []
            user_data =[]
            user_s = self.get_all_users()
            if user_s:
                for user in user_s:
                    user_data = self.split_data(user)
                    #for i in user_data:
                    #    print("USER_DATA: ", str(i))
                    user_list.append(user_data)
                    user_data = []
                return user_list
                    
        except Exception as e:
            print("[ERROR]:[GET_SET_USERS]:",str(e))        
        pass
    def split_data(self, user_data):
        try:
            ret_user = ["N$:name_", "E$:email_", "M$:msg_"]
            ret_ = user_data.split("*")
            #print("SPLIT?:: ")
            for i in ret_:
                if "N$:" in i:
                    name_ = "N$:"+str(str(i).split("N$:")[1])+"*"
                    #print("NAME: ", name_)
                if "E$:" in i:
                    email_ = "E$:"+str(str(i).split("E$:")[1])+"*"
                    #print("EMAIL: ", email_)
                if "M$:" in i:
                    msg_ = "M$:"+str(str(i).split("M$:")[1])+"*"
                    #print("NAME: ", msg_)
            ret_user = [name_, email_, msg_]
            return ret_user
        except Exception as e:
            print("[ERROR]:[SPLIT_DATA]:",str(e))


    # EAMILING DAEMON    
        # 
    def slots_time_convert(self, slots):
        try:
            if type(slots) != list:
                print("\n**********************************************\n", "[SLOTS NOT A LIST >:~| ]")

            send_slot = []
            new_slot = ["6:30-7:00","7:00-7:30","7:30-8:00","8:00-8:30","8:30-9:00","9:00-9:30","9:30-10:00","10:00-10:30","10:30-11:00","11:00-11:30","11:30-12:00","12:00-12:30","12:30-13:00","13:00-13:30","13:30-14:00","14:00-14:30","14:30-15:00","15:00-15:30","15:30-16:00", "16:00-16:30"]



            for i, val in enumerate(slots):
                if "True" in str(val):
                    send_slot.append(new_slot[i])

            for test in send_slot:
                print("SLOT_TO_SEND: ", str(test))
            return send_slot

        except Exception as e:
            print("[ERROR]:[SLOT_TIME_CONVERT]:",str(e))
                    # BOOKINGS    (name_, date_1, people_num, child_num, new_slots, ref_, price_
    def craft_booking_email(self,  name_, date_, set_cel, beach_, set_speed, adults_,  kids_,  slots_, ref_, price_):
        try:
            set_slots = self.slots_time_convert(slots_)

            # INDEX TEMPLATE
            index_ = f"<div style='display: block; justify-content: center; text-align: center; align-items: center; color: black;'>\
                        <div style='background-color: aqua; width: 100%; display:flex; align-items: center; justify-content: center;' id='HEADER_SUBJECT'>\
                        <h3 style='color: black; padding: 2px 2px; font-size: x-large; '>\
                        Booking made on ThunderCats268 for { name_ }</h3></div>\
                        <div>On the date of {date_}<br> at {beach_} <br>\
                        for time slot(S): <br>{set_slots}<br> with {adults_} and {kids_}\
                        <br> adding up to an amount of <br> $ {price_} (USD) \
                        <br><div>Cell-Phone Number:  {set_cel} </div><br>\
                        <br>For this booking please use the reference: <br> {ref_}<br> We will contact you shortly regarding payment options which suit you best  </div>\
                        <div id='BODY' style='justify-content: center; width: 100%;'>\
                        <h6 style='font-size:x-large;'>Feel free to make another booking</h6><div style='display: flex; justify-content: center; align-items: center;'>\
                        <a href='http://beta.thundercats268.com/' style='text-decoration: none; width: 45%;color: black; margin: 20px 25px auto;  padding: 1px 1px;\
                        text-align: center;font-size: x-large;justify-content: center;align-items: center;border-radius: 0.8rem;background-color: rgba(17, 206, 219, 0.9);'>\
                        <h6>BOOK NOW</h6></a></div>\
                        <div><h5 style=' text-align: center;'>\
                        Thank you for your continued support</h5> </div>"

            return index_
            # SMASH TOGETHER AND SEND
        except Exception as e:
            print("[ERROR]:[EAMIL_TEMPLATE]:", str(e))
    def craft_custom_booking_email(self,  name_, email_, num_, msg_):
        try:
            # INDEX TEMPLATE
            index_ = f"""<div style='display: block; justify-content: center; text-align: center; align-items: center; color: black; background-color: white;'>
                        <div style='background-color: aqua; width: 100%; display:flex; flex-direction: column;align-items: center; justify-content: center;' id='HEADER_SUBJECT'>
                        <h3 style='padding: 2px 2px; '>HELLO { name_ },</h3>
                        <h5>We will contact you sortly on {email_} or {num_}</h5>
                        <br>
                        <h5>Regarding your booking<br> and respond to your message:<br> {msg_}</h5>
                        <div id='BODY' style='justify-content: center; width: 100%;'>
                            <h5 style='font-size:x-large; text-align: center;'>
                            Thank you for your continued support</h5>
                            <h6 style='font-size:x-large;'>Feel free to make another booking</h6>
                            <div style='display: flex; justify-content: center;'>
                                <a href='http://beta.thundercats268.com/' 
                                style='text-decoration: none; width: 45%;color: black;display: 
                                block;margin: 5px 5px auto;margin-top: 20px;padding: 1px 1px;text-align: center;
                                font-size: x-large;justify-content: center;align-items: center;border-radius: 0.8rem;
                                background-color: rgba(17, 206, 219, 0.9);'>
                                <h6>BOOK NOW</h6></a>
                            </div>
                        </div>
                        </div>
                        </div>"""
            return index_
            # SMASH TOGETHER AND SEND
        except Exception as e:
            print("[ERROR]:[EAMIL_TEMPLATE]:", str(e))



        # NEWS_LETTER
    def craft_new_sub(self, name_, email_, msg_):
        try:
            craft = f"""<div>
                        <div style='display: block; justify-content: center; text-align: center; align-items: center; color: black; background-color: white;'>
                        <div style='background-color: aqua; width: 100%; display:flex; flex-direction: column;align-items: center; justify-content: center;' id='HEADER_SUBJECT'>
                        <h3 style='padding: 2px 2px; '>HELLO { name_ },</h3>
                        </div>
                        </div>
                        <h5>We will contact you on {email_}</h5>
                        <br>
                        <h5>Regarding your message:<br> {msg_}</h5>
                        <div id='BODY' style='justify-content: center; width: 100%;'>
                        <h5 style='font-size:x-large; text-align: center;'>
                        Thank you for your continued support</h5>
                        <h6 style='font-size:x-large;'>Feel free to make a booking</h6>
                        <div style='display: flex; justify-content: center; align-items: center;'>
                            <a href='http://beta.thundercats268.com/' 
                            style='text-decoration: none; width: 45%;color: black;display: 
                            block;margin: 5px 5px auto;margin-top: 20px;padding: 1px 1px;text-align: center;
                            font-size: x-large;justify-content: center;align-items: center;border-radius: 0.8rem;
                            background-color: rgba(17, 206, 219, 0.9);'>
                            <h6>BOOK NOW</h6></a>
                        </div></div></div>
                        """
            return craft
        except Exception as e:
            print("[ERROR]:[CRAFTING_NEW_SUB]:",str(e))

    def craft_news_letter(self,body, foot_note):
        try:
            craft = f"""<div><br><div>{str(body)}</div><br> <div> {str(foot_note)} </div> 
                        <div><a href='http://beta.thundercats268.com/' style='text-decoration: none; width: 45%;color: black;display: block;margin: 5px 5px auto;margin-top: 20px;padding: 1px 1px;text-align: center;font-size: x-large;justify-content: center;align-items: center;border-radius: 0.8rem;background-color: rgba(17, 206, 219, 0.9);'>
                        <h6>BOOK NOW</h6></a></div>
                        </div>"""

            # SMASH TOGETHER AND SEND
            return craft
        except Exception as e:
            print("[ERROR]:[EAMIL_TEMPLATE]:", str(e))

    def run_newsletter(self):
        try:
            new_letter = ""
            users_ = self.get_all_users()
            # loop through each
            for user in users_:
                # craft letter
                new_letter = self.craft_news_letter(user)
                self.send_letter(user, new_letter)
        except Exception as e:
            print('[ERROR]:[RUN_NEWSLETTER]:', str(e))




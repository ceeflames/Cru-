from file_handle import File_man
from datetime import datetime 


class Slot_Update():
    def __init__(self, **kw):
        super(Slot_Update, self).__init__(**kw)
        pass

    def is_here(self, date_, list_):
        for i in list_:
            if date_ in i:
                return False

    def set_slots(self, buff_, item):
        try:
            new_slot = ["","","","","","","","","","","","","","","","","","","",""]
            # NOW HARD CODE THAT SHIT 
            if len(buff_) > 0:
                #print(":P", str(buff_[1][0]))
                if str(buff_[1][0]) == "True" or str(item[1][0]) == "True":
                    new_slot[0] = "True"
                else:
                    new_slot[0] = "False"
                if str(buff_[1][1]) == "True" or str(item[1][1]) == "True":
                    new_slot[1] = "True"
                else:
                    new_slot[1] = "False"
                if str(buff_[1][2]) == "True" or str(item[1][2]) == "True":
                    new_slot[2] = "True"
                else:
                    new_slot[2] = "False"
                if str(buff_[1][3]) == "True" or str(item[1][3]) == "True":
                    new_slot[3] = "True"
                else:
                    new_slot[3] = "False"
                if str(buff_[1][4]) == "True" or str(item[1][4]) == "True":
                    new_slot[4] = "True"
                else:
                    new_slot[4] = "False"
                if str(buff_[1][5]) == "True" or str(item[1][5]) == "True":
                    new_slot[5] = "True"
                else:
                    new_slot[5] = "False"
                if str(buff_[1][6]) == "True" or str(item[1][6]) == "True":
                    new_slot[6] = "True"
                else:
                    new_slot[6] = "False"
                if str(buff_[1][7]) == "True" or str(item[1][7]) == "True":
                    new_slot[7] = "True"
                else:
                    new_slot[7] = "False"
                if str(buff_[1][8]) == "True" or str(item[1][8]) == "True":
                    new_slot[8] = "True"
                else:
                    new_slot[8] = "False"
                if str(buff_[1][9]) == "True" or str(item[1][9]) == "True":
                    new_slot[9] = "True"
                else:
                    new_slot[9] = "False"
                if str(buff_[1][10]) == "True" or str(item[1][10]) == "True":
                    new_slot[10] = "True"
                else:
                    new_slot[10] = "False"
                if str(buff_[1][11]) == "True" or str(item[1][11]) == "True":
                    new_slot[11] = "True"
                else:
                    new_slot[11] = "False"
                if str(buff_[1][12]) == "True" or str(item[1][12]) == "True":
                    new_slot[12] = "True"
                else:
                    new_slot[12] = "False"
                if str(buff_[1][13]) == "True" or str(item[1][13]) == "True":
                    new_slot[13] = "True"
                else:
                    new_slot[13] = "False"
                if str(buff_[1][14]) == "True" or str(item[1][14]) == "True":
                    new_slot[14] = "True"
                else:
                    new_slot[14] = "False"
                if str(buff_[1][15]) == "True" or str(item[1][15]) == "True":
                    new_slot[15] = "True"
                else:
                    new_slot[15] = "False"
                if str(buff_[1][16]) == "True" or str(item[1][16]) == "True":
                    new_slot[16] = "True"
                else:
                    new_slot[16] = "False"
                if str(buff_[1][17]) == "True" or str(item[1][17]) == "True":
                    new_slot[17] = "True"
                else:
                    new_slot[17] = "False"
                if str(buff_[1][18]) == "True" or str(item[1][18]) == "True":
                    new_slot[18] = "True"
                else:
                    new_slot[18] = "False"
            #print("\nNEW_SLOT_DATE:: ", str(buff_[0]), "::", str(new_slot))
            return str(buff_[0]), new_slot
        except Exception as e:
            print("[ERROR]:[SET_SLOT]:", str(e))

    def check_dates(self, update_, date_decomp):
        buff_list = date_decomp
        try:
            y_n = False
            date_ = ""
            slot_s = []
            new_date = str(update_[0])
            #if update_:
            #    print("\n**\nCHECKING: \n", str(new_date))
            for v in buff_list:
                w = ""
                w = str(v[0])
                try:
                    #print("V:", str(w), "::", str(new_date))
                    if str(new_date) in str(w):
                        y_n = True
                        #print("UPDATING: ", str(new_date))
                        try:
                            date_, slot_s = self.set_slots(update_, v)
                            #print("\n**\n\nSLOT_UPDATE_RETURN:: ", str(date_), "::", str(slot_s))
                        except:
                            print("geting_slots error")
                        #print("UPDATED:: ", str(date_), str(slot_s))
                except:
                    print('check_list_error')
            if y_n == True:
                return (date_, slot_s)
            else:
                return ("NOPE", "NOPE")
        except Exception as e:
            print("[ERROR]:[CHECK_LIST]:", str(e))
            return (["NOPE", "NOPE"])

    def update_lists(self, new_, list_):
        try:
            new_li = []
            #for w in list_:
            #    print("W::", str(w))
            #print("NEW_: ", str(new_))
            for i, val in enumerate(list_):

                if str(new_[0]) in str(val[0]):


                    list_[i] = [str(new_[0]),new_[1][0:18]]
                    uhm = str(val[1][0:19])
                    #print("######\nlets try_a croppp :|  \n ::", str(uhm))
            for i in list_:
                #print("\n***\n*1*\n***\nLI:: ", str(i))
                n_i = [str(i[0]),i[1][0:19]]
                #print("NEW_I: ", str(n_i))
                new_li.append(n_i)
                i = n_i
                #print("\n***\n*2*\n***\nLI:: ", str(i))


            print("*****************")
            #for j in new_li:
            #    print("&&&:::: J: ", str(j))
            return new_li
        except Exception as e:
            print("[ERROR]:[UPDATE_LIST]:", str(e))


    # ToDo:
        # RE_ORGANIZE : BY : DATE

        # AND RETURNS AS LIST
    def ret_set_(self, new_list):
        try:
            ret_set = []
            set_str = ""
            for f in new_list:
                set_str = "@"+str(f[0])+"*"
                #print("FFFF: ", str(set_str))
                for e in f[1]:
                    set_str += str(e) +"&"
                ret_set.append(set_str)
                set_str = ""
            return ret_set
        except Exception as e:
            print("[ERROR]:[RET_SET]:",str(e))

    # LOAD FILE DATA
    def get_stack(self, file_name, delim):
        try:
            return File_man().read_file(file_name, delim)
        except Exception as e:
            print("[ERROR]:[GET_STACK]:",str(e))

    # GET LIST OF FULLY BOOKED DATES
    def full_dates(self, ti_sl_list):
        try:
            dates_list = ""
            set_count = 0
            for n, val in enumerate(ti_sl_list):
                # SPLIT DATE_FROM_SLOTS
                date_slots = str(val).split("*")
                #print("CHECK_DATE_FILL?:", str(date_slots[0]))
                for s in date_slots:
                    if str(date_slots[0]) not in str(s):
                        #print("\n\n???", str(date_slots))

                        just_slots = s.split("&")
                        for j in just_slots:
                            if "False" in str(j):
                                pass
                            elif "True" in str(j):
                                set_count += 1
                            elif "True" not in str(j) and "False" not in str(j):
                                print("WHAT NOW???? \n:::", str(j))
                                continue
                            elif "\\" in str(j):
                                print("PROBLEM HERE \n\nlist_sys:::line-218\n\n", str(j))
                                continue
                                #print("SET_COUNT:[IN_LOOP] ", str(set_count))
                        #print("SET_COUNT: ", str(set_count))
                        if set_count >= 18:
                            n_date = str(date_slots[0])
                            dates_list += str(n_date) + "*"
                        set_count = 0
                    else:
                        pass

                        #print("DATES_SLOTS_CHECKED: ", str(date_slots[0]))
            return dates_list
        except Exception as e:
            print("[ERROR]:[FULL_DATES]:",str(e))


    # IF YOU'RE DEBBUGGING MY CODE... THE PROBLEM IS MOST LIKELY HERE SOMEWHERE ... ^
    def new_time_slots(self, update_, file_name, delim):
        date_slots = []
        c_slots = []
        dt_struct = []
        boat_1_books = self.get_stack(file_name, delim)
        try:
            # LIST OF ALL BOAKT DATES_w_SLOTS "@"
            for d_s in boat_1_books:
                date_slots = d_s.split("*")
                # DATE "*" SLOTS
                if len(date_slots) > 1:
                    c_slots = str(date_slots[1]).split("&")
                    # SLOTS -> "&"
                    dt_struct.append([str(date_slots[0]), c_slots])
        except Exception as e:
            print("[ERROR]:[COLLECTING_DATA]:[NEW_TIME_SLOTS]:",str(e))

        try:
            new_j = ""
            n_dates_, new_slot = self.check_dates(update_, dt_struct)
            n_dat_slot = [n_dates_, new_slot]
            #print("\n**\nCHECK_DATES:RETURN :: ",str(n_dates_) ,":", str(new_slot))
            if "NOPE" not in new_slot:
                try:
                    new_list = self.update_lists(n_dat_slot, dt_struct)
                    final_set = self.ret_set_(new_list)
                    #for i in final_set:
                    #    print("F: ", str(i))
                    # THEN WRITE TO FILE :P
                    File_man().write_file(file_name, final_set, "\n", "w")
                except Exception as e:
                    print("[ERROR]:[NEW_TIME_SLOT]:[!_NOPE]")

            elif "NOPE" in new_slot:
                try:
                    #print("NEW_DATE")
                    #for i in update_:
                    #    print("::",str(i))
                    for j in update_[1]:
                        new_j += str(j)+"&"
                        #print("J:", str(j))
                    up_load = "@"+str(update_[0])+"*"+str(new_j)
                    File_man().write_file(file_name, up_load, "\n", "a")
                except Exception as e:
                    print("[ERROR]:[NEW_TIME_SLOT]:[is_NOPE]")


        except Exception as e:
            print("[ERROR]:[NEW_TIME_SLOTS]:[UPDATEING]:",str(e))


    # STACK_ITEM_STR
    def stack_item_str(self, stack_item):
        try:
            #print("STACK_ITEM::::::", str(stack_item))
            ret_set = ""
            date_str = ""
            set_str = ""
            for f in stack_item:
                if len(f) <= 11:
                    date_str = "@"+str(f)+"*"
                    continue
                    #print("FFFF: ", str(date_str))
                else:
                    for E in f:
                        set_str += str(E) +"&"
                #print("[SET_STR]::", str(set_str))
                ret_set += date_str + set_str
            return ret_set
        except Exception as e:
            print("[ERROR]:[STACK_ITEM_STR]:",str(e))


    # UPDATE NEW_STACK to FILE
    def update_new_stack(self, new_stack):
        try:
            File_man().write_file("dataBase/CAL_DATES.txt", new_stack, "%", "w")
            return
        except Exception as e:
            print("[ERROR]:[UPDATE_NEW_STACK]:[RM_SLOT]:[SLOT_UPDATE]")

    # SET_STACK_W
    def set_stack_w(self, new_stack):
        try:
            ret_stack_ = []
            fet_slots_ = ""
            ret_s_item = ""
            for i, val in enumerate(new_stack):
                # CONVERT SLOTS TO STR
                if len(val) > 1:
                    #print("CONVERTING:: ", str(val[0]))
                    # CONVERT STACK_ITEM TO STR
                    fet_slots_ = self.stack_item_str(val)
                    ret_stack_.append(fet_slots_)

            # RETURN LIST_OF STACK_ITEMS(STRs)
            return ret_stack_
        except Exception as e:
            print("[ERROR]:[SET_STACK_W]:", str(e))
    

    # REMOVE SLOT_INDEX
    def remove_slot(self, slot_lst, slot_index):
        try:
            ret_slot_ = slot_lst
            #print("[INDEX_TO_REMOVE]:",str(slot_index))
            #print("[SLOT_LIST]:", str(slot_lst))
            ret_slot_[1][slot_index] = 'False'
            return slot_lst
        except Exception as e:
            print("[ERROR]:[REMOVE_SLOT]:", str(e))

    # SLOT_STR -> SLOT_LIST
    def slotStr_toLst(self, slot_str):
        try:
            #print("SLOT_STR: ", str(slot_str))
            ret_lst_ = []
            ret_slots_ = []
            date_ = ""
            brk_lst = []
            break_str = []

            #c_t = ["", [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]
            # GET THE DATE
            if "*" in slot_str:
                brk_lst = slot_str.split("*")
                date_ = brk_lst[0]
                ret_lst_.append(date_)
                #print("DATE:: ", str(date_))
            break_str = str(brk_lst[1]).split("&")
            for i, val in  enumerate(break_str):
                #print(":I:", str(i), ":VA:", str(val))
                if "True" in val or "False" in val:
                    ret_slots_.append(val)
            ret_lst_.append(ret_slots_)
            return ret_lst_
        except Exception as e:
            print("[ERROR]:[SlotStr_toLst]:",str(e))

    # DELETE SLOT -> OPEN BOOKING AVAILIBILITY
    def open_slot(self, date_, slot_index):
        try:
            ret_stack_ = []
            slot_lst_ = []
            n_slot = []
            new_stack_ = []
            #print("OPENING_SLOT:[DATE]:",str(date_), ":[SLOT_INDEX]:", str(slot_index))
            # GET SLOT STACK
            slot_stack = self.get_stack("dataBase/CAL_DATES.txt", "@")
            for date_set in slot_stack:
                if len(date_set) < 10:
                    continue
                #print("COLLECTED:: ", str(date_set))
                slot_lst_ = self.slotStr_toLst(date_set)
                # SET_SLOT OF SLOT_DATE
                if date_ in slot_lst_:
                    # UPDATE DATE_SLOT BY INDEX
                    n_slot = self.remove_slot(slot_lst_, int(slot_index))
                    #for s_l in n_slot:
                    #    print("RET_LIST:ITEM:", str(s_l))
                # SET STACK FOR WRITING
                ret_stack_.append(slot_lst_)
            new_stack_ = self.set_stack_w(ret_stack_)
            #for slot_stack in new_stack_:
            #    print("[NEW_SLOT_STACK]:", str(slot_stack))
            self.update_new_stack(new_stack_)
            #File_man().write_file("dataBase/DUMMY.txt", new_stack_, "@", "w")
            # RIGHT NEW STACK TO DATA_BASE
        except Exception as e:
            print("[ERROR]:[OPEN_SLOT]:[SLOT_UPDATE]:",str(e))



class Break_Data(object):
    def __init__(self, **kw):
        super(Break_Data, self).__init__(**kw)
        self. FM = File_man()


    def show_list(self, list_):
        try:
            print("Break_Data().Show_List(): ")
            for x in list_:
                print("[::]", str(x))
        except Exception as e:
            print("[ERROR]:[SHOW_LIST]:[BREAK_DATA]:",str(e))
    # E.G.
    #update_ = ["2022/10/4",["False","False", "False", "True", "True", "True", "True", "True", "True", "True", "True", "True","True","False","False","False","False","True","True"]]
    # CLIENT_DATA_ >> ADMIN
    # SLOT FUNCS
    def new_entry(self, f_date, new_slots, client_data):
        # SETS NEW SLOTS WITH 
        try:
            i_ = ["%#!:FALSE*", "N$:NONE*", "E$:NONE*", "B#$:NONE*", "S#$:NONE*", "P#$:NONE*", "C#$:NONE*"]
            ret_slot = [i_,i_,i_,i_,i_,i_,i_,i_,i_,i_,i_,i_,i_,i_,i_,i_,i_,i_,i_]
            for i, val in enumerate(new_slots):
                if i >= 19:
                    break
                #print(f" new_ent-> I: {str(i)} VAL: {str(val)}")
                if "True" in str(val):
                    # IF SLOT BEING BOOKED :: SET_SLOT_VAL >> CLIENT_DATA
                    try:
                        cl_num = str("%#!:FALSE*")
                        client_data[0] = cl_num
                        ret_slot[i] = client_data
                    except Exception as e:
                        print("[ERROR]:[NEW_ENTRY]:[SLOT_NUM]: ", str(e))
                else:
                    ret_slot[i] = ["%#!:FALSE*", "N$:NONE*", "E$:NONE*", "B#$:NONE*", "S#$:NONE*", "P#$:NONE*", "C#$:NONE*"]
            return ret_slot
        except Exception as e:
            print('[ERROR]:[NEW_ENTRY]', str(e))

    def get_slot_by_Date(self, date_):
        #print("DATE_TO_FIND: ", str(date_))
        # return ?[DATE: [slot#[#,#,#,#,#]], [slot#[#,#,#,#,#]], [slot#[#,#,#,#,#]],..]
        try:
            u_stack = self.FM.read_file("dataBase/BOAT_1_CLIENT.txt", "?")
            for slots in u_stack:
                #print("\n@::",str(slots))
                if str(date_) in str(slots):
                    #print("\n@::",str(slots))
                    #print(":Y:")
                    return slots
        except Exception as e:
            print("[ERROR]:[GET_SLoT_BY_DATE]: ", str(e))

    def str_to_slots(self, old_slots):
        try:
            #print("STR_TO_SLOT:::::")
            client_data = []
            item_ = ["","","","","","",""]
            item_2 = ["%#!:FALSE*", "N$:NONE*", "E$:NONE*", "B#$:NONE*", "S#$:NONE*", "P#$:NONE*", "C#$:NONE*"]
            ret_slot  = []  #= [item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_,item_]
            #print("\n\n\n::::str_to_slots:::\n\n")

            break_str = old_slots.split("&")
            #print("[STR_TO_SLOTS]:DATE:: ", str(break_str[1]))
            #print("[STR_TO_SLOTS]:FODIS:: ", str(break_str[2]))

            # BREAK INTO SLOTS
            slot_str = str(break_str[2]).split("%")
            for i, val in enumerate(slot_str):
                #print("FF: ", str(i))
                if len(val) >= 35 and i <= 19:
                    client_data = val.split("*")
                    #print("CL__: ", str(client_data))
                    if "REMOVE" in str(client_data):
                        item_= ["%#!:FALSE*", "N$:REMOVED*", "E$:REMOVED*", "B#$:REMOVED*", "S#$:REMOVED*", "P#$:REMOVED*", "C#$:REMOVED*"]
                        ret_slot.append(item_)
                        item_ = ["","","","","","",""]
                    else:
                        for j, cVal in enumerate(client_data):
                            sVal = cVal.translate(str.maketrans("","","['&, ]"))
                            #print("CL_s_: ", str(j),"::", str(sVal))
                            if "#!:" in sVal:
                                item_[0] = "%"+str(sVal)+"*"
                            if "N$:" in sVal:
                                item_[1] = str(sVal)+"*"
                            if "E$:" in sVal:
                                item_[2] = str(sVal)+"*"
                            if "B#$:" in sVal:
                                item_[3] = str(sVal)+"*"
                            if "S#$:" in sVal:
                                item_[4] = str(sVal)+"*"
                            if "P#$:" in sVal:
                                item_[5] = str(sVal)+"*"
                            if "C#$:" in sVal:
                                item_[6] = str(sVal)+"*"
                            if j == 6:
                                break
                        ret_slot.append(item_)
                        item_ = ["","","","","","",""]
            return ret_slot
        except Exception as e:
            print("[ERROR]:[STR_TO_SLOTS]:",str(e))

    def entry_update(self, f_date, new_slots, set_old_slots, client_data):
        try:
            print("\n**********************************************\n", "[ENTRY_UPDATE]")

            date_ = str(f_date[4:])
            ret_slot = ["","","","","","","","","","","","","","","","","","",""]
            # GET OLD SLOTS
            # UPDATE SLOT >> RET_SLOT
            for n, sl_ in enumerate(set_old_slots):
                # APPEND EITHER {OLD_CLIENT_SLOT || NEW_CLIENT_SLOT} >> RET_SLOT
                #print("\nWTF::\n::??n_ss", str(new_slots[n]), ":::::o_SS", str(set_old_slots[n]))
                if "REMOVED" in str(new_slots[n]):
                    try:
                        # CHECK NEW SLOT VAL
                        ret_slot[n] = ["%#!:FALSE*", "N$:REMOVED*", "E$:REMOVED*", "B#$:REMOVED*", "S#$:REMOVED*", "P#$:REMOVED*", "C#$:REMOVED*"]

                        #print("::\n::\n:THE REMOVED::\n::\n:? ",str(n), str(ret_slot[n]))
                        continue
                    except Exception as e:
                        print("[ERROR]:[REMOVING]", str(e))

                elif "NONE" not in str(new_slots[n]):
                    try:
                        ret_slot[n] = new_slots[n]
                        #print("::\n::\n:THE NEW_ADDED::\n::\n:? ",str(n), str(ret_slot[n]))
                    except Exception as e:
                        print("[ERROR]:[REMOVING]", str(e))
                else: 
                    try:
                        # CHECK NEW SLOT VAL
                        ret_slot[n] = set_old_slots[n]
                    except Exception as e:
                        print("[ERROR]:[REMOVING]", str(e))
        
                #print("::\n::\n:THE OLD_STAYS::\n::\n:? ",str(n), str(ret_slot[n]))

                #print("::\n::\n:THE PROOOOOOBLEM::\n::\n:? ",str(n))

            # RETURN UPDATED SLOTS_LIST
            return ret_slot
        except Exception as e:
            print("[ERROR]:[ENTRY_UPDATE]:[BREAK_DATA]:", str(e))


    # STACK FUNCS
    def set_stack(self):
        # GET ALL STACK ITEMS:: 
            # RETURN >> STACK_LIST = [@[DATE[...]], @[DATE[...]], @.. ]
        try:
            ret_stack = []
            stack_item = []
            clean_slot = []
            ret_slot = []
            f_date = ""
            stack_dates = self.get_stack_dates()
            # LOOP STACK_DATES_LIST
            # >> STR_TO_SLOTS
            for n, val in enumerate(stack_dates):
                stack_item = self.get_slot_by_Date(val)
                clean_slot = self.str_to_slots(stack_item)
                # INSERT DATE TO STACK ITEM
                f_date = "&D1$:"+str(val)
                ret_slot = [f_date, clean_slot]
                ret_stack.append(ret_slot)
            return ret_stack
        except Exception as e:
            print("[ERROR]:[SET_STACK]:", str(e))

    def get_stack_dates(self):
        try:
            stack_dates = []
            #print("\n\n!!GET_STACK_DATES!!\n\n")
            u_stack = self.FM.read_file("dataBase/BOAT_1_CLIENT.txt", "?")
            for date_ in u_stack:
                if len(date_) > 9:
                    #print("[?IS_DATE]::[",str(date_[5:9]),"]")
                    try:
                        temp = str(date_[5:9])
                        datetime.strptime(temp, "%Y").year
                        stack_dates.append(str(date_[5:15]))
                        #print("[STACK_DATE]::",str(date_[5:15]))
                    except Exception as e:
                        pass
            return stack_dates
        except Exception as e:
            print("[ERROR]:[GET_STACK_DATES]: ", str(e))

    def check_dates(self, date):
        try:
            #print("GET_STACK_DATES")
            u_stack = self.FM.read_file("dataBase/BOAT_1_CLIENT.txt", "?")
            for date_ in u_stack:
                if date in date_:
                    print("DATE_IS_HERE: ", str(date))
                    return True
            return False
        except Exception as e:
            print("[ERROR]:[GET_STACK_DATES]: ", str(e))

    def update_stack(self, date_, new_item, set_stack_):
        #print("NEXT_\nUPDATE_\nSTACK_\n", "::[", str(date_),"]::\n")
        # UPDATE NEW_SLOTS TO STACK >> RETURN NEW_STACK_LIST
        try:
            ret_stack_ = []
            for i, val in enumerate(set_stack_):
                if len(val) >= 2:
                    #print("::I::", str(i), "::VAL::", str(val[0]), "::\n\n")
                    if  date_ in str(val[0]):
                        #print("DATE_MATCHED:: NOW UPDATE THAT :<", str(val))
                        ret_stack_.append(new_item)
                    else:
                        ret_stack_.append(val)
            return ret_stack_
        except Exception as e:
            print("[ERROR]:[UPDATE_STACK_]:",str(e))

    def check_stack(self, set_stack):
        for item in set_stack:
            #print("\nITEM[0]:", str(item[0]))
            #print("\nITEM[1]:", str(item[1]))
            if item[1]:
                for slot in item[1]:
                    print("SLOT:&&:", str(slot))
            else:
                print("[WARNING]:[CHECK_STACK]:[INDEX_OoR]:", str(item))

    def data_to_write(self, dt, rwm):
        try:
            ready_item = ""
            if rwm == "a":
                try:
                    with open("dataBase/BOAT_1_CLIENT.txt", rwm) as wf:
                        wf.write(dt)
                        wf.close()
                    return
                except Exception as e:
                    print("[ERROR]:[DATA_TO_WRITE]:[APPEND]: ",str(e))
                #print("!!!!!!!!!!!!!!\nAPPENDED!!!!!!!!!!!!!!\n!!!!!!!!!!!!!")
                return
            elif rwm == "w":
                # THIS WILL TURNICATE DATA FILE !!!!
                try:
                    #print("!!!!!!!!!!!!!!!\nTURNICATING\n!!!!!!!!!!!!!!!!!!!\nBOAT_1_CLIENT\n!!!!!!!!!!!!!!!!!!!")
                    self.FM.write_file("dataBase/BOAT_1_CLIENT.txt", "", "", "w")
                    for item in dt:
                        try:
                            ready_item = "?"+str(item[0])+"&"+str(item[1])
                            set_item = ready_item.replace("\\", "")+"&\n"
                            with open("dataBase/BOAT_1_CLIENT.txt", "a") as wf:
                                #print("[WRITING_NEW_STACK]:\n #######\n", str(ready_item), "\n$$$$$$$$$$$$$$\n")
                                wf.write(set_item)
                                wf.close()
                        except Exception as e:
                            print("[![TRUNICATION]![ERROR]!]:[!DATA_NOT_WRITTEN!]\n{{--",str(e),"--}}\n")
                except Exception as e:
                    print("[ERROR]:[DATA_TO_WRITE]:[APPEND]: ",str(e))
        except Exception as e:
            print("[ERROR]:[DATA_TO_WRITE]:",str(e))

    # MAIN CLIENT DATA UPDATE FUNC
    def update_new_slots(self, date_, new_slots, client_data):
        try:
            #print("F_DATE::: ", str(date_))
            ## SET NEW SLOTS >> LIST_FORMAT
            #print("SETTING NEW_SLOTS")
            new_set_slots = self.new_entry(date_, new_slots, client_data)
            # COMPARE & UPDATE (OLD_SLOTS || NEW_SLOTS >> RET_SLOTS)
                # IF THE THE DATE DOES EVEN FUCKN EXISTS!!
            if self.check_dates(date_) != False:
                old_slots = self.get_slot_by_Date(date_)    # RETURNS STR "@2022/11/30*True&True&True&F..."

                set_old_slots = self.str_to_slots(old_slots) # LIST ""

                #print("OLD_SLOT+FROM[GET_BY_DATES]:: ")
                #for s in set_old_slots:
                #    print("OLD_SLOTS: ", str(s))
                print("\n**********************************************\n")
                updated_slots = self.entry_update(date_, new_set_slots, set_old_slots, client_data)

                #for slots in updated_slots:
                #    print("UPDATED_SLOT: ", str(slots))



                # SET STACK 
                #print("SETTING_STACK")
                set_stack_ = self.set_stack()

                # CHECK THE STACK..
                #print("\nSTACK_BEFORE_UPDATE\n  @ ")
                #print("*********************\n")
                #self.check_stack(set_stack_)
                #print("*********************\n")

                # UPDATE STACK
                new_stack_item = [date_, updated_slots]

    
                new_stack = self.update_stack(date_, new_stack_item, set_stack_)
                ## CHECK UPDATE
                #print("\nSTACK_AFTER_UPDATE\n")
                #print("*********************\n")
                ##self.check_stack(new_stack)
                #print("*********************\n")
                ## WRITE UPDATES TO DUMMY.txt
                print("[DATE_FOUND]:!:[TURNICATING]")
                self.data_to_write(new_stack, "w")
            else:
                #print("DATE_NOT_FOUND_NEW_LISTING\n", str(new_set_slots))
                ready_item = "?"+str(date_)+"&"+str(new_set_slots)+"&\n"
                self.data_to_write(ready_item, "a")
        except Exception as e:
            print("[Update_New_Slots]: ", str(e))

    # RETRIEVE THE FULL DATA STACK
    def pull_stack(self):
        try:
            # GET ALL DATES 
            # LOOP THROUGH DATES
            # DATE_ = GET_SLOT_BY_DATE
                # str_to_list -> each_
            #print("GETTING_STACK:: ")
            slot_str = ""
            slot_lst = []
            ret_stack = []
            date_list = self.get_stack_dates()
            for i, date_ in enumerate(date_list):
                #print(":i:", str(i), ":date_:", str(date_))
                if date_:
                    slot_str = self.get_slot_by_Date(date_)
                    if slot_str:
                        slot_lst = self.str_to_slots(slot_str)
                        if slot_lst:
                            ret_stack.append(["?",date_, slot_lst])
                            slot_str = ""
                            slot_lst = []
            #self.show_list(ret_stack)

        
            #for k in ret_stack:
            #    print("KARDAEO:", str(k))
            return ret_stack
        except Exception as e:
            print("[ERROR]:[PULL_STACK]:[BREAK_DATA]:",str(e))

    # SLOT_SET FOR RM OF SLOT
    def rm_slot(self, date_, slot_index):
        try:
            #print("[RM_DATE_]:",str(date_))
            #print("[SLOT_INDEX]:", str(slot_index))
            rm_slots = ["","","","","","","","","","","","","","","","","","",""]
            rm_item_ = ["%#!:FALSE*", "N$:REMOVED*", "E$:REMOVED*", "B#$:REMOVED*", "S#$:REMOVED*", "P#$:REMOVED*", "C#$:REMOVED*"]

            for i in rm_slots:
                i = "NONE"#["%:", "N$:NONE", "E$:NONE", "S#$:NONE", "P#$:NONE", "C#$:NONE"]
            rm_slots[int(slot_index)] = True
            #print(str(rm_slots))

            self.update_new_slots("&D1$:"+date_, rm_slots, rm_item_)
        except Exception as e:
            print("[ERROR]:[RM_SLOT]:[BREAK_DATA]",str(e))

    def gap_slot(self, slots):
        try:
            ret_slot = ["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False"]
            #print("SETTING_GAP_SLOT")
            for i, val in enumerate(slots):
                print("I_I:",str(i))
                if  int(i+1) >= 19:
                    if "True" in str(slots[i]):
                        ret_slot[i] = "True"
                    break
                elif "True" in str(slots[i]) and "True" in str(slots[i+1]):
                    ret_slot[i] = "True"
                elif "True" in str(slots[i]) and "False" in str(slots[i+1]):
                    ret_slot[i] = "True"
                    ret_slot[i+1] = "True"


            return ret_slot
        except Exception as e:
            print("[ERROR]:[GAP_SLOTS]:",str(e))


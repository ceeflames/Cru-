import os
import pathlib
import time
import requests
from pip._vendor import cachecontrol

#FLASK IMPORTS
from flask import Flask, render_template, redirect, url_for, request, flash, Response, session, abort
from datetime import datetime

# FALSK EMAILER
from flask_mail import Mail, Message

# FLASK_LOGIN
from werkzeug.security import generate_password_hash, check_password_hash

#LOCAL IMPORTS
from file_handle import File_man
from list_sys import Slot_Update, Break_Data
from emails import Register, Login, Forgot
from users_ import User_Set


# INIT THE APP
app=Flask(__name__)

# INIT MAIL(APP)
mail = Mail(app)
mail.init_app(app)

# SECRETE KEY
app.secret_key = "TheBoats268!"
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

#################
# CONFIG SETUP #
try:
    app.config['MAIL_SERVER']='smtp.mail.yahoo.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'custom.vm@yahoo.com'
    app.config['MAIL_PASSWORD'] = 'vogtgrfvobdnxypj'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_.db'
except Exception as e:
    print("[ERROR]:[EMAIL_CONFIG]")

mail = Mail(app)

###       HOME PAGE         ###
@app.route('/', methods=["GET", "POST"])
def index():

        # DECLARE ALL VARIABLES (FLASK_PAIN)
    try:
        news_update = File_man().read_file("dataBase/NEWS.txt", "*")
        news_data = str(news_update[0][:-2])

        #HOLDS
        set_name = ""
        set_mail = ""
        set_beach = ""
        set_speed = ""
        set_people_num = ""
        set_child_num = ""
        set_price = ""
        set_cel = ""
        set_msg = ""


        # DATA_BASE
        boat_1_books = []
        # USER _INPUT
        right_format = []
        bookings = []
        pay_ = "%#!:FALSE*"   # TO BE REPLACED WITH PayPal UID_CODE
        name_ = "N$:NONE*"      # N$:
        email_ = "E$:NONE*"
        beach_ = "B#$:NONE*"
        speed_ = "S#$:NONE*"     # S#$:
        people_num = "P#$:NONE*" # P#$:
        child_num = "C#$:*"  # c#$:
        boat_num = ""   # B#$:
        date_1 = ""     # D1$:
        time_slot = ""  # T1$:
        set_date = ""
        f_date = ""
        sub_name = ""
        price_ = ""
        fin_ = ""
        ref_ = "REF: "
        slot_count = 0
        dt = []
        dt_w = ""
        client_data = ["%#!:FALSE*", "N$:NONE*", "E$:NONE*", "B#$:NONE*", "S#$:NONE*", "P#$:NONE*", "C#$:*"]
    except:
        print("VARIABLE_ERROR??: index('/')")
    if request.method == 'POST':
        # BOOKINGS FORMS
        try:
            # STANDARD BOOKING
            if request.form['submit_button'] == 'Book Now':
                print("BOOKING_MADE>>>")
                # BASE DATA COLLECTION
                try:
                    # CLIENT DATA
                    print("ATTEMPTING")
                    try:
                        set_name = request.form['client-name']
                        name_ = "N$:" + set_name + "*"

                        set_mail = request.form['client-email']
                        email_ = "E$:" + set_mail +"*"

                        try:
                            set_cel = request.form['phum']
                            set_msg = request.form['user-msg-pb']
                        except Exception as e:
                            print("CEL_NUMBER BS\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", str(e))

                        set_beach = request.form['beach-select']
                        beach_ = "B#$:" + set_beach + "*"

                        set_speed = request.form['speed-select']
                        speed_ = "S#$:" + set_speed + "*"

                        set_people_num = request.form['people-select']
                        people_num = "P#$:" + set_people_num + "*"


                        if request.form.get('child-count') != None:
                            set_child_num = request.form['child-count']
                            child_num = "C#$:" + set_child_num + "*"
                        else:
                            set_child_num = "0"
                            child_num = "C#$:*"

                        
                        fin_ = request.form.get('hidden_tot')
                        price_ = request.form.get('price_')
                        print("PRICE FROM HIDDEN_TOT:: ", str(fin_), "::PRICE_",str(price_))
                        
                        try:
                            price_ = "USD_$:"+str(fin_)+ "*"
                            print("######$$$$$$$$\n\nFIN_PRICE:: \n\n[", str(price_), "]\n\n##################")
                        except Exception as e:
                            print("[ERROR]:[GETTING_PRICE]:", str(e))
                        try:
                            File_man().write_file("dataBase/EMAILS.txt", set_mail, "", "a")
                        except Exception as e:
                            print("[ERROR]:[SETTING_EMAIL]:", str(e))
                    except Exception as e:
                        print("[ERROR]:[GETTING_CLIENT_DATA]", str(e))

                    # CALENDAR SELECTION {DATE}
                    date_1 =  request.form['calendar1']
                except Exception as e:
                    print("BASE_BOOKING_ERROR:: ", str(e))

                # BOOKING SLOTS
                try:
                    time_0 = request.form.get('30_slot0') != None
                    time_1 = request.form.get('30_slot1') != None
                    time_2 = request.form.get('30_slot2') != None
                    time_3 = request.form.get('30_slot3') != None
                    time_4 = request.form.get('30_slot4') != None
                    time_5 = request.form.get('30_slot5') != None
                    time_6 = request.form.get('30_slot6') != None
                    time_7 = request.form.get('30_slot7') != None
                    time_8 = request.form.get('30_slot8') != None
                    time_9 = request.form.get('30_slot9') != None
                    time_10 = request.form.get('30_slot10') != None
                    time_11 = request.form.get('30_slot11') != None
                    time_12 = request.form.get('30_slot12') != None
                    time_13 = request.form.get('30_slot13') != None
                    time_14 = request.form.get('30_slot14') != None
                    time_15 = request.form.get('30_slot15') != None
                    time_16 = request.form.get('30_slot16') != None
                    time_17 = request.form.get('30_slot17') != None
                    time_18 = request.form.get('30_slot18') != None
                except Exception as e:
                    print("[ERROR]:[GET_SLOTS]:",str(e))

                # CORRECT FORMAT
                try:
                    wrong_date = date_1.split("/")
                    right_format = [str(wrong_date[2]),"/",str(wrong_date[0]),"/",str(wrong_date[1])]
                    # DATE[LIST] -> DATE[STRING]
                    set_date = ""
                    for i in right_format:
                        set_date+=str(i)
                    f_date = "&D1$:" + str(set_date)
                except Exception as e:
                    print("[ERROR]:[SET_F_DATE]:",str(e))
                
                # CALENDAR UPDATE "DNT"
                try:
                    # FOR CALENDAR DATA
                    new_slots =  [time_0, time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8, time_9, time_10, time_11, time_12, time_13, time_14, time_15, time_16, time_17, time_18]
                    new_slot_gap = Break_Data().gap_slot(new_slots)
                    c_t = [set_date, new_slot_gap]

                    for i in new_slots:
                        if "True" in str(i):
                            slot_count+=1
                    ref_ = "REF_"+set_date+"@"+str(slot_count)
                    #UPDATE CLAENDAR DATA
                    Slot_Update().new_time_slots(c_t, "dataBase/CAL_DATES.txt", "@")
                except Exception as e:
                    print("[ERROR]:[UPDATING_DATE/SLOT]:",str(e))
                # CALENDAR UPDATE "DNT"

                # CLIENT BOAKING_DATA_
                try:
                    #UPDATE CLIENT DATA
                    # FOR CLIENT DATA
                    client_data = ["%#!:FALSE*", name_, email_, beach_,  speed_, people_num, child_num]
                    Break_Data().show_list(client_data)

                    # UPDATE "BOAT_1_CLIENT.txt"


                    # GAP SLOTS
                    try:

                        new_ent = Break_Data().update_new_slots(f_date, new_slot_gap, client_data)

                    except Exception as e:
                        print("[ERROR]:[NEW_GAP]:",str(e))
                    # MAKE TIME SLOT VALUE ADAPTOR
                #  send new_ent as email to all bot client and admin
                except Exception as e:
                    print("[ERROR]:[CLIENT_DATA]:",str(e))
                try:
                    msg = Message(f"BOOKING ON THUNDERCATS268 FOR {str(set_name)} MADE!",sender = 'custom.vm@yahoo.com', recipients = [str(set_mail), "thundercats268antigua@gmail.com"])
                    msg.html =  User_Set().craft_booking_email(set_name, date_1, set_cel, set_beach, set_speed, set_people_num, set_child_num, new_slots, ref_,  fin_) 
                    mail.send(msg)
                    print("[SENT_EMAIL]:[NAME]:[",str(set_name), "]:[EMAIL]:[", str(set_mail),"]")
                except Exception as e:
                    print("[ERROR]:[BOOKING_EMAIL]", str(e))
            # CUSTOM BOOKINGS
            elif request.form['submit_button'] == "Contact Now":
                print("CONTACT NOW")
                try:
                    name_pb = request.form['client-name']
                    set_mail_ = request.form['client-email']
                    phum = request.form['phum']
                    user_msg = request.form['user-msg-pb']
                    File_man().write_file("dataBase/EMAILS.txt", set_mail_, "", "a")
                    print("CUSTOM BOOKING TO BE EMAILED")
                    print(f"NAME: {name_pb} \nEMAIL: {set_mail_} \nPHONE: {phum} \nMSG: {user_msg}\n\n")
                    try:
                        msg = Message(f"THANK YOU {str(name_pb)} FOR CONTACTING US ",sender = 'custom.vm@yahoo.com', recipients = [str(set_mail_), "thundercats268antigua@gmail.com"])
                        msg.html =  User_Set().craft_custom_booking_email(name_pb, set_mail_, phum,  user_msg)
                        mail.send(msg)
                        print("[SENT_EMAIL]:[NAME]:[",str(name_pb), "]:[EMAIL]:[", str(set_mail_),"]")
                    except Exception as e:
                        print("[ERROR]:[BOOKING_EMAIL]", str(e))
                except Exception as e:
                    print("[ERROR]:[CUSTOM_BOOKINGS]:",str(e))
        except Exception as e:
            print("[ERROR]:[SUMBIT]:[BOOKINGS]:: ", str(e))
            pass
        # NEW SUBSCRIBERS
        try:
            if request.form['submit_button'] == 'SUBSCRIBE':
                print("NEW_SUB__:_:_:\n")
                on_set = []
                try:
                    print("NEW_SUB__:\n")
                    sub_name = request.form.get('name_sub')
                    name_sub = "N$:" + sub_name  + "*"
                    print("NAME:: ", str(name_sub))

                    sub_email = request.form.get('email_sub')
                    email_sub = "E$:"+ sub_email +"*"
                    print("EMAIL:: ", str(email_sub))

                    sub_msg = request.form.get('msg_sub')
                    msg_sub = "M$:" + sub_msg+ "*"
                    print("MSG:: ", str(msg_sub))

                    File_man().write_file("dataBase/EMAILS.txt", sub_email, "", "a")
                    user_data = [name_sub, email_sub, msg_sub]
                    print("\nNEW SUB\n", str(name_sub), str(email_sub), str(msg_sub), "\n")
                    on_set = User_Set().add_user(user_data)
                    if on_set[0] == False:
                        print("NEW_USER:: ", str(on_set[1]))
                        flash(message=f"WELCOME SUBSCRIBER :) [{str(name_sub)}]")
                        
                    if on_set[0] == True:
                        print("OLD_USER:: ", str(on_set[1]))
                        flash(message=f"ALREADY SUBSCRIBED :) [{str(name_sub)}]")

                    try:
                        msg = Message(f"WELCOME {sub_name} TO THUNDERCATS268",sender = 'custom.vm@yahoo.com', recipients = ['thundercats268antigua@gmail.com', str(sub_email)])


                        msg.html = User_Set().craft_new_sub(sub_name, sub_email, sub_msg)
                        #msg.body = f"WELCOME {str(sub_name)} TO THUNDERCATS268!"
                        mail.send(msg)
                        print("[SENT_EMAIL]:[NAME]:[",str(sub_name), "]:[EMAIL]:[", str(sub_email),"]")
                    except Exception as e:
                        print("[ERROR]:[SENDING_SUB_CONFIRM]:", str(e))
                    return redirect(request.url)
                except Exception as e:
                    print("[ERROR]:[UPDATING_SUBS]:", str(e))
                #return render_template('index_.html', full_dates=full_dates, boat_1_dates=set_book, show_news=news_data )
        except print(0):
            pass


    
    
    try:
        try:
            boat_1_books = File_man().read_file("dataBase/CAL_DATES.txt", "@")
            set_book = ""
            pre_ = ""
            for i in boat_1_books:
                pre_ = "@"+str(i)
                set_book += pre_
                pre_ = ""
            print("set_book::: ",str(set_book))
            # FILTER OUT DATA -> GET DATES: COMBINE DATES_TIME_SLOTS
            full_dates = Slot_Update().full_dates(boat_1_books)
            about_ = str(File_man().read_file("dataBase/PARA.txt", "*")[0][:-2])
            print("\n*****\n#####\nABOUT: \n", about_)
        except:
            about_ = "[ERROR]"
            print("[ERROR]:[ABOUT_]:")
        return render_template('index_.html', full_dates=full_dates, boat_1_dates=set_book, show_news=news_data, para=about_)
    except Exception as e:
        print("[ERROR]:[DATA_BASE]:[HOME]:",str(e))
        return render_template('index_.html', full_dates=full_dates, boat_1_dates=set_book, show_news=news_data, para=about_)

@app.route("/user/<name>", methods=["GET","POST"])
def users(name):
    return render_template("users_.html", name=name)

## READ THE DATA FROM dataBase/NEWS_LETTER.txt ## ToDo... tjis funct is not available yet
@app.route('/mailer', methods=[ "GET","POST"])
def mailer_():
    recipt_s = list(File_man().get_file_list("dataBase/EMAILS.txt", "\n"))
    msg = Message("HELLO:",sender = 'custom.vm@yahoo.com', recipients = ['DillonB_ach@yahoo.com', 'conorwright@thundercats268.com', recipt_s ])
    msg.body = "GET THIS PART FROM THE STATIC DATA_BASE"#
    mail.send(msg)
    return "SENT"


###       ADMIN PAGE        ###
@app.route('/myAdmin', methods=["GET", "POST"])
def admin():
    if "TC268!@" in session["state"]:
        print("SESSION:: ", str(session))
        try:
            # # # 
            # ToDo::
            # # #
            # UPDATES ALL NEWS/EVENTS:
                # FRONT PAGE -> *** CLEAN DATA ***
                # EMAIL ALL SUBSCRIBERS

            if request.method == 'POST':
                try:
                    if request.form['emailer'] == "SEND":
                        print("#############\nREQUEST=>SEND NEWSLETTER\n###################")
                        subject_text = request.form['subject']
                        body_text = str(request.form['body'])
                        foot_note = str(request.form['foot-note'])
                        print("SENDING>>>?: \n", str(subject_text), "\n:**:\n", str(body_text), "n\:**:\n", str(foot_note))
                        try:
                            recipt_s = list(File_man().get_file_list("dataBase/EMAILS.txt", "\n"))

                            for i in recipt_s:
                                print("RECPIENT:: ", str(i))
                                try:
                                    msg = Message(f"SUBJECT: {str(subject_text)} ..", sender='custom.vm@yahoo.com' ,recipients=[str(i)])
                                    print("MSG_MADE")
                                    msg.body = User_Set().craft_news_letter(body_text, foot_note)
                                    mail.send(msg)
                                    print("MSG_SENT>>>?")
                                except Exception as e:
                                    print("SEND_ERROR")
                                    print(str(e))

                        except Exception as e:
                            print("[ERROR]:[SENDING_NEWS_LETTER]:", str(e))
                except Exception as e:
                    print("[ERROR]:[NEWS_LETTER_SEND]:",str(e))

                try:
                    if request.form['submit_it'] == 'DELETE_SLOT':
                        print("\n\n\n\n\n\n\n\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nDELETING>>>")

                        try:
                            date_ = request.form['date_']
                            slot_num = request.form['slot_num']
                            name_ = request.form['user_name']
                            mail_ = request.form['user_email']
                            print("\n@\n#\n!\n::DATE:: ", str(date_), "\n::SLOT_::", str(slot_num), "\n::NAME_::", str(name_), "\n::EMAIL_::", str(mail_), ":::@\n#\n")

                            # GET THE SLOT VALUE
                            if len(slot_num) == 11:
                                print("[SLOT_INDEX]:", str(slot_num[-2:]))
                                lst_index = slot_num[-2:]
                            elif len(slot_num) == 10:
                                print("[SLOT_INDEX]:", str(slot_num[-1]))
                                lst_index = slot_num[-1]

                            Slot_Update().open_slot(date_, lst_index)
                            print("OPENING_SLOT_BY_INDEX")

                            Break_Data().rm_slot(date_, lst_index)

                        except Exception as e:
                            print("[ERROR]:[SLOT_INDEX_UPDATE]:", str(e))
                except Exception as e:
                    print("GET_REQ ERROR ", str(e))

                    #UPDATE FROM ADMIN
                try:
                    if request.form['news']:
                        news_i =request.form["in_put"]
                        File_man().write_file("dataBase/NEWS.txt", news_i, "*", "w")
                except Exception as e:
                    print("[ERROR]:[LOADING_NEWS]:", str(e))

                #UPDATE FROM ADMIN
                try:
                    if request.form['about']:
                        para_=request.form["para-set"]
                        File_man().write_file("dataBase/PARA.txt", para_, "*", "w")
                except Exception as e:
                    print("[ERROR]:[LOADING_NEWS]:", str(e))

            try:
                # UPDATE TO ADMIN
                try:
                    news_ = str(File_man().read_file("dataBase/NEWS.txt", "*")[0][:-2])
                    print("\n*****\n#####\nNEWS: \n")
                except:
                    news_ = "[ERROR]"
                    print("[ERROR]:[NEWS_]:")
                try:
                    about_ = str(File_man().read_file("dataBase/PARA.txt", "*")[0][:-2])
                    print("\n*****\n#####\nNEWS: \n")
                except:
                    about_ = "[ERROR]"
                    print("[ERROR]:[ABOUT_]:")
                try:
                    bookings = Break_Data().pull_stack()
                    print("\n*****\n#####\nSTACK_PULL: \n")
                except:
                    bookings = "[ERROR]"
                    print("[ERROR]:[BOOKINGS]:")
                try:
                    boat_1_books = File_man().read_file("dataBase/CAL_DATES.txt", "@")
                    print("\n*****\n#####\nBAOT_1_BOOK: \n")
                except:
                    boat_1_books = "[ERROR]"
                    print("[ERROR]:[BOAT_!_BOOK]:")
                try:
                    full_dates = Slot_Update().full_dates(boat_1_books)
                    print("\n*****\n#####\nFULL_DATES: \n")
                except:
                    full_dates = "[ERROR]"
                    print("[ERROR]:[FULL_DATES]:")
                try:
                    #our_users = Users_.query.all()
                    our_users = User_Set().get_set_users()
                    print("\n*****\n#####\nSET_USERS: \n", str(our_users))
                except Exception as e:
                    our_users = "[ERROR]"
                    print("[ERROR]:[USERS]:", str(e))
                    pass

                return render_template("admin_.html",news_up=news_,bookings=bookings,  users=our_users, about=about_)
            except Exception as e:
                print("E:admin:", str(e))
                return render_template("admin_.html", news_up="[ERROR]")

        except Exception as e:
            print("E:admin:LOGIN:", str(e))
            return render_template("/login")
    else:
        return redirect(url_for("index"))

@app.route('/login', methods=["GET","POST"])
def login():
    pswd = ""
    if request.method == 'POST':
        try:
            if request.form['submit_pswd'] == 'login':
                pswd = str(request.form['PSWD'])
                print("PSWD:: ", str(pswd))
                if "TC268" in pswd:
                    try:
                        session["state"] = pswd

                    except Exception as se:
                        print("[ERROR]:[SEESION]:",str(se))
                    return redirect(url_for("admin"))
                else:
                    return redirect(url_for("index"))

        except Exception as e:
            print("[ERROR]:[LOGIN]:",str(e))

    return render_template("login_admin.html")

@app.route('/callback', methods=["GET","POST"])
def callback():
    #flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500) # State doe not match
        return redirect(url_for("index"))

@app.route('/logout', methods=["GET","POST"])
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/calendar', methods=["GET", "POST"])
def calendar():
    return render_template('calendar.html')

if __name__=='__main__':
    app.run(debug=False)

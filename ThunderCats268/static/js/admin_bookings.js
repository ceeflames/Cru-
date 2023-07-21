
console.log("AMDIN.JS")




var current_date;
var current_slot;
var set_email;
var set_name;
var set_beach;

const s_data = ["%#!:FALSE*", "N$:NONE*", "E$:NONE*", "B#$:NONE*", "S#$:NONE*", "P#$:NONE*", "C#$:NONE*"]

const del_popup = document.querySelector('.del_popup');
const popup_close = document.querySelector('.close');



// send_del_request
var del_Req = document.querySelector('.del_');
function hit_that()
{
    var del_date = document.querySelector('#del_date');
    var del_slot = document.querySelector('#del_slot');
    var user_email = document.querySelector('#del_data');
    var user_name = document.querySelector('#del_name');

    
    del_date.value = current_date;
    del_slot.value = current_slot;
    user_email.value = set_email;
    user_name.value = set_name;


    console.log("DEL_DATE", current_date);
    console.log("DEL_DATE", del_date.value);
    console.log("DEL_SLOT", current_slot);
    console.log("DEL_SLOT", del_slot.value);

}

popup_close.addEventListener("click", function(){
    del_popup.style.display = 'none';

});




try{
    function filter_mail(temp_)
    {
        let myList = temp_.split("|EMAIL|:----------")[1]
        let mail__ = myList.split("|BEACH|")[0]
        console.log("\n\nTHIS EMAIL?\n\n?::: ", mail__)
        return mail__
    }


    function del_popup_open(user_data, slot_)
    {
        console.log("DELETING_USER_???", slot_);

        document.getElementById('u_name').innerHTML = user_data;
        console.log("SLOT_: ", slot_);
        var temp_ = document.getElementById(slot_).textContent;
        var mail_ = filter_mail(temp_);
        console.log("CONTACT_USER_???", mail_);
        document.getElementById('u_mail').innerHTML = "<br><br><a style='background-color: lime; padding: 5px 5px; border-radius: 0.4rem;' href='mailto: "+mail_+"'>" +"EMAIL: "+mail_+"</a>";

        del_popup.style.display = 'flex';

    }
}
catch
{
    console.log(":::::uhm, poup not open?")
}


var slot_list = [
    "6:30-7:00",
    "7:00-7:30",
    "7:30-8:00",
    "8:00-8:30",   
    "8:30-9:00",
    "9:00-9:30",
    "9:30-10:00",
    "10:00-10:30", 
    "10:30-11:00", 
    "11:00-11:30",
    "11:30-12:00",
    "12:00-12:30",
    "12:30-13:00",
    "13:00-13:30",
    "13:30-14:00",
    "14:30-14:30",
    "14:30-15:00",
    "15:00-15:30",
    "15:30-16:00"
]




// PROMPT FOR SLOT UPDATE
try
{
    // SELECTED TIME SLOTS {ToDo: COLOR_CHANGE}
var items = document.querySelectorAll("#t30m_slots li");
for(var i = 0; i < items.length; i++)
{

    let li_ti_ = "ti30_slot"+i;
    let li_id_a = "t30_a_"+i;
    //let val = document.getElementById(li_id).checked;
    //console.log("VAL:0: ", li_id_a);
    items[i].onclick = function(e){



        console.log("LOADING_SLOTS:; ", li_ti_);
        current_slot = li_ti_;

        //document.getElementById(li_ti_).click();
        let val1 = document.getElementById(li_id_a).innerHTML;
        console.log("CURRENT_innerHTML:1: ", val1)





        let set_val = val1.split("$")
        let s_i = 0;
        let name_;
        let email_;
        let speed_;
        let adult_;
        let childs_;
        let beach_;
        for (s_i;s_i<set_val.length;s_i++)
        {
            console.log("S_I::", set_val[s_i]);
        }
        try
        {
            name_ = set_val[1].replace(/[,\/#!%\^&\*;:{}=\-`~()]/g, "");
            email_ = set_val[2].replace(/[,\/#!%\^&\*;:{}=\-`~()]/g, "");
            beach_ = set_val[3].replace(/[,\/#!%\^&\*;:{}=\-`~()]/g, "");
            speed_ = set_val[4].replace(/[,\/#!%\^&\*;:{}=\-`~()]/g, "");
            adult_ = set_val[5].replace(/[,\/#!%\^&\*;:{}=\-`~()]/g, "");
            childs_= set_val[6].replace(/[,\/#!%\^&\*;:{}=\-`~()]/g, "");

            // CLEAN UP
            let ret_data = ["%:",name_, email_, beach_, speed_, adult_, childs_];
            console.log("RET_DATA:: ", ret_data);
            set_name = name_.split(" ").slice(0,1)
            console.log("USER_NAME::: ", set_name)
            set_email = email_.split(" ").slice(0,1)
            console.log("USER_MAIL::: ", set_email)
            set_beach = beach_.split(" ").slice(0,1)
            console.log("PICKUP_POINT::: ",  set_beach)

            //document.getElementById('u_name').innerHTML = set_name;
            //document.getElementById('u_mail').innerHTML = set_email;



        }
        catch
        {
            console.log("[ERROR]:[LOADING_SLOT_DATA]:")
        }
        try{
            del_popup_open(val1, current_slot);
        }
        catch{
            console.log("NOT_OPENED")
        }
        
    };
}

}
catch
{
    console.log("[ERROR]:[SLOT_PROMPT]");

}



function show_data(data){
    console.log("WTH ACTUAL FUCK??>", data);
    var ret_data = data.split("%#!")
    for (var x = 0; x < ret_data.length; x++)
    {
        console.log("X:: ", x, "VAL:: ", ret_data[x])
    }
}



// UPDATE SLOTS DISPLAY
try{
    function filterDates(selcDate, dates_1)
    {




        current_date = selcDate;
        let this_date = dates_1.split("?");

        let s = 0;
        for(s=0;s<this_date.length;s++)
        {
            //console.log("[THIS_DATE]: ", this_date[s])
            if (this_date[s].includes(selcDate))
            {
                console.log("[FOUND_DATE]:[", selcDate, "]")
                
                let slots_set = this_date[s].split("%");
                let slot_ = 0;
                for (slot_=0; slot_<slots_set.length;slot_++)
                {
                    console.log("[SLOT]: [",slot_, "]::[", slots_set[slot_],"]");
                    if (slots_set[slot_].includes(selcDate))
                    {
                        document.getElementById("selcDate").innerHTML = selcDate;
                    }
                    else
                    {
                        let set_val_ = slots_set[slot_].split("*")
                        let PAY__   = set_val_[0].slice(3);
                        let name__  = set_val_[1].slice(7, set_val_[1].length);                        
                        let email__ = set_val_[2].slice(7, set_val_[2].length);
                        let beach__ = set_val_[3].slice(8, set_val_[3].length);
                        let speed__ = set_val_[4].slice(8, set_val_[4].length);
                        let adult__ = set_val_[5].slice(8, set_val_[5].length);
                        let childs__= set_val_[6].slice(8, set_val_[6].length);

                        console.log("NAME: ", name__, ":KIDS: ", childs__)
                        var to_print_ = "|SLOT|:-----------"+ slot_list[slot_-1] +  "<br>|PAID|:------------" + PAY__ +  "<br>|NAME|:----------" + name__ + " <br>|EMAIL|:----------" + email__ + "<br>|BEACH|:---------" + beach__ +
                        "<br>|SPEED|:---------" + speed__ + "<br>|ADULTS|:------" + adult__ + "<br>|CHILDREN|:--" + childs__
                        console.log("[SLOT_]:[",slot_, "]::[" ,slots_set[slot_],"]")
                        let id_str = "#ti30_slot"+(slot_-1);
                        let id_a = "t30_a_"+(slot_-1);
                        console.log("@@%% ", id_a)
                        document.querySelector(id_str).style.backgroundColor = ' rgba(17, 206, 219, 0.3)';
                        document.getElementById(id_a).innerHTML = to_print_;
                    }
                }
            }


        }
    }
}
catch{
    console.log("[ERROR]:[FILTER_DATES]")
}










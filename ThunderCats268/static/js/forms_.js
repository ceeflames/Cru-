console.log('[forms.js]:: [opened]');
console.log('[CONTENT] :: ');
console.log('           >> [BOOKINGS_MODAL]');
console.log('           >> [UIX_STAGING]');
console.log('           >> [SELECTIONS]');
//------------------------------------------------------------------
// BOOKINGS FORM POPUP [MODAL]
//------------------------------------------------------------------


//------------------------------------------------------------------
// MODAL CONTROL
//------------------------------------------------------------------
// OPEN MODAL
document.getElementById('btn').addEventListener('click',
function(){
    //console.log("OPEN_POUP");
    document.querySelector('.bg-modal').style.display = 'flex';
    document.querySelector('#contact_').style.display = "none";

    hide_all();
})

function hide_all(){

    console.log("HIDE_ALL");


    document.querySelector('.people_select-head').style.display = "none";
    document.querySelector('.people_select').style.display = "none";

    document.querySelector('.kids').style.display = "none";
    // SOME DON'T WORK WITH query ':-|
    document.getElementById('kids-head').style.display = "none";
    document.getElementById('price_set').style.display = "none";
    document.getElementById('t_m').style.display = "none";
    document.getElementById('slots_drop').style.display = "none";
    document.getElementById('price_set').style.display = "none";
    document.getElementById('calendar_head').style.display = "none";
    document.querySelector('.drop-down').style.display = "none";
    document.getElementById('enter_').style.display = "none";
    document.getElementById('pick_up').style.display = "none";
    
    // BEACHES
    document.getElementById('speedy_').style.display = "none";
    document.querySelector('.contact_').style.display = "none";

};
// CLOSE MODAL
document.getElementById('close').addEventListener('click',
function(){
    //console.log("CLOSE_POUP");
    document.querySelector('.bg-modal').style.display = 'none';
});
//------------------------------------------------------------------


//------------------------------------------------------------------
// REQUIRED VARIABLES
//------------------------------------------------------------------


var set_date;
var set_dates_;
var items = document.querySelectorAll("#t30m_slots li");
var num_of_slots = 0;
var radioKids = document.getElementsByName('child-count');
var radioPeeps = document.getElementsByName('people-select');

const speed_high = document.querySelector('.speed-select1');
const speed_low = document.querySelector('.speed-select2');
const ch_High = document.getElementById("high-speed");
const ch_Low = document.getElementById("low-speed");

const adult_1 = document.getElementById('peep-select1');
const adult_box_1 = document.getElementById('people_1');
const adult_2 = document.getElementById('peep-select2');
const adult_box_2 = document.getElementById('people_2');
const adult_3 = document.getElementById('peep-select3');
const adult_box_3 = document.getElementById('people_3');
const adult_4 = document.getElementById('peep-select4');
const adult_box_4 = document.getElementById('people_4');

var update_price = document.getElementById('price_set');

var speed1 = 0;
var speed2 = 0;
var selecT_adult = "none";
var people_count = 0;
var child_count = 0;
var kid_1 = false;
var kid_2 = false;
var selected = 0; // SLOTS
var sel_ = 0 // DO NOT USE SELECTED (FUNCTION LOOPS TWICE)
var beach_select = "none";
//------------------------------------------------------------------

// kid__d :: id
const kid_1_d = document.getElementById('child-1-');
const kid_2_d = document.getElementById('child-2-');

// kid__q :: div "CLASS"
const kid_1_q = document.querySelector('.child-1');
const kid_2_q = document.querySelector('.child-2');


//------------------------------------------------------------------
//QUERY SELECTIONS
//------------------------------------------------------------------




// CUSTOM BOOKINGS



//------------------------------------------------------------------

var book_type = document.getElementById('half-hour');
book_type.addEventListener("click", function(){
    document.querySelector('.pb_btn').checked = false;
    document.querySelector('.hh_btn').checked = true;

    document.querySelector('#contact_').style.display = "none";

    open_beaches();

    // DON'T FORGET UIX
        // ACTIVE hh_btn
    document.querySelector('#half-hour').style.color = 'rgba(17, 206, 219, 0.9)';
    document.querySelector('#half-hour').style.backgroundColor = 'rgba(0, 0, 0, 1)';
    
        // DEACTIVE pb_btn    
    document.querySelector('#persona').style.color = 'rgba(0,0,0,1)';
    document.querySelector('#persona').style.backgroundColor = 'rgba(17, 206, 219, 0.9)';
    

})

var book_type = document.getElementById('persona');
book_type.addEventListener("click", function(){
    document.querySelector('.hh_btn').checked = false;
    document.querySelector('.pb_btn').checked = true;

    document.querySelector('#contact_').style.display = "block";
    // also hide all other elements

    close_beaches();

    // DON'T FORGET UIX
        // ACTIVE pp_btn
    document.querySelector('#persona').style.color = 'rgba(17, 206, 219, 0.9)';
    document.querySelector('#persona').style.backgroundColor = 'rgba(0, 0, 0, 1)';
    // DEACTIVE hh_btn      
    document.querySelector('#half-hour').style.color = 'rgba(0,0,0,1)';
    document.querySelector('#half-hour').style.backgroundColor = 'rgba(17, 206, 219, 0.9)';

    hide_all();
})



//------------------------------------------------------------------










var beach_chosen = false;

// pick up point

const beach_1 = document.getElementById('beach_1');
const beach_2 = document.getElementById('beach_2');
const beach_3 = document.getElementById('beach_3');
const beach_4 = document.getElementById('beach_4');
const beach_5 = document.getElementById('beach_5');

const beach_head = document.getElementById('pick_up');
const beach_div =  document.getElementById('beaches');


//------------------------------------------------------------------
// BEACH OPEN / CLOSSE
//------------------------------------------------------------------
function open_beaches(){
    beach_div.style.display = 'block';
    beach_head.style.display = 'block';
    beach_1.style.display = 'block';
    beach_2.style.display = 'block';
    beach_3.style.display = 'block';
    beach_4.style.display = 'block';
    beach_5.style.display = 'block';

}

function close_beaches(){
    console.log("CLOSE BEACHES");
    beach_div.style.display = 'none';
    beach_head.style.display = 'none';
    beach_1.style.display = 'none';
    beach_2.style.display = 'none';
    beach_3.style.display = 'none';
    beach_4.style.display = 'none';
    beach_5.style.display = 'none';

}


//------------------------------------------------------------------
// BEACH SELECTIONS
//------------------------------------------------------------------
function un_select_beaches()
{
    var all_beaches = document.querySelectorAll(".beaches div");
    for (let b_i = 1; b_i < all_beaches.length+1; b_i++)
    {
        let beach_id = "#beach_"+b_i;
        let that_beach = document.querySelector(beach_id);
        console.log(":THTA_BEACH:: ", that_beach);
        that_beach.style.color = 'rgba(0,0,0,0.8)';
        that_beach.style.boxShadow = '0px 0px rgba(17, 206, 219, 0.9)';
        that_beach.style.backgroundColor = 'rgba(17, 206, 219, 0.9)';
        // CLEAR ALL OTHER DATA GOING DOWN
    }
}
function clear()
{
    beach_select = "none";
    document.getElementById('speedy_').style.display = "none";
    document.querySelector('.kids').style.display = "none";
    document.getElementById('kids-head').style.display = "none";
    document.getElementById('price_set').style.display = "none";
    document.getElementById('t_m').style.display = "none";
    document.getElementById('slots_drop').style.display = "none";
    document.getElementById('calendar_head').style.display = "none";
    document.querySelector('.drop-down').style.display = "none";
    document.getElementById('enter_').style.display = "none";
    speed1 = 0;
    speed2 = 0;
    selecT_adult = "none";
    people_count = 0;
    child_count = 0;
    kid_1 = false;
    kid_2 = false;
    open_adult_(0);
    //un_slot_all()
}

function beach_active(val)
{
    val.style.backgroundColor = 'rgba(0,0,0,0.8)';
    val.style.boxShadow = '5px 5px rgba(17, 206, 219, 0.9)';
    val.style.color = 'rgba(17, 206, 219, 0.9)';  
}

beach_1.addEventListener("click", function(e){
    e.preventDefault();
    e.stopPropagation();
    const beach1 = document.getElementById('beach1');
    if (beach_select === "jolly")
    {
        un_select_beaches();
        document.getElementById('beach1').checked = false;
        return;
    }
    else if (beach_select !== "jolly")
    {
        document.getElementById('beach1').checked = true;
        un_select_beaches();
        beach_select = "jolly";
        beach_active(this);
        document.getElementById('speedy_').style.display = "block";
    }

})

beach_2.addEventListener("click", function(e){
    e.preventDefault();
    e.stopPropagation();
    const beach2 = document.getElementById('beach2');
    if (beach_select === "valleychurch")
    {
        document.getElementById('beach2').checked = false;
        un_select_beaches();
        return;
    }
    else if (beach_select !== "valleychurch")
    {
        document.getElementById('beach2').checked = true;
        un_select_beaches();
        beach_select = "valleychurch";
        beach_active(this);
        document.getElementById('speedy_').style.display = "block";
    }

})

beach_3.addEventListener("click", function(e){
    e.preventDefault();
    e.stopPropagation();
    const beach3 = document.getElementById('beach3');
    if (beach_select === "smallffryes")
    {
        document.getElementById('beach3').checked = false;
        un_select_beaches();
        return;
    }
    else if (beach_select !== "smallffryes")
    {
        document.getElementById('beach3').checked = true;
        un_select_beaches();
        beach_select = "smallffryes";
        beach_active(this);
        document.getElementById('speedy_').style.display = "block";
    }

})

beach_4.addEventListener("click", function(e){
    e.preventDefault();
    e.stopPropagation();
    const beach4 = document.getElementById('beach4');
    if (beach_select === "bigffryes")
    {
        document.getElementById('beach4').checked = false;
        un_select_beaches();
        return;
    }
    else if (beach_select !== "bigffryes")
    {
        document.getElementById('beach4').checked = true;
        un_select_beaches();
        beach_select = "bigffryes";
        beach_active(this);
        document.getElementById('speedy_').style.display = "block";
    }

})

beach_5.addEventListener("click", function(e){
    e.preventDefault();
    e.stopPropagation();
    const beach5 = document.getElementById('beach5');
    if (beach_select === "darkwood")
    {
        document.getElementById('beach5').checked = false;
        un_select_beaches();
        return;
    }
    else if (beach_select !== "darkwood")
    {
        document.getElementById('beach5').checked = true;
        un_select_beaches();
        beach_active(this);
        beach_select = "darkwood";
        document.getElementById('speedy_').style.display = "block";
    }

})





//------------------------------------------------------------------
//  SPEED SELECT
//------------------------------------------------------------------


speed_high.addEventListener("click", function(e) {
    // IF HIGH_SPEED UNCHECKED
    e.preventDefault();
    e.stopPropagation();
    if (ch_High.checked != true)
    {
        // CHECK_HIGH && UNCHECK_LOW
        open_adult_(1);
        speed_color(1);
        ch_High.checked = true;
        return;
    }
    // IF HIGH_SPEED CHECKED  
    else if (ch_High.checked == true)
    {
        // UNCHECK BOTH
        open_adult_(0);
        speed_color(0);
        ch_High.checked = false;
        return;
    }

})
speed_low.addEventListener("click", function(e) {
    e.preventDefault();
    e.stopPropagation();
    if (ch_Low.checked != true)
    {
        // CHECK_HIGH && UNCHECK_LOW
        open_adult_(2);
        speed_color(2);
        ch_Low.checked = true;
        return;
    }
    // IF HIGH_SPEED CHECKED  
    else
    {
        // UNCHECK BOTH
        open_adult_(0);
        speed_color(0);
        ch_Low.checked = false;
        return;
    }


})
//------------------------------------------------------------------

//------------------------------------------------------------------

//------------------------------------------------------------------
//------------------------------------------------------------------
// ADULT SELECT     select_peeps('people-select1')
//------------------------------------------------------------------

try{


adult_1.addEventListener("click", function(e) {
    // IF HIGH_SPEED UNCHECKED
    e.preventDefault();
    e.stopPropagation();
    if (radioPeeps[0].checked != true)
    {
        radioPeeps[0].checked = true;
        select_peeps('1');
    }
    else{
        radioPeeps[0].checked = false;
        un_check(adult_1);
    }
});

adult_2.addEventListener("click", function(e) {
    // IF HIGH_SPEED UNCHECKED
    e.preventDefault();
    e.stopPropagation();
    if (radioPeeps[1].checked != true)
    {
        select_peeps('2');
        radioPeeps[1].checked = true;
    }
    else{
        radioPeeps[1].checked = false;
        un_check(adult_2);
    }

});

adult_3.addEventListener("click", function(e) {
    // IF HIGH_SPEED UNCHECKED
    e.preventDefault();
    e.stopPropagation();
    if (radioPeeps[2].checked != true)
    {
        select_peeps('3');
        radioPeeps[2].checked = true;
    }
    else
    {
        radioPeeps[2].checked = false;
        un_check(adult_3);
    }
});

adult_4.addEventListener("click", function(e) {
    // IF HIGH_SPEED UNCHECKED
    e.preventDefault();
    e.stopPropagation();
    if (radioPeeps[3].checked == false)
    {
        select_peeps('4');
        radioPeeps[3].checked = true;
    }
    else{
        radioPeeps[3].checked = false;
        un_check(adult_4);
    }

});
function un_check(box){
    // uncheck selected Adult_CheckBoxes
    box.style.backgroundColor = "rgba(17, 206, 219, 0.9)";
    box.style.boxShadow = "0 0 rgba(17, 206, 219, 0.1)";
    box.style.color = "rgba(0,0, 0, 0.8)";
    // Disable and UnCheck kids
    document.querySelector('.kids').style.display = "none";
    //child_space = 0
    kid_1_q.style.display = "none";
    kid_2_q.style.display = "none";
    radioKids[0].checked = false;
    radioKids[1].checked = false;
    // and everything else
    selecT_adult = "none";
    people_count = 0;
    child_count = 0;
    kid_1 = false;
    kid_2 = false;
    document.getElementById('calendar_head').style.display = "none";
    document.getElementById('calendar1').style.display = "none";

}

}
catch{
    console.log("peep-select::ERROR");
}

//------------------------------------------------------------------
//  CHILD SELECT
//------------------------------------------------------------------
kid_1_d.addEventListener("click", function(e){
    //check if selected
    e.preventDefault();
    e.stopPropagation();
    if (radioKids[0].checked == false)
    {
        child_select('child-1');
        radioKids[0].checked = true;
        return;
    }
    else if (radioKids[0].checked == true)
    {clear_child()}
});

kid_2_d.addEventListener("click", function(e){
    //check if selected
    e.preventDefault();
    e.stopPropagation();
    if (radioKids[1].checked == false)
    {
        child_select('child-2');
        radioKids[1].checked = true;
    }
    else if (radioKids[1].checked == true)
    {clear_child()}
});


//------------------------------------------------------------------
// STAGING UIX
//------------------------------------------------------------------
// SPEED_SELECT -->> OPEN: ADULT_SELECT
function open_adult_(val)
{
    price_Total();
    // IF HIGH SPEED ACTIVATE ONLY 2 SEATS
    if (val == 1)
    {
        document.querySelector('.people_select-head').style.display = "block";
        document.querySelector('.people_select').style.display = "block";
        document.querySelector('.first-2').style.display = "block";
        document.querySelector('.last-2').style.display = "none";
        return;
    }
    // IF LOW SPEED ACTIVATE 4 SEATS
    if(val == 2)
    {
        document.querySelector('.people_select-head').style.display = "block";
        document.querySelector('.people_select').style.display = "block";
        document.querySelector('.first-2').style.display = "block";
        document.querySelector('.last-2').style.display = "block";
        return;
    }
    // IF BOTH UNACTIVE CLEAR UP
    if (val == 0)
    {
        document.querySelector('.people_select-head').style.display = "none";
        document.querySelector('.people_select').style.display = "none";
        document.querySelector('.first-2').style.display = "none";
        document.querySelector('.last-2').style.display = "none";
        return;
    }

    try{
        // RESET IF CHANGED
        document.querySelector('.kids').style.display = "none";
        document.querySelector('.drop-down').style.display = "none";
        // SOME DON'T WORK WITH query ':-|
        document.getElementById('kids-head').style.display = "none";
        document.getElementById('price_set').style.display = "none";
        document.getElementById('t_m').style.display = "none";
        document.getElementById('slots_drop').style.display = "none";
        // ALSO RESET PEEPS_SELECTED
        for (var i = 1; i <= 4; i++)
        {
            let peep_id = 'people-select'+i;
            //console.log("PEEP_ID:RESET: ", peep_id);
            document.getElementById(peep_id).style.backgroundColor = "rgba(156, 156, 156, 0.7)";
        }
        // RESET COUNTS
        selecT_adult = "none";
        people_count = 0;
        child_count = 0;
        speed1 = 0;
        speed2 = 0;
    }
    catch {
        console.log("open_adult_error::");
    }
    return;
}
// ADULT_SELECT -->> OPEN: CHILD_SELECT  & CALENDAR
function open_dates()
{
    price_Total();
    document.getElementById('t_m').style.display = "block";
}
// CALENDAR_SELECTED -->> OPEN: SLOT_SELECT
function open_slots()
{
    price_Total();
    document.getElementById('slots_drop').style.display = "block";
    document.querySelector('.drop-down').style.display = "block";
}

var open_drop = false;
// OPEN/CLOSE TIME SLOTS LIST
document.querySelector('.select').addEventListener('click',
function(e){
    console.log("SELECTOR_DROP", e);
    e.preventDefault();
    e.stopPropagation();
    price_Total();
    if (open_drop == false)
    {
        //console.log("OPEN_SLOTS");
        document.querySelector('.t30_menu').style.display = 'block';
        document.querySelector('.t30_menu').style.opacity = 1;
        open_drop = true;
    }
    else 
    {
        //console.log("CLOSE_SLOTS");
        document.querySelector('.t30_menu').style.display = 'none';
        document.querySelector('.t30_menu').style.opacity = 0;
        open_drop = false;
    }
});
// OPEN PRICING
function open_pricing(y_n)
{
    price_Total();
    if (y_n == 0)
    {
        document.getElementById('price_set').style.display = "none";
        document.getElementById('enter_').style.display = "none";

    }
    if (y_n == 1)
    {
        document.getElementById('price_set').style.display = "block";
        document.getElementById('enter_').style.display = "block";
    }
}
//------------------------------------------------------------------







//------------------------------------------------------------------
// SELECTIONS UIX
//------------------------------------------------------------------
// SPEED SELECTED // 
// RADIO BUTTON SHOW/HIDE {SPEED-> #_OF_SEATS}
function speed_color(val){
    price_Total();
    console.log("speed_color(",val,")");
    if (val == 1)
    {
        document.querySelector('.speed-select1').style.backgroundColor = 'rgb(7, 7, 7)';
        document.querySelector('.speed-select1').style.boxShadow = '5px 5px rgba(17, 206, 219, 0.9)';
        document.querySelector('#high_a').style.color = 'rgba(17, 206, 219, 0.9)';
        document.querySelector('#low_a').style.color = 'rgba(0, 0, 0, 0.9)';
        document.querySelector('.speed-select2').style.backgroundColor = 'rgba(17, 206, 219, 0.9)';
        document.querySelector('.speed-select2').style.boxShadow = '0 0 rgba(0, 0, 0, 0.1)';
        speed1 = 1;
        speed2 = 0;
        return;
    }
    if (val == 2)
    {
        document.querySelector('.speed-select2').style.backgroundColor = 'rgb(7, 7, 7)';
        document.querySelector('.speed-select2').style.boxShadow = '5px 5px rgba(17, 206, 219, 0.9)';
        document.querySelector('#low_a').style.color = 'rgba(17, 206, 219, 0.9)';
        document.querySelector('.speed-select1').style.backgroundColor = 'rgba(17, 206, 219, 0.9)';
        document.querySelector('.speed-select1').style.boxShadow = '0 0 rgba(0, 0, 0, 0.1)';
        document.querySelector('#high_a').style.color = 'rgba(0, 0, 0, 0.9)';
        speed1 = 0;
        speed2 = 1;
        return;
    }
    if (val == 0)
    {
        document.querySelector('.speed-select1').style.backgroundColor = 'rgba(17, 206, 219, 0.9)';
        document.querySelector('.speed-select1').style.boxShadow = '0 0 rgba(0, 0, 0, 0.1)';
        document.querySelector('#high_a').style.color = 'rgba(0, 0, 0, 0.9)';
        document.querySelector('#low_a').style.color = 'rgba(0, 0, 0, 0.9)';
        document.querySelector('.speed-select2').style.backgroundColor = 'rgba(17, 206, 219, 0.9)';
        document.querySelector('.speed-select2').style.boxShadow = '0 0 rgba(0, 0, 0, 0.1)';
        speed1 = 0;
        speed2 = 0;
        return;
    }
};
// ADULT - CHILD CONFIG

// >> SELECT # OF PEOPLE
function select_peeps(val, sel_a){
    price_Total();
    // CHECK VALUES :: 
    //console.log("ADULT_SELECTED: 155:", selecT_adult, "::", val);
    // SET SELECTED_ADULT_

    let id_sel = "peep-select"+val;
    let text_id = "ad_"+val;

    if (selecT_adult != id_sel && val != 0)
    {

        // CHANGE TO SELECTED COLOR
        document.getElementById(id_sel).style.backgroundColor = "rgba(0, 0, 0, 1)";
        document.getElementById(id_sel).style.boxShadow = " 5px 5px rgba(17, 206, 219, 0.9)";
        document.getElementById(id_sel).style.color = "rgba(17, 206, 219, 0.9)";

        document.getElementById('t_m').style.display = "block";
        document.querySelector('#calendar1').style.display = "block";
        //document.getElementById('slot_base').style.display = "flex";

        // SET SELECTED_ADULT 
        selecT_adult = val;
        // GET CHILD_SPACE:: 
        let c_space =  val.charAt(val.length-1);
        child_space(c_space)

        // REVERT ANY PRIOR SELECTED 
        for (var i = 1; i <= 4; i++)
        {
            let peep_id = 'peep-select'+i;
            let tex_id = "ad_"+i
            if (id_sel != peep_id)
            {
                document.getElementById(peep_id).style.backgroundColor = "rgba(17, 206, 219, 0.9)";
                document.getElementById(peep_id).style.boxShadow = "0 0 rgba(17, 206, 219, 0.9)";
                document.getElementById(peep_id).style.color = "rgba(0,0, 0, 0.8)";
            }

        }
        return;
    }
    // if Un_Select: revert to DEFAULT 
    if (val == 0)
    {

        // NULL OUT SELECTED_ADULT_ [AS THERE ARE NONE SELECTED]
        selecT_adult = "none";
        // MAKE KIDS _UNSELECTED AND UNAVAILABLE
        kid_1 = false;
        kid_2 = false;
        document.querySelector('.kids').style.display = "none";
        kid_1_q.style.backgroundColor = "rgba(156, 156, 156, 0.7)";
        kid_1_d.style.color = "rgba(0, 0, 0, 0.9)";
        kid_2_q.style.backgroundColor = "rgba(156, 156, 156, 0.7)";
        kid_2_d.style.color = "rgba(0, 0, 0, 0.9)";
        document.getElementById('calendar_head').style.display = "none";
        document.getElementById('calendar1').style.display = "none";
        return;
    }


}
// >> CHILD SLOTS SELECTION
function child_space(val){
    price_Total();
    document.querySelector('.kids').style.display = "block";
    document.getElementById('kids-head').style.display = "block";
    // RESET BEFORE ENABLING
    kid_1 = false;
    kid_2 = false;
    child_count = 0;
    kid_1_d.style.backgroundColor = "rgba(17, 206, 219, 0.9)";
    kid_1_d.style.color = "rgba(0, 0, 0, 0.9)";
    kid_2_d.style.backgroundColor = "rgba(17, 206, 219, 0.9)";
    kid_2_d.style.color = "rgba(0, 0, 0, 0.9)";

    if (val == 1) // if 1 Adult and High Speed
    {
        people_count = 1;
        //child_space = 1
        kid_1_q.style.display = "block";
        kid_2_q.style.display = "none";
    }
    if (val == 2) 
    {
        people_count = 2;
        // if 2 Adult and High Speed
        if (speed1 == 1 && speed2 == 0)
        {
            document.querySelector('.kids').style.display = "none";
            //child_space = 0
            kid_1_q.style.display = "none";
            kid_2_q.style.display = "none";    
        }
        // if 2 Adult and Low Speed
        if (speed2 == 1 && speed1 == 0)
        {
            //child_space = 2
            kid_1_q.style.display = "flex";
            kid_2_q.style.display = "flex";
        }
    }
    if (val == 3)
    {
        people_count = 3;
        // if 3 Adult and Low Speed
        //child_space = 1
        kid_1_q.style.display = "flex";
        kid_2_q.style.display = "none";
    }
    if (val == 4)
    {
        people_count = 4;
        // if 4 Adult and Low Speed
        document.querySelector('.kids').style.display = "none";
        //child_space = 0
        kid_1_q.style.display = "none";
        kid_2_q.style.display = "none";

    }
    //console.log("PEOPLE_COUNT", people_count);
    // OPEN CALENDAR AFTER PEEPS HAVE BEEN SELECTED
    //open_dates()
}
// >> SELECT # OF CHILDREN
function child_select(val){
    price_Total();
    // if selected: unselect all others, revert all other color changes
    if (val == 'child-1')
    {
        //console.log("SELCECTED:: ", val);
        if (kid_1 == false)
        {
            // KID_1 :: ACTIVE SELECTION
            kid_1_d.style.backgroundColor = "rgba(0, 0, 0, 0.9)";
            kid_1_d.style.color = "rgba(17, 206, 219, 0.9)";
            kid_2_d.style.backgroundColor = "rgba(17, 206, 219, 0.9)";
            kid_2_d.style.color = "rgba(0, 0, 0, 0.9)";
            kid_1 = true;
            kid_2 = false;
            child_count = 1;
            //console.log("kid_1: SELECTED:: ");
        }
        else{clear_child()}
        return;
    }
    
    if (val == 'child-2')
    {
        //console.log("SELCECTED:: ", val);
        if (kid_2 == false)
        {
            // KID_2 :: ACTIVE SELECTION
            kid_2_d.style.backgroundColor = "rgba(0, 0, 0, 0.9)";
            kid_2_d.style.color = "rgba(17, 206, 219, 0.9)";
            kid_1_d.style.backgroundColor = "rgba(17, 206, 219, 0.9)";
            kid_1_d.style.color = "rgba(0, 0, 0, 0.9)";

            kid_2 = true;
            kid_1 = false;
            child_count = 2;
            //console.log("kid_2: SELECTED:: ");
        }
        else{clear_child()}
        return;
    }
}

// CLEAR CHILD SELECTION
function clear_child()
{
   // KID_2 :: DE_ACTIVE SELECTION
   kid_1_d.style.backgroundColor = "rgba(17, 206, 219, 0.9)";
   kid_2_d.style.backgroundColor = "rgba(17, 206, 219, 0.9)";
   kid_2 = false;
   kid_1 = false;
   radioKids[0].checked = false;
   radioKids[1].checked = false;
   child_count = 0;
   //console.log("kid_2: UN_SELECTED:: ");
}

const t30_menu = document.querySelectorAll(".t30_menu li");
for(let i = 0; i <t30_menu.length;i++)
{
    t30_menu[i].addEventListener("click", function(e){
        let in_ = "#ti30_slot"+i;
        console.log("SELECETED:: ", selected)
        console.log("SLOT-- ", in_);
        let ch_li = document.querySelector(in_+" input").checked;
        console.log("INPUT_-- ", ch_li);
        if (ch_li == false)
        {
            t30_menu[i].style.backgroundColor = 'black';
            t30_menu[i].style.color = 'rgba(17, 206, 219, 0.9)';
            document.querySelector(in_+" input").checked = true;

            selected += 1;
            console.log("SELECETED:: ", selected)
            check_set();
            return;
        }
        else
        {
            t30_menu[i].style.backgroundColor = 'rgba(17, 206, 219, 0.9)';
            t30_menu[i].style.color = 'black';
            document.querySelector(in_+" input").checked = false;
            selected -= 1
            console.log("SELECETED:: ", selected)
            check_set();
            return;
        }

    })
}
// SELECTED TIME SLOTS {ToDo: COLOR_CHANGE}
function check_set()
{
    if (selected == 0 || selected < 1)
    {
        console.log("CLOSING_PRICE")
        open_pricing(0);
        price_Total();
    }
    else{
        open_pricing(1);
        console.log("OPENING_PRICE");
    }
    price_Total();
}
function un_slot_all()
{
    var slots = document.querySelectorAll("#t30m_slots li")
    console.log("UNSLOT_ALL....")    
    for(var i = 0; i < slots.length; i++)
    {
        let li_id = "t30_slot"+i;
        let li_ti_ = "ti30_slot"+i;
        let li_id_a = "t30_a_"+i;
        let val = document.getElementById(li_id).checked;
        console.log("UN_SELECTING_SLOT: ", li_id_a);
        console.log("LI_ID; ", li_id, "::: ", val);
        //document.getElementById(li_id).click();
        //document.getElementById(li_id).checked;
        document.getElementById(li_ti_).style.backgroundColor = "rgba(10, 4, 61, 0.5)";
        document.getElementById(li_ti_).style.color = "black";
        //
    }
    console.log("UN___SEL_ : -= : ", selected);

}


//------------------------------------------------------------------
// ToDo: 
// PRICE CALCULATION
//      // DISCOUNT RATES
function price_Total()
{
    // FIX SLOT COUNT...

    console.log("SELECTED_SLOTS[PRICING]:", selected);
    //console.log("SLOT_COUNT::SEL_: ", sel_ ,":SLOTS:", num_of_slots);
    //             T_A         T_C          #_S
    // TOTAL = ((pA * #A) + (pC * #C)) * (#Slot)
    var price_A = 50;
    var price_C = 50;

    // T_A = Total_#_Adults * Price/Adult
    var T_A = people_count * price_A;
    //console.log("FOR : ", people_count, " people at $250 per 30m : ", T_A);

    // T_C = Total_#_Kids * Price/Child
    var T_C = child_count * price_C;
    ///console.log("FOR : ", child_count, " child at $50 per 30m : ", T_C);

    // PER_SLT = T_A + T_C
    var per_slot = T_A + T_C;
    //console.log("WITH A TOTAL OF : ", per_slot, " PER SLOT \n FOR ", num_of_slots, " SLOTS BOOKED");

    // TOTAL = PER_SLT * #_OF_SLOTS
    var total_ =per_slot * selected;
    //console.log("WHICH AMOUNTS TO : ", total_)

    // DISPLAY TOTAL_
    document.getElementById("total_").textContent = total_;

    // FOR FOMRS FLASK
    document.getElementById("myFin").value = total_;
    document.getElementById("hidden_tot").value = total_;

    console.log(":::FIN_:::", document.getElementById("myFin").value);
    console.log(":::HIDDEN_TOT_:::", document.getElementById("hidden_tot").value);


    return total_;
}
//------------------------------------------------------------------
update_price.addEventListener("click", function(e)
{
    e.preventDefault();
    e.stopPropagation();
    price_Total();
    console.log("UPDATING_PRICE");

})

/////////////////////////////////////////////////////////
///////////////      CALENDAR               /////////////
// DO NOT TOUCH< MIGHT NOT WORK ON ALL WEB BROWERS :~|  :-| :|
try{
    function slotSelect(date_, dates_1){
        // IF DATE NOT FOUND :: ENABLE ALL SLOTS
        set_date = date_;
        set_dates_ = dates_1;
        var pre_check = dates_1.includes(date_);
        if (pre_check == false)
        {
            //console.log(pre_check, "NOT_HERE", date_);
            for (var t_ = 0; t_ <= 18; t_++)
            {
                let id_str = "#30_slot"+t_
                let wr_str = "#ti30_slot"+t_
                $(id_str).removeAttr("disabled","disabled");
                $(wr_str).removeAttr("disabled","disabled");
                document.querySelector(wr_str).style.backgroundColor = 'rgba(10, 4, 61, 0.5)';
                document.querySelector(wr_str).style.display = "block";
            }
        }
        for (var d_ = 0; d_ < dates_1.length; d_++)
        {
            //console.log("LOOKING:", dates_1[d_]);
            let this_date = dates_1[d_].split("*");
            for (var s_ = 0; s_ < this_date.length; s_++)
            {
                //console.log("WTF:?", this_date[s_]);
                if (date_ == this_date[s_])
                {
                    //console.log("FOUND_IT?: ", this_date[0])
                    let time_slots = this_date[1].split('&');
                    console.log(" \n\nALL  SLOTS:::  ",time_slots, "\n\n");
                    for (var t_ = 0; t_ < time_slots.length; t_++)
                    {
                        let id_str = "#30_slot"+t_;
                        let wr_str = "#ti30_slot"+t_;
                        let wr_id = "ti30_slot"+t_;

                        if (t_ >= 19)
                        {
                            console.log("FUCK OFFF");
                            break;
                        }
                        //console.log("ID_STR:: ", id_str, "::TIME_SLOT_[t_]:", time_slots[t_]);
                        if (time_slots[t_] != "True" && time_slots[t_] != "False")
                        {
                            continue;
                        }

                        if (time_slots[t_] == "True")
                        {
                            $(id_str).attr("disabled","disabled");
                            $(wr_str).attr("disabled","disabled");
                            // DON'T SHOW BOOKED DATES
                            //document.querySelector(wr_str).style.display = "none";
                            document.getElementById(wr_id).style.display = 'none';

                            console.log("DATE_SLOT_TAKEN:: ", wr_str, t_);
                        }
                        else
                        {
                            console.log("wtp: ", wr_id);
                            $(id_str).removeAttr("disabled","disabled");
                            $(wr_str).removeAttr("disabled","disabled");
                            document.getElementById(wr_id).style.backgroundColor = 'rgba(10, 4, 61, 0.5)';
                            // OR DO 
                            document.querySelector(wr_str).style.display = "block";
                            console.log("DATE_SLOT_OPEN:: ", wr_str, t_);
                        }
                    }
                }
            }
        }
        return "Y"
    }
}
catch(err){
    console.log("[ERROR]:[TIME SLOT FILTER]:{BOAT_1}:{home.html:<script>} \n[err]: ", err);
    }

/////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////





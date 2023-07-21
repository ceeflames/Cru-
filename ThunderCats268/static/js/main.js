// PARALLAX EFFECT

var floaty = document.querySelector('#floaty');
var bg_parallax = document.querySelector("#bg-parallax");
window.addEventListener("scroll", function(e){
    let current = Math.round(window.scrollY);
    let w_width = window.innerWidth-280;
    let c_it = Math.round(w_width)+"px"
    console.log("WINDOW: WIDTH", c_it)
    if (current >= 2900)
    {bg_parallax.style.top = '-2230px';}
    else
    {
        if (parseInt(current) < parseInt(c_it))
        {floaty.style.left = Math.round(current*1)+"px";}
        bg_parallax.style.top = -(current*0.4)+"px";
    }
});

// floaty




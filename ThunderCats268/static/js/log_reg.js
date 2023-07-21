console.log("[OPEN] :: [LRC.JS]");

// OPEN LOGIN MODAL
var lf_modal = document.getElementById('login_me_');
lf_modal.addEventListener("click", function()
{document.getElementById('lf_modal').style.display = "flex";});
// CLOSE LOGIN MODAL
var lf_close = document.getElementById('lf_exit');
lf_close.addEventListener("click", function()
{document.getElementById('lf_modal').style.display = 'none';});


// OPEN REGISTER MODAL
var reg_modal = document.getElementById('opt_regi_');
reg_modal.addEventListener("click", function()
{document.getElementById('reg_modal').style.display = "flex";
console.log("OPENING_REG_MODAL");});
// CLOSE LOGIN MODAL
var reg_close = document.getElementById('reg_exit');
reg_close.addEventListener("click", function()
{document.getElementById('reg_modal').style.display = 'none';});


// OPEN FORGOT MODAL
var forgot_modal = document.getElementById('opt_change_');
forgot_modal.addEventListener("click", function()
{document.getElementById('forgot_modal').style.display = "flex";});
// CLOSE LOGIN MODAL
var forgot_close = document.getElementById('forgot_exit');
forgot_close.addEventListener("click", function()
{document.getElementById('forgot_modal').style.display = 'none';});


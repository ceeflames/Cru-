import FormData from '../../node_modules/form-data';


const subForm = document.getElementById("sub_form");
const s_Form = document.querySelector("#sub_form");
subForm.addEventListener("submit", function(e){
    alert("e.preventDefault.. not working");
    e.preventDefault();
    console.log("PREVENT_DEFAULT_SUB_FORM")
    const form_data = FormData(subForm);
    

    fetch('/', {
        method: 'POST',
        body: form_data,
    }).then(function(response){
        console.log("HAPPINESS", response);
    });
});

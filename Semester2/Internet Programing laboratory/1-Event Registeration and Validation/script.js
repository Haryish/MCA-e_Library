function validate(){
    var result="";
    result+= validateName();
    result+= validateEmail();
    result+= validatePassword();
    result+= validateTerms();
    if (result=="") return true;
    alert("Validation Result:\n\n"+result);
}

function validateName(){
    console.log(document.getElementsByName("name"));
    var uname= document.getElementsByName("name")[0].value;
    console.log(uname);
    if(uname.length<=3){
        console.log("Name should be atlease three characters.\n");
    }
    return "";
}

function validatePassword(){
    var password=valueOf("password");
    var retype=valueOf("retype_password");
    if(password.length<=6){
        alert("password should be more than 6 characters");
    }
    if(password != retype){
        alert("Password does not match");
    }
}

function validateEmail(){
    var email=valueOf("email");
    var retype= valueOf("retype_email");
    if(email.indexOf('@'==-1)){
        alert("Email ID should be valid");
    }
    if(email!=retype){
        alert("Email ID doesn't match");
    }
    return "";
}

function validateTerms(){
    var terms=document.getElementsByName("terms")[0].value;
    if(!terms.checked){
        alert("Consent the form");
    }
    return "";
}

function valueOf(name){
    return document.getElementsByName(name)[0].value;
}
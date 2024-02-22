function validateUserForm() {
  let first_name = document.forms["account_modification"]["first_name"].value;
  let last_name = document.forms["account_modification"]["last_name"].value;
  let email = document.forms["account_modification"]["email"].value;
  let username = document.forms["account_modification"]["username"].value;
  let password = document.forms["account_modification"]["password"].value;

  if (first_name == "") {
    alert("Veuillez saisir un prénom");
    return false;
  }
  if (last_name == "") {
    alert("Veuillez saisir un nom");
    return false;
  }
  if (email == "") {
    alert("Veuillez saisir un mail");
    return false;
  }
  if (username == "") {
    alert("Veuillez saisir un login");
    return false;
  }
  if(password == ""){
    alert("Veuillez saisir un mot de passe")
    if(password.length < 12) {
      alert("Le mot de passe doit au moins contenir 12 caractères")
    }else if(password.search(/[a-z]/) < 0) {

console.log(“Error: Password must contain at least one lowercase letter”);

} else if(password.search(/[A-Z]/) < 0) {

console.log(“Error: Password must contain at least one uppercase letter”);

} else if(password.search(/[0-9]/) < 0) {

console.log(“Error: Password must contain at least one number”);

} else {

console.log(“Success!”);

}  ”’
    alert("Veuillez saisir un mot de passe fort contenant 1 chiffre, 1 majuscule, 1 minuscule et un caractère spécial");
    return false;
  }
}
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
    alert("Veuillez saisir un mot de passe fort contenant 1 chiffre, 1 majuscule, 1 minuscule et un caractère spécial");
        return false;
    }
  else if(password.length < 12) {
      alert("Le mot de passe doit au moins contenir 12 caractères")
        return false;
    }
  else if(password.search(/[a-z]/) < 0) {
      alert("Le mot de passe doit contenir au moins une minuscule");
          return false;
    }
  else if(password.search(/[A-Z]/) < 0) {
      alert("Le mot de passe doit contenir au moins une majuscule");
          return false;

    }
  else if(password.search(/[0-9]/) < 0) {
      alert("Le mot de passe doit contenir au moins un chiffre");
          return false;
  }
}

function ajouterQuantite() {
  // Récupérer l'élément contenant la quantité
  var champQuantite = document.getElementById("quantite");
  // Récupérer la valeur actuelle de la quantité
  var quantiteActuelle = parseInt(champQuantite.value);
  // Incrémenter la quantité
  var nouvelleQuantite = quantiteActuelle + 1;
  // Mettre à jour la valeur affichée
  champQuantite.value = nouvelleQuantite;
}

fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
// Event handler
  document.querySelector("#paymentButton").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session/")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});
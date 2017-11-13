/**
 * Handles the sign in button press.
 */
function toggleSignIn() {
    if (firebase.auth().currentUser) {
        // [START signout]
        firebase.auth().signOut();
        // [END signout]
    } else {
        var email = document.getElementById('email').value;
        var password = document.getElementById('password').value;
        if (email.length < 4) {
            alert('Please enter an email address.');
            return;
        }
        if (password.length < 4) {
            alert('Please enter a password.');
            return;
        }
        // Sign in with email and pass.

        firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
      // Handle Errors here.
      var errorCode = error.code;
      var errorMessage = error.message;
      // [START_EXCLUDE]
      if (errorCode === 'auth/wrong-password') {
      alert('Wrong password.');
      document.getElementById('quickstart-sign-in').style.visibility = 'visible';
      document.getElementById('quickstart-sign-up').style.visibility = 'visible';
      document.getElementById('email').style.visibility = 'visible';
      document.getElementById('password').style.visibility = 'visible';
      document.getElementById('signintext').style.visibility = 'visible';
      document.getElementById('signinhead').style.visibility = 'visible';
      document.getElementById('Search').style.display = 'none';
      document.getElementById('Searchtxt').style.display = 'none';
      } else {
      alert(errorMessage);
      document.getElementById('quickstart-sign-in').style.visibility = 'visible';
      document.getElementById('quickstart-sign-up').style.visibility = 'visible';
      document.getElementById('email').style.visibility = 'visible';
      document.getElementById('password').style.visibility = 'visible';
      document.getElementById('signintext').style.visibility = 'visible';
      document.getElementById('signinhead').style.visibility = 'visible';
      document.getElementById('Search').style.display = 'none';
      document.getElementById('Searchtxt').style.display = 'none';

      }
      console.log(error);
      document.getElementById('quickstart-sign-in').disabled = false;
      // [END_EXCLUDE]
      });
// [END authwithemail]
    }
    document.getElementById('quickstart-sign-in').style.visibility = 'hidden';
    document.getElementById('quickstart-sign-up').style.visibility = 'hidden';
    document.getElementById('email').style.visibility = 'hidden';
    document.getElementById('password').style.visibility = 'hidden';
    document.getElementById('signintext').style.visibility = 'hidden';
    document.getElementById('signinhead').style.visibility = 'hidden';
    document.getElementById('Search').style.display = 'block';
    document.getElementById('Searchtxt').style.display = 'block';

}
/**
 * Handles the sign up button press.
 */
function handleSignUp() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    if (email.length < 4) {
        alert('Please enter an email address.');
        return;
    }
    if (password.length < 4) {
        alert('Please enter a password.');
        return;
    }
    // Sign in with email and pass.
    // [START createwithemail]
    firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
      // Handle Errors here.
      var errorCode = error.code;
      var errorMessage = error.message;
      // [START_EXCLUDE]
      if (errorCode == 'auth/weak-password') {
      alert('The password is too weak.');
      } else {
      alert(errorMessage);
      }
      console.log(error);
      // [END_EXCLUDE]
      });
// [END createwithemail]
}

/**
 * initApp handles setting up UI event listeners and registering Firebase auth listeners:
 *  - firebase.auth().onAuthStateChanged: This listener is called when the user is signed in or
 *    out, and that is where we update the UI.
 */
function initApp() {
    // Listening for auth state changes.
    // [START authstatelistener]
    firebase.auth().onAuthStateChanged(function(user) {
                                       // [START_EXCLUDE silent]
       //document.getElementById('quickstart-verify-email').disabled = true;
       // [END_EXCLUDE]
       if (user) {
       //document.getElementById('quickstart-sign-in').style.visibility = 'hidden';
       
       
       // [START_EXCLUDE]
       document.getElementById('quickstart-sign-in-status').textContent = 'Signed in';
       document.getElementById('quickstart-sign-in').textContent = 'Sign out';
       document.getElementById('quickstart-account-details').textContent = JSON.stringify(user, null, '  ');
       if (!emailVerified) {
       document.getElementById('quickstart-verify-email').disabled = false;
       }
       // [END_EXCLUDE]
       } else {
       // User is signed out.
       // [START_EXCLUDE]
       document.getElementById('quickstart-sign-in-status').textContent = 'Signed out';
       document.getElementById('quickstart-sign-in').textContent = 'Sign in';
       document.getElementById('quickstart-account-details').textContent = 'null';
       // [END_EXCLUDE]
       }
       // [START_EXCLUDE silent]
       document.getElementById('quickstart-sign-in').disabled = false;
       // [END_EXCLUDE]
       });
    // [END authstatelistener]
    document.getElementById('quickstart-sign-in').addEventListener('click', toggleSignIn, false);
    document.getElementById('quickstart-sign-up').addEventListener('click', handleSignUp, false);
    document.getElementById('quickstart-verify-email').addEventListener('click', sendEmailVerification, false);
    document.getElementById('quickstart-password-reset').addEventListener('click', sendPasswordReset, false);
}
window.onload = function() {
    initApp();
};



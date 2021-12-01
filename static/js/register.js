document.getElementById("next").addEventListener("click", redir);
function redir(){
  if (document.getElementById('person-acc').checked) {
    var a = document.getElementById("1");
    a.click();
  } if(document.getElementById('org-acc').checked) {
    var a = document.getElementById("2");
    a.click();
  } if(document.getElementById('doc-acc').checked) {
    var a = document.getElementById("3d");
    a.click();
  }
}

/*
  if (document.getElementById('person-acc').checked) {
    window.location.href = "/register-patient/";
  } if(document.getElementById('org-acc').checked) {
    window.location.href = "/register-staff/";
  }
*/

/*
  if (document.getElementById('person-acc').checked) {
    window.location = '/register-patient/';
    return false;
  } if(document.getElementById('org-acc').checked) {
    window.location = '/register-staff/';
    return false;
  }
*/
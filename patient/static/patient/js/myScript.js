// MODAL BOX FOR USER SIGN UP

let regModalBox = document.querySelector(".modal-cta");
let register = document.querySelector("#getStarted");

// MODAL FUNCTIONALITY
register.addEventListener("click", (e) => {
  e.preventDefault();
  loginModalBox.style.display = "none";

  if (regModalBox.style.display == "block") {
    regModalBox.style.display = "none";
  } else {
    regModalBox.style.display = "block";
  }
});

// MODAL BOX FOR USER LOGIN

let loginModalBox = document.querySelector(".loginModal");
let login = document.querySelector("#login");

// MODAL FUNCTIONALITY
login.addEventListener("click", (e) => {
  e.preventDefault();
  regModalBox.style.display = "none";

  if (loginModalBox.style.display == "block") {
    loginModalBox.style.display = "none";
  } else {
    loginModalBox.style.display = "block";
  }
});

// PASSWORD TOGGLE FOR REGISTRATION FORM

// VARs FOR PASSWORD FIELD
let RegPsw = document.querySelector("#regPassword");
let pswEyeOpen = document.querySelector("#eyeOpen");
let pswEyeClosed = document.querySelector("#eyeClosed");
let togglePsw = document.querySelector(".eyeToggle");

// EVENTS FOR PASSWORD TOGGLE

togglePsw.onclick = function () {
  if (RegPsw.type == "text") {
    RegPsw.type = "password";

    pswEyeClosed.style.display = "none";
    pswEyeOpen.style.display = "block";
  } else {
    RegPsw.type = "text";

    pswEyeClosed.style.display = "block";
    pswEyeOpen.style.display = "none";
  }
};

// VARs FOR CONFIRM PASSWORD FIELD
let confirmPsw = document.querySelector("#confirmRegPass");
let confirmPswEyeOpen = document.querySelector("#eyeOpenkonfirm");
let ConfirmPswEyeClosed = document.querySelector("#eyeClosedkonfirm");
let toggleConfirmPsw = document.querySelector(".eyeToggle2");

// EVENT FOR CONFIRM PASSWORD TOGGLE
toggleConfirmPsw.onclick = function () {
  if (confirmPsw.type == "text") {
    confirmPsw.type = "password";
    confirmPswEyeOpen.style.display = "block";
    ConfirmPswEyeClosed.style.display = "none";
  } else {
    confirmPsw.type = "text";
    confirmPswEyeOpen.style.display = "none";
    ConfirmPswEyeClosed.style.display = "block";
  }
};

// PASSWORD TOGGLE FOR LOGIN FORM
// VARs FOR LOGIN
let LoginPswInput = document.querySelector("#password");
let toggleLogin = document.querySelector(".loginToggle");
let logEyeOpen = document.querySelector("#eyeOpenLogin");
let logCloseEye = document.querySelector("#eyeClosedLogin");

toggleLogin.onclick = function () {
  if (LoginPswInput.type == "password") {
    LoginPswInput.type = "text";
    logEyeOpen.style.display = "none";
    logCloseEye.style.display = "block";
  } else {
    LoginPswInput.type = "password";
    logEyeOpen.style.display = "block";
    logCloseEye.style.display = "none";
  }
};

// INDEX PAGE AUTO COUNTER
// Declaring vars
let statNums = document.querySelectorAll(".numbers");
interval = 0.000005;
// counter function for each of the stat boxes
statNums.forEach(function (statNum) {
  let startVal = 0;
  let endVal = parseInt(statNum.getAttribute("data-val"));

  let duration = Math.floor(interval / endVal);

  let counter = setInterval(function () {
    startVal += 1;
    statNum.textContent = `${startVal}+`;
    if (startVal == endVal) {
      clearInterval(counter);
    }
  }, duration);
});

// ABOUT PAGE AUTO COUNTER
// declaring UI vars

let aboutStatNums = document.querySelectorAll(".count");
let Interval = 1000;

aboutStatNums.forEach((aboutStatNum) => {
  let startVal = 0;
  let endVal = parseInt(aboutStatNum.getAttribute("data-val"));

  let duration = Math.trunc(Interval / endVal);

  let counter = setInterval(() => {
    startVal += 1;
    aboutStatNum.innerText = `${startVal}+`;

    if (startVal == endVal) {
      clearInterval(counter);
    }
  }, duration);

  // console.log(endVal);
});

// call sign up action for clicks on DOM

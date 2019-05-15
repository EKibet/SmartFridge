// Variables
const signupButton = document.getElementById('signup-button'),
    loginButton = document.getElementById('login-button'),
		signupButtonMb = document.getElementById('signup-button-mb'),
    loginButtonMb = document.getElementById('login-button-mb'),
		forgetButton = document.getElementById('forget-button'),
    userForms = document.getElementById('user_options-forms'),
		loginForm = document.getElementById('user_forms-login'),
		signUpForm = document.getElementById('user_forms-signup');

// Add event listener to the "Sign Up" button
signupButton.addEventListener('click', () => {
	userForms.classList.remove('show-forgotPass');
  userForms.classList.remove('bounceRight');
  userForms.classList.add('bounceLeft');	
}, false)

// Add event listener to the "Login" button
loginButton.addEventListener('click', () => {
	userForms.classList.remove('show-forgotPass');
  userForms.classList.remove('bounceLeft');
  userForms.classList.add('bounceRight');
}, false)

// Add event listener to the "Forget Password" button
forgetButton.addEventListener('click', () => {
	userForms.classList.add('show-forgotPass');
  // userForms.classList.add('bounceRight');
  // userForms.classList.remove('bounceLeft');
	userForms.classList.remove('show-login');
	userForms.classList.remove('show-signup');	
}, false)

// Add event listener to the "Signup" button mobile
signupButtonMb.addEventListener('click', () => {
	userForms.classList.remove('show-forgotPass');
	userForms.classList.remove('show-login');
	userForms.classList.add('show-signup');	
}, false)

// Add event listener to the "Login" button mobile
loginButtonMb.addEventListener('click', () => {
	userForms.classList.remove('show-forgotPass');
  userForms.classList.add('show-login');	
	userForms.classList.remove('show-signup');
}, false)
// REGISTER FORM
const $registerForm = document.querySelector('.js-register-form')

/**
 * Sends registers post data and handles messages.
 * @param {Object} formData - Register formdata object.
 */
const sendRegisterRequest = (formData) => {
    const url = 'register'

    fetch(url, {
        method:'POST',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        clearFormErrors($registerForm)

        if (response.hasOwnProperty('success')) {
            showAlert(response.success, 'success')
            $registerForm.reset()
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
            $registerForm.reset()
        }
        else {
            showFormErrors($registerForm, response)
        }
    })
}

/**
 * Validates register form data.
 * @returns {Object} Error messages with inpuut names as a key.
 */
const validateRegisterForm = (formData) => {
    const username = formData.get('username').trim()
    const email = formData.get('email').trim()
    const password = formData.get('password').trim()
    const repassword = formData.get('repassword').trim()
    const policy = formData.get('policy')

    const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    const passwordRegex = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/
    const result = {}

    if (username === '') {
        result.username = 'User name is required.'
    }
    else if (username.length < 8) {
        result.username = 'The user name must be at least 8 characters long.'
    }

    if (email === '') {
        result.email = 'E-mail address is required.'
    }
    else if (!email.match(emailRegex)) {
        result.email = 'The e-mail address format is invalid.'
    }

    if (password === '') {
        result.password = 'Password is required.'
    }
    else if (!password.match(passwordRegex)) {
      result.password = 'The password should be at least 8 characters long, including at least one uppercase letter, one lowercase letter, one digit, and one special character.'
    }

    if (repassword != '' && password !== repassword) {
        result.repassword = 'The re password field does not match the previously entered password.'
    }

    if (policy != '1') {
      result.policy = 'Privacy policy is required.'
    }

    return result
}

/**
 * Handles register form actions.
 */
const handleRegisterForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateRegisterForm(formData)
    clearFormErrors($form)

    if (true) { // Object.keys(errors).length === 0
        sendRegisterRequest(formData)
    }
    else {
       showFormErrors($form, errors)
    }
}

if ($registerForm) {
    $registerForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleRegisterForm(e)
    })
}

// LOGIN FORM
const $loginForm = document.querySelector('.js-login-form')

/**
 * Sends login post data and handles messages.
 * @param {Object} formData - Login formdata object.
 */
const sendLoginRequest = (formData) => {
    const url = 'login'

    fetch(url, {
        method:'POST',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        clearFormErrors($loginForm)

        if (response.hasOwnProperty('success')) {
          window.location.href = '/'
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
            $loginForm.reset()
        }
        else {
            showFormErrors($loginForm, response)
        }
    })
}

/**
 * Validates login form data.
 * @returns {Object} Error messages with inpuut names as a key.
 */
const validateLoginForm = (formData) => {
    const email = formData.get('email').trim()
    const password = formData.get('password').trim()

    const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    const passwordRegex = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/
    const result = {}

    if (email === '') {
        result.email = 'E-mail address is required.'
    }
    else if (!email.match(emailRegex)) {
        result.email = 'The e-mail address format is invalid.'
    }

    if (password === '') {
        result.password = 'Password is required.'
    }
    else if (!password.match(passwordRegex)) {
      result.password = 'The password should be at least 8 characters long, including at least one uppercase letter, one lowercase letter, one digit, and one special character.'
    }

    return result
}

/**
 * Handles login form actions.
 */
const handleLoginForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateLoginForm(formData)
    clearFormErrors($form)

    if (true) { // Object.keys(errors).length === 0
        sendLoginRequest(formData)
    }
    else {
       showFormErrors($form, errors)
    }
}

if ($loginForm) {
    $loginForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleLoginForm(e)
    })
}
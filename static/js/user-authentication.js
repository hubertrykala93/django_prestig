// REGISTER FORM
const $registerForm = document.querySelector('.js-register-form')

/**
 * Sends registers post data and handles messages.
 * @param {Object} formData - Register formdata object.
 */
const sendRegisterRequest = (formData) => {
    const url = 'api/v1/accounts/account-register'

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
        result.username = 'Username is required.'
    }
    else if (username.length < 8) {
        result.username = 'The username should consist of at least 8 characters.'
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
        result.repassword = 'The confirm password does not match the password.'
    }

    if (policy != '1') {
      result.policy = 'The privacy policy must be accepted.'
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
    const url = 'api/v1/accounts/account-login'

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
        console.log(response)

        if (response.hasOwnProperty('success')) {
            document.cookie = 'authtoken=' + response.token
            // window.location.href = '/'
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

// LOGOUT FORM
const $logoutForm = document.querySelector('.js-logout-form')

/**
 * Sends logout post data and handles messages.
 * @param {Object} formData - Logout formdata object.
 */
const sendLogoutRequest = (formData) => {
    const url = 'api/v1/accounts/account-logout'

    fetch(url, {
        method:'POST',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        console.log(response)

        if (response.hasOwnProperty('success')) {
            document.cookie = 'authtoken=' + '=; Max-Age=-99999999;'
            window.location.href = '/'
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
        }
    })
}

/**
 * Handles logout form actions.
 */
const handleLogoutForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    sendLogoutRequest(formData)
}

if ($logoutForm) {
    $logoutForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleLogoutForm(e)
    })
}
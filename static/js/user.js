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

    if (Object.keys(errors).length === 0) { 
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

    if (Object.keys(errors).length === 0) {
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

/**
* MY ACCOUNT
*/

// UPLOAD IMAGE
const $uploadInputs = document.querySelectorAll('.js-form-upload-input')

/**
 * Updates label of file uploader.
 * @param {HTMLElement} $input - Input which belongs to particular file uploader.
 * @param {string} content - Text to show in label.
*/
const updateFileLabel = ($input, content) => {
  const $uploadedFileLabel = $input.closest('.js-form-upload-container').querySelector('.js-form-upload-filelabel')
  $uploadedFileLabel.textContent = content
}

/**
 * Updates source of preview image.
 * @param {HTMLElement} $input - Input which belongs to particular file uploader.
 * @param {object} file - Image file which to show in preview.
 */
const updateImagePreview = ($input, file) => {
  const $previewImage = $input.closest('.js-form-upload-container').querySelector('.js-form-upload-preview-image')

  $previewImage.src = URL.createObjectURL(file)
}

/**
 * Checks if file from given event is of the correct type and handles label contents to show.
 * @param {object} e - Event object of file input.
 */
const validateImage = (e) => {
  const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp']
  const $input = e.target
  const file = $input.files[0]
  if (allowedTypes.indexOf(file.type) > -1) {
    updateFileLabel($input, $input.value.split("\\").pop())
    updateImagePreview($input, file)
  }else {
    updateFileLabel($input, 'Not supported image type');
  }
}

if ($uploadInputs) {
  $uploadInputs.forEach($input => {
    $input.addEventListener('change', function (e) {
      validateImage(e)
    })
  })
}

// ACCOUNT SETTINGS

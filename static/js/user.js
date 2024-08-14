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
    else if (username.length > 35) {
        result.username = 'The username cannot be longer than 35 characters.'
    }

    if (email === '') {
        result.email = 'E-mail address is required.'
    }
    else if (!email.match(emailRegex)) {
        result.email = 'The e-mail address format is invalid.'
    }
    else if (email.length > 255) {
        result.email = 'The email cannot be longer than 255 characters.'
    }

    if (password === '') {
        result.password = 'Password is required.'
    }
    else if (!password.match(passwordRegex)) {
      result.password = 'The password should be at least 8 characters long, including at least one uppercase letter, one lowercase letter, one digit, and one special character.'
    }
    else if (password.length > 255) {
        result.password = 'The password cannot be longer than 255 characters.'
    }
    else if (password !== repassword) {
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
    else if (email.length > 255) {
        result.email = 'The e-mail address cannot be longer than 255 characters.'
    }

    if (password === '') {
        result.password = 'Password is required.'
    }
    else if (!password.match(passwordRegex)) {
      result.password = 'The password should be at least 8 characters long, including at least one uppercase letter, one lowercase letter, one digit, and one special character.'
    }
    else if (password.length > 255) {
        result.password = 'The password cannot be longer than 255 characters.'
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
 * Shows button that deletes uploaded image.
 */
const showDeleteImageButton = () => {
    document.querySelector('.js-form-upload-delete-image').classList.add('active')
}

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
    showDeleteImageButton()
  }else {
    $input.value = null
    updateFileLabel($input, 'Not supported image type')
  }
}

if ($uploadInputs) {
  $uploadInputs.forEach($input => {
    $input.addEventListener('change', function (e) {
      validateImage(e)
    })
  })
}

// DELETE IMAGE
const $deleteImageButton = document.querySelector('.js-form-upload-delete-image')

/**
 * Hides button that deletes uploaded image.
 */
const hideDeleteImageButton = () => {
    document.querySelector('.js-form-upload-delete-image').classList.remove('active')
}

/**
 * Restores file input to starting point.
 */
const resetFileInput = () => {
    document.querySelector('[name="profilepicture"]').value = null
    document.querySelector('.js-form-upload-filelabel').textContent = 'No File Selected'
}

/**
 * Restores preview image source to default.
 */
const resetPreviewImage = () => {
    document.querySelector('.js-form-upload-preview-image').src = '/media/profile_images/default_profile_image.png'
}

/**
 * Sends delete profile picture request and handles messages.
 */
const sendDeleteProfilePictureRequest = () => {
    const url = '/api/v1/profiles/delete-profile-picture'
    const formData = new FormData()

    fetch(url, {
        method:'DELETE',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        if (response.hasOwnProperty('success')) {
            showAlert(response.success, 'success')
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
        }
    })
}

/**
 * Handles delete profile picture button actions.
 */
const hadleDeleteImage = () => {
    resetFileInput()
    resetPreviewImage()
    hideDeleteImageButton()
    sendDeleteProfilePictureRequest()
}

if ($deleteImageButton) {
    $deleteImageButton.addEventListener('click', hadleDeleteImage)
}

// ACCOUNT SETTINGS
const $accountSettingsForm = document.querySelector('.js-account-settings-form')

/**
 * Sends account settings post data and handles messages.
 * @param {Object} formData - Account settings formdata object.
 */
const sendAccountSettingsRequest = (formData) => {
    const url = '/api/v1/accounts/update-account'

    const clearPasswordFields = () => {
        const $passwordFields = $accountSettingsForm.querySelectorAll('[name="password"], [name="repassword"]')

        $passwordFields.forEach($input => { $input.value = '' })
    }

    fetch(url, {
        method:'PATCH',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        clearFormErrors($accountSettingsForm)

        if (response.hasOwnProperty('success')) {
            clearPasswordFields()
            showAlert(response.success, 'success')
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
        }
        else {
            showFormErrors($accountSettingsForm, response)
        }
    })
}

/**
 * Validates account settings form data.
 * @returns {Object} Error messages with inpuut names as a key.
 */
const validateAccountSettingsForm = (formData) => {
    const username = formData.get('username').trim()
    const email = formData.get('email').trim()
    const password = formData.get('password').trim()
    const repassword = formData.get('repassword').trim()

    const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    const passwordRegex = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/
    const result = {}

    if (username === '') {
        result.username = 'Username is required.'
    }
    else if (username.length < 8) {
        result.username = 'The username should consist of at least 8 characters long.'
    }
    else if (username.length > 35) {
        result.username = 'The username cannot be longer than 35 characters.'
    }

    if (email === '') {
        result.email = 'E-mail address is required.'
    }
    else if (!email.match(emailRegex)) {
        result.email = 'The e-mail address format is invalid.'
    }
    else if (email.length > 255) {
        result.email = 'The email cannot be longer than 255 characters.'
    }

    if (password) {
        if (!password.match(passwordRegex)) {
        result.password = 'The password should be at least 8 characters long, including at least one uppercase letter, one lowercase letter, one digit, and one special character.'
        }
        else if (password.length > 255) {
            result.password = 'The password cannot be longer than 255 characters.'
        }
        else if (password !== repassword) {
            result.repassword = 'The confirm password does not match the password.'
        }
    }

    return result
}

/**
 * Handles account settings form actions.
 */
const handleAccountSettingsForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateAccountSettingsForm(formData)
    clearFormErrors($form)

    if (Object.keys(errors).length === 0 ) {
        sendAccountSettingsRequest(formData)
    }
    else {
       showFormErrors($form, errors)
    }
}

if ($accountSettingsForm) {
    $accountSettingsForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleAccountSettingsForm(e)
    })
}

// PROFILE SETTINGS
const $profileSettingsForm = document.querySelector('.js-profile-settings-form')

/**
 * Sends profile settings post data and handles messages.
 * @param {Object} formData - Profile settings formdata object.
 */
const sendProfileSettingsRequest = (formData) => {
    const url = '/api/v1/profiles/update-profile'

    fetch(url, {
        method:'PATCH',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        clearFormErrors($profileSettingsForm)

        if (response.hasOwnProperty('success')) {
            showAlert(response.success, 'success')
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
        }
        else {
            showFormErrors($profileSettingsForm, response)
        }
    })
}

/**
 * Validates profile settings form data.
 * @returns {Object} Error messages with inpuut names as a key.
 */
const validateProfileSettingsForm = (formData) => {
    const firstname = formData.get('firstname').trim()
    const lastname = formData.get('lastname').trim()
    const dateofbirth = formData.get('dateofbirth')
    const profilepicture = formData.get('profilepicture')
    const bio = formData.get('bio').trim()
    const gender = formData.get('gender')
    const facebook = formData.get('facebook').trim()
    const instagram = formData.get('instagram').trim()

    const onlyLettersRegex = /^[a-z]+$/i
    const dateRegex = /^\d{4}-\d{2}-\d{2}$/
    const usernameRegex = /^[\w.-]+$/

    const result = {}
    
    if (firstname) {
        if (!firstname.match(onlyLettersRegex)) {
            result.firstname = 'The first name should contain only letters.'
        }
        else if (firstname.length < 2) {
            result.firstname = 'The first name should consist of at least 2 characters long.'
        }
        else if (firstname.length > 35) {
            result.firstname = 'The first name cannot be longer than 35 characters.'
        }
    }
    
    if (lastname) {
        if (!lastname.match(onlyLettersRegex)) {
            result.lastname = 'The last name should contain only letters.'
        }
        else if (lastname.length < 2) {
            result.lastname = 'The last name should consist of at least 2 characters long.'
        }
        else if (firstname.length > 35) {
            result.lastname = 'The last name cannot be longer than 35 characters.'
        }
    }

    if (dateofbirth) {
        if (!dateofbirth.match(dateRegex)) {
            result.dateofbirth = "Invalid date format. The correct format is 'YYYY-MM-DD'."
        }
        else {
            const now = new Date().getTime()
            const chosenDate = new Date(dateofbirth).getTime()
            
            if (chosenDate > now) {
                result.dateofbirth = 'You cannot enter a future date. Please select a valid date.'
            }
        }
    }

    if (profilepicture.name) {
        const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp']
        if (allowedTypes.indexOf(profilepicture.type) === -1) {
            result.profilepicture = "Invalid file format. The correct formats are 'jpeg', 'jpg', 'png', 'webp'."
        }
    }

    if (bio) {
        if (bio.length < 10) {
            result.bio = 'The bio should consist of at least 10 characters long.'
        }
        else if (bio.length > 150) {
            result.bio = 'The bio cannot be longer than 150 characters.'
        }
    }

    if (gender) {
        const allowedGenders = ['male', 'female', 'undefined']
        if (allowedGenders.indexOf(gender) === -1) {
            result.gender = 'Wrong gender value.'
        }
    }
    else {
        result.gender = 'The gender must be selected.'
    }

    if (facebook) {
        if (facebook.length > 50) {
            result.facebook = 'The facebook username cannot be longer than 50 characters.'
        }
        else if (!facebook.match(usernameRegex)) {
            result.facebook = 'The facebook username should contain only letters, digits, dashes, underscores, periods.'
        }
    }

    if (instagram) {
        if (instagram.length > 50) {
            result.instagram = 'The instagram username cannot be longer than 50 characters.'
        }
        else if (!instagram.match(usernameRegex)) {
            result.instagram = 'The instagram username should contain only letters, digits, dashes, underscores, periods.'
        }
    }

    return result
}

/**
 * Handles profile settings form actions.
 */
const handleProfileSettingsForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateProfileSettingsForm(formData)
    clearFormErrors($form)

    if (Object.keys(errors).length === 0 ) {
        sendProfileSettingsRequest(formData)
    }
    else {
       showFormErrors($form, errors)
    }
}

if ($profileSettingsForm) {
    $profileSettingsForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleProfileSettingsForm(e)
    })
}

// DELIVERY DETAILS
const $deliveryDetailsForm = document.querySelector('.js-delivery-details-form')

/**
 * Sends delivery details post data and handles messages.
 * @param {Object} formData - Delivery details formdata object.
 */
const sendDeliveryDetailsRequest = (formData) => {
    const url = '/api/v1/delivery-details/update-delivery-details'

    fetch(url, {
        method:'PATCH',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        clearFormErrors($deliveryDetailsForm)

        if (response.hasOwnProperty('success')) {
            showAlert(response.success, 'success')
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
        }
        else {
            showFormErrors($deliveryDetailsForm, response)
        }
    })
}

/**
 * Validates delivery details form data.
 * @returns {Object} Error messages with input names as a key.
 */
const validateDeliveryDetailsForm = (formData) => {
    const phone = formData.get('phone').trim()
    const country = formData.get('country').trim()
    const state = formData.get('state').trim()
    const city = formData.get('city').trim()
    const street = formData.get('street').trim()
    const housenumber = formData.get('housenumber').trim()
    const apartmentnumber = formData.get('apartmentnumber').trim()
    const postalcode = formData.get('postalcode').trim()
    const onlyDigitsRegex = /^[\d]+$/
    const onlyLettersAndDigitsRegex = /^[a-z0-9]+$/i

    const result = {}

    if (phone === '') {
        result.phone = 'Phone number is required.'
    }
    else if (!phone.match(onlyDigitsRegex)) {
        result.phone = 'The phone number should consist of digits only.'
    }
    else if (phone.length < 8) {
        result.phone = 'The phone number should consist of at least 8 characters long.'
    }
    else if (phone.length > 20) {
        result.phone = 'The phone number cannot be longer than 20 characters.'
    }

    if (country === '') {
        result.country = 'Country is required.'
    }
    else if (country.length < 3) {
        result.country = 'The country should consist of at least 3 characters long.'
    }
    else if (country.length > 56) {
        result.country = 'The country cannot be longer than 56 characters.'
    }

    if (state === '') {
        result.state = 'State is required.'
    }
    else if (state.length < 3) {
        result.state = 'The state should consist of at least 3 characters long.'
    }
    else if (state.length > 56) {
        result.state = 'The state cannot be longer than 50 characters.'
    }

    if (city === '') {
        result.city = 'City is required.'
    }
    else if (city.length < 3) {
        result.city = 'The city should consist of at least 3 characters long.'
    }
    else if (city.length > 169) {
        result.city = 'The city cannot be longer than 169 characters.'
    }

    if (street === '') {
        result.street = 'Street is required.'
    }
    else if (street.length < 3) {
        result.street = 'The street should consist of at least 3 characters long.'
    }
    else if (street.length > 50) {
        result.street = 'The street cannot be longer than 50 characters.'
    }

    if (housenumber === '') {
        result.housenumber = 'House number is required.'
    }
    else if (!housenumber.match(onlyLettersAndDigitsRegex)) {
        result.housenumber = 'The house number must consist of letters or digits only.'
    }
    else if (housenumber.length > 5) {
        result.housenumber = 'The house number cannot be longer than 5 characters.'
    }

    if (apartmentnumber) {
        if (!apartmentnumber.match(onlyLettersAndDigitsRegex)) {
            result.apartmentnumber = 'The apartment number must consist of letters or digits only.'
        }
        else if (apartmentnumber.length > 5) {
            result.apartmentnumber = 'The apartment number cannot be longer than 5 characters.'
        }
    }

    if (postalcode === '') {
        result.postalcode = 'Postal code is required.'
    }
    else if (postalcode.length < 5) {
        result.postalcode = 'The postal code should consist of at least 5 characters long.'
    }
    else if (postalcode.length > 10) {
        result.postalcode = 'The postal code cannot be longer than 10 characters.'
    }

    return result
}

/**
 * Handles delivery details form actions.
 */
const handleDeliveryDetailsForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateDeliveryDetailsForm(formData)
    clearFormErrors($form)

    if (Object.keys(errors).length === 0 ) {
        sendDeliveryDetailsRequest(formData)
    }
    else {
       showFormErrors($form, errors)
    }
}

if ($deliveryDetailsForm) {
    $deliveryDetailsForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleDeliveryDetailsForm(e)
    })
}

// FORGOT PASSWORD
const $forgotPasswordForm = document.querySelector('.js-forgot-password-form')

/**
 * Sends forgot password post data and handles messages.
 * @param {Object} formData - Forgot password formdata object.
 */
const sendForgotPasswordRequest = (formData) => {
    const url = '/api/v1/accounts/forgot-password'

    fetch(url, {
        method:'POST',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        clearFormErrors($forgotPasswordForm)

        if (response.hasOwnProperty('success')) {
            showAlert(response.success, 'success')
            $forgotPasswordForm.reset()
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
            $forgotPasswordForm.reset()
        }
        else {
            showFormErrors($forgotPasswordForm, response)
        }
    })
}

/**
 * Validates forgot password form data.
 * @returns {Object} Error messages with inpuut names as a key.
 */
const validateForgotPasswordForm = (formData) => {
    const email = formData.get('email').trim()

    const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    const result = {}

    if (email === '') {
        result.email = 'E-mail address is required.'
    }
    else if (!email.match(emailRegex)) {
        result.email = 'The e-mail address format is invalid.'
    }
    else if (email.length > 255) {
        result.email = 'The e-mail address cannot be longer than 255 characters.'
    }

    return result
}

/**
 * Handles forgot password form actions.
 */
const handleForgotPasswordForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateForgotPasswordForm(formData)
    clearFormErrors($form)

    if (Object.keys(errors).length === 0) { //Object.keys(errors).length === 0
        sendForgotPasswordRequest(formData)
    }
    else {
       showFormErrors($form, errors)
    }
}

if ($forgotPasswordForm) {
    $forgotPasswordForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleForgotPasswordForm(e)
    })
}
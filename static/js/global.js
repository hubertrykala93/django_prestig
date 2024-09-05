// BOTTOM GALLERY

const bottomGallery = new Swiper('.js-bottom-gallery-carousel', {
  loop: true,
  draggable: true,
  grabCursor: true,
  effect: 'slide',
  autoplay: {
      delay: 1000,
  },
  speed: 800,
  breakpoints: {
      480: {
          slidesPerView: 2,
      },
      768: {
          slidesPerView: 3,
      },
      992: {
          slidesPerView: 4,
      },
      1200: {
          slidesPerView: 5,
      },
      1600: {
          slidesPerView: 6,
      }
  }
})

// CREATE ALERT

/**
 * Removes alert after few seconds.
 */
const removeAlert = ()=> {
    const $alert = document.querySelector('.js-alert')

    if ($alert) {
        setTimeout(() => {
            $alert.remove()
        }, 2500);
    }
}

/**
 * Shows alert message.
 * @param {string} message - Message to show in alert
 * @param {string} type - Type of alert (error, success)
 */
const showAlert = (message, type) => {
    const html = `
        <div class="alert alert--${type} js-alert">
            <div class="alert__message">${message}</div>
        </div>
    `

    document.querySelector('body script').insertAdjacentHTML('beforebegin', html)
    removeAlert()
}

// FORMS

/**
 * Clear error messages from given form.
 * @param {HTMLElement} $form - Form where to remove all error messages.
 */
const clearFormErrors = ($form) => {
    const $errors = $form.querySelectorAll('.js-error')

    if ($errors.length) {
        $errors.forEach($error => $error.remove())
    }
}

/**
 * Shows error messages in given form.
 * @param {HTMLElement} $form - Form where to show error messages.
 * @param {Object} errors - Object with input names as a key and error messages.
 */
const showFormErrors = ($form, errors) => {
    for (const [key, value] of Object.entries(errors)) {
        const $input = $form.querySelector(`[name="${key}"]`)
    if ($input) {
        const $error = document.createElement('span')
        $error.classList.add('js-error')
        $error.classList.add('form__error')
        $error.textContent = value
        $input.closest('.js-form-field').append($error)
    }
    }
}

// CLOSE MESSAGE BAR
const $messageBar = document.querySelector('.js-message-bar')

/**
 * Removes message bar from DOM.
 */
const closeMessageBar = (e) => {
    $messageBar.remove()
}

if ($messageBar) {
    const $closeMessageBar = $messageBar.querySelector('.js-message-bar-close')

    $closeMessageBar.addEventListener('click', closeMessageBar)
}

// ADD TO WISHLIST
const $productsCardsParents = document.querySelectorAll('.js-products-cards-parent')

/**
 * Sends add to wishlist post data.
 * @param {Object} formData - Add to wishlist formdata object.
 */
const sendAddToWishlistRequest = (formData) => {
    const url = 'add-to-wishlist'

    fetch(url, {
        method:'POST',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        if (response.hasOwnProperty('success')) {
            showAlert(response.success, 'success')
            return response
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
            return false
        }
    })
}

const handleCardsParent = (e) => {
    $addToWishlistBtn = e.target.closest('.js-add-to-wishlist')
    if (!$addToWishlistBtn) {return false}

    const id = $addToWishlistBtn.closest('.js-product-card').dataset.id
    const formData = new FormData()
    formData.append('id', id)
    const response = sendAddToWishlistRequest(formData)
    
    if (response) {
        $addToWishlistBtn.classList.toggle('active')
    }
}

if ($productsCardsParents) {
    $productsCardsParents.forEach($cardsParent => {
        $cardsParent.addEventListener('click', handleCardsParent)
    })
}
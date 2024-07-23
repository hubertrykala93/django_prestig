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

// FORM

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
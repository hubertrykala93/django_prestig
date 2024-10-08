/**
* HEADER
*/

// MOBILE MENU
const $mobileNavToggler = document.querySelector('.js-mobile-nav-toggler')
const $mobileNavTogglerIcon = document.querySelector('.js-mobile-nav-toggler i')
const $headerNav = document.querySelector('.js-header-nav')

/**
 * Changes mobile nav toggler icon into hamburger
 */
const togglerHamburgerIcon = () => {
    $mobileNavTogglerIcon.classList.remove('ri-close-line')
    $mobileNavTogglerIcon.classList.add('ri-menu-3-line')
}

/**
 * Changes mobile nav toggler icon into closing
 */
const togglerCloseIcon = () => {
    $mobileNavTogglerIcon.classList.remove('ri-menu-3-line')
    $mobileNavTogglerIcon.classList.add('ri-close-line')
}

/**
 * Show and hide mobile version of main navigation
 */
const mobileMenuToggle = () => {
    if ($headerNav.classList.contains('active')) {
        $mobileNavToggler.setAttribute('aria-expanded', "false")
        togglerHamburgerIcon()
    } else {
        $mobileNavToggler.setAttribute('aria-expanded', "true")
        togglerCloseIcon()
    }
    $headerNav.classList.toggle('active')
}

if ($mobileNavToggler && $headerNav) {
    $mobileNavToggler.addEventListener('click', mobileMenuToggle)
}

// HEADER BUTTONS
const $headerButtons = document.querySelector('.js-header-buttons')

/**
 * Closes chosen header dropdown.
 * @param {HTMLElement} $dropdown - Particular dropdown to close.
 */
const closeDropdown = ($dropdown) => {
    $dropdown.classList.remove('active')
}

/**
 * Closes all open dropdowns.
 */
const closeDropdowns = () => {
    document.querySelectorAll('.js-header-buttons-dropdown').forEach($dropdown => {
        if ($dropdown.classList.contains('active')) {
            closeDropdown($dropdown)
        }
    })
}

/**
 * Removes highlighting of active header buttons.
 */
const deemphasizeDropdownButtons = () => {
    document.querySelectorAll('.js-header-dropdown-button').forEach($btn => {
        if ($btn.classList.contains('active')) {
            $btn.classList.remove('active')
        }
    })
}

/**
 * Handles opening particular header dropdown.
 * @param {HTMLElement} $btn - Currently clicked dropdown button.
 */
const handleHeaderDropdown = ($btn) => {
    const $dropDown = $btn.nextElementSibling
    deemphasizeDropdownButtons()
    
    if ($dropDown.classList.contains('active')) {
        $dropDown.classList.remove('active')
    }
    else {
        closeDropdowns()
        $dropDown.classList.add('active')
        $btn.classList.add('active')
    }
} 

if ($headerButtons) {
    $headerButtons.addEventListener('click', e => {
        const $target = e.target.closest('button')
        if (!$target) {return false}

        if ($target.classList.contains('js-header-dropdown-button')) {
            handleHeaderDropdown($target)
        }
    })

    document.addEventListener('click', e => {
        $openDropdown = document.querySelector('.js-header-buttons-dropdown.active')

        if ($openDropdown) {
            const $target = e.target
            if (!($target.closest('.js-header-buttons-dropdown') || $target.closest('.js-header-dropdown-button'))) {
                closeDropdown($openDropdown)
                deemphasizeDropdownButtons()
            }

        }
    })
}

/**
* HOME PAGE
*/

// HOME SLIDER
const slider = new Swiper('.js-slider', {
    loop: true,
    draggable: true,
    grabCursor: true,
    effect: 'slide',
    autoplay: {
        delay: 5000,
    },
    speed: 1500,

    pagination: {
      el: '.js-slider-pagination',
      clickable: true,
    },
});

// FEATURED PRODUCTS TABS
const $featuredProducts = document.querySelector('.js-featured-products')

/**
 * Show and hide chosen category rows
 * @param {string} category - Name of category to show
 */
const toggleTabsContents = (category) => {
    $rows = $featuredProducts.querySelectorAll('.js-featured-products-row')
    
    $rows.forEach(row => {
        if (row.dataset.category === category) {
            row.classList.add('active')
        } else {
            row.classList.remove('active')
        }
    })
}

/**
 * Handles tabs navigation click event
 */
const handleNav = (e) => {
    const $target = e.target
    if ($target.tagName !== 'BUTTON') { return false }
    const $navItems = $featuredProducts.querySelectorAll('.js-featured-products-nav-item')
    $navItems.forEach(btn => btn.classList.remove('active'))
    $target.classList.add('active')
    
    const category = $target.dataset.category
    toggleTabsContents(category)
}

if ($featuredProducts) {
    const $nav = $featuredProducts.querySelector('.js-featured-products-nav')

    $nav.addEventListener('click', (e) => {
        handleNav(e)
    })
}

// NEW PRODUCTS CAROUSEL

const $newProductsSection = document.querySelector('.js-new-products')

if ($newProductsSection) {
    const $leftArrow = $newProductsSection.querySelector('.js-arrow-left')
    const $rightArrow = $newProductsSection.querySelector('.js-arrow-right')

    const newProductsCarousel = new Swiper('.js-new-products-carousel', {
        draggable: true,
        grabCursor: true,
        effect: 'slide',
        autoplay: {
            delay: 5000,
        },
        speed: 1000,
        navigation: {
            nextEl: $rightArrow,
            prevEl: $leftArrow,
        },
        spaceBetween: 30,
        breakpoints: {
            640: {
                slidesPerView: 2,
            },
            992: {
                slidesPerView: 3,
            },
            1200: {
                slidesPerView: 4,
            }
        }
    });
}

// LOGOS CAROUSEL

const logos = new Swiper('.js-logos-carousel', {
    loop: true,
    draggable: true,
    grabCursor: true,
    effect: 'slide',
    autoplay: {
        delay: 500,
    },
    speed: 800,
    slidesPerView: 2,
    spaceBetween: 50,
    breakpoints: {
        480: {
            slidesPerView: 3,
        },
        768: {
            slidesPerView: 4,
        },
        1200: {
            slidesPerView: 5,
        }
    }
});

// TOP PRODUCTS CAROUSEL

const $topProductsSection = document.querySelector('.js-top-products')

if ($topProductsSection) {
    const $leftArrow = $topProductsSection.querySelector('.js-arrow-left')
    const $rightArrow = $topProductsSection.querySelector('.js-arrow-right')

    const topProductsCarousel = new Swiper('.js-top-products-carousel', {
        draggable: true,
        grabCursor: true,
        effect: 'slide',
        autoplay: {
            delay: 5000,
        },
        speed: 1000,
        navigation: {
            nextEl: $rightArrow,
            prevEl: $leftArrow,
        },
        spaceBetween: 30,
        breakpoints: {
            640: {
                slidesPerView: 2,
            },
            992: {
                slidesPerView: 3,
            },
            1200: {
                slidesPerView: 4,
            }
        }
    });
}

// TESTIMONIALS CAROUSEL

const testimonials = new Swiper('.js-testimonials-slider', {
loop: true,
draggable: true,
grabCursor: true,
effect: 'slide',
autoplay: {
    delay: 5000,
},
speed: 1000,

navigation: {
    nextEl: '.js-arrow-right',
    prevEl: '.js-arrow-left',
  },
});

// NEWSLETTER FORM

const $newsletterForm = document.querySelector('.js-newsletter-form')

/**
 * Sends newsletter's post data and handles messages.
 * @param {Object} formData - Newsletter form data object.
 */
const sendNewsletterRequest = (formData) => {
    const url = 'api/v1/newsletters/create'

    fetch(url, {
        method:'POST',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        clearFormErrors($newsletterForm)

        if (response.hasOwnProperty('success')) {
            showAlert(response.success, 'success')
            $newsletterForm.reset()
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
            $newsletterForm.reset()
        }
        else {
            showFormErrors($newsletterForm, response)
        }
    })
}

/**
 * Validates newsletter form data.
 * @returns {Object} Error messages with inpuut names as a key.
 */
const validateNewsletterForm = (formData) => {
    const email = formData.get('email').trim()
    const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    const result = {}

    if (email === '') {
        result.email = 'E-mail Address is required.'
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
 * Handles newsletter form actions.
 */
const handleNewsletterForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateNewsletterForm(formData)
    clearFormErrors($form)

    if (Object.keys(errors).length === 0) {
        sendNewsletterRequest(formData)
    }
    else {
        showFormErrors($form, errors)
    }
}

if ($newsletterForm) {
    $newsletterForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleNewsletterForm(e)
    })
}

/**
* ABOUT PAGE
*/

// VIDEO POPUP
const $openPopupBtn = document.querySelector('.js-videopopup-btn')

/**
 * Closes video popup if it's currently open.
 */
const closeVideoPopup = (e) => {
    if (e.target.classList.contains('js-video-popup')) {
        const $videoPopup = document.querySelector('.video-popup')
    
        if ($videoPopup) {
            $videoPopup.remove()
        }
        document.removeEventListener('click', closeVideoPopup)
    }

}

/**
 * Generates html of video popup.
 * @param {string} src - Source of video to show.
 */
const openVideoPopup = (src) => {
    const html = `
        <div class="video-popup js-video-popup">
            <div class="video-popup__video-wrapper">
                <video controls mute autoplay>
                    <source src="${src}" type="video/mp4" />

                    Download the
                    <a href="${src}">MP4</a>
                    video.
                </video>
            </div>
        </div>
    `

    document.querySelector('body script').insertAdjacentHTML('beforebegin', html)
    document.addEventListener('click', closeVideoPopup)
}

/**
 * Handles opening video popup button trigger.
 */
const handleVideoPopup = (e) => {
    const $btn = e.target.closest('button')
    const videoSource = $btn.dataset.video
    
    if ($btn && videoSource) {
        openVideoPopup(videoSource)
    }
}

if ($openPopupBtn) {
    $openPopupBtn.addEventListener('click', handleVideoPopup)
}

/**
* CONTACT PAGE
*/

// CONTACT FORM

const $contactForm = document.querySelector('.js-contact-form')

/**
 * Sends contact's post data and handles messages.
 * @param {Object} formData - Contact form data object.
 */
const sendContactRequest = (formData) => {
    const url = 'api/v1/contact-mails/create'

    fetch(url, {
        method:'POST',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        clearFormErrors($contactForm)

        if (response.hasOwnProperty('success')) {
            showAlert(response.success, 'success')
            $contactForm.reset()
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
            $contactForm.reset()
        }
        else {
            showFormErrors($contactForm, response)
        }
    })
}

/**
 * Validates contact form data.
 * @returns {Object} Error messages with inpuut names as a key.
 */
const validateContactForm = (formData) => {
    const fullname = formData.get('fullname').trim()
    const email = formData.get('email').trim()
    const subject = formData.get('subject').trim()
    const message = formData.get('message').trim()
    const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    const result = {}

    if (fullname === '') {
        result.fullname = 'Full name is required.'
    }
    else if (fullname.length < 8) {
        result.fullname = 'The full name must be at least 8 characters long.'
    }
    else if (fullname.length > 50) {
        result.fullname = 'The full name cannot be longer than 50 characters.'
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

    if (subject === '') {
        result.subject = 'Subject is required.'
    }
    else if (subject.length < 8) {
        result.subject = 'The subject must be at least 8 characters long.'
    }
    else if (subject.length > 100) {
        result.subject = 'The subject cannot be longer than 100 characters.'
    }

    if (message === '') {
        result.message = 'Message is required.'
    }
    else if (message.length < 20) {
        result.message = 'The message must be at least 20 characters long.'
    }
    else if (message.length > 1000) {
        result.message = 'The message cannot be longer than 1000 characters.'
    }

    return result
}

/**
 * Handles contact form actions.
 */
const handleContactForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateContactForm(formData)
    clearFormErrors($form)

    if (Object.keys(errors).length === 0) {
        sendContactRequest(formData)
    }
    else {
       showFormErrors($form, errors)
    }
}

if ($contactForm) {
    $contactForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleContactForm(e)
    })
}

/**
* TABS
*/
const $tabsButtons = document.querySelectorAll('.js-tabs-nav-button')

/**
 * Hides currently open tab content.
 */
const hideActiveTabContent = () => {
    document.querySelectorAll('.js-tab-contents-item').forEach($content => {
        if ($content.classList.contains('active')) {
            $content.classList.remove('active')
        }
    })
}

/**
 * Removes active state from currently active one.
 */
const removeTabNavActivity = () => {
    document.querySelectorAll('.js-tabs-nav-button').forEach($button => {
        if ($button.classList.contains('active')) {
            $button.classList.remove('active')
        }
    })
}

/**
 * Shows tab content of clicked tab nav button.
 * @param {number} showIndex - Index of tab content to show.
 */
const showTabContent = (showIndex) => {
    document.querySelectorAll('.js-tab-contents-item').forEach(($content, index) => {
        if (showIndex == index) {
            $content.classList.add('active')
        }
    })
}

/**
 * Activate tab nav button of clicked one.
 * @param {number} showIndex - Index of tab nav button to activate.
 */
const addTabNavActivity = (showIndex) => {
    document.querySelectorAll('.js-tabs-nav-button').forEach(($button, index) => {
        if (showIndex == index) {
            $button.classList.add('active')
        }
    })
}

/**
 * Handles tabs changing.
 * @param {number} index - Index of clicked tab.
 */
const handleTabsNav = (index) => {
    removeTabNavActivity()
    addTabNavActivity(index)
    hideActiveTabContent()
    showTabContent(index)
}

if ($tabsButtons) {
    $tabsButtons.forEach(($button, index) => {
        $button.addEventListener('click', () => {
            handleTabsNav(index)
        })
    })
}
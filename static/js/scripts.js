// const $form = document.querySelector('form')

// const sendData = (data) => {
//     const url = 'send-file'
//     fetch(url, {
//        method:'POST',
//        headers:{
//        'X-CSRFToken':csrftoken,
//        },
//        body: data
//     }).then((response) => {
//          return response.json()
//     }).then((data) => {
//           console.log('data:',data)
//     })
// }

// $form.addEventListener('submit', function (e) {
//     e.preventDefault()

//     let data = new FormData($form)
//     console.log(data)
//     sendData(data)
// })

/**
* HEADER
*/
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

// NEWSLETTER

const $newsletterForm = document.querySelector('.js-newsletter-form')

const clearFormErrors = ($form) => {
    const $errors = $form.querySelectorAll('.js-error')

    if ($errors.length) {
        $errors.forEach($error => $error.remove())
    }
}

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

const sendNewsletterRequest = (formData) => {
    const url = 'join-newsletter'

    fetch(url, {
        method:'POST',
        headers:{
        // 'X-CSRFToken':csrftoken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((data) => {
          console.log('data:', data)
    })
}

const validateNewsletterForm = (formData) => {
    const email = formData.get('email')
    const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

    if (email === '') {
        return {'email': 'Email cannot be empty!'}
    }
    else if (!email.match(emailRegex)) {
        return {'email': 'Wrong email format!'}
    }

    return ''
}

const handleNewsletterForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateNewsletterForm(formData)
    clearFormErrors($form)

    if (errors === '') {
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


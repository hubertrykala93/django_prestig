// const $form = document.querySelector('form')

// const sendData = (data) => {
//     const url = 'send-file'
//     fetch(url, {
//        method:'POST',
//        headers:{
// //        'X-CSRFToken':csrftoken,
//        },
//        body: data
//       })
//       .then((response) => {
//          return response.json()
//       })
//       .then((data) => {
//           console.log('data:',data)
//       });
//     }

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
});
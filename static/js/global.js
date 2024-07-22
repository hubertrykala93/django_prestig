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
});
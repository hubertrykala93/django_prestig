// SHOW FILTER
const $openFilterBtn = document.querySelector('.js-open-filter-btn')
const $filterWrapper = document.querySelector('.js-filter')

/**
 * Opens shop aside filer.
 */
const openFilter = () => {
  if ($filterWrapper) {
    $filterWrapper.classList.add('active')
  }
}

/**
 * Close shop aside filer.
 */
const closeFilter = () => {
  if ($filterWrapper) {
    $filterWrapper.classList.remove('active')
  }
}

if ($openFilterBtn) {
  const $closeFilterBtn = document.querySelector('.js-close-filter-btn')

  $openFilterBtn.addEventListener('click', openFilter)
  $closeFilterBtn.addEventListener('click', closeFilter)
}

// FILTER ACCORDION
const $filterAccordion = document.querySelector('.js-filter-accordion')

const handleFilterAccordion = ($heading) => {
  $body = $heading.nextElementSibling
  $icon = $heading.querySelector('i')
  if ($body.offsetHeight == 0) {
    $body.style.maxHeight = $body.scrollHeight + 'px'
    $icon.classList.remove('ri-add-line')
    $icon.classList.add('ri-subtract-line')
  }
  else {
    $body.style.maxHeight = '0px'
    $icon.classList.remove('ri-subtract-line')
    $icon.classList.add('ri-add-line')
  }
}

if ($filterAccordion) {
  $filterAccordion.addEventListener('click', e => {
    const $heading = e.target.closest('.js-filter-accordion-heading')
    if ($heading) {
      handleFilterAccordion($heading);
    }
  })
}

// CHANGE VIEW
const $changeProductsViewButtons = document.querySelector('.js-products-view-buttons')
const $shopCards = document.querySelector('.js-shop-cards')

/**
 * Sets products view to grid view.
 */
const setProductsGrid = () => {
  $shopCards.classList.remove('shop__cards--list')
}

/**
 * Sets products view to list view.
 */
const setProductsList = () => {
  $shopCards.classList.add('shop__cards--list')
}

/**
 * Changes products view depending on value storing in local storage.
 */
const changeProductsView = () => {
  if (!$shopCards) {return false}
  const view = localStorage.getItem("productsView") ?? 'grid'
  
  if (view === 'list') {
    setProductsList()
    document.querySelector('.js-products-view-list-button').classList.add('active')
  }
  else {
    setProductsGrid()
    document.querySelector('.js-products-view-grid-button').classList.add('active')
  }
}

/**
 * Sets products view parameter in local storage.
 */
const setStorageProductsView = (view) => {
  localStorage.setItem("productsView", view)
}

/**
 * Handles products view change after clicking buttons.
 * @param {HTMLElement} $button - Clicked change view button.
 */
const handleChangeProductsViewButtons = ($button) => {
  if ($button.closest('.js-products-view-grid-button')) {
    $button.closest('.js-products-view-grid-button').classList.add('active')
    document.querySelector('.js-products-view-list-button').classList.remove('active')
    setStorageProductsView('grid')
    setProductsGrid()
  }
  else if ($button.closest('.js-products-view-list-button')) {
    $button.closest('.js-products-view-list-button').classList.add('active')
    document.querySelector('.js-products-view-grid-button').classList.remove('active')
    setStorageProductsView('list')
    setProductsList()
  }

  changeProductsView()
}

if ($changeProductsViewButtons) {
  $changeProductsViewButtons.addEventListener('click', e => {
    handleChangeProductsViewButtons(e.target);
  })
}

if ($shopCards) {
  changeProductsView()
}

// PRODUCT GALLERY
const $productsImagesSlider = document.querySelector('.js-product-images-slider')

/**
 * Changes main image src when user clicks on slider image.
 * @param {string} src - Image src.
 * @param {alt} src - Image alt text.
 */
const changeMainImage = (src, alt) => {
  document.querySelector('.js-product-main-image').src = src
  document.querySelector('.js-product-main-image').alt = alt
}

if ($productsImagesSlider) {
    const newProductsCarousel = new Swiper('.js-product-images-slider', {
        effect: 'slide',
        speed: 1000,
        spaceBetween: 16,
        slidesPerView: 3,
        loopPreventsSliding: true,
        breakpoints: {
            1200: {
                slidesPerView: 4,
                direction: 'vertical',
                spaceBetween: 32,
            },
        },
        on: {
          click: function (e) {
            if (!e.clickedSlide) { return false }
            const $image = e.clickedSlide.querySelector('img')
            if ($image) {
              changeMainImage($image.src, $image.alt)
            }
          }
        },
    });
}

// RELATED PRODUCTS CAROUSEL

const $relatedProductsSection = document.querySelector('.js-related-products')

if ($relatedProductsSection) {
    const $leftArrow = $relatedProductsSection.querySelector('.js-arrow-left')
    const $rightArrow = $relatedProductsSection.querySelector('.js-arrow-right')

    const relatedProductsCarousel = new Swiper('.js-related-products-carousel', {
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
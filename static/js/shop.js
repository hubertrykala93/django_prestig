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
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

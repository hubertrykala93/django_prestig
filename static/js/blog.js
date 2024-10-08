// ADD COMMENT
const $articleCommentForm = document.querySelector('.js-article-comment-form')

/**
 * Sends add comment post data and handles messages.
 * @param {Object} formData - Add comment formdata object.
 */
const sendAddCommentRequest = (formData) => {
//    const slug = window.location.href.substring(window.location.href.lastIndexOf('/') + 1)
    const url = '/api/v1/comments/create-comment'

    fetch(url, {
        method:'POST',
        headers:{
         'X-CSRFToken':csrfToken,
        },
        body: formData
    }).then((response) => {
         return response.json()
    }).then((response) => {
        clearFormErrors($articleCommentForm)

        if (response.hasOwnProperty('success')) {
            showAlert(response.success, 'success')
            $articleCommentForm.reset()
        }
        else if (response.hasOwnProperty('error')) {
            showAlert(response.error, 'error')
            $articleCommentForm.reset()
        }
        else {
            showFormErrors($articleCommentForm, response)
        }
    })
}

/**
 * Validates add comment form data.
 * @returns {Object} Error messages with input names as a key.
 */
const validateCommentForm = (formData) => {
  const comment = formData.get('comment').trim()
  const result = {}

  if (comment === '') {
    result.comment = 'Comment is required.'
  }
  else if (comment.length < 5) {
    result.comment = 'The comment should consist of at least 5 characters long.'
  }
  else if (comment.length > 200) {
    result.comment = 'The comment cannot be longer than 200 characters.'
  }
  
  if (formData.has('email')) {
    const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    const email = formData.get('email').trim()
    if (email === '') {
      result.email = 'E-mail address is required.'
    }
    else if (!email.match(emailRegex)) {
        result.email = 'The e-mail address format is invalid.'
    }
    else if (email.length > 255) {
      result.email = 'The email cannot be longer than 255 characters.'
    }
  }

  if (formData.has('fullname')) {
    const onlyLettersRegex = /^[a-zżźćńółęąś]+$/i
    const name = formData.get('fullname').trim()
    if (name === '') {
      result.name = 'Fullname is required.'
    }
    else if (!name.match(onlyLettersRegex)) {
      result.name = 'The fullname should contain only letters.'
    }
    else if (name.length < 2) {
      result.name = 'The fullname should consist of at least 2 characters long.'
    }
    else if (name.length > 35) {
      result.name = 'The fullname cannot be longer than 35 characters.'
    }
  }

  return result
}

/**
 * Handles add comment form actions.
 */
const handleAddCommentForm = (e) => {
    const $form = e.target
    const formData = new FormData($form)
    const errors = validateCommentForm(formData)
    clearFormErrors($form)

    if (true) { // Object.keys(errors).length === 0
        sendAddCommentRequest(formData)
    }
    else {
       showFormErrors($form, errors)
    }
}

if ($articleCommentForm) {
    $articleCommentForm.addEventListener('submit', (e) => {
        e.preventDefault()
        handleAddCommentForm(e)
    })
}

// DELETE & EDIT COMMENT
const $articleCommentsParent = document.querySelector('.js-article-comments')

/**
 * Updates total number of comments to article.
 * @param {Number} number - New number of total comments.
 */
const updateCommentsTotal = (number) => {
  document.querySelector('.js-article-comments-total').innerText = number
}

/**
 * Deletes particular comment on blog article.
 * @param {Number} commentId - Id of comment to delete.
 */
const deleteComment = (commentId) => {
  const $comments = document.querySelectorAll('.js-article-comment')
  if (!$comments) { return }

  $comments.forEach($comment => {
    if ($comment.dataset.id == commentId) {
      $comment.remove()
    }
  })
}

/**
 * Updates particular comment content on blog article.
 * @param {Number} commentId - Id of comment to delete.
 * @param {String} content - Content of comment to update.
*/
const updateCommentContent = (commentId, content) => {
  const $comments = document.querySelectorAll('.js-article-comment')
  if (!$comments) { return }

  $comments.forEach($comment => {
    if ($comment.dataset.id == commentId) {
      $comment.querySelector('.js-article-comment-content').innerText = content
    }
  })
}

/**
 * Sends delete comment post data and handles messages and comment deletion.
 * @param {Object} formData - Delete comment formdata object.
 */
const sendCommentDeletionRequest = (formData) => {
  const url = '/api/v1/comments/delete-comment'

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
          deleteComment(response.id)
          updateCommentsTotal(response.total)
      }
      else if (response.hasOwnProperty('error')) {
          showAlert(response.error, 'error')
      }
  })
}

/**
 * Sends edit comment post data and handles messages and comment replace.
 * @param {Object} formData - Edit comment formdata object.
 */
const sendCommentEditRequest = (formData) => {
  const url = '/api/v1/comments/edit-comment'

  fetch(url, {
      method:'PATCH',
      headers:{
       'X-CSRFToken':csrfToken,
      },
      body: formData
  }).then((response) => {
       return response.json()
  }).then((response) => {
      console.log(response)
      if (response.hasOwnProperty('success')) {
          showAlert(response.success, 'success')
          updateCommentContent(response.id, response.content)
      }
      else if (response.hasOwnProperty('error')) {
          showAlert(response.error, 'error')
      }
  })
}

/**
 * Handles delete comment form actions.
 */
const handleCommentDeletion = ($form) => {
  const formData = new FormData($form)
  sendCommentDeletionRequest(formData)
}

/**
 * Handles edit comment form actions.
 */
const handleCommentEdit = ($form) => {
  const formData = new FormData($form)
  const errors = validateCommentForm(formData)
  clearFormErrors($form)

  if (true) { // Object.keys(errors).length === 0
      sendCommentEditRequest(formData)
  }
  else {
      showFormErrors($form, errors)
  }
}

if ($articleCommentsParent) {
  $articleCommentsParent.addEventListener('submit', e => {
    e.preventDefault()
    
    if (e.target.classList.contains('js-delete-article-comment-form')) {
      handleCommentDeletion(e.target)
    }
    else if (e.target.classList.contains('js-edit-article-comment-form')) {
      handleCommentEdit(e.target)
    }
  })
}

/**
 * Apends edit comment form with filled value.
 * @param {HTMLElement} $comment - Html comment element to edit.
 * @param {String} content - Content of comment.
 */
const createEditCommentForm = ($comment, content) => {
  if ($comment.querySelector('.js-edit-article-comment-form')) { return false }

  const id = $comment.dataset.id
  const formHTML = `
    <form class="article__comment-form article__comment-form--edit form js-edit-article-comment-form">
      <input type="hidden" name="id" value="${id}">
      <div class="form__row">
        <div class="form__field js-form-field">
            <div class="form__input-wrap">
                <textarea type="text" id="comment" name="comment" placeholder="Write your comment *">${content}</textarea>
            </div>
        </div>
      </div>

      <div class="form__row form__row--submit">
        <div class="form__field form__field--submit">
            <button class="btn btn--primary" type="submit">Edit comment</button>
        </div>
      </div>
    </form>
  `
  $comment.insertAdjacentHTML('beforeend', formHTML)
}

if ($articleCommentsParent) {
  $articleCommentsParent.addEventListener('click', e => {
    if (e.target.closest('.js-edit-article-comment-button')) {
      const $comment = e.target.closest('.js-article-comment')
      const content = $comment.querySelector('.js-article-comment-content').innerText
      createEditCommentForm($comment, content)
    }
  })
}
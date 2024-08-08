// ADD COMMENT
const $articleCommentForm = document.querySelector('.js-article-comment-form')

/**
 * Sends add comment post data and handles messages.
 * @param {Object} formData - Add comment formdata object.
 */
const sendAddCommentRequest = (formData) => {
    const url = 'add-comment'

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
  else if (comment.length < 20) {
    result.comment = 'The comment must be at least 20 characters long.'
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
  }

  if (formData.has('name')) {
    const name = formData.get('name').trim()
    if (name === '') {
      result.name = 'Name is required.'
    }
    else if (name.length < 8) {
        result.name = 'The name should consist of at least 8 characters.'
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

// DELETE COMMENT
const $articleCommentsParent = document.querySelector('.js-article-comments')

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
 * Sends delete comment post data and handles messages and comment deletion.
 * @param {Object} formData - Delete comment formdata object.
 */
const sendCommentDeletionRequest = (formData) => {
  const url = 'delete-comment'

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
          deleteComment(response.id)
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

if ($articleCommentsParent) {
  $articleCommentsParent.addEventListener('submit', e => {
    e.preventDefault()
    if (e.target.classList.contains('js-delete-article-comment-form')) {
      handleCommentDeletion(e.target)
    }
  })
}
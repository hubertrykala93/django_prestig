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
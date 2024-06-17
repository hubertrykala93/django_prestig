const $form = document.querySelector('form')

const sendData = (data) => {
    const url = 'send-file'
    fetch(url, {
       method:'POST',
       headers:{
//        'X-CSRFToken':csrftoken,
       },
       body: data
      })
      .then((response) => {
         return response.json()
      })
      .then((data) => {
          console.log('data:',data)
      });
    }

$form.addEventListener('submit', function (e) {
    e.preventDefault()

    let data = new FormData($form)
    console.log(data)
    sendData(data)
})
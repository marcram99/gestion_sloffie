console.log('script "facture.js" démmaré')

function closeModal(){
    $('#user_modal').modal('hide')
    window.location.reload()
}

function generate_pdf(id){
    event.preventDefault()
    var client_id = (id.id).split("_")[1]
    console.log('facure no: ' + client_id)
    fetch("/generate_pdf/" + client_id,{
        method:"POST", 
        headers: {"Content-Type" : "application/json"},
        mode: 'cors',
        body: JSON.stringify(client_id)}
    )
    .then(window.location.reload())
}



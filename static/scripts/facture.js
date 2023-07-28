console.log('script "facture.js" démmaré')

function closeModal(){
    $('#user_modal').modal('hide')
    window.location.reload()
}

function creeFacture(id){
    var client_id = (id.id).split("_")[1]
    console.log('new facture for: ' + client_id)
    $('#fact_modal').modal('show')
    //document.getElementById("modal_title").innerHTML = "Nouveau Client"
    document.getElementById("lockIcon").className = "d-none"
    document.getElementById("formAff").className = "d-none"
    document.getElementById("formEdit").className = "d-block"
    document.getElementById("createUser").className = "btn btn-success d-block"
    document.getElementById("dateAff").value = ""
    document.getElementById("produitAff").value = ""
    document.getElementById("prixAff").value = ""
    document.getElementById("remiseAff").value = ""
}

function validFactForm(){
    var date = document.getElementById("dateMod").value
    var produit = document.getElementById("produitMod").value
    var prix = document.getElementById("prixMod").value
    var remise = document.getElementById("remiseMod").value
    var mode = document.getElementById("modal_title").innerHTML
    var user_id = document.getElementById("user_id").innerHTML
    var reponse = {"date_facture": date, "produit": produit, "prix": prix, "remise": remise, "user_id": user_id}
    var fact_id = null
    if (mode == "Nouvelle facture"){
        sendUserData(reponse, "POST", user_id, fact_id)
    } if (mode == "Modification facture"){
        var fact_id = document.getElementById("fact_id").innerHTML
        sendUserData(reponse, "PUT", user_id, fact_id)
    } else {
        console.log('ELSE')
    }
    console.log('debug' + reponse)
    $('#user_modal').modal('hide')
    window.location.reload()
}

function sendUserData(data, method, user_id, fact_id){ 
    event.preventDefault()
    console.log('DEBUG_SendUserData: ' + method)
    console.log('date= ' + data.date_facture)
    console.log('produit= ' + data.produit)
    console.log('prix= ' + data.prix)
    console.log('remise= ' + data.remise)
    console.log('User_id = ' + data.user_id)
    console.log('Fact_id = ' + fact_id)
    if(fact_id){
        var url = '/factures/'+ user_id + '/' + fact_id
    }else{
        var url = '/factures/'+ user_id
    }
    console.log('url=' + method +':' + url)
    console.log('data=' + data)
    alert('Check Console')
    fetch(url,{
        method:method, 
        headers: {"Content-Type" : "application/json"},
        mode: 'cors',
        body: JSON.stringify(data)},
        function(result){
            console.log(result)
        }
    )
}


function generate_pdf(id){
    event.preventDefault()
    var fact_id = (id.id).split("_")[2]
    var client_id = (id.id).split("_")[1]
    console.log('facure no: ' + fact_id + ' pour client no: ' + client_id)
    fetch("/generate_pdf/" + client_id + "/" + fact_id,{
        method:"POST", 
        headers: {"Content-Type" : "application/json"},
        mode: 'cors',
        body: JSON.stringify()}
    )
    .then(window.location.reload())
}


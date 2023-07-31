console.log('script "facture.js" démmaré')

function closeModal(){
    $('#user_modal').modal('hide')
    window.location.reload()
}

function changeLock(){
    var icone = document.getElementById('lockIcon').className
    if(icone == "fa fa-unlock-alt mt-n4"){
        document.getElementById("modal_title").innerHTML = "Information Facture"
        document.getElementById('lockIcon').className = "fa fa-lock mt-n4"
        document.getElementById('formEdit').className = "d-none"
        document.getElementById('formAff').className = "d-block"
        document.getElementById('deleteFact').className = "btn btn-danger d-none"
        document.getElementById('validFact').className = "btn btn-success d-none"
    } else {
        document.getElementById("modal_title").innerHTML = "Modification facture"
        document.getElementById('lockIcon').className = "fa fa-unlock-alt mt-n4"
        document.getElementById('formEdit').className = "d-block"
        document.getElementById('formAff').className = "d-none"
        document.getElementById('deleteFact').className = "btn btn-danger d-block"
        document.getElementById('validFact').className = "btn btn-success d-block"
    }
}

function InformationFacture(id){
    event.preventDefault()
    var fact_id = (id.id).split("_")[1]
    console.log('you click on facture : ' + fact_id)
    url = "/facture/" + fact_id
    fetch(url,{
        method:"POST", 
        headers: {"Content-Type" : "application/json"},
        mode: 'cors',
        }
    )
    .then((resp) => resp.json())
    .then(function(data) {
    document.getElementById("produitAff").innerHTML = data.produit
    document.getElementById("produitMod").value = data.produit
    document.getElementById("dateAff").innerHTML = data.timestamp
    document.getElementById("dateMod").value = data.timestamp
    document.getElementById("prixAff").innerHTML = data.prix
    document.getElementById("prixMod").value = data.prix
    document.getElementById("remiseAff").innerHTML = data.remise
    document.getElementById("remiseMod").value = data.remise
    })
    $('#fact_modal').modal('show')
    document.getElementById("modal_title").innerHTML = "Information Facture"
   document.getElementById("factInfo_id").innerHTML = fact_id
}


function creeFacture(id){
    var client_id = (id.id).split("_")[1]
    console.log('new facture for: ' + client_id)
    $('#fact_modal').modal('show')
    //document.getElementById("modal_title").innerHTML = "Nouveau Client"
    document.getElementById("lockIcon").className = "d-none"
    document.getElementById("formAff").className = "d-none"
    document.getElementById("formEdit").className = "d-block"
    document.getElementById("createFact").className = "btn btn-success d-block"
    document.getElementById("dateAff").value = ""
    document.getElementById("produitAff").value = ""
    document.getElementById("prixAff").value = ""
    document.getElementById("remiseAff").value = ""
}

function effaceFacture(){
    event.preventDefault()
    var fact_id = document.getElementById("factInfo_id").innerHTML
    fetch('/facture/' + fact_id,{
        method: "DELETE",
    })
    closeModal()
}
    
function validFactForm(){
    var date = document.getElementById("dateMod").value
    var produit = document.getElementById("produitMod").value
    var prix = document.getElementById("prixMod").value
    var remise = document.getElementById("remiseMod").value
    var mode = document.getElementById("modal_title").innerHTML
    var user_id = document.getElementById("user_id").innerHTML
    var fact_id = document.getElementById("factInfo_id").innerHTML
    var data = {"timestamp": date, "produit": produit, "prix": prix, "remise": remise, "user_id": user_id}
    if (mode == "Nouvelle facture"){
        var url = '/factures/' + user_id
        var method = 'POST'
        sendUserData(url, method, data)
    } if (mode == "Modification facture"){
        var url = '/facture/' + fact_id
        var method = 'PUT'
        sendUserData(url, method, data)
    } else {
        console.log('ELSE')
    }
    $('#user_modal').modal('hide')
    window.location.reload()
}

function sendUserData(url, method, data){ 
    event.preventDefault()
    console.log('DEBUG_SendUserData:')
    console.log('date= ' + data.timestamp)
    console.log('produit= ' + data.produit)
    console.log('prix= ' + data.prix)
    console.log('remise= ' + data.remise)
    console.log('url=' + method +':' + url)
    console.log('data=' + data)
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


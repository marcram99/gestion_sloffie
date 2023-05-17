console.log('script "client.js" démmaré')

function closeModal(){
    $('#user_modal').modal('hide')
    window.location.reload()
}

function recup_client_info(id){
    url = "/client/" + id
    fetch(url,{
        method:"POST", 
        headers: {"Content-Type" : "application/json"},
        mode: 'cors',
        }
    )
    .then((resp) => resp.json())
    .then(function(data) {
        return data
    })
}

function creeClient(){
    event.preventDefault()
    $('#user_modal').modal('show')
    document.getElementById("modal_title").innerHTML = "Nouveau Client"
    document.getElementById("lockIcon").className = "d-none"
    document.getElementById("formAff").className = "d-none"
    document.getElementById("formEdit").className = "d-block"
    document.getElementById("createUser").className = "btn btn-success d-block"
    document.getElementById("clientNomAff").value = ""
    document.getElementById("clientPrenomAff").value = ""
    document.getElementById("clientTelAff").value = ""
    document.getElementById("clientMailAff").value = ""
}

function changeLock(){
    var icone = document.getElementById('lockIcon').className
    if(icone == "fa fa-unlock-alt mt-n4"){
        document.getElementById("modal_title").innerHTML = "Information Client"
        document.getElementById('lockIcon').className = "fa fa-lock mt-n4"
        document.getElementById('formEdit').className = "d-none"
        document.getElementById('formAff').className = "d-block"
        document.getElementById('deleteUser').className = "btn btn-danger d-none"
        document.getElementById('validUser').className = "btn btn-success d-none"
    } else {
        document.getElementById("modal_title").innerHTML = "Modification Client"
        document.getElementById('lockIcon').className = "fa fa-unlock-alt mt-n4"
        document.getElementById('formEdit').className = "d-block"
        document.getElementById('formAff').className = "d-none"
        document.getElementById('deleteUser').className = "btn btn-danger d-block"
        document.getElementById('validUser').className = "btn btn-success d-block"
    }
}

function nouvelleFacture(id){
    event.preventDefault()
    var client_id = (id.id).split("_")[1]
    fetch("/factures/" + client_id,{
        method:"POST", 
        headers: {"Content-Type" : "application/json"},
        mode: 'cors',
        body: JSON.stringify(client_id)}
    )
    .then(window.location.reload())
}

function infoFacture(id){
    event.preventDefault()
    var client_id = (id.id).split("_")[1]
    console.log('modal facture')
    $('#facture_modal').modal('show')
    document.getElementById("facture_id").innerHTML = client_id
    url = "/client/" + client_id
    fetch(url,{
        method:"POST", 
        headers: {"Content-Type" : "application/json"},
        mode: 'cors',
        }
    )
    .then((resp) => resp.json())
    .then(function(data) {
        document.getElementById("facture_id").innerHTML = data.prenom + " " + data.nom
        console.log('factures :')
        console.log(data.bill)
    })
    
}

function InformationClient(id){
    event.preventDefault()
    var client_id = (id.id).split("_")[1]
    console.log('you click on user : ' + client_id)
    var data = recup_client_info(client_id)
    console.log('infos from db')
    console.log('nom :' + data.nom)
    console.log('prenom :' + data.prenom)
    console.log('mail :' + data.mail)

    var nom = document.getElementById("nom_" + client_id).innerHTML
    var prenom = document.getElementById("prenom_" + client_id).innerHTML
    var adresse = document.getElementById("adresse_" + client_id).innerHTML
    var code = document.getElementById("code_" + client_id).innerHTML
    var mail = document.getElementById("mail_" + client_id).innerHTML
    var tel = document.getElementById("no_tel_" + client_id).innerHTML
    $('#user_modal').modal('show')
    document.getElementById("modal_title").innerHTML = "Information User"
    document.getElementById("userInfo_id").innerHTML = client_id
    document.getElementById("clientNomAff").innerHTML = nom
    document.getElementById("nomMod").value = nom
    document.getElementById("clientPrenomAff").innerHTML = prenom
    document.getElementById("prenomMod").value = prenom
    document.getElementById("clientAdresseAff").innerHTML = adresse
    document.getElementById("adresseMod").value = adresse
    document.getElementById("clientCodeAff").innerHTML = code
    document.getElementById("codeMod").value = code
    document.getElementById("clientMailAff").innerHTML = mail
    document.getElementById("mailMod").value = mail
    document.getElementById("clientTelAff").innerHTML = tel
    document.getElementById("telMod").value = tel
}

function effaceClient(){
    event.preventDefault()
    var client_id = document.getElementById("userInfo_id").innerHTML
    console.log(client_id)
    fetch('/client/' + client_id,{
        method: "DELETE",
    })
    closeModal()
}

function creeUser(id){
    event.preventDefault()
    $('#user_modal').modal('show')
    document.getElementById("modal_title").innerHTML = "New User"
    document.getElementById("lockIcon").className = "d-none"
    document.getElementById("formAff").className = "d-none"
    document.getElementById("formEdit").className = "d-block"
    document.getElementById("createUser").className = "btn btn-success d-block"
    document.getElementById("usernameMod").value = ""
    document.getElementById("emailMod").value = ""
    document.getElementById("roleMod").value = ""
    document.getElementById("passwordMod").value = ""
}

function validUserform(id){
    var nom = document.getElementById("nomMod").value
    var prenom = document.getElementById("prenomMod").value
    var adresse = document.getElementById("adresseMod").value
    var code = document.getElementById("codeMod").value
    var tel = document.getElementById("telMod").value
    var mail = document.getElementById("mailMod").value
    var mode = document.getElementById("modal_title").innerHTML
    var reponse = {"nom": nom, "prenom": prenom, "adresse": adresse, "code_postal": code, "no_tel": tel, "mail":mail}
    if (mode == "Nouveau Client"){
        sendUserData(reponse, "POST", null)
    } if (mode == "Modification Client"){
        var userID = document.getElementById("userInfo_id").innerHTML
        sendUserData(reponse, "PUT", userID)
    } else {
        console.log('ELSE')
    }
    console.log('debug' + reponse)
    $('#user_modal').modal('hide')
    window.location.reload()
}

function sendUserData(data, method, id){ 
    event.preventDefault()
    console.log('DEBUG JS: sendUserData' + method)
    console.log('nom= ' + data.nom)
    console.log('prenom= ' + data.prenom)
    console.log('adresse= ' + data.adresse)
    console.log('code= ' + data.code_postal)
    console.log('tel= ' + data.no_tel)
    console.log('mail= ' + data.mail)
    console.log('ID= ' + id)
    if(id){
        var url = '/client/'+ id
    }else{
        var url = '/client'
    }
    console.log('url=' + url)
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

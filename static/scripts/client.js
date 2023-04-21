console.log('script "client.js" démmaré')

function closeModal(){
    $('#user_modal').modal('hide')
    window.location.reload()
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
    var tel = document.getElementById("telMod").value
    var mail = document.getElementById("mailMod").value
    var mode = document.getElementById("modal_title").innerHTML
    var reponse = {"nom": nom, "prenom": prenom, "no_tel": tel, "mail":mail}
    if (mode == "Nouveau Client"){
        sendUserData(reponse, "POST", null)
    } 
    if (mode == "Modification User"){
        var userID = document.getElementById("userInfo_id").innerHTML
        sendUserData(reponse, "PUT", userID)
    }
    console.log('debug' + reponse)
    $('#user_modal').modal('hide')
    window.location.reload()
}

function sendUserData(data, method, id){ 
    event.preventDefault()
    console.log('DEBUG JS: sendUserData')
    console.log('nom= ' + data.nom)
    console.log('prenom= ' + data.prenom)
    console.log('tel= ' + data.no_tel)
    console.log('mail= ' + data.mail)
    console.log('ID= ' + id)
    if(id){
        var url = '/api/users/'+ id
    }else{
        var url = '/api/users'
    }
    console.log('url=' + url)
    alert('aaa')
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

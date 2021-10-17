/////////////////////////////////////////////////////////////////////////////////////////
// Sistema de mostrar e ocultar descrição de card ///////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////

let showDescBTNs = document.getElementsByClassName('btn-aid-show-desc')
let showInfosBTNs = document.getElementsByClassName('btn-aid-show-infos')

for(ind=0; ind < showDescBTNs.length; ind++) {
    showDescBTNs[ind].onclick = function() {
        let aidCard = this.parentElement.parentElement.parentElement
        aidCard.children[0].style.display = 'none'
        aidCard.children[1].style.display = 'initial'
    }
}
for(ind=0; ind < showInfosBTNs.length; ind++) {
    showInfosBTNs[ind].onclick = function() {
        let aidCard = this.parentElement.parentElement.parentElement
        aidCard.children[0].style.display = 'initial'
        aidCard.children[1].style.display = 'none'
    }
}

/////////////////////////////////////////////////////////////////////////////////////////

//Sistema de ocultar pagination com 1 pagina ////////////////////////////////////////////

if (document.getElementById('explore-pagination').children.length == 1) {
    document.getElementById('explore-pagination').style.display = 'none';
}
//////////////////////////////////////////////////////////////////////////////////////////

//Sistema de limitar o nome de author no primeiro nome ou em 10 caracteres 

let aidAuthors = document.getElementsByClassName('aid-profile-user')

for(i=0; i < aidAuthors.length; i++) {
    let authorName = aidAuthors[i].children[1].innerText
    let masked_name = ''
    for(n=0; n < authorName.length; n++) {
        if (masked_name == '' && authorName[n] == ' ') {
            undefined
        }
        else if (authorName[n] == ' ' || masked_name.length >= 11) {
            break
        }
        else {
            masked_name += authorName[n]
        }
    }
    aidAuthors[i].children[1].innerText = masked_name
}
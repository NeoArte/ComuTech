/////////////////////////////////////////////////////////////////////////////////////////
// Sistema de mostrar e ocultar descrição de card ///////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////
console.log('homeeeeeeeeeeeeeeeeeeeeeeeeeeee')
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

/// Sistema de limitar o número de caracteres do titulo de aids

let titlesSections = document.getElementsByClassName('aid-title-section')
for (i=0; i < titlesSections.length; i++) {
    let title = titlesSections[i].children[0].innerText
    let masked_title = ''
    if (title.length > 33) {
        let ind = 0
        for (n=0; n <= 33; n++) {
            masked_title += title[n]
        }
        masked_title += " [...]"
        titlesSections[i].children[0].innerText = masked_title
    }
    else if (title.length < 16) {
        titlesSections[i].children[0].style.fontSize = '36px'
    }
}

//////////////////////////////////////////////////////////////////////


// Script da avaliação por estrela ////////////////////////////

let stars5 = document.getElementsByClassName('review-star-5')
for (i=0; i < stars5.length; i++) {
stars5[i].onclick = function() {
    this.parentElement.parentElement.children[1].value = '5'
    this.parentElement.children[4].style.color = 'yellow'
    this.parentElement.children[3].style.color = 'yellow'
    this.parentElement.children[2].style.color = 'yellow'
    this.parentElement.children[1].style.color = 'yellow'
    this.parentElement.children[0].style.color = 'yellow'
}
}
let stars4 = document.getElementsByClassName('review-star-4')
for (i=0; i < stars4.length; i++) {
stars4[i].onclick = function() {
    this.parentElement.parentElement.children[1].value = '4'
    this.parentElement.children[4].style.color = 'yellow'
    this.parentElement.children[3].style.color = 'yellow'
    this.parentElement.children[2].style.color = 'yellow'
    this.parentElement.children[1].style.color = 'yellow'
    this.parentElement.children[0].removeAttribute('style')
}
}
let stars3 = document.getElementsByClassName('review-star-3')
for (i=0; i < stars3.length; i++) {
stars3[i].onclick = function() {
    this.parentElement.parentElement.children[1].value = '3'
    this.parentElement.children[4].style.color = 'yellow'
    this.parentElement.children[3].style.color = 'yellow'
    this.parentElement.children[2].style.color = 'yellow'
    this.parentElement.children[1].removeAttribute('style')
    this.parentElement.children[0].removeAttribute('style')
}
}
let stars2 = document.getElementsByClassName('review-star-2')
for (i=0; i < stars2.length; i++) {
stars2[i].onclick = function() {
    this.parentElement.parentElement.children[1].value = '2'
    this.parentElement.children[4].style.color = 'yellow'
    this.parentElement.children[3].style.color = 'yellow'
    this.parentElement.children[2].removeAttribute('style')
    this.parentElement.children[1].removeAttribute('style')
    this.parentElement.children[0].removeAttribute('style')
}
}
let stars1 = document.getElementsByClassName('review-star-1')
for (i=0; i < stars1.length; i++) {
stars1[i].onclick = function() {
    this.parentElement.parentElement.children[1].value = '1'
    this.parentElement.children[4].style.color = 'yellow'
    this.parentElement.children[3].removeAttribute('style')
    this.parentElement.children[2].removeAttribute('style')
    this.parentElement.children[1].removeAttribute('style')
    this.parentElement.children[0].removeAttribute('style')
}
}
/////////////////////////////////////////////////////////////////////////
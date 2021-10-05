
let showDescBTNs = document.getElementsByClassName('btn-aid-show-desc')
let showInfosBTNs = document.getElementsByClassName('btn-aid-show-infos')
console.log('yyyeeeeeeeeyyyyyy')

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
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

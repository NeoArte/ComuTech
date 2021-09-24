function socialAddButtons() {
    let socialAdd = document.getElementsByClassName("social-add")
    for (n=0; n < socialAdd.length; n+= 1) {
        socialAdd[n].onclick = function(){
            let inputID = "input-" + this.getAttribute("id")
            let input = document.getElementById(inputID)
            this.setAttribute("class", "social-remove")
            input.style.display = "flex";
            socialNetworks()
        }
    }
}
function socialRemoveButtons() {
    let socialRemove = document.getElementsByClassName("social-remove")
    for (n=0; n < socialRemove.length; n+= 1) {
        socialRemove[n].onclick = function(){
            let inputID = "input-" + this.getAttribute("id")
            let input = document.getElementById(inputID)
            this.setAttribute("class", "social-add")
            input.style.display = "none";
            socialNetworks()
        }
    }
}
function socialNetworks() {
    socialAddButtons()
    socialRemoveButtons()
    let facebook = document.getElementById("input-facebook")
    let whatsapp = document.getElementById("input-whatsapp")
    let instagram = document.getElementById("input-instagram")
    let twitter = document.getElementById("input-twitter")
}
socialNetworks()
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

//File load section

/*
document.getElementById('imagem').onchange = function(event) {
    let image = event.target.files[0] // Esta linha pega um determinado arquivo do input
    let rend = new FileReader() //Cria um objeto com uma classe com acesso a funções de leitura de arquivos
    rend.readAsDataURL(image)
    
    rend.onload = function(){ //Função que determinada um bloco de código ao carregar um arquivo
        let imageRender = document.getElementById('output') //Pega o objeto html em que a imagem vai ser renderizado
        imageRender.src = this.result //Atribui a rota de renderização criada pela função .readAsDataURL()
    }
}*/

//Register File Load 

function preRenderImage(route, content_display, file_display) {//Função que pré-renderiza a imagem de perfil do Usuario
    document.getElementById('img-render').src = route //Define a rota da imagem
    document.getElementById('img-render-content').style.display = content_display; //Display do bloco de conteúdo
    document.getElementById('file-img').style.display = file_display; //Display do bloco de conteúdo de inserir imagem
}

document.getElementById('_inputIMG').onchange = function(event) {
    let image = event.target.files[0] // Esta linha pega um determinado arquivo do input
    let render = new FileReader() //Cria um objeto com uma classe com acesso a funções de leitura de arquivos
    render.readAsDataURL(image)
    
    render.onload = function(){ //Função que renderiza a imagem ao carregar no objeto 'this' dessa função
        preRenderImage(this.result, 'flex', 'none')
    }
}

document.getElementById('register-img-remove').onclick = function() { //Função que remove a render e o conteudo da imagem que já tinha sido renderizada
    document.getElementById('_inputIMG').value = ''
    preRenderImage('', 'none', 'flex')
}

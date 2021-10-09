// Show social networks inputs section

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

//Register File Load 

if (document.getElementById('_inputIMG').getAttribute('class') == 'edit-img') {
    // Este if verifica se o inputIMG é da area de edit-account pela classe, asssim pré-renderizando
    // por padrão a imagem vinda do banco de dados.
    let route = document.getElementById('_inputIMG').parentElement.children[0].getAttribute('href')
    preRenderImage(route, 'flex', 'none')
}
document.getElementById('_inputIMG').onchange = function(event) {
    let image = this.files[0] // Esta linha pega um determinado arquivo do input
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
function preRenderImage(route, content_display, file_display) {//Função que pré-renderiza a imagem de perfil do Usuario
    document.getElementById('img-render').src = route //Define a rota da imagem
    document.getElementById('img-render-content').style.display = content_display; //Display do bloco de conteúdo
    document.getElementById('file-img').style.display = file_display; //Display do bloco de conteúdo de inserir imagem
}
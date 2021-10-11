// Show social networks inputs section//////////////////////////////////////////////////////////////////////////////////
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
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


//Register File Load ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

// Address auto-complete and CEP validation block script ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
document.getElementById('cep').onkeyup = function() {
    let cep = this.value.replace(/\D/g, '')
    getAddressFromCep(cep)
}
document.getElementById('cep').onfocusout = function() {
    let cep = this.value.replace(/\D/g, '')
    let cepValidation = /^[0-9]{8}$/
    
    console.log(cepValidation.test(cep))
    if (!(cepValidation.test(cep))) {
        this.parentElement.setAttribute('class','input-group wrong-form-control')
        this.setAttribute('input-valid','false')
    }
    else {
        this.parentElement.setAttribute('class','input-group')
        this.setAttribute('input-valid','true')
    }
}
function getAddressFromCep(cep) {
    let url = 'https://viacep.com.br/ws/' + cep + '/json/'
    let readAddressJSON = new XMLHttpRequest()
    let cepIsValid = /^[0-9]{8}$/
    if (cepIsValid.test(cep)) {
        readAddressJSON.open("GET", url, true)
        readAddressJSON.send()
        readAddressJSON.onerror = function() {
            console.log('error at Address auto-complete')
        }
        readAddressJSON.onload = function() {
            addressJSON = JSON.parse(readAddressJSON.responseText)
            
            let oldAddressJSON = document.getElementById('addressJSON')
            if (oldAddressJSON !== null) {
                oldAddressJSON.remove()
            }
            let saveAddressJSON = document.createElement('span')
            saveAddressJSON.setAttribute('id','addressJSON')
            document.getElementById('cep').appendChild(saveAddressJSON)
            document.getElementById('addressJSON').value = addressJSON

            document.getElementById('cep').onblur = function(){
                let state = document.getElementById('state')
                let city = document.getElementById('city')
                let neighborhood = document.getElementById('neighborhood')
                let street = document.getElementById('street')
                if ((addressJSON.uf !== null) && (addressJSON.uf !== undefined)) {
                    state.value = addressJSON.uf
                }
                if ((addressJSON.localidade !== null) && (addressJSON.localidade !== undefined)) {
                    city.value = addressJSON.localidade
                }
                if ((addressJSON.bairro !== null) && (addressJSON.bairro !== undefined)) {
                    neighborhood.value = addressJSON.bairro
                }
                if ((addressJSON.logradouro !== null) && (addressJSON.logradouro !== undefined)) {
                    street.value = addressJSON.logradouro
                }
            }
        }
    }
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Show/Hide password block script //////////////////////////////////////////////////////////////////////////////////
let passwordsIcons = document.getElementsByClassName('passwordIcon')
for (i=0; i < passwordsIcons.length; i++) {
    passwordsIcons[i].onclick = function() {
        let input = this.parentElement.parentElement.children[0]
        if (input.getAttribute('type') == 'text') {
            input.setAttribute('type','password')

            let path1 = document.createElementNS("http://www.w3.org/2000/svg",'path')
            let path2 = document.createElementNS("http://www.w3.org/2000/svg",'path')
            let defines1 = "m10.79 12.912-1.614-1.615a3.5 3.5 0 0 1-4.474-4.474l-2.06-2.06C.938 6.278 0 8 0 8s3 5.5 8 5.5a7.029 7.029 0 0 0 2.79-.588zM5.21 3.088A7.028 7.028 0 0 1 8 2.5c5 0 8 5.5 8 5.5s-.939 1.721-2.641 3.238l-2.062-2.062a3.5 3.5 0 0 0-4.474-4.474L5.21 3.089z"
            let defines2 = "M5.525 7.646a2.5 2.5 0 0 0 2.829 2.829l-2.83-2.829zm4.95.708-2.829-2.83a2.5 2.5 0 0 1 2.829 2.829zm3.171 6-12-12 .708-.708 12 12-.708.708z"
            path1.setAttribute('d', defines1)
            path2.setAttribute('d', defines2)
            this.innerHTML = ''
            this.appendChild(path1)
            this.appendChild(path2)
        }
        else if (input.getAttribute('type') == 'password') {
            input.setAttribute('type','text')

            let path1 = document.createElementNS("http://www.w3.org/2000/svg",'path')
            let path2 = document.createElementNS("http://www.w3.org/2000/svg",'path')
            let defines1 = "M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"
            let defines2 = "M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"
            path1.setAttribute('d', defines1)
            path2.setAttribute('d', defines2)
            this.innerHTML = ''
            this.appendChild(path1)
            this.appendChild(path2)
        }
    }
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// System that mask a input text how a input number /////////////////////////////////////////////////////////////////////////
let inputNumbers = document.getElementsByClassName('inputNumber')
for (i=0; i < inputNumbers.length; i++) {
    inputNumbers[i].oninput = function() {
        this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');
    }
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

document.getElementById('cpf').onblur = function() {
    validateInputCPF(this)
}
function isCpf(cpf) {
    exp = /\.|-/g;
    cpf = cpf.toString().replace(exp, "");
    var digitoDigitado = eval(cpf.charAt(9) + cpf.charAt(10));
    var soma1 = 0,
            soma2 = 0;
    var vlr = 11;
    for (i = 0; i < 9; i++) {
        soma1 += eval(cpf.charAt(i) * (vlr - 1));
        soma2 += eval(cpf.charAt(i) * vlr);
        vlr--;
    }
    soma1 = (((soma1 * 10) % 11) === 10 ? 0 : ((soma1 * 10) % 11));
    soma2 = (((soma2 + (2 * soma1)) * 10) % 11);
    if (cpf === "11111111111" || cpf === "22222222222" || cpf === "33333333333" || cpf === "44444444444" || cpf === "55555555555" || cpf === "66666666666" || cpf === "77777777777" || cpf === "88888888888" || cpf === "99999999999" || cpf === "00000000000") {
        var digitoGerado = null;
    } else {
        var digitoGerado = (soma1 * 10) + soma2;
    }
    if (digitoGerado !== digitoDigitado) {
        return false;
    }
    return true;
}
function validateInputCPF(element) {
    let valueCPF = element.value.replace(/\D/g, '')
    if (valueCPF.length == 11) {
        if (!(isCpf(valueCPF))) {
            element.parentElement.setAttribute('class','input-group wrong-form-control')
            element.setAttribute('input-valid','false')
        }
        else {
            element.parentElement.setAttribute('class','input-group')
            element.setAttribute('input-valid','true')
        }
    }
}

document.getElementById('password').onblur = function() {
    validatePassword(this)
}
function isAlphaNumeric(value = String ) {
    let hasLowLetter = false
    let hasHighLetter = false
    let hasNumber = false
    let result = false
    let numbers = '1234567890'
    let lowLetters = 'abcdefghijklmnopqrstuvwxyz'
    let highLetters = lowLetters.toUpperCase()

    for (i=0; i < value.length; i++) {
        if (numbers.indexOf(value[i]) != -1) {
            hasNumber = true
        }
        if (lowLetters.indexOf(value[i]) != -1) {
            hasLowLetter = true
        }
        if (highLetters.indexOf(value[i]) != -1) {
            hasHighLetter = true
        }
    }
    if (hasNumber && hasLowLetter && hasHighLetter) {
        result = true
    }
    return {
        'hasNumber':hasNumber, 
        'hasLowLetter':hasLowLetter, 
        'hasHighLetter':hasHighLetter,
        'result':result,
    }
}
function validatePassword(element) {
    let diversity = isAlphaNumeric(element.value).result
    if (element.value.length > 0) {    
        if (diversity && element.value.length > 7) {
            element.parentElement.setAttribute('class','input-group')
            element.setAttribute('input-valid','true')
        }
        else {
            element.parentElement.setAttribute('class','input-group wrong-form-control')
            element.setAttribute('input-valid','false')
        }
    }
}

document.getElementById('ConfirmPassword').onblur = function() {
    validateConfirmPassword(this)
}
function validateConfirmPassword(element) {
    let password = document.getElementById('password').value
    let confirmPassword = element.value
    let diversity = isAlphaNumeric(element.value).result

    if (element.value.length > 0) {    
        if (diversity && element.value.length > 7 && password == confirmPassword) {
            element.parentElement.setAttribute('class','input-group')
            element.setAttribute('input-valid','true')
        }
        else {
            element.parentElement.setAttribute('class','input-group wrong-form-control')
            element.setAttribute('input-valid','false')
        }
    }
}

document.getElementById('phone').onblur = function() {
    let phoneNumber = this.value.replace(/\D/g, '')
    let whatsapp = document.getElementById('whatsapp-input')
    if ((phoneNumber.length === 13) && (whatsapp.value == "")) {
        whatsapp.value = this.value
    }
}

function validateAddres() {
    let cep = document.getElementById('cep').value.replace(/\D/g, '')
    let address = getAddressFromCep(cep)
    let url = 'https://viacep.com.br/ws/' + cep + '/json/'
    let cepIsValid = /^[0-9]{8}$/
    let readAddressJSON = new XMLHttpRequest()
    
    if (cepIsValid.test(cep)) {
        readAddressJSON.open("GET", url, true)
        readAddressJSON.send()
        readAddressJSON.onerror = function() {
            console.log('error at Address verification')
        }
        readAddressJSON.onload = function() {
            addressJSON = JSON.parse(readAddressJSON.responseText)

            let state = document.getElementById('state')
                city = document.getElementById('city')
                neighborhood = document.getElementById('neighborhood')
                street = document.getElementById('street')

                stateIsValid = (state.value == addressJSON.uf)
                cityIsValid = (city.value == addressJSON.localidade)
                neighborhoodIsValid = (neighborhood.value == addressJSON.bairro)
                streetIsValid = (street.value == addressJSON.logradouro)

                if (stateIsValid) {
                    state.setAttribute('class','form-control')
                    state.setAttribute('input-valid','true')
                }
                else {
                    state.setAttribute('class','form-control wrong-form-control')
                    state.setAttribute('input-valid','false')
                }

                if (cityIsValid) {
                    city.setAttribute('class','form-control')
                    city.setAttribute('input-valid','true')
                }
                else {
                    city.setAttribute('class','form-control wrong-form-control')
                    city.setAttribute('input-valid','false')
                }

                if (neighborhoodIsValid) {
                    neighborhood.setAttribute('class','form-control')
                    neighborhood.setAttribute('input-valid','true')
                }
                else {
                    neighborhood.setAttribute('class','form-control wrong-form-control')
                    neighborhood.setAttribute('input-valid','false')
                }

                if (streetIsValid) {
                    street.setAttribute('class','form-control')
                    street.setAttribute('input-valid','true')
                }
                else {
                    street.setAttribute('class','form-control wrong-form-control')
                    street.setAttribute('input-valid','false')
                }
        }
    }
}

document.getElementById('state').onchange = document.getElementById('city').onchange = document.getElementById('neighborhood').onchange = document.getElementById('street').onchange = function() {  
    validateAddres()
}
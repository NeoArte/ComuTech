//Aid pre-render images system
document.getElementById('_plusAidIMG').onchange = function() {
    let aidMainInput  = document.getElementById('_aidInputIMG')
    let aidImagesInput = aidMainInput.files
    let total = this.files.length + aidImagesInput.length
    if ( total > 4 ) { //Esta verificação alerta o usuario de quantas imagens ele ainda possa adicionar caso exceda o limite
        let range = 4 - aidImagesInput.length
        if ( range > 1 ){
            alert(`Você só pode adicionar mais ${range} imagens`)
        }
        else {
            alert(`Você só pode adicionar mais ${range} imagem`)
        }
    }
    else {
        let protoFileList = new DataTransfer()
        for (ind=0; ind < aidImagesInput.length ; ind++) {
            protoFileList.items.add(aidImagesInput[ind])    
        }
        for (ind=0; ind < this.files.length ; ind++) {
            protoFileList.items.add(this.files[ind])
        }
        aidMainInput.files = protoFileList.files  
        processRenderImages(aidMainInput.files) // Usar aidMainInput.files pois ele pega o valor atual e aidImagesInput tem os files iniciais salvos
    }
}
document.getElementById('_aidInputIMG').onchange = function(event) {
    let images = event.target.files // Esta linha pega todas as imagens do input de imagens
    if ( images.length > 4) {
        this.value = ''
        alert("Você só pode selecionar até 4 arquivos")
    }
    else {
        processRenderImages(images)
    }
}
function processRenderImages(images) {
    if (images.length > 0) {
        document.getElementById('file-imgs').style.display = 'none'
        document.getElementById('carouselExampleIndicators').style.display = 'inherit'
        document.getElementById('aidCarouselIndicators').style.display = document.getElementById('aid-control-next').style.display = document.getElementById('aid-control-prev').style.display = 'flex'
        if (images.length == 1) {
            document.getElementById('aidCarouselIndicators').style.display = document.getElementById('aid-control-next').style.display = document.getElementById('aid-control-prev').style.display = 'none'
        }
    }
    else {
        document.getElementById('carouselExampleIndicators').style.display = 'none'
        document.getElementById('aid-imgs-section').style.display = 'block'
        document.getElementById('file-imgs').style.display = 'flex'
    }

    aidSlideImagesPreRender(images)
    aidImagesBoxes(images)
}
function aidSlideImagesPreRender(images) {
    let links = createAidSlideLinks(images.length)
    let innerItems = createAidSlideImages(images)
    document.getElementById('aidCarouselIndicators').innerHTML = ''
    document.getElementById('aidCarouselInner').innerHTML = ''

    for (ind = 0; ind < links.length; ind++) {
        document.getElementById('aidCarouselIndicators').appendChild(links[ind])
    }
    for (ind = 0; ind < innerItems.length; ind++) {
        document.getElementById('aidCarouselInner').appendChild(innerItems[ind])
    }
}
function aidImagesBoxes(images) {
    let boxes = []
    document.getElementById('aid-imgs-section').innerHTML = ''
    for (ind=0; ind<images.length; ind++) {
        let aidImageBox = createAid_ImageBox(images[ind])
        aidImageBox.setAttribute('id',`remove-${ind + 1}`)
        boxes.push(aidImageBox)
    }
    let numbersOfImages = boxes.length
    if (( boxes.length < 4) && ( boxes.length != 0 ) ) {
        boxes.push(createAid_AddImageBox())
    }
    while (( boxes.length < 4 ) && ( boxes.length != 0 )) {
        boxes.push(createAid_EmptyBox())
    }
    document.getElementById('aid-imgs-section').style.display = "flex"
    for (ind=0; ind < boxes.length; ind++) {
        document.getElementById('aid-imgs-section').appendChild(boxes[ind])
    }
    if ( numbersOfImages >= 1) {
        document.getElementById('remove-1').onclick = function() {removeAidImage(0)}
        if ( numbersOfImages >= 2) {
            document.getElementById('remove-2').onclick = function() {removeAidImage(1)}
            if ( numbersOfImages >= 3) {
                document.getElementById('remove-3').onclick = function() {removeAidImage(2)}
                if ( numbersOfImages >= 4) {
                    document.getElementById('remove-4').onclick = function() {removeAidImage(3)}
                }
            }
        }
    }
}
function eventsRemoveAidImage() {
    let boxRemoves = document.getElementsByClassName('aid-remove-img')
}
function removeAidImage(id) {
    console.log('yaaaaaaaaaay', id)

    let aidMainInput  = document.getElementById('_aidInputIMG')
    let aidImagesInput = aidMainInput.files
    let protoFileList = new DataTransfer()
    for (ind=0; ind < aidImagesInput.length ; ind++) {
        if (!( ind == id)) {
            protoFileList.items.add(aidImagesInput[ind])    
        }
    }
    aidMainInput.files = protoFileList.files  
    processRenderImages(aidMainInput.files) // Usar aidMainInput.files pois ele pega o valor atual e aidImagesInput tem os files iniciais salvos
}
function createAidSlideImages(images) {
    let aidSlideItems = []
    for( ind=0; ind < images.length; ind++) {
        let img = images[ind]
        let carouselItem = document.createElement('div')
        let imgCarouselItem = document.createElement('img')
        let render = new FileReader()
        
        if (ind === 0) {
            carouselItem.setAttribute('class','carousel-item aid-image active')
        }
        else {
            carouselItem.setAttribute('class','carousel-item aid-image')
        }
        render.readAsDataURL(img)
        render.onloadend = function() {
            imgCarouselItem.src = this.result
        }
        carouselItem.appendChild(imgCarouselItem)
        aidSlideItems.push(carouselItem)
        }
    return aidSlideItems
}
function createAidSlideLinks(len) {
    let aidSlideLinks = []
    for( round=0; round < len; round++) {
        let aidImageLink = document.createElement('li')
        aidImageLink.setAttribute('data-target','#carouselExampleIndicators')
        aidImageLink.setAttribute('data-slide-to', `${round}`)
        if (round === 0) {
            aidImageLink.setAttribute('class', 'active')
        }
        aidSlideLinks.push(aidImageLink)
    }
    return aidSlideLinks
}
function createAid_ImageBox(image) {
    let box = document.createElement('label')
    let img = document.createElement('img')
    let svgMinus = document.createElementNS("http://www.w3.org/2000/svg", "svg")
    let path = document.createElementNS("http://www.w3.org/2000/svg", "path")
    let definesMinus = 'M0 8a1 1 0 0 1 1-1h14a1 1 0 1 1 0 2H1a1 1 0 0 1-1-1z'
    let render = new FileReader()

    box.setAttribute('class','aid-img-box aid-remove-img')
    svgMinus.setAttribute('class','minus')
    svgMinus.setAttribute('fill','currentColor')
    svgMinus.setAttribute('viewBox','0 0 16 16')
    render.readAsDataURL(image)
    render.onloadend = function() {
        img.src = this.result
    }
    
    path.setAttribute('d', definesMinus)
    svgMinus.appendChild(path)

    box.appendChild(img)
    box.appendChild(svgMinus)

    return box
}
function createAid_AddImageBox() {
    let AddImageBox = document.createElement('label')
    let svgAddImageBox = document.createElementNS("http://www.w3.org/2000/svg", "svg");

    AddImageBox.setAttribute('class','aid-img-box')
    AddImageBox.setAttribute('id','aid-img-plus')
    AddImageBox.setAttribute('for','_plusAidIMG')

    svgAddImageBox.setAttribute('class','plus')
    svgAddImageBox.setAttribute('fill','currentColor')
    svgAddImageBox.setAttribute('viewBox','0 0 16 16')

    let path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    let definesSvgAddImage = "M8 0a1 1 0 0 1 1 1v6h6a1 1 0 1 1 0 2H9v6a1 1 0 1 1-2 0V9H1a1 1 0 0 1 0-2h6V1a1 1 0 0 1 1-1z"
    
    path.setAttribute('d', definesSvgAddImage)
    svgAddImageBox.appendChild(path)
    AddImageBox.appendChild(svgAddImageBox)

    return AddImageBox
}
function createAid_EmptyBox() {
    let box = document.createElement('div')
    box.setAttribute('class','aid-img-empty-box')
    return box
}
//Events to box remove 

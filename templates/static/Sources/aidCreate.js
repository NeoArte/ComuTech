//Aid pre-render images system

document.getElementById('_aidInputIMG').onchange = function(event) {
    let images = event.target.files // Esta linha pega todas as imagens do input de imagens
    if ( images.length > 4) {
        this.value = ''
        alert("Você só pode selecionar até 4 arquivos")
    }

    aidSlideImagesPreRender(images)
    aidImagesBoxes(images)
}
function aidSlideImagesPreRender(images) {
    let links = createAidSlideLinks(images.length)
    let innerItems = createAidSlideImages(images)
    
    document.getElementById('file-imgs').style.display = 'none'
    document.getElementById('carouselExampleIndicators').style.display = 'inherit'
    for (ind = 0; ind < links.length; ind++) {
        document.getElementById('aidCarouselIndicators').appendChild(links[ind])
    }
    for (ind = 0; ind < innerItems.length; ind++) {
        document.getElementById('aidCarouselInner').appendChild(innerItems[ind])
    }
}
function aidImagesBoxes(images) {
    let boxes = []
    for (ind=0; ind<images.length; ind++) {
        boxes.push(createAid_ImageBox(images[ind]))
    }
    if ( boxes.length < 4) {
        boxes.push(createAid_AddImageBox())
    }
    if ( boxes.length < 4 ) {
        let diference = 4 - boxes.length
        for (ind=0; ind < diference; ind++) {
            boxes.push(createAid_EmptyBox())
        }
    }
    document.getElementById('aid-imgs-section').style.display = "flex"
    for (ind=0; ind < boxes.length; ind++) {
        document.getElementById('aid-imgs-section').appendChild(boxes[ind])
    }
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
    let box = document.createElement('div')
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
    let AddImageBox = document.createElement('div')
    let svgAddImageBox = document.createElementNS("http://www.w3.org/2000/svg", "svg");

    AddImageBox.setAttribute('class','aid-img-box')
    AddImageBox.setAttribute('id','aid-img-plus')

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
}
async function getGato() {
    let resultado = await fetch("https://api.thecatapi.com/v1/images/search")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_gato(dados)
    }

}

function render_gato(dados) {
    let urlImg = dados[0].url
    const imgGato = document.getElementById('img-gato')
    const iconGato = document.getElementById('icon-gato')


    iconGato.style.display = "none"
    imgGato.style.display = "block"
    imgGato.src = urlImg
}
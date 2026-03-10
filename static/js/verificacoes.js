// let nome = prompt("Como você chama?")
//
// if (nome == null) {
//     alert("Recarregue a pagina")
// } else {
//
//     let correto = confirm("Você se chama " + nome + "mesmo?")
//
//     if (correto) {
//         alert(` ${nome} Bem vindo ao site de cursos`)
//     } else {
//         alert("Recarregue a página")
//     }
// }

function limpaInputsLogin() {
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')

    inputEmail.value = ''
    inputSenha.value = ''
}

function limpaInputsModal() {
    const inputEmail2 = document.getElementById('input-email2')
    const inputSenha2 = document.getElementById('input-senha2')
    const inputNome = document.getElementById('input-nome')
    const inputData = document.getElementById('input-data')
    const inputCpf = document.getElementById('input-cpf')
    const inputCargo = document.getElementById('input-cargo')
    const inputSalario = document.getElementById('input-salario')

    inputEmail2.value = ''
    inputSenha2.value = ''
    inputNome.value = ''
    inputData.value = ''
    inputSalario.value = ''
    inputCpf.value = ''
    inputCargo.value = ''
}


document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById('form-login')

    formLogin.addEventListener("submit", function (event) {
        const inputEmail = document.getElementById('input-email')
        const inputSenha = document.getElementById('input-senha')
        let temErro = false
        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro) {
            event.preventDefault()
            alert("Preencha todos os erros")
        }
    })

    const formModal = document.getElementById('form-modal')

    formModal.addEventListener("submit", function (event) {
        const inputNome = document.getElementById('input-nome')
        const inputData = document.getElementById('input-data')
        const inputCpf = document.getElementById('input-cpf')
        const inputEmail2 = document.getElementById('input-email2')
        const inputSenha2 = document.getElementById('input-senha2')
        const inputCargo = document.getElementById('input-cargo')
        const inputSalario = document.getElementById('input-salario')

        let temErro = false
        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome.classList.remove('is-invalid')
        }

        if (inputData.value === '') {
            inputData.classList.add('is-invalid')
            temErro = true
        } else {
            inputData.classList.remove('is-invalid')
        }

        if (inputCpf.value === '') {
            inputCpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf.classList.remove('is-invalid')
        }

        if (inputEmail2.value === '') {
            inputEmail2.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail2.classList.remove('is-invalid')
        }

        if (inputSenha2.value === '') {
            inputSenha2.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha2.classList.remove('is-invalid')
        }

        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')
        }

        if (inputSalario.value === '') {
            inputSalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario.classList.remove('is-invalid')
        }


        if (temErro) {
            event.preventDefault()
            alert("Preencha todos os erros")
        }

    })
})
// // Validation 
import { validateFields, inputFields } from "./validate.js" 

let investimentos = []

const clearFields = () => {
    const fields = document.querySelectorAll('.modal-field')
    fields.forEach(fields => fields.value = "")
}

const alertError = (error) => {
    switch (error) {
        case 'code':
            alert("Código inválido!")
            break
       case 'data':
            alert('Data inválida! Padrão - DD/MM/AAAA')
            break
        case 'amount':
            alert("Quantidade inválida")
            break
        case 'unitaryValue':
            alert('Valor unitário inválido.')
            break
        case 'brokerageFee':
            alert("Taxa corretária inválida.")
            break
        default:
            alert("Todos estão inválidos.")
            break
    }
}

function openModal() {
    document.getElementById('modal').classList.add('active')
}

function closeModal() {
    document.getElementById('modal').classList.remove('active')
    clearFields()
}

function calcularValorFinal(option, valorOp, taxa, imposto) {
    if (option  === "V") {
        return +valorOp - +taxa - +imposto
    } else if (option === "C") {
        return +valorOp + +taxa + +imposto
    }
    return "C"
}

function calcularMedia(code, compraOuVenda, quantidade, valorFinal) {
    const cod = investimentos.filter(i => i.codigo === code)
    const vendas = cod.filter(i => i.compraOuVenda === "V")
    const compras = cod.filter(i => i.compraOuVenda === "C")
 
    if (cod.length === 0) {
        return +valorFinal / +quantidade
    } else if(compraOuVenda === "V") {
        return +cod[cod.length - 1].media
    } else {
        const somaVendas = vendas.reduce((cont, el) => cont + +el.quantidade, 0)
        const soma = compras.reduce((cont, el) => cont + +el.quantidade, 0) - somaVendas

        return (soma * +cod[cod.length - 1].media + +valorFinal) / (soma + +quantidade)
    }

}

async function saveInvestimentos(ev) {
    ev.preventDefault()
    try {
        validateFields()
        const codigo = document.querySelector('#code').value
        const data = moment(document.querySelector('#date').value).format('DD/MM/YYYY')
        const quantidade = document.querySelector('#amount').value
        const valorUnitario = document.querySelector('#unitary-value').value
        const compraOuVenda = document.querySelector('#buy-sell').value
        const taxaCorretaria = document.querySelector('#brokerage-fee').value
        const valorOp = (quantidade * (valorUnitario).replace(',', '.')).toFixed(2)
        const imposto = (valorOp * 0.0003).toFixed(2)
        const valorFinal = (calcularValorFinal(compraOuVenda, valorOp, (taxaCorretaria).replace(',', '.'), imposto)).toFixed(2)
    
        const response = await fetch(' http://localhost:3000/investimentos', {
            method: 'POST',
            body: JSON.stringify({codigo, data, quantidade, valorUnitario, compraOuVenda, taxaCorretaria, valorOp, imposto, valorFinal}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
    
        const investimento = await response.json()
        investimentos.push(investimento)
        console.log(investimentos)
        closeModal()
        

    } catch (err) {
        inputFields[err.input].classList.add('error')
        alertError(err.input)
    }
}

async function setup() {
    const results = await fetchInvestimento()
    console.log('Deu certo!!')
    investimentos.push(...results)
    console.log(investimentos)
    
}

async function fetchInvestimento() {
    return await fetch('http://localhost:3000/investimentos').then(res => res.json()).catch(error => console.log(error))
}

document.addEventListener('DOMContentLoaded', setup)
document.querySelector('form').addEventListener('submit', saveInvestimentos)
document.getElementById('cadastrarCliente').addEventListener('click', openModal)
document.querySelector('.modal-close').addEventListener('click', closeModal)






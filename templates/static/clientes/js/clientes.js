function add_tratamento(){

    container = document.getElementById('form-tratamento')

    html = "<br> <div class='row'> <div class='col-md'> <input type='text' placeholder='Tratamento' class='form-control' name='tratamento'> </div> <div class='col-md'> <input type='text' placeholder='Triagem' class='form-control' name='triagem'></div><div class 'col-md'> <input type='number' placeholder='Idade' class='form-control' name='idade'> </div> </div><"

    container.innerHTML += html

}
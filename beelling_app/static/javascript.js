(function(win,doc){
    'use strict';

    // Confirm if user wants to delete data
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Do you want to delete this bill?')){
                    return true;
                } else {
                    event.preventDefault();
                }
            });
        }
    }

    //Form ajax
    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form');
        function sendForm(event){
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;

            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN', token)
            ajax.onreadystatechange = function(){
                if(ajax.status === 200 && ajax.readyState === 4){
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Bill saved!';
                    if ( result.classList.contains('alert-danger')){
                        result.classList.remove('alert-danger')
                        result.classList.add('alert-success');
                    } else {
                        result.classList.add('alert-success');
                    }
                } else {
                    result.innerHTML = 'Invalid request! Check if the fields are valid.';
                    if ( result.classList.contains('alert-success')){
                        result.classList.remove('alert-success')
                        result.classList.add('alert-danger');
                    } else {
                        result.classList.add('alert-danger');
                    }
                }
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit', sendForm, false);
    }
})(window, document);
//console.log('register workring')

const usernameField = document.querySelector(id = "#UsernameField");
const feedbackArea = document.querySelector(".invalid-feedback");
const emailField = document.querySelector(id = '#emailField');
const emailfeedbackArea = document.querySelector('.emailfeedbackArea');
const usernameSuccessOutput  = document.querySelector('.usernameSuccessOutput');
const showPasswordToggle =document.querySelector('.showPasswordToggle');
const passwordField = document.querySelector(id = '#passwordField');
const submitBtn = document.querySelector('.submit-btn');

const handleToggleInput=(e) =>{
    if(showPasswordToggle.textContent ==='SHOW'){
        showPasswordToggle.textContent = "HIDE";

        passwordField.setAttribute("type", "text")
    }else {
        showPasswordToggle.textContent = 'SHOW';
        passwordField.setAttribute("type", "password")

    }
};

showPasswordToggle.addEventListener("click" , handleToggleInput );



emailField.addEventListener("keyup" , (e) =>{
    const emailVal = e.target.value;
    emailField.classList.remove("is-invalid");
    emailfeedbackArea.style.display = "none";

    if(emailVal.length > 0){
        console.log("8888" , 8888);
 
    //  console.log('');
     fetch('/authentication/validate-email', {
         body:JSON.stringify( {email : emailVal}),
         method:'POST',
     
     })
     .then((res) => res.json())
     .then((data) => {
         console.log("data", data);
       

         if(data.email_error){
             console.log('ok');
             submitBtn.disabled = true ;
             emailField.classList.add("is-invalid");
             emailfeedbackArea.style.display = "block";
             emailfeedbackArea.innerHTML=`<p my-3 >${data.email_error}</p>`;
             
            }
            else{
                submitBtn.removeAttribute('disabled')
            }
     });
     

    }
})



usernameField.addEventListener("keyup" , (e) =>{
       console.log("7777" , 7777);
       const usernameVal = e.target.value;
       usernameSuccessOutput.style.display = "block";

       usernameSuccessOutput.textContent = `Checking ${usernameVal}`;
       //console.log("usernameVal" , usernameVal);
       usernameField.classList.remove("is-invalid");
       feedbackArea.style.display = "none";


       if(usernameVal.length > 0){

      //  console.log('');
        fetch('/authentication/validate-username', {
            body:JSON.stringify( {username : usernameVal}),
            method:'POST',
        
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            usernameSuccessOutput.style.display = "none";
            
           
            if(data.username_error){
                console.log('lund');
                usernameField.classList.add("is-invalid");
                feedbackArea.style.display = "block";
                feedbackArea.innerHTML=`<p my-3 >${data.username_error}</p>`;
                submitBtn.disabled = true ;
                
            }
            else{
                submitBtn.removeAttribute('disabled')
            }
        });
        
 
       }
     


});
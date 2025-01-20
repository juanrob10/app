/*=============== SHOW MENU ===============*/
// Load the full build.

const showMenu = (toggleId, navId) =>{
  
  const toggle = document.getElementById(toggleId),
  nav = document.getElementById(navId)

  
  // Validate  that variables exist
  if(toggle && nav){
      toggle.addEventListener('click', ()=>{
         
          nav.classList.toggle("max-md:hidden")
         
         
      })
  }
}
showMenu('nav-toggle','nav-menu')





/*=============== CHANGE BACKGROUND HEADER ===============*/
function scrollHeader(){
   
    
  const nav = document.getElementById('nav')
  // When the scroll is greater than 80 viewport height, add the scroll-header class to the header tag
  if(this.scrollY >= 100) nav.classList.add('scroll-header'); else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

  

  window.onload = function() {
    const message = document.getElementById('message');
    if(message) {

      setTimeout(function() {

        message.classList.add('hidden');
      }, 3000); // Espera 2 segundos antes de ocultar el mensaje
   

    }
   
  };



  
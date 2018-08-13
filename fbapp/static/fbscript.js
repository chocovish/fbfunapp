window.fbAsyncInit = function() {
    FB.init({
      appId      : '845952675793239',
      cookie     : true,
      xfbml      : true,
      version    : 'v3.1'
    });
      
    //FB.AppEvents.logPageView(); 
      
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "https://connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));


   function loginbtnfunc(){
    FB.login(function(response){
        console.log(response)
        if(response.status=="connected"){
            console.log("connected..doing process..")
            let token = response.authResponse.accessToken
            let id = response.authResponse.userID
            let url = "info/?token="+token+"&id="+id
            window.location = url
        }
    },
{
    scope: "email",
})
}

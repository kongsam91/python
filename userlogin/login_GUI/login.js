

/*
button_login.addEventListener("click",()=>
    {
        sucess_login.textContent    =  eel.login(user,passwd);
        console.log(eel.login(user,passwd));
    }
)
*/
async function btn_click(){ 
    const userElement = document.getElementById("user_login_input");
    const user  =   userElement.value;
    const passwdElement = document.getElementById("passwd_login_input");
    const passwd    =   passwdElement.value;
    const sucess_login = document.getElementById("sucess_login");   
    //呼叫的方式，就是加上eel.加上剛剛被expose PY function的名稱然後多加()輸入參數，最後加()取值
    reply = await eel.login(user,passwd)();
    
    //最後將返回的值設定在HTML上的<p>內
    document.querySelector('p').textContent = reply;
    console.log(user,passwd);
    //alert("你的姓名是 " + user + "\n密碼是 " + passwd);
}

import axios from "axios";
import React from "react";
import { useState } from "react/cjs/react.development";
import { apiAddr, checkAuth, getDefaultHeaders } from "../services/requests";

export default function Authorization() {

  const [logined, setLogined] = useState(checkAuth());

  async function login () {
    const loginForm = document.querySelector("[id='login-form']");
    const loginInput = loginForm.querySelector("[name='login-input']");
    const passwordInput = loginForm.querySelector("[name='password-input']");
    

    let data = {
      username: loginInput.value,
      password: passwordInput.value
    }
    console.log(data);

    try {
      const response = await axios.post(apiAddr + "core/auth/login/", data, {headers: getDefaultHeaders()})
      localStorage.setItem("token", response.data.token);
      window.location.pathname = "/surveys"
    }
    catch (err){
      alert(err.response.data);
    }
  }

  return(
    <div id="range1">

      <div className="outer">
        <div className="middle">
          <div className="inner">

              <div className="login-wr">
                <h2>Авторизация</h2>
                
                <div className="form">
                  <form id="login-form">
                    <input type="text" placeholder="Логин" name="login-input" />
                    <input type="password" placeholder="Пароль" name="password-input" />
                  </form>
                  <button id="login" onClick={login}> Войти </button>
                  <a href={window.location.origin + "/registration"}> <p> У вас нет аккаунта? Регистрация </p></a>
                </div>
              </div>

          </div>
        </div>
      </div>

    </div>
  )
}
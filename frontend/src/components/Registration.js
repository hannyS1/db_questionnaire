import axios from "axios";
import React from "react";
import { apiAddr, getDefaultHeaders } from "../services/requests";

export default function Registration() {

  async function register() {
    const authForm = document.querySelector("[id='auth-form']");
    const loginInput = authForm.querySelector("[name='login-input']");
    const passwordInput = authForm.querySelector("[name='password-input']");
    const passwordRepeatInput = authForm.querySelector("[name='password-repeat-input']");

    if (passwordInput.value != passwordRepeatInput.value){
      alert("Пароли не совпадают");
      throw "Пароли не совпадают"
    }

    let data = {
      username: loginInput.value,
      password: passwordInput.value,
    }

    try{
      const response = await axios.post(apiAddr + "core/auth/register/", data, getDefaultHeaders());
      localStorage.setItem("token", response.data.token);
      window.location.pathname = "/surveys"
    }
    catch (err){
      alert(err.response.data)
    }

  }

  return(
    <div id="range1">

      <div className="outer">
        <div className="middle">
          <div className="inner">

              <div className="login-wr">
                <h2>Регистрация</h2>
                
                <div className="form">
                  <form id="auth-form">
                    <input type="text" placeholder="Логин" name="login-input" />
                    <input type="password" placeholder="Пароль" name="password-input" />
                    <input type="password" placeholder="Повторите пароль" name="password-repeat-input" />
                  </form>
                  <button id="register" onClick={register} > Зарегистрироваться </button>
                  <a href={window.location.origin + "/auth"}> <p> У вас есть аккаунт? Войти </p></a>
                </div>
              </div>

          </div>
        </div>
      </div>

    </div>
  )
}
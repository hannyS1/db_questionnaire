import axios from "axios";

const backendAddr = "http://localhost:8000"
const apiAddr = backendAddr + "/api/"

function getDefaultHeaders() {
  let headers = new Object();
  let token = localStorage.getItem("token");

  if (token != null){
    headers.Authorization = 'Token ' + token;
  }

  return headers;
}

function checkAuth() {
  try{
    if (localStorage.getItem("token").length) {
      return true;
    }
    return false;
  }
  catch{
    return false;
  }
}

function logout() {
  if (localStorage.getItem("token").length) {
    localStorage.removeItem("token");
  }
}

async function getUserInfo() {
  const response = await axios.get(apiAddr + "core/auth/user-info/", {headers: getDefaultHeaders()})
  if (response.status == 200) {
    return response.data
  }
  return null;
}

export {apiAddr, getDefaultHeaders, backendAddr, checkAuth, getUserInfo, logout}
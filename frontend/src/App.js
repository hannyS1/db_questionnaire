import './App.css';
import SurveyList from './components/SurveyList';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SurveyDetail from './components/SurveyDetai';
import Authorization from './components/Authorization';
import { checkAuth, getUserInfo, logout } from './services/requests';
import { useState } from 'react/cjs/react.development';
import { useEffect } from 'react';
import Registration from './components/Registration';
import AnswerList from './components/AnswerList';
import AnswerDetail from './components/AnswerDetail';


function App() {

  const [loading, setLoading] = useState(true);
  const [userInfo, setUserInfo] = useState(null);

  async function setUser() {
    if (checkAuth()) {
      const userData = await getUserInfo();
      console.log(userData)
      if (userData != null) {
        setUserInfo(userData);
      }
    }
    setLoading(false);
  }

  function renderNav() {
    if (loading){
      return ""
    }
    else if (userInfo == null){
      return <nav><a href="/auth">Вход</a></nav>
    }
    else {
      return(
        <nav>
          <a href="/answers">Мои ответы</a>
          <a href="/auth" id="logout" onClick={logout}>Выход</a>
        </nav>
      )
    }
    
  }
    

  useEffect(() => {
    setUser();
  }, [])

  return (
    <div>

      <Router>
        
        <header>
          <h1><a href="/surveys">Опросник</a></h1>
          {renderNav()}
        </header>

        <Routes>
          <Route path="/surveys" element={<SurveyList />} />
          <Route path="/surveys/:id" element={<SurveyDetail />} />
          <Route path="/auth" element={<Authorization />} />
          <Route path="/registration" element={<Registration />} />
          <Route path="/answers" element={<AnswerList />} />
          <Route path="/answers/:id" element={<AnswerDetail />} />
        </Routes>

      </Router>
      
      
    </div>
  );
}


export default App;

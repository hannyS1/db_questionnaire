import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import { getDefaultHeaders, apiAddr } from '../services/requests';
import { useEffect } from 'react';
import { useParams } from 'react-router';
import QuestionList from './QustionList';
import Loader from '../services/Loader';



export default function SurveyDetail(props) {

  const [survey, setSurvey] = useState("");
  const [loading, setLoading] = useState(true);

  const id = useParams().id;

  let headers = getDefaultHeaders();

  const getSurveyById = async function(id) {
    const response = await axios.get(apiAddr + 'questionnaire/survey/' + id + "/", {headers: headers})
      .catch((error) => {
        alert(error.response.data);
      })
      .then((response) => {
        if(response.status === 200){
          setSurvey(response.data);       
          setLoading(false);   
        }
        else{
          alert(response.data);
        }
      })
  }

  function getAnswerData() {
    let data = {}
    data.survey_id = survey.id;

    let questionsAnswers = [];
    let questions = document.getElementById("question-list").getElementsByTagName("li");
    console.log(questions);

    Array.from(questions).forEach(question => {

      let choices = question.querySelectorAll(".choice-item input");
      console.log(choices);

      Array.from(choices).forEach(choice => {
        if (choice.checked == true) {
          questionsAnswers.push({question_id: question.getAttribute("question-id"), choice_id: choice.getAttribute("choice-id")});
        }
      })
    });

    data.questions_answers = questionsAnswers;
    return data;
  }

  async function sendSurveyAnswer() {
    const response = await axios.post(
      apiAddr + "questionnaire/answer-survey/",
      getAnswerData(),
      {headers: headers}
    )
    .then((response) => {
      console.log(response);
      window.location.pathname = '/answers'
    })
  }

  useEffect(() => {
    getSurveyById(id)
  }, [])

  return (
    <div className="survey" survey-id={survey.id}>
      {
        loading ? <Loader /> : 
          <div>
            <h1>Опрос {survey.name}</h1>
            <QuestionList questions={survey.questions} /> 
            <strong><button id="send-answer" onClick={sendSurveyAnswer}>Отправить</button></strong>
          </div>        
      }
      
    </div>
  );
}


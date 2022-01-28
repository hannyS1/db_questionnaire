import axios from "axios";
import React, { useEffect } from "react";
import { useState } from "react/cjs/react.development";
import { apiAddr, getDefaultHeaders } from "../services/requests";
import { useParams } from "react-router";
import Loader from "../services/Loader";

export default function AnswerDetail() {

  const [loading, setLoading] = useState(true);
  const [answer, setAnswer] = useState(null);

  const id = useParams().id;

  

  async function getAnswer() {
    try{
      const response = await axios.get(apiAddr + "questionnaire/answer-survey/" + id + "/", {headers: getDefaultHeaders()})
      console.log(response.data);
      setAnswer(response.data);
      console.log(answer)
      setLoading(false);
    }
    catch (error){
      alert(error.text);
    }

  }

  function renderChoices(choices) {
    return choices.map((choice, index) => {
      return(  
        <div key={choice.id} className="choice-item">
          <input type="radio" choice-id={choice.id} value={choice.text} name={choice.question.text} />
          <label htmlFor={choice.text}>{choice.text}</label>
        </div>
      )
      
    })
  }

  function renderQuestion(question) {
    return(
      <li question-id={question.id}>
        <p>{question.text}</p>
        {renderChoices(question.choices)}
      </li> 
    )
  }

  useEffect(() => {
    getAnswer();
  }, [])

  return(
    <div>
      {
        loading ? <Loader /> :
        <ul>
          {answer.questions_answers.map((question_answer, index) => {
            return(renderQuestion(question_answer.question))
          })}
        </ul>
      }
    </div>
    
  )


  return (
    ""
  )
}

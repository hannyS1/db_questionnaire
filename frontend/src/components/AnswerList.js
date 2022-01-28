import axios from "axios";
import React, { useEffect } from "react";
import { useState } from "react/cjs/react.development";
import { apiAddr, getDefaultHeaders } from "../services/requests";
import AnswerItem from "./AnswerItem";


export default function AnswerList() {

  const [answers, setAnswers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getAnswers();
  }, [])

  async function getAnswers() {
    try{
      const response = await axios.get(apiAddr + "questionnaire/answer-survey/", {headers: getDefaultHeaders()});
      setAnswers(response.data);
      setLoading(false);
    }
    catch (error){
      alert(error.response.data);
    }
  }

  return(
    <div id='answer-list'>
      
      <ul className='rounded'>
        {answers.map(answer => {
          return <AnswerItem answer={answer} id={answer.id} />
        })}
      </ul>
    </div>
  )
}
import React, { useEffect, useState } from "react";
import axios from "axios";
import { apiAddr } from "../services/requests";
import SurveyItem from "./SurveyItem";
import { getDefaultHeaders } from "../services/requests";


export default function SurveyList() {

  const [surveys, setSurveys] = useState([]);

  const headers = getDefaultHeaders();

  useEffect(() => {
    getSurveys()
  }, [])


  const getSurveys = async function() {
    const response = await axios.get(apiAddr + 'questionnaire/survey/', {headers: headers})
      .catch((error) => {
        alert(error.response.data);
      })
      .then((response) => {
        if(response.status === 200){
          setSurveys(response.data);
        }
      })
  }

  
  return(
    <div id='survey-list'>
      
      <ul className='rounded'>
        {surveys.map(survey => {
          return <SurveyItem survey={survey} key={survey.id} />
        })}
      </ul>
    </div>
  )
}

<style>
  
</style>




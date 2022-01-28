import React from "react";
import { useLocation } from "react-router";
import { backendAddr } from "../services/requests";


export default function SurveyItem(props) {

  const detailPath = window.location.origin + useLocation().pathname + "/" + props.survey.id;

  function getStartDate() {
    if (props.survey.start_date == null){
      return "";
    }
    return props.survey.start_date.replace('-', '.').replace('-', '.');
  }

  function getEndDate() {
    if (props.survey.end_date == null){
      return "";
    }
    return props.survey.end_date.replace('-', '.').replace('-', '.');
  }

  function checkDates() {
    if (props.survey.start_date == null && props.survey.end_date == null) {
      return false;
    }
    return true;
  }

  

  return(
    <li>
      <a href={detailPath}>
        <h4>Название: {props.survey.name}</h4>
        {checkDates() ? <p>Дата опроса: {getStartDate()} - {getEndDate()}</p>: <p>Дата не указана</p>}
        
      </a>
    </li>
  )
}

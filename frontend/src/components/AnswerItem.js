import React from "react";
import { useLocation } from "react-router";

export default function AnswerItem(props) {

  const detailPath = window.location.origin + useLocation().pathname + "/" + props.answer.id;

  return(
    <li>
      <a href={detailPath}>
        <h4>Название: {props.answer.survey_name}</h4>       
      </a>
    </li>
  )
}
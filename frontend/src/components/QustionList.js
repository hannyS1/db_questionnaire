import React from "react";
import QuestionItem from "./QuestionItem";


export default function QuestionList(props) {
  
  const questions = props.questions;
  console.log(questions);
  return(
    <div>
      <ul id="question-list">
        {questions.map((question, index) => {
          if (question.choices.length){
            return <QuestionItem question={question} key={index} />
          }
          return ""
        })}
      </ul>      
    </div>
  )
}
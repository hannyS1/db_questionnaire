import React from "react";


export default function QuestionItem(props) {

  function renderChocies(choices) {
    return choices.map((choice, index) => {
      return(
        <div key={choice.id} className="choice-item">
          <input type="radio" choice-id={choice.id} value={choice.text} name={props.question.text} />
          <label htmlFor={choice.text}>{choice.text}</label>
        </div>
      )
      
    })
  }

  return(
    <li question-id={props.question.id}>
    <p>{props.question.text}</p>
    {renderChocies(props.question.choices)}
    </li> 
  )
}
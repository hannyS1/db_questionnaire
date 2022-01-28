import React from "react";
import TodoItem from "./TodoItem";

export default function TodoList() {

  const styles = {
    ul: {
      listStyle: 'none',
      margin: 0,
      padding: 0
    }
  }

  return (
    <ul style={styles.ul}>
      <TodoItem></TodoItem>
      <TodoItem></TodoItem>
      <TodoItem></TodoItem>
      <TodoItem></TodoItem>
    </ul>
  )
}
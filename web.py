import streamlit as st
import functions
st.title("To Do App")


todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.file_dump(todos)

for index, todo in enumerate(todos):
    checkbox= st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.file_dump(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='', placeholder="add new todo..." ,
              on_change= add_todo, key='new_todo')

st.session_state








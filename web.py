
import streamlit as st
import functions


todos=functions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("MY TODO APP")
st.subheader("THIS IS MY TODO APP")
st.write("<h1>App is used to increase your <br>productivity</br></h1>", unsafe_allow_html=True)

for index, todo in enumerate(todos):

   checkbox = st.checkbox(todo,key=todo)
   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st._experimental_rerun()


st.text_input(label="",placeholder="Add new todo...",on_change=add_todo,key="new_todo")

print('Hello')

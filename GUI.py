import functions
import PySimpleGUI as sg

label= sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
# layout=[[label, input_box]]) this puts it on one line horizontally and above is 2 seperate rows for the displayment of them #
# each list within the layout list is its own row #
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos('todos_gui.txt')
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos, 'todos_gui.txt')
        case sg.WIN_CLOSED:
            break

window.close()


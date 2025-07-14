## Note:
### Source:
[https://www.pythontutorial.net/tkinter/] - tkinter tutorial from Python Tutorial
### General:
- ttk is the themed version of tk
- both version have same attributes, but ttk's output are a lot more modernised compared to tk
- ttk is native to win11, whereas tk is the classical version

### Interactives:
- you can use lamba within buttons
- the "command" option is only limited to button and some other widgets
    - binds to "left-click" and "backspace", but not the 'Return' key
- event binding can overcome the limitations
#### .bind(event, handler)
- *event* refers to the interaction the user have given to the application
- *handler* refers to the action the application responds with
- can create a function *log(event)* that passes through the function *print(event)*. This can be handy when it comes to debugging.
#### Event patterns
- for all event types/modifiers/patterns, refer to this section of the tutorial: [https://www.pythontutorial.net/tkinter/tkinter-event-binding/#event-patterns]
#### Buttons
- syntax: Button(master, kw)
    - *master* arg is the parent widget, basically refers to where you are placing the button
    - *kw* refers to the keywords that changes the appearence of the behaviour of the button
- Similar to pygame, there is also a *quit()* method where it terminates the program. This can be the attribute of a button.
    - This prevents error msg to come across into the terminal of the compiler when running the code.
- If an image is wished to be used as a button, simply change the behaviour of the button with the *image* argument
- 

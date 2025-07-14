## Note:
### General:
- ttk is the themed version of tk
- both version have same attributes, but ttk's output are a lot more modernised compared to tk
- ttk is native to win11, whereas tk is the classical version

### Interactives:
- you can use lamba within buttons
- the "command" option is only limited to button and some other widgets
    - binds to "left-click" and "backspace", but not the 'Return' key
- event binding can overcome the limitations

- .bind(event, handler)
    - *event* refers to the interaction the user have given to the application
    - *handler* refers to the action the application responds with


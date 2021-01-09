# API REST ToDo-List

|           ENDPOINT          |  METHOD |                  URI                |           BODY             | RESPONSE      | COMMENTS |
| ------------------------    | ------- | ----------------------------------- | -------------------------- | ------------- | -------- |
| Create a ToDo               | POST    | `/todos/`                           |      `TODO`                | 201 - Created `TODO`  |
| Remove ToDo                 | DELETE  | `/todos/<id>/`                      |                            | `{}`          | 
| Update ToDo list as done    | PATCH   | `/todos/`                           | `{ action: "done", ids: [{ id: int }] }`           | 200 - Ok \ 400 - Bad Request: can't parse `ids`         | Change the value of `completed` to `true` in `TODO`s that have an id from the `ids` list. |
| List ToDos                  | GET     | `/todos/`                           | `{ creationDate?: datetimestr, title?: str, description?: str }`    | 200 - `[TODO]` \ 404 - Not found if: * `creationDate`  doesn't exist * `title`  doesn't exist * `description` doesn't contain the string passed. \ 400 - Bad Request if: * can't parse `creationDate` * can't parse  `title` * can't parse `description`  | If there aren't params, return all ToDos. |

--------------------------------------------------------------------------

|   Types             |                                                                                 |
| --------------------| ------------------------------------------------------------------------------- |
|  `TODO`             | `{ title: str, description?: str, creationDate: datetimestr, completed: bool }` | 

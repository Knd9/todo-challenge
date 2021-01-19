# API REST ToDo-List

|           ENDPOINT          |  METHOD |                  URI                |           BODY             | RESPONSE      | COMMENTS |
| ------------------------    | ------- | ----------------------------------- | -------------------------- | ------------- | -------- |
| Create a To Do               | POST    | `/todos/`                           |      `{ title: str, description: str}`                | 201 - Created `TODO` \ 400 - Bad Request if: * `title` is blank * `title` has more than 100 characters. * `title` or `description` have `null` value. |
| Update ToDo list as done    | PATCH   | `/todos/`                           | `id: [ int ] }`           | 200 - `[TODO]` \ 404 - Not Found: some ID of the `id` list does not exist. \ 400 Bad Request: can't parse `id`.| Change the value of `completed` to `true` in `TODO`s that have an ID from the `id` list. Return a ToDo list with the ToDo's updated. |
| List ToDo's                  | GET     | `/todos/`                           | `{ creationDate?: datetimestr, title?: str, description?: str }`    | 200 - `[TODO]` | If there aren't params, return all ToDo's. If nothing matches, return []. |
| Remove ToDo                 | DELETE  | `/todos/{id}/`                      |                            | 204 - No Content \ 404 - Not Found: ToDo with `{id}` given does not exist.  | 

--------------------------------------------------------------------------

|   Types             |                                                                                 |
| --------------------| ------------------------------------------------------------------------------- |
|  `TODO`             | `{ title: str, description?: str, creationDate: datetimestr, completed: bool }` | 

# API REST ToDo-List

|           ENDPOINT          |  METHOD |                  URI                |           BODY             | RESPONSE      | COMMENTS |
| ------------------------    | ------- | ----------------------------------- | -------------------------- | ------------- | -------- |
| Create a To Do               | POST    | `/todos/`                           |      `{ title: str, description: str}`                | 201 - Created `TODO` \ 400 - Bad Request if: * `title` is blank * `title` has more than 100 characters. * `title` or `description` have `null` value |
| Remove ToDo                 | DELETE  | `/todos/<id>/`                      |                            | 204 - No Content          | 
| Update ToDo list as done    | PATCH   | `/todos/`                           | `ids: [ int ] }`           | 200 - Ok \ 404 - Not Found: some id of the `id` list does not exist | Change the value of `completed` to `true` in `TODO`s that have an id from the `id` list. |
| List ToDo's                  | GET     | `/todos/`                           | `{ creationDate?: datetimestr, title?: str, description?: str }`    | 200 - `[TODO]` \ 200 - [] - if: * `creationDate` or `title` or `description` doesn't exist * `creationDate` or `title` or `description` doesn't contain the string passed. \ 400 - Bad Request if: * can't parse `creationDate` or  `title` or `description`  | If there aren't params, return all ToDos. |

--------------------------------------------------------------------------

|   Types             |                                                                                 |
| --------------------| ------------------------------------------------------------------------------- |
|  `TODO`             | `{ title: str, description?: str, creationDate: datetimestr, completed: bool }` | 

# Django Model

## Many-To-One Relationship
-




## Many-to-Many Relationship
- It create a intermediate table and populate data from those defined signle data like we have two table "course" and another table "student" then what it does,is it crete a new table called anything, here i assume membership and it that table it include the id from "course" and "student" respectively and the combine it.
  - Let's understan by example:
    ``` python
    class course(model.models):
      title = models.Charfiled(title)
    ```
- [Awsome video to get understanding about many-to-many](https://www.youtube.com/watch?v=gf2-J9YOMcc&list=PLlRFEj9H3Oj5e-EH0t3kXrcdygrL9-u-Z&index=66)

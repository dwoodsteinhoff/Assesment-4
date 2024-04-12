### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
A) A open source RDBMS(reltaional database management system). It follows SQL standard pretty closely

- What is the difference between SQL and PostgreSQL?
A) PostgreSQL is open source while SQL is not. PostgreSQL uses SQL language but also has it's own procedural language

- In `psql`, how do you connect to a database?
A) In terminal - sudo service postgresql start (if server is not started already). Then, psql - allows you to access the database.

- What is the difference between `HAVING` and `WHERE`?
A) HAVING filters a group of rows based on a condition and WHERE just filters rows based on a condition. 

- What is the difference between an `INNER` and `OUTER` join?
A) INNER join gives rows that match conditions in both tables. OUTER join includes all rows from one or both tables regardless of match conditions.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
A) LEFT OUTER join gives all the rows from LEFT table combined with all the matching rows from the RIGHT table. RIGHT OUTER join is the opposite, gives all rows from RIGHT table combined with matching rows from LEFT table.

- What is an ORM? What do they do?
A) it is object-relational mapping. It is a translationg service between Object-Oriented Programming in our server langauge and relational data in our database

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  A) AJAX is used to make asynchronous requests from a web page and update the content on the page. The server side http requests are based off certain constraints that follow a standardized protocol. AJAX can work with many data formats and server side RESTful API's typically use things like just JSON. server side requests are also "stateless" where each request contains all the information needed to process a request and does not store any information about the client's state.

- What is CSRF? What is the purpose of the CSRF token?
A) makes sure the form came from our server and not from somewhere else. it is checked by the server on form submission.

- What is the purpose of `form.hidden_tag()`?
A) to creat form fields that a user is not going to change or update. send data you want server to have but you don't need a user to specify.
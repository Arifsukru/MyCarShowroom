# MyCarShowroom

Purpose of this project is helping user to keep data about cars in a showroom and data of workers of a car renting/selling company.
Firstly, program crates a database calls "MyCarShowroom". I preferred Sqllite3 for database.
There are three table exist in the database:

1. workers
2. cars
3. sold

First table keeps data of employees. It has seven column; name, gender, age, phone, position, salary and number. "Number" is a nine digit number that is given by program automatically, special for every employee, we can call it "serial number".

Second table is for cars. It has six column; brand, model, year, price, number and rent. There is also "Number" column and it work like the same but more crucial. About every operation on cars which are selling, rneting, removing you need to write that serial number of car. There is another column that needs to be explained; "Rent". That column tells us car's availabilitiy for renting, goig to explain later in the text.

Third table is exact same column with second. Existing purpose of that table is keeping data of sold cars.

When you start program, after a "System opened." massage, you will connect to "Login screen". There are three options:

1. ADMIN LOGIN
2. EMPLOYEE LOGIN
3. EXIT

If you select "ADMIN LOGIN", followings are the actions you can make:

1. Adding employee
2. Removing employee
3. List of employees
4. List of cars
5. Log out


As an admin you can add an employee, remove an employee (fire!), check lists of cars or workers. After every action you make, program asks that: "Would you like to do another operation? " According to your answer, it will direct you to "Login screen" or operation options as I wrote above. Also, you can turn back to "Login screen" to select "Log out".

With the "EMPLOYEE LOGIN", things you can make is different:

1. Adding car
2. Removing car
3. Renting car
4. Selling car
5. Log out

For adding a car, you need the enter requested data of the car. After that, program gives nine digit number to car and put it in the database with the informations. If user wants to remove a car from the system, first, car list apears and then user should enter enter serial number of car that wanted to remove. While you are doing renting operation, you need to specify a date so car is not be available for renting or selling until that date. Selling a car will be move a car's data to table named "sold".
Also after every action that user makes as an employee, there will be a questioning to make another operation or log out.

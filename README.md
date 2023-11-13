# CS3773 Final Project

## Installing Dependencies

### pip (If you don't have it)

- For Windows
> The get-pip.py file is included in the repo
> Note: Make sure you add the install location to your environment
> varibles "path"

```commandline
$: python get-pip.py
```

### Installing project dependencies

- For Windows

```commandline
$: pip.exe install -r requirements.txt
```

## Running the application

### Using an IDE
1. just click run or debug
2. In a browser, navigate to http://127.0.0.1:5000/

### From the Command prompt (Windows) or terminal (Unixish)

1. Launch the application

```commandline
$: python app.py
```

2. In a browser, navigate to http://127.0.0.1:5000/

## How to Work With the Database

#### NOTE: The first four steps will only be done when initially adding a new table. Once you start running your populate scripts you will not have to go back to those steps!

1. Create a new class under the 'model' directory. This will be the new table.
   - Follow along with the layout of book.py or user_account.py, it shouldn't change too much.
2. Import this new class in env.py located in the 'migrations' directory.
    > For example: from model.book import Book
3. Run the follow command in the terminal to create a new version
    ```commandline
    $: alembic revision --autogenerate -m "message of what table was added(ex: "books")"
    ```
4. Run the following command in the terminal to update the head
    ```commandline
    $: alembic upgrade head
    ```
5. To populate the table create a new populate script under 'migrations/test_data'.
   - The naming convention for these scripts should follow along with the general name of the table (i.e., populate_books.py).
   - These scripts will all have a similar base, only needing to change the things specific to the table you are populating, so stick with the same outline as the one's already done.
6. Once your script is complete you should be able to run the script and it will populate the table for you.
   - NOTE: You will need to update the path in the config.ini to match the absolute path for CalicoReads.db on your machine.

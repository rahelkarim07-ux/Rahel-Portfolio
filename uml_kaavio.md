# UML-arkkitehtuuri ja kaaviot

Tässä dokumentissa kuvataan repositorion keskeisten ohjelmistokomponenttien rakenne ja toimintalogiikka UML-kaavioiden avulla.

---

## 1. Luokkakaavio: To-Do CLI -sovellus (`todo.py`)

Alla oleva luokkakaavio kuvaa tehtävänhallintasovelluksen tietomallin ja toimintalogiikan.

```mermaid
classDiagram
    class TodoApp {
        -list tasks
        -str data_file
        +__init__(data_file)
        +load_tasks()
        +save_tasks()
        +add_task(title)
        +list_tasks()
        +mark_completed(task_id)
        +remove_task(task_id)
        +run_interactive_loop()
    }

    class Task {
        +int id
        +str title
        +bool completed
        +to_dict() dict
        +from_dict(dict) Task
    }

    TodoApp "1" o-- "*" Task : sisältää ja hallinnoi
```

---

## 2. Toimintokohtainen sekvenssikaavio: Tehtävän lisääminen

```mermaid
sequenceDiagram
    autonumber
    actor Kayttaja as Käyttäjä
    participant App as TodoApp
    participant Task as Task-olio
    participant File as Tallennustiedosto (JSON/TXT)

    Kayttaja->>App: Syötä tehtävän nimi (add_task)
    App->>Task: Luo uusi Task(id, title, completed=False)
    Task-->>App: Palauta uusi tehtävä
    App->>App: Lisää listaan (tasks.append)
    App->>File: Tallenna päivitetyt tiedot (save_tasks)
    File-->>App: Tallennus onnistui
    App-->>Kayttaja: Kuittaus: Tehtävä lisätty onnistuneesti
```

---

## 3. Komponenttikaavio: Portfolio & Scriptit

```mermaid
graph TD
    Client[Käyttäjän Selain] -->|HTTP / GitHub Pages| HTML[index.html]
    HTML --> CSS[style.css]
    HTML --> Assets[Assets / Images]
    
    subgraph Python CLI Työkalut
        Calc[calculator.py]
        Todo[todo.py]
    end
```

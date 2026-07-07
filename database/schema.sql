DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS complaints;
DROP TABLE IF EXISTS admins;

--------------------------------------------------
-- Admin Table
--------------------------------------------------

CREATE TABLE admins (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

--------------------------------------------------
-- Students
--------------------------------------------------

CREATE TABLE students (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    username TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    room_number TEXT,

    phone TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

--------------------------------------------------
-- Complaints
--------------------------------------------------

CREATE TABLE complaints (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id INTEGER NOT NULL,

    title TEXT NOT NULL,

    category TEXT NOT NULL,

    description TEXT NOT NULL,

    priority TEXT DEFAULT 'Medium',

    status TEXT DEFAULT 'Pending',

    image TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(student_id)

    REFERENCES students(id)

);

--------------------------------------------------
-- Default Admin
--------------------------------------------------

INSERT INTO admins (

username,

password

)

VALUES(

'admin',

'admin123'

);
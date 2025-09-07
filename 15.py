import sqlite3
# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()


# Create Student and Subject Tables

cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    Enrollment INTEGER PRIMARY KEY,
    Name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Subjects (
    SubjectID INTEGER PRIMARY KEY AUTOINCREMENT,
    Enrollment INTEGER,
    Subject TEXT,
    Mark INTEGER,
    FOREIGN KEY (Enrollment) REFERENCES Students (Enrollment)
)
''')


# Insert Student Data (with multiple subjects)
def enroll_student(enrollment, name, subjects):
    # Insert student (only once)
    cursor.execute('''
        INSERT OR IGNORE INTO Students (Enrollment, Name)
        VALUES (?, ?)
    ''', (enrollment, name))
    
    # Insert multiple subjects
    cursor.executemany('''
        INSERT INTO Subjects (Enrollment, Subject, Mark)
        VALUES (?, ?, ?)
    ''', [(enrollment, sub, mark) for sub, mark in subjects])
    conn.commit()

#  student records
enroll_student(92400133118, 'Shiva prasad', [
    ('PWP', 98),
    ('ICE', 95),
    ('DMGT', 92),
    ('DSC', 89),
    ('SS', 86),
    ('COA', 84)
])


# Fetch Student Data

print("\nAll Student Records:")
cursor.execute('''
    SELECT s.Enrollment, s.Name, sub.Subject, sub.Mark
    FROM Students s
    JOIN Subjects sub ON s.Enrollment = sub.Enrollment
''')
for row in cursor.fetchall():
    print(row)

# Fetch Data with Specific Criteria (e.g., marks > 90)

print("\nSubjects with Marks > 90:")
cursor.execute('''
    SELECT s.Name, sub.Subject, sub.Mark
    FROM Students s
    JOIN Subjects sub ON s.Enrollment = sub.Enrollment
    WHERE sub.Mark > 90
''')
for row in cursor.fetchall():
    print(row)


# Update Student Information 

cursor.execute('''
    UPDATE Subjects
    SET Mark = 99
    WHERE Enrollment = ? AND Subject = ?
''', (92400133118, 'DSC'))
conn.commit()

# Verify Update
print("\nAfter Update (DSC subject):")
cursor.execute('''
    SELECT Subject, Mark
    FROM Subjects
    WHERE Enrollment = ?
''', (92400133118,))
for row in cursor.fetchall():
    print(row)


# Delete a Subject

cursor.execute('''
    DELETE FROM Subjects
    WHERE Enrollment = ? AND Subject = ?
''', (92400133118, 'COA'))
conn.commit()

# Verify Deletion
print("\nAfter Deletion (COA subject removed):")
cursor.execute('''
    SELECT Subject, Mark
    FROM Subjects
    WHERE Enrollment = ?
''', (92400133118,))
for row in cursor.fetchall():
    print(row)


# Calculate Average Marks

cursor.execute('''
    SELECT AVG(Mark)
    FROM Subjects
    WHERE Enrollment = ?
''', (92400133118,))
avg_mark = cursor.fetchone()[0]
print(f"\nAverage Marks for Enrollment 92400133118: {avg_mark:.2f}")

# Close Connection

conn.close()

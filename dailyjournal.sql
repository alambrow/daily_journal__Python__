DROP TABLE Entries;
DROP TABLE Moods;

CREATE TABLE `Entries` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `title`  TEXT NOT NULL,
    `entry`     TEXT NOT NULL,
    `timestamp` TEXT NOT NULL,
    `moodId` INTEGER NOT NULL,
    FOREIGN KEY(`moodId`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood`  TEXT NOT NULL
);

INSERT INTO 'Entries' VALUES (null, 'Learning SQL', 'Learning about basic commands', 'July 15 2021', 1);
INSERT INTO 'Moods' VALUES (null, 'trying to keep up the pace');
INSERT INTO 'Moods' VALUES (null, 'brainded');

INSERT INTO Entries
    ( title, entry, timestamp, moodId )
VALUES
    ( "Learning Python", "Figuring out serverz", "21 July 2021", 1)
;


SELECT * FROM Entries;
SELECT * FROM Moods;




SELECT
    a.id,
    a.title,
    a.entry,
    a.timestamp,
    a.moodId,
    b.id mood_id,
    b.mood mood
FROM Entries a
JOIN Moods b
    ON b.id = a.moodId;




        SELECT
            a.id,
            a.title,
            a.entry,
            a.timestamp
        FROM entries a
        WHERE entry LIKE "%earn%"
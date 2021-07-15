CREATE TABLE `Entries` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `title`  TEXT NOT NULL,
    `entry`     TEXT NOT NULL,
    `timestamp` TEXT NOT NULL
);

CREATE TABLE `Moods` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood`  TEXT NOT NULL
);

INSERT INTO 'Entries' VALUES (null, 'Learning SQL', 'Learning about basic commands', 'July 15 2021');
INSERT INTO 'Moods' VALUES (null, 'trying to keep up the pace');

SELECT * FROM Entries;
SELECT * FROM Moods;
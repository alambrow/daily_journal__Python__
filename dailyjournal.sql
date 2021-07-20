DROP TABLE Entries;
DROP TABLE Moods;

CREATE TABLE `Entries` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `title`  TEXT NOT NULL,
    `entry`     TEXT NOT NULL,
    `timestamp` TEXT NOT NULL
);

CREATE TABLE `Moods` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood`  TEXT NOT NULL,
    `entry_id` INTEGER NOT NULL,
    FOREIGN KEY(`entry_id`) REFERENCES `Entries`(`id`)
);

INSERT INTO 'Entries' VALUES (null, 'Learning SQL', 'Learning about basic commands', 'July 15 2021');
INSERT INTO 'Moods' VALUES (null, 'trying to keep up the pace', 1);

SELECT * FROM Entries;
SELECT * FROM Moods;


        SELECT
            a.id,
            a.title,
            a.entry,
            a.timestamp
        FROM entries a
        WHERE entry LIKE "%earn%"

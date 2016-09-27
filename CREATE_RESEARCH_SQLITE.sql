CREATE TABLE "history" (
	"HID" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE  DEFAULT 1,
	"fk_demographics" INTEGER NOT NULL UNIQUE,
	"fk_variables" INTEGER NOT NULL UNIQUE,
	"filename" TEXT, 
	"timestamp" DATETIME,
	FOREIGN KEY("fk_demographics") REFERENCES demographics("DID"),
	FOREIGN KEY("fk_variables") REFERENCES variables("VID")
);
CREATE TABLE "geography" (
	""
);
CREATE TABLE "demographics" (
	"DID" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE  DEFAULT 1, 
	"male" REAL, 
	"female" REAL
);
CREATE TABLE "variables" (
	"VID" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE  DEFAULT 1, 
	"innerCityMulti" 
);
CREATE TABLE "provider" (
	"PID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL  UNIQUE  DEFAULT 1, 
	"name" TEXT,
	"description" TEXT, 
	"address1" TEXT, 
	"address2" TEXT, 
	"city" TEXT, 
	"state" TEXT, 
	"zip" TEXT, 
	"userDefinedRadius" REAL, 
	"userDefinedFade" REAL,
	"longitude" REAL,
	"latitude" REAL
);
CREATE TABLE "resource" (
	"RID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL  UNIQUE  DEFAULT 1,
	"name" TEXT NOT NULL,
	"description" TEXT NOT NULL,
	"radiusMultiplier" REAL,
	"type" INTEGER NOT NULL,
	FOREIGN KEY ("type") REFERENCES resourceType("RTID")
);
CREATE TABLE "resourceType" (
	"RTID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL  UNIQUE  DEFAULT 1,
	"name" TEXT, 
	"description" TEXT, 
	"radius" REAL
);
CREATE TABLE "rule" (
	"RUID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL  UNIQUE  DEFAULT 1,
	"population" BLOB,
	"location" BLOB
);
CREATE TABLE "pivot" (
	"provider" INTEGER NOT NULL,
	"rule" INTEGER NOT NULL,
	"resource" INTEGER NOT NULL,
	FOREIGN KEY ("provider") REFERENCES provider("PID"),
	FOREIGN KEY ("rule") REFERENCES rule("RUID"),
	FOREIGN KEY ("resource") REFERENCES resource("RID")
);
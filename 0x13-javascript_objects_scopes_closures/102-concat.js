#!/usr/bin/node
const myFileSystem = require('fs');
const a = myFileSystem.readFileSync(process.argv[2], 'utf8');
const b = myFileSystem.readFileSync(process.argv[3], 'utf8');
myFileSystem.writeFileSync(process.argv[4], a + b);

import * as mysql from 'mysql2';

export class Server {
    public readonly connection: mysql.Connection;
    
connection = mysql.createConnection({
    host: '127.0.0.1',
    user: 'scrapper',
    password: 'Scrapper#1322',
    database: 'scrapper'
});

this.connection.connect(function(err: any) {
    if(err)
    {
        return console.error('error: ' + err.message);
    }
    
    console.log('Connected to the MySQL Server.');
});